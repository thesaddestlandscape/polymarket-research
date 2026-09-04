# Hipótesis automáticas — 2026-09-04 00:14 UTC
_Generado por shadow_postmortem.py sobre 273261 resoluciones (PNL=+26538.14€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.176 (n=109)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.263 (n=331)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.392 (n=81)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=280)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.263 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.154)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.169 (n=303)

  - _Acción_: Kelly boost +0.84€ cuando `n_ballena_banda` > 19.0 (IC base=+0.154)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.154)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.259 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.154)

- **PATRÓN** `banda_z` > `11.806` → IC=+0.268 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.806 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.173 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.161 (n=237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 12.0 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=343)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `3094.168` → IC=+0.197 (n=150)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3094.168 (IC base=+0.154)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=280)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.5 (IC base=+0.004)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.387 (n=51)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=156)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=180)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.278 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.185)

- **PATRÓN** `n_ballena_banda` > `18.0` → IC=+0.200 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 18.0 (IC base=+0.185)

- **PATRÓN** `n_total_lado` > `100.0` → IC=+0.290 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 100.0 (IC base=+0.185)

- **PATRÓN** `banda_hit_calibrado` > `0.8038` → IC=+0.266 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8038 (IC base=+0.185)

- **PATRÓN** `banda_z` > `11.818` → IC=+0.273 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.818 (IC base=+0.185)

- **PATRÓN** `ballenas_wallet_edge_medio` > `3.098` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `ballenas_wallet_edge_medio` > 3.098 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.192 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 7.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.195 (n=165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2928.5072` → IC=+0.200 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2928.5072 (IC base=+0.185)

- **PATRÓN** `py_entrada` < `0.475` → IC=+0.128 (n=84)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.475 (IC base=-0.017)

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
- **FILTRO** `restante_s_al_confirmar` < `146.76` → IC=-0.298 (n=3685)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.76
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=11056)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `140.63` → IC=-0.290 (n=478)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.63
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1435)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `625.5` → IC=-0.141 (n=324)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 625.5
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=630)

- **FILTRO** `restante_s_al_confirmar` < `458.44` → IC=-0.171 (n=238)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 458.44
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=716)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `113.97` → IC=-0.402 (n=490)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 113.97
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=1470)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `142.69` → IC=-0.315 (n=818)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.69
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=2456)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.39` → IC=-0.378 (n=889)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.39
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=1807)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.189 (n=7991)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.7 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=2017)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2373.3986` → IC=+0.171 (n=1933)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2373.3986 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.146 (n=4825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=6372)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.253 (n=4882)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=3835)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1928.8728` → IC=+0.175 (n=3279)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1928.8728 (IC base=+0.141)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.218 (n=852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.211 (n=869)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.392 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `13033.0053` → IC=+0.224 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13033.0053 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.196 (n=831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.258 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=1166)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `12436.8097` → IC=+0.202 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12436.8097 (IC base=+0.187)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.127 (n=561)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 15.0 (IC base=+0.116)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.136 (n=632)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` > 0.555 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=271)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `4800.0243` → IC=+0.151 (n=216)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4800.0243 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.188 (n=213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.177 (n=329)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.41 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `5317.6696` → IC=+0.165 (n=234)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5317.6696 (IC base=+0.127)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=93)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.145 (n=1550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=1368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.312 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.264 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.263 (n=695)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` < `0.2` → IC=+0.404 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.2 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.262 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1943.5814` → IC=+0.267 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1943.5814 (IC base=+0.258)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.137 (n=268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.151 (n=336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.66` → IC=+0.260 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.66 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=457)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1880.2618` → IC=+0.162 (n=338)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 1880.2618 (IC base=+0.136)

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

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.206 (n=369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.348 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.214 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `915.2245` → IC=+0.217 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 915.2245 (IC base=+0.206)

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
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.224 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=294)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.110)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.344 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=126)

- **FILTRO** `libro_liquidez` < `11307.5209` → IC=-0.262 (n=141)

  - _Acción_: SKIP cuando `libro_liquidez` < 11307.5209
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=47)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=6150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=5175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.202 (n=2930)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3780.1464` → IC=+0.329 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3780.1464 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.178 (n=1341)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=1581)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.165)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=86)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=87)

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
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=1307)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.174 (n=1588)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.179 (n=1060)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.72 (IC base=+0.169)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.238 (n=1178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.314 (n=498)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=1280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.189 (n=786)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.7 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.182 (n=646)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.73 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.455 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.447)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.449 (n=273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.481 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.447)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.446 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.447)

- **PATRÓN** `libro_liquidez` > `2008.7424` → IC=+0.453 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2008.7424 (IC base=+0.447)

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
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.445 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.439 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.445)

- **PATRÓN** `libro_liquidez` > `1800.3787` → IC=+0.439 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1800.3787 (IC base=+0.445)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.198 (n=6364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 18.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.207 (n=17381)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.188)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=3391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.147 (n=2401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 12.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.175 (n=2554)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.72 (IC base=+0.146)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=3008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.228 (n=1100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.258 (n=2212)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.226)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.177 (n=1111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.179 (n=2996)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.161)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=1540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.228 (n=1119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.269 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.217 (n=1053)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.236 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.191 (n=1078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=2251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.204 (n=2908)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.204 (n=2457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.132)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.146 (n=2313)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` < 4.01 (IC base=+0.132)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.152 (n=2474)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` > 4.93 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.149 (n=3347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.132)

- **PATRÓN** `lag_apertura_s` < `4.17` → IC=+0.155 (n=2301)

  - _Acción_: Kelly boost +0.77€ cuando `lag_apertura_s` < 4.17 (IC base=+0.132)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.209 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.137)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.150 (n=1145)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` < 3.95 (IC base=+0.137)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.151 (n=1579)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.88 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.155 (n=2410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 12.0 (IC base=+0.137)

- **PATRÓN** `lag_apertura_s` < `7.01` → IC=+0.150 (n=1509)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 7.01 (IC base=+0.137)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=1217)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.127)

- **PATRÓN** `restante_min` < `4.43` → IC=+0.134 (n=1531)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.43 (IC base=+0.127)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.159 (n=1295)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 4.94 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.130 (n=3489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.137 (n=1693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.127)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.167 (n=1158)

  - _Acción_: Kelly boost +0.84€ cuando `lag_apertura_s` < 3.33 (IC base=+0.127)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.314 (n=637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.295 (n=271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.366 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.294)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.301 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.376 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.301)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.301)

- **PATRÓN** `libro_liquidez` > `1617.6179` → IC=+0.319 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1617.6179 (IC base=+0.301)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.265)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.422 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.285 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1040.7995` → IC=+0.284 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1040.7995 (IC base=+0.265)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.314 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.265)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.422 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.285 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `1040.7995` → IC=+0.284 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1040.7995 (IC base=+0.265)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.3571` → IC=+0.128 (n=3659)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.3571 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.2745` → IC=+0.225 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2745 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.603` → IC=+0.150 (n=1399)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 5.603 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.6936` → IC=+0.224 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6936 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` > `1.0858` → IC=+0.245 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0858 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.1732` → IC=+0.174 (n=624)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1732 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` < `2.88` → IC=+0.175 (n=2187)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.88 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` > `1.4763` → IC=+0.170 (n=2187)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4763 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.198 (n=1091)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 54.0 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.404` → IC=+0.127 (n=3517)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.404 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.3436` → IC=+0.145 (n=1270)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.3436 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.6862` → IC=+0.150 (n=544)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6862 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.0471` → IC=+0.138 (n=561)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0471 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.3045` → IC=+0.259 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3045 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.8613` → IC=+0.214 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8613 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.212 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=+0.041)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.184 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0076 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2788` → IC=+0.157 (n=815)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2788 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.627` → IC=+0.299 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.627 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2285` → IC=+0.215 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2285 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.6736` → IC=+0.138 (n=718)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.6736 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.4443` → IC=+0.144 (n=717)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4443 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.188 (n=649)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.184 (n=464)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 62.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.261 (n=362)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.273 (n=487)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1082` → IC=+0.330 (n=239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1082 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.265 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.277 (n=571)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.4038` → IC=+0.283 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4038 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.14` → IC=+0.274 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.14 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.0675` → IC=+0.260 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0675 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.357 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `1.6072` → IC=+0.283 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6072 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.269 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1701.724` → IC=+0.283 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1701.724 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.259 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 63.0 (IC base=+0.259)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.251 (n=215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.227 (n=214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.236 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=643)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9278` → IC=+0.241 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9278 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1847` → IC=+0.222 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1847 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.49` → IC=+0.218 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.49 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.257` → IC=+0.227 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.257 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.068` → IC=+0.216 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.068 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2608` → IC=+0.216 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2608 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `1.099` → IC=+0.230 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.099 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.1` → IC=+0.218 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `2.109` → IC=+0.228 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.109 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `11005.6828` → IC=+0.235 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11005.6828 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.157 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.1766` → IC=+0.150 (n=467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1766 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.141 (n=636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.140 (n=731)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 18.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6603` → IC=+0.162 (n=700)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.6603 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.342` → IC=+0.158 (n=674)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.342 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.496` → IC=+0.214 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.496 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.618` → IC=+0.178 (n=234)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.618 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1499` → IC=+0.216 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1499 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.7307` → IC=+0.153 (n=396)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.7307 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4046` → IC=+0.154 (n=593)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4046 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `12529.5931` → IC=+0.152 (n=467)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 12529.5931 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.156 (n=338)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 290.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.209 (n=256)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.202 (n=283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.257 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.299` → IC=+0.266 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.299 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.1322` → IC=+0.161 (n=658)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.1322 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.3915` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.3915 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `3.9006` → IC=+0.154 (n=684)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 3.9006 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8939` → IC=+0.174 (n=612)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8939 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.184 (n=790)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.04 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.221 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.252 (n=622)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.3782` → IC=+0.245 (n=547)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3782 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.245 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.262 (n=280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0364` → IC=+0.305 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0364 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.556` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.556 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3755` → IC=+0.314 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3755 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7042` → IC=+0.269 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7042 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.4461` → IC=+0.222 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4461 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.224 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.240)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.147 (n=168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=544)

- **FILTRO** `ibs_20min` > `0.8252` → IC=-0.189 (n=287)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8252
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=862)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=72)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1077)

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

- **PATRÓN** `dist_vwap_pct` > `0.2997` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2997 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.5827` → IC=+0.141 (n=179)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5827 (IC base=-0.040)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=143)

- **FILTRO** `ibs_20min` < `0.28` → IC=-0.161 (n=60)

  - _Acción_: SKIP cuando `ibs_20min` < 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=123)

- **FILTRO** `sigma_ewma_delta_pct` > `8.313` → IC=-0.193 (n=203)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.313
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1557)

- **FILTRO** `volumen_pendiente_norm` < `0.1212` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1212
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=18)

- **FILTRO** `volumen_spike_ratio` > `1.4382` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4382
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=14)

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

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.531` → IC=-0.155 (n=346)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.531
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=674)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.193 (n=112)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=908)

- **FILTRO** `ibs_20min` > `0.7927` → IC=-0.186 (n=409)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7927
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1231)

- **FILTRO** `sigma_ewma_delta_pct` > `8.911` → IC=-0.137 (n=191)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.911
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1449)

- **PATRÓN** `dist_vwap_pct` > `0.5839` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5839 (IC base=-0.101)

- **PATRÓN** `dist_vwap_pct` < `0.2041` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2041 (IC base=-0.101)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=-0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.0602` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0602 (IC base=-0.101)

- **PATRÓN** `volumen_spike_ratio` < `1.4824` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4824 (IC base=-0.101)

- **PATRÓN** `volumen_spike_ratio` > `2.3039` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.3039 (IC base=-0.101)

- **PATRÓN** `dist_vwap_pct` < `0.2681` → IC=+0.214 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2681 (IC base=-0.049)

- **PATRÓN** `volumen_regimen` < `0.7364` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.7364 (IC base=-0.049)

- **PATRÓN** `volumen_regimen` > `1.3205` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3205 (IC base=-0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=-0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.339` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.339 (IC base=-0.049)

- **PATRÓN** `volumen_spike_ratio` > `1.906` → IC=+0.157 (n=68)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.906 (IC base=-0.049)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 20.0 (IC base=-0.049)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.172 (n=1509)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0094 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.2903` → IC=+0.139 (n=4519)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.2903 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.9264` → IC=+0.288 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9264 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.48` → IC=+0.120 (n=2388)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` > 2.48 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `0.6802` → IC=+0.219 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6802 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` < `0.0869` → IC=+0.214 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0869 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2535` → IC=+0.230 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2535 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.4925` → IC=+0.234 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4925 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `2.835` → IC=+0.223 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.835 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.296 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 95.0 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.5829` → IC=+0.131 (n=4377)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5829 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.7924` → IC=+0.247 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7924 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.2297` → IC=+0.222 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2297 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.228 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7144 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` > `1.2326` → IC=+0.250 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2326 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.2598` → IC=+0.346 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2598 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.274 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.270 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.052)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2955` → IC=-0.150 (n=375)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2955
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=763)

- **FILTRO** `sigma_ewma_delta_pct` > `2.431` → IC=-0.162 (n=323)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.431
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=715)

- **PATRÓN** `ibs_20min` > `0.825` → IC=+0.211 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.825 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.072` → IC=+0.125 (n=427)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.072 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.341 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `1.9482` → IC=+0.222 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9482 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `2.7084` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7084 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.317 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.019)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8634` → IC=-0.162 (n=380)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8634
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=1144)

- **PATRÓN** `dist_vwap_pct` > `0.9466` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.9466 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.6989` → IC=+0.130 (n=217)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.6989 (IC base=-0.013)

- **PATRÓN** `ballena_activa_n` < `287.0` → IC=+0.152 (n=136)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 287.0 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` < `0.1689` → IC=+0.159 (n=165)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1689 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` < `0.5824` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5824 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` > `1.1181` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1181 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.143 (n=127)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.0817` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0817 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.7706` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7706 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.3934` → IC=+0.149 (n=129)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.3934 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `261.0` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 261.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.291 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1252` → IC=+0.224 (n=320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1252 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.255 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.712` → IC=+0.254 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.712 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.299` → IC=+0.294 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.299 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.1403` → IC=+0.235 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1403 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.7273` → IC=+0.225 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7273 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.249 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.257 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.327 (n=455)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.336 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.310)

- **PATRÓN** `ibs_20min` < `0.3299` → IC=+0.322 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3299 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.68` → IC=+0.340 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.68 (IC base=+0.310)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.359 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` < `3.4973` → IC=+0.311 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.4973 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` > `2.3933` → IC=+0.321 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3933 (IC base=+0.310)

- **PATRÓN** `libro_liquidez` > `1841.9597` → IC=+0.326 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1841.9597 (IC base=+0.310)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.307 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.310)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.155 (n=227)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=504)

- **FILTRO** `ibs_20min` < `0.7743` → IC=-0.134 (n=482)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7743
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=249)

- **FILTRO** `ibs_20min` > `0.8665` → IC=-0.166 (n=303)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8665
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=910)

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
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1131)

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
- **FILTRO** `ibs_20min` < `0.8077` → IC=-0.141 (n=644)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8077
  - _Potencial_: sin este filtro IC_bueno=+0.287 (n=332)

- **FILTRO** `ibs_20min` > `0.7551` → IC=-0.223 (n=280)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7551
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=843)

- **FILTRO** `sigma_ewma_delta_pct` > `4.705` → IC=-0.152 (n=285)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.705
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=838)

- **PATRÓN** `ibs_20min` > `0.9231` → IC=+0.330 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9231 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` > `0.5696` → IC=+0.324 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5696 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.247 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.1627` → IC=+0.304 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1627 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` < `0.1176` → IC=+0.254 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1176 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.231` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.231 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.296 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.302 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `0.7284` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.7284 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1614` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1614 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.9868` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.9868 (IC base=-0.030)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 60.0 (IC base=-0.030)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.332 (n=491)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.262 (n=346)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `0.8915` → IC=+0.324 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8915 (IC base=+0.251)

- **PATRÓN** `dist_vwap_pct` > `0.1627` → IC=+0.314 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1627 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.191` → IC=+0.292 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.191 (IC base=+0.251)

- **PATRÓN** `volumen_regimen` > `0.8467` → IC=+0.289 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8467 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` > `0.2423` → IC=+0.299 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2423 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` < `2.5766` → IC=+0.260 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5766 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.255 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `2467.2556` → IC=+0.255 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2467.2556 (IC base=+0.251)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.282 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.297 (n=264)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.3185` → IC=+0.279 (n=528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3185 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.292 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.317 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.5433` → IC=+0.280 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5433 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.2116` → IC=+0.282 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2116 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.408` → IC=+0.311 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.408 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.284 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` > `1.2708` → IC=+0.304 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2708 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.2435` → IC=+0.381 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2435 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.4369` → IC=+0.266 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4369 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.1971` → IC=+0.297 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1971 (IC base=+0.278)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.208 (n=1275)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.3424` → IC=+0.169 (n=3361)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3424 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.168 (n=3846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.283 (n=1748)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.7965` → IC=+0.236 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7965 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.704` → IC=+0.233 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.704 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `0.6283` → IC=+0.165 (n=2582)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6283 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.1061` → IC=+0.183 (n=1425)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1061 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `2.324` → IC=+0.162 (n=3124)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.324 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.166 (n=3900)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `3936.5622` → IC=+0.178 (n=1273)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 3936.5622 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.179 (n=2733)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 143.0 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.190 (n=3119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0083 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0793` → IC=+0.214 (n=1182)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0793 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=1748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=1600)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 7.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.4375` → IC=+0.231 (n=3545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4375 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.23` → IC=+0.174 (n=2673)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.23 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.992` → IC=+0.218 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.992 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.168 (n=2682)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1753 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.162 (n=2682)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6226 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.256 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.5767` → IC=+0.173 (n=1285)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5767 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.661` → IC=+0.200 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.661 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.180 (n=2506)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 156.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.179 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0057 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.201 (n=292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.2838` → IC=+0.195 (n=643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.2838 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.225 (n=242)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.705` → IC=+0.272 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.705 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.252 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `2.6388` → IC=+0.160 (n=559)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.6388 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `1.4557` → IC=+0.163 (n=559)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4557 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.183 (n=370)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 66.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.264 (n=358)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1585` → IC=+0.307 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1585 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.265 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.2712` → IC=+0.266 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2712 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.664` → IC=+0.252 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.664 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.0645` → IC=+0.227 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0645 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2422` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2422 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.9291` → IC=+0.235 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9291 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.243 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.277 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1698.2448` → IC=+0.280 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1698.2448 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.239 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 63.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.223 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.4155` → IC=+0.174 (n=565)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.4155 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.4793` → IC=+0.209 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4793 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.2059` → IC=+0.223 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2059 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.986` → IC=+0.231 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.986 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.439` → IC=+0.168 (n=537)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 7.439 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.6381` → IC=+0.186 (n=189)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6381 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.0731` → IC=+0.183 (n=257)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.0731 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.200 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4857` → IC=+0.206 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4857 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.169 (n=179)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `11289.7522` → IC=+0.192 (n=505)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 11289.7522 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.182 (n=653)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0061 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2988` → IC=+0.173 (n=653)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2988 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.4833` → IC=+0.192 (n=653)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.4833 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.2004` → IC=+0.173 (n=653)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.2004 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.118` → IC=+0.234 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.118 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6967` → IC=+0.221 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6967 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.219 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.4443` → IC=+0.164 (n=545)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.4443 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.4043` → IC=+0.160 (n=545)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4043 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `15532.7795` → IC=+0.159 (n=218)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 15532.7795 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `238.0` → IC=+0.167 (n=154)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 238.0 (IC base=+0.154)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.221 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.2845` → IC=+0.186 (n=523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.2845 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.193 (n=203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 5.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.569` → IC=+0.314 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.569 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1304` → IC=+0.168 (n=215)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1304 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `3.9175` → IC=+0.161 (n=532)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 3.9175 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `1.7083` → IC=+0.161 (n=532)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7083 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=599)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.213 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.258 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.2233` → IC=+0.256 (n=310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2233 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.257 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3724` → IC=+0.273 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3724 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.609` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.609 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3666` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3666 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.6637` → IC=+0.235 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6637 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.364` → IC=+0.225 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.364 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1855.026` → IC=+0.239 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1855.026 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.209 (n=380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.1299` → IC=+0.176 (n=251)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1299 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.174 (n=584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.4382` → IC=+0.202 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4382 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.1538` → IC=+0.191 (n=399)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1538 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.328` → IC=+0.271 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.328 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.2113` → IC=+0.224 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2113 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2487` → IC=+0.218 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2487 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4303` → IC=+0.156 (n=184)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4303 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.6272` → IC=+0.204 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6272 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=634)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `8750.1763` → IC=+0.193 (n=379)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 8750.1763 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.146 (n=340)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 135.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.160 (n=639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0076 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.381` → IC=+0.154 (n=639)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.381 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.171 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.3925` → IC=+0.202 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3925 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.3513` → IC=+0.145 (n=700)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3513 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.371` → IC=+0.201 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.371 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.1618` → IC=+0.140 (n=639)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1618 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.613` → IC=+0.141 (n=639)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.613 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1051` → IC=+0.174 (n=216)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1051 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.8616` → IC=+0.152 (n=354)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.8616 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `2.5391` → IC=+0.165 (n=177)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5391 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5079.8508` → IC=+0.145 (n=426)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 5079.8508 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `181.0` → IC=+0.128 (n=401)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 181.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.154 (n=642)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0065 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.193 (n=717)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5385 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.9064` → IC=+0.242 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9064 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.352` → IC=+0.269 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.352 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.7086` → IC=+0.129 (n=640)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.7086 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` < `0.1682` → IC=+0.133 (n=714)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1682 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4397` → IC=+0.151 (n=227)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4397 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3182.8788` → IC=+0.218 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3182.8788 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.147 (n=525)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 57.0 (IC base=+0.113)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.153 (n=298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0094 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.5245` → IC=+0.138 (n=652)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.5245 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.4642` → IC=+0.228 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4642 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.2538` → IC=+0.147 (n=613)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2538 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.22` → IC=+0.176 (n=254)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.22 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.1973` → IC=+0.151 (n=652)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1973 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.8568` → IC=+0.149 (n=434)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.8568 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `2.3273` → IC=+0.209 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3273 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `3176.6468` → IC=+0.176 (n=217)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3176.6468 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0177` → IC=+0.214 (n=488)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0177 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.1739` → IC=+0.211 (n=323)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1739 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.271 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.2567` → IC=+0.229 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2567 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.219` → IC=+0.242 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.219 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` > `0.686` → IC=+0.210 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.686 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.0832` → IC=+0.248 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0832 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `2.5276` → IC=+0.209 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5276 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.194 (n=844)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.275 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.6471` → IC=+0.222 (n=740)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6471 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.219 (n=340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.246 (n=337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.41` → IC=+0.256 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.41 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.5192` → IC=+0.218 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5192 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.833` → IC=+0.268 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.833 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.6917` → IC=+0.234 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6917 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.6631` → IC=+0.227 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6631 (IC base=+0.211)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.168 (n=266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0097 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.170 (n=716)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 9.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.4762` → IC=+0.168 (n=797)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.4762 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.9607` → IC=+0.221 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9607 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.14` → IC=+0.181 (n=202)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 8.14 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.159 (n=429)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8709 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.1751` → IC=+0.154 (n=215)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.1751 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1796` → IC=+0.173 (n=221)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1796 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.2724` → IC=+0.149 (n=653)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.2724 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.8529` → IC=+0.142 (n=495)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8529 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=596)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `7277.355` → IC=+0.175 (n=266)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7277.355 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.184 (n=194)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 12.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.31` → IC=+0.134 (n=544)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.31 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.149 (n=297)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 20.0 (IC base=+0.069)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.152 (n=116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0036 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.174 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 10.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.6242` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.6242 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.7807` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7807 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.673` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.673 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.573` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.573 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `11027.9657` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11027.9657 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 165.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.6147` → IC=+0.143 (n=239)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6147 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.021` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.021 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 146.0 (IC base=+0.062)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.269 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.309 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.291 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` > `0.7776` → IC=+0.313 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7776 (IC base=+0.262)

- **PATRÓN** `dist_vwap_pct` > `0.1807` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1807 (IC base=+0.262)

- **PATRÓN** `dist_vwap_pct` < `0.8295` → IC=+0.268 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8295 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.247` → IC=+0.319 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.247 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` < `0.8463` → IC=+0.276 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8463 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` > `1.1816` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1816 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.3885` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3885 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.0848` → IC=+0.322 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0848 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1033` → IC=+0.167 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1033 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `10445.3218` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 10445.3218 (IC base=+0.048)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5758` → IC=-0.177 (n=60)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5758
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=180)

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
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 14.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` > `0.85` → IC=+0.180 (n=120)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.85 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.6912` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6912 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 25.0 (IC base=-0.045)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0215` → IC=+0.155 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0215 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3042` → IC=+0.159 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3042 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.180 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 16.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.140 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 10.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.164 (n=138)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.4 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1962` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1962 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.4434` → IC=+0.147 (n=154)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.4434 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.183 (n=118)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.9857` → IC=+0.142 (n=121)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.9857 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.6516` → IC=+0.161 (n=122)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6516 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.2212` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.2212 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.9259` → IC=+0.205 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9259 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.225 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0146` → IC=+0.204 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0146 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.27` → IC=+0.122 (n=96)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.27 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0263` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0263 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.481` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.481 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.137 (n=144)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6197 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2474` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2474 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.8779` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.8779 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 15.0 (IC base=+0.111)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.201 (n=2075)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=4607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.2357` → IC=+0.201 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2357 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.639` → IC=+0.222 (n=2570)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.639 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.159 (n=2111)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8847 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `1.0878` → IC=+0.154 (n=1435)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.0878 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1676` → IC=+0.190 (n=1238)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1676 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.8746` → IC=+0.172 (n=2830)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8746 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.168 (n=4317)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3848.1598` → IC=+0.188 (n=1524)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3848.1598 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.211 (n=2149)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.197 (n=4224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0108 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.4823` → IC=+0.198 (n=4222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.4823 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.206 (n=1866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.5625` → IC=+0.241 (n=4224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5625 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.45` → IC=+0.174 (n=2973)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.45 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.672` → IC=+0.212 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.672 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.585` → IC=+0.189 (n=4154)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.585 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.6228` → IC=+0.173 (n=1005)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6228 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.249 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.3149` → IC=+0.203 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3149 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `140.0` → IC=+0.182 (n=3094)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 140.0 (IC base=+0.189)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.185 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0053 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.235 (n=341)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.215 (n=279)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.073` → IC=+0.296 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.073 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2211` → IC=+0.259 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2211 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5882` → IC=+0.180 (n=295)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5882 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.8897` → IC=+0.174 (n=446)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8897 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.231 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.276 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.277 (n=553)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.1757` → IC=+0.295 (n=369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1757 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.278 (n=508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.280 (n=556)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.4087` → IC=+0.306 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4087 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.482` → IC=+0.285 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.482 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.1771` → IC=+0.309 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1771 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `1.517` → IC=+0.290 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.517 (IC base=+0.270)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.274 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `1456.1771` → IC=+0.280 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1456.1771 (IC base=+0.270)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.271 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.270)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.179 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.003 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.163 (n=250)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0069 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0968` → IC=+0.171 (n=250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0968 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.184 (n=672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.3271` → IC=+0.206 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3271 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.2372` → IC=+0.220 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2372 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.181 (n=183)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.417` → IC=+0.174 (n=652)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 4.417 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2687` → IC=+0.167 (n=749)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2687 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.1034` → IC=+0.170 (n=340)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1034 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.0723` → IC=+0.176 (n=627)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0723 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.147` → IC=+0.188 (n=206)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.147 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `2.4168` → IC=+0.179 (n=700)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.4168 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.7228` → IC=+0.182 (n=466)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.7228 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `10634.3743` → IC=+0.189 (n=669)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 10634.3743 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.171 (n=687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0062 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.2725` → IC=+0.178 (n=604)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2725 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.167 (n=709)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 18.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.199 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` < `0.2091` → IC=+0.178 (n=609)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2091 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.732` → IC=+0.201 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.732 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `0.6181` → IC=+0.236 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6181 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.1411` → IC=+0.229 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1411 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.3982` → IC=+0.194 (n=197)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.3982 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `2.0753` → IC=+0.178 (n=268)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.0753 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.187 (n=164)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 288.0 (IC base=+0.162)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.242 (n=219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.242 (n=308)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.6825` → IC=+0.253 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6825 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.609` → IC=+0.342 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.609 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.2205` → IC=+0.211 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2205 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `3.9512` → IC=+0.201 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.9512 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.4715` → IC=+0.203 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4715 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `1451.2984` → IC=+0.208 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1451.2984 (IC base=+0.204)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.263 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 63.0 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.290 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.243)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.249 (n=301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.269 (n=301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.4048` → IC=+0.296 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4048 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.453` → IC=+0.301 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.453 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.3579` → IC=+0.289 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3579 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `3.0458` → IC=+0.248 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0458 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.3386` → IC=+0.223 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3386 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.244 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.220 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.243)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.159 (n=664)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0071 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.160 (n=686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 8.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.7425` → IC=+0.241 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7425 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.383` → IC=+0.190 (n=308)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.383 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.371` → IC=+0.172 (n=345)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.371 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.9021` → IC=+0.172 (n=504)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.9021 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `1.2078` → IC=+0.158 (n=252)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.2078 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.225 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1579` → IC=+0.203 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1579 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=820)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `9488.8794` → IC=+0.245 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9488.8794 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.160 (n=530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0072 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4487` → IC=+0.157 (n=602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4487 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.178 (n=299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 8.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6727` → IC=+0.180 (n=602)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6727 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4106` → IC=+0.140 (n=600)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.4106 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.341` → IC=+0.226 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.341 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.291` → IC=+0.138 (n=570)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.291 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.825` → IC=+0.139 (n=402)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.825 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1367` → IC=+0.170 (n=201)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1367 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.5341` → IC=+0.161 (n=181)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5341 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `11624.4939` → IC=+0.209 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11624.4939 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `192.0` → IC=+0.155 (n=462)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 192.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.146 (n=527)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0085 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.136 (n=539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 12.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.48` → IC=+0.180 (n=791)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.48 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `1.1427` → IC=+0.197 (n=153)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 1.1427 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.428` → IC=+0.222 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.428 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2940.9508` → IC=+0.271 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2940.9508 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.143 (n=499)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 54.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.169 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1316` → IC=+0.173 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1316 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.143 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.138 (n=285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 6.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.200 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.5202` → IC=+0.136 (n=731)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.5202 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.205` → IC=+0.136 (n=754)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.205 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.8761` → IC=+0.136 (n=509)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8761 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.0725` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0725 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.142 (n=205)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.1908` → IC=+0.146 (n=278)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1908 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2637.4052` → IC=+0.164 (n=346)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2637.4052 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.028` → IC=+0.258 (n=291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.028 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.1698` → IC=+0.251 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1698 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.172` → IC=+0.245 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.172 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.230 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.1676` → IC=+0.243 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1676 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4407` → IC=+0.202 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4407 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.208 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.283 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.224 (n=320)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.5323` → IC=+0.217 (n=843)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5323 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.218 (n=1006)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.4984` → IC=+0.266 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4984 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.5002` → IC=+0.219 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5002 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.288` → IC=+0.281 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.288 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.7056` → IC=+0.224 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7056 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.310 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.8679` → IC=+0.214 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8679 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.189 (n=679)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 34.0 (IC base=+0.212)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=1718)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.134 (n=1311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.01 (IC base=+0.121)

- **PATRÓN** `drift_60min` |x|≤ `0.5519` → IC=+0.132 (n=1490)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.5519 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.168 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 18.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.921` → IC=+0.191 (n=497)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.921 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.976` → IC=+0.123 (n=1512)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 5.976 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.8968` → IC=+0.122 (n=665)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.8968 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.175` → IC=+0.149 (n=406)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.175 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.4626` → IC=+0.150 (n=492)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4626 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `1.8992` → IC=+0.140 (n=983)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.8992 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `8988.6997` → IC=+0.137 (n=676)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 8988.6997 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.174 (n=434)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0039 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.4002` → IC=+0.154 (n=1144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4002 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.146 (n=498)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.153 (n=572)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.4828` → IC=+0.132 (n=359)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.4828 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.363` → IC=+0.138 (n=1298)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.363 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2326` → IC=+0.136 (n=1269)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2326 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.069` → IC=+0.146 (n=619)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.069 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.4847` → IC=+0.135 (n=1287)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.4847 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.794` → IC=+0.130 (n=858)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.794 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=1718)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `8426.6807` → IC=+0.136 (n=1162)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 8426.6807 (IC base=+0.126)

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

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.173 (n=273)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0035 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.0862` → IC=+0.149 (n=206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0862 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.1703` → IC=+0.163 (n=271)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1703 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.141 (n=614)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.151 (n=411)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8709 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.0622` → IC=+0.154 (n=290)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0622 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.147 (n=205)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `11116.1452` → IC=+0.126 (n=616)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 11116.1452 (IC base=+0.114)

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
- **PATRÓN** `sigma_h` < `0.009` → IC=+0.152 (n=547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.009 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.136 (n=548)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0046 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4818` → IC=+0.150 (n=547)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4818 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.159 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.186` → IC=+0.149 (n=548)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.186 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `1.0816` → IC=+0.177 (n=125)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 1.0816 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4443` → IC=+0.147 (n=516)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.4443 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.953` → IC=+0.151 (n=549)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.953 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2728` → IC=+0.147 (n=547)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2728 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.1177` → IC=+0.140 (n=503)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1177 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1784` → IC=+0.152 (n=162)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1784 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.825` → IC=+0.140 (n=359)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.825 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8953.8054` → IC=+0.148 (n=489)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 8953.8054 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.170 (n=362)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0078 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4222` → IC=+0.208 (n=361)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4222 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.148 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.156 (n=274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 10.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.1096` → IC=+0.160 (n=410)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.1096 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.155 (n=416)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.4298 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.921` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 10.921 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.170 (n=410)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2227 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.7334` → IC=+0.147 (n=366)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7334 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.1489` → IC=+0.152 (n=418)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1489 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.159 (n=180)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.1791` → IC=+0.171 (n=354)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1791 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.163 (n=402)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `8176.6816` → IC=+0.163 (n=410)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8176.6816 (IC base=+0.146)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `dist_vwap_pct` < `0.7269` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7269
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=28)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.008)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.290 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=181)

- **FILTRO** `dist_vwap_pct` > `0.1153` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1153
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=82)

- **FILTRO** `volumen_regimen` > `0.8474` → IC=-0.134 (n=69)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8474
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=70)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.208 (n=224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.256 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.3935` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3935 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.919` → IC=+0.288 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.919 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.6313` → IC=+0.185 (n=109)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6313 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `1.0983` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.0983 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.0797` → IC=+0.228 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0797 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.367 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `1.7631` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7631 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.201 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `1319.0384` → IC=+0.188 (n=197)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1319.0384 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.0875` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0875 (IC base=-0.130)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0059` → IC=-0.167 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0059
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=60)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.235 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.175 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 10.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.7937` → IC=+0.241 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7937 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.3468` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3468 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.206` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.206 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6265` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6265 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.0651` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0651 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.1124` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1124 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.6708` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6708 (IC base=+0.128)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.357 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=58)

- **FILTRO** `ibs_20min` > `0.1031` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1031
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=13)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.181 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.007 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.5632` → IC=+0.298 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5632 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.4727` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4727 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1427` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1427 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.249` → IC=+0.333 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.249 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.789` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.789 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.0453` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0453 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.1428` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1428 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.6009` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6009 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2227.7698` → IC=+0.245 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2227.7698 (IC base=+0.148)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0159` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0159
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=64)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.273 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=43)

- **FILTRO** `volumen_regimen` > `0.8617` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8617
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.045)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6667 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.9778` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9778 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.36` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.36 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` > `0.9891` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.9891 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.0856` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0856 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `2.0054` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.0054 (IC base=+0.045)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.04 (IC base=+0.045)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `14.0` → IC=-0.463 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=78)

- **FILTRO** `ibs_20min` < `0.6316` → IC=-0.335 (n=77)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6316
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `volumen_pendiente_norm` < `0.1779` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1779
  - _Potencial_: sin este filtro IC_bueno=-0.375 (n=6)

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
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `volumen_regimen` > `0.6161` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.6161
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.220 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `ibs_20min` < `0.5833` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.447 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.6292` → IC=-0.232 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6292
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=165)

- **FILTRO** `ibs_20min` > `0.4` → IC=-0.154 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=160)

- **PATRÓN** `ibs_20min` > `0.6292` → IC=+0.129 (n=165)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.6292 (IC base=+0.038)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.123 (n=160)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.4 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.892` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 5.892 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.0687` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.0687 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `3965.7979` → IC=+0.153 (n=73)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3965.7979 (IC base=+0.053)

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
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=33)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0023 (IC base=+0.082)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.149 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.7289` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7289 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.0986` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.0986 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.514` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 7.514 (IC base=+0.082)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.302` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.302 (IC base=+0.054)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.55` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `dist_vwap_pct` > `0.1937` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1937
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `volumen_regimen` < `0.9796` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9796
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **PATRÓN** `ibs_20min` < `0.75` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.75 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.7917 (IC base=+0.084)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.084)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2814.271` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2814.271 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2261.2692` → IC=+0.135 (n=228)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2261.2692 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2814.271` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2814.271 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2261.2692` → IC=+0.135 (n=228)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2261.2692 (IC base=+0.103)

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
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=166)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=1046)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=47)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=79)

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

- **FILTRO** `libro_liquidez` < `15381.0964` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 15381.0964
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

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
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=348)

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
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=157)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=157)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=115)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=115)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.151 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=89)

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
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=47)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.177 (n=1443)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=4342)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.183 (n=1476)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=4544)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.222 (n=221)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=667)

- **FILTRO** `ibs_20min` < `0.7348` → IC=-0.210 (n=222)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7348
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=666)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.161 (n=249)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=801)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.185 (n=233)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=727)

- **FILTRO** `ballena_activa_n` > `60.0` → IC=-0.151 (n=239)

  - _Acción_: SKIP cuando `ballena_activa_n` > 60.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=721)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=925)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.202 (n=303)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=638)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.221 (n=238)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=778)

- **FILTRO** `ibs_20min` > `0.7162` → IC=-0.198 (n=253)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7162
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=763)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.167 (n=232)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=742)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.171 (n=238)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=736)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.144 (n=262)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=711)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.163 (n=250)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=758)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.203 (n=224)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=692)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=901)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.185 (n=328)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=684)

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
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=461)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=467)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.242 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

- **FILTRO** `ibs_20min` > `0.8905` → IC=-0.173 (n=47)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8905
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `libro_liquidez` < `15251.0076` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 15251.0076
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `drift_20min_pct` |x|> `0.1641` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1641
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=82)

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
- **FILTRO** `hora_utc` < `7.0` → IC=-0.135 (n=3524)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=10627)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.282 (n=3479)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=10672)

- **FILTRO** `ibs_7min` < `0.712` → IC=-0.246 (n=3537)

  - _Acción_: SKIP cuando `ibs_7min` < 0.712
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=10614)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.171 (n=4733)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=9418)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.220 (n=4380)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=13431)

- **FILTRO** `ibs_7min` > `0.7143` → IC=-0.172 (n=4437)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=13374)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.155 (n=604)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=1458)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=509)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1553)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.260 (n=678)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=1384)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.228 (n=512)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=1550)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.230 (n=765)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2333)

- **FILTRO** `drift_7min_pct` |x|> `0.114` → IC=-0.128 (n=1053)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.114
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2045)

- **FILTRO** `ibs_7min` > `0.8333` → IC=-0.188 (n=774)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8333
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2324)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=573)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=2070)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.259 (n=642)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2001)

- **FILTRO** `ibs_7min` < `0.7711` → IC=-0.195 (n=660)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7711
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=1983)

- **FILTRO** `ballena_activa_n` > `168.0` → IC=-0.179 (n=656)

  - _Acción_: SKIP cuando `ballena_activa_n` > 168.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1987)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.248 (n=613)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2039)

- **FILTRO** `ballena_activa_n` > `107.0` → IC=-0.174 (n=894)

  - _Acción_: SKIP cuando `ballena_activa_n` > 107.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1758)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.184 (n=657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=1436)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.311 (n=665)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1428)

- **FILTRO** `ibs_7min` < `0.2135` → IC=-0.290 (n=523)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2135
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=1570)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.252 (n=493)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=1600)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.225 (n=742)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2451)

- **FILTRO** `ibs_7min` > `0.797` → IC=-0.171 (n=798)

  - _Acción_: SKIP cuando `ibs_7min` > 0.797
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2395)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.139 (n=718)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=1682)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.259 (n=586)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=1814)

- **FILTRO** `ibs_7min` < `0.7519` → IC=-0.194 (n=600)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7519
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=1800)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.177 (n=805)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=1595)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.239 (n=783)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1627)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.180 (n=602)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=1808)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.183 (n=591)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=1819)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.250 (n=638)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2002)

- **FILTRO** `ibs_7min` < `0.7353` → IC=-0.213 (n=660)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7353
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1980)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.193 (n=626)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=2014)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.178 (n=800)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=2546)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.123 (n=739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=1574)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.297 (n=565)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1748)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.248 (n=574)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1739)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.233 (n=559)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1754)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.254 (n=612)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=2500)

- **FILTRO** `ibs_7min` > `0.7767` → IC=-0.162 (n=777)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7767
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2335)

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

- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.143 (n=508)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.177 (n=162)

  - _Acción_: Kelly boost +0.88€ cuando `total_vol_5m` < 451.687 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=227)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3299.6255` → IC=+0.153 (n=197)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3299.6255 (IC base=+0.130)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.259 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4125` → IC=+0.190 (n=56)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.4125 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.131 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 10.0 (IC base=+0.111)

- **PATRÓN** `total_vol_5m` < `699.4537` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `total_vol_5m` < 699.4537 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `7404.0146` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7404.0146 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 135.0 (IC base=+0.111)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4038` → IC=+0.227 (n=75)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4038 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.196)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 6300.756 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `3757.1854` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3757.1854 (IC base=+0.196)

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

- **PATRÓN** `pct_vs_K` |x|≤ `1.2308` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.2308 (IC base=-0.048)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.289 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=34)

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
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=270)

- **PATRÓN** `streak_estiramiento` < `0.3697` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.3697 (IC base=+0.038)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=537)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=264)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=357)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1581)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=886)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=894)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.165 (n=174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0035 (IC base=+0.124)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.145 (n=347)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0053 (IC base=+0.124)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0599` → IC=+0.130 (n=520)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio_macro` |x|> 0.0599 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.138 (n=558)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 19.0 (IC base=+0.124)

- **PATRÓN** `ibs_15` > `0.5787` → IC=+0.215 (n=520)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5787 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.4346` → IC=+0.149 (n=132)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.4346 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.5526` → IC=+0.120 (n=538)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.5526 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.701` → IC=+0.205 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.701 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=538)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3043.835` → IC=+0.150 (n=347)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3043.835 (IC base=+0.124)

### UPDOWN_GBM#5min
- **FILTRO** `sigma_ewma_delta_pct` > `6.469` → IC=-0.205 (n=59)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.469
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=802)

### UPDOWN_GBM#60min
- **FILTRO** `ibs_15` < `0.1763` → IC=-0.167 (n=25)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1763
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=77)

- **FILTRO** `sigma_ewma_delta_pct` > `16.462` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.462
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=59)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.005` → IC=-0.167 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=138)

- **FILTRO** `ibs_15` > `0.6398` → IC=-0.160 (n=45)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.6398
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=139)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.186 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0031 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.171 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0045 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.1916` → IC=+0.195 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1916 (IC base=+0.165)

- **PATRÓN** `drift_15min` |x|≤ `0.4863` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.4863 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.192 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 4.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.165 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_15` > `0.8791` → IC=+0.282 (n=99)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8791 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.3112` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3112 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` < `0.5508` → IC=+0.169 (n=164)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.5508 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.708` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 18.708 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `13923.332` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13923.332 (IC base=+0.165)

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
- **FILTRO** `ibs_15` < `0.6404` → IC=-0.191 (n=40)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6404
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=123)

- **PATRÓN** `ibs_15` > `0.9606` → IC=+0.151 (n=41)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.76€ cuando `ibs_15` > 0.9606 (IC base=+0.011)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.671` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 18.671 (IC base=+0.011)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6314` → IC=-0.233 (n=43)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6314
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1908` → IC=+0.145 (n=60)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio_macro` |x|> 0.1908 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.192 (n=131)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.6314 (IC base=+0.085)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=72)

- **FILTRO** `dist_vwap_pct` > `0.1505` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1505
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=84)

- **FILTRO** `drift_15min` |x|> `0.5024` → IC=-0.153 (n=142)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5024
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=428)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.5217` → IC=-0.241 (n=25)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5217
  - _Potencial_: sin este filtro IC_bueno=+0.259 (n=52)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0636` → IC=+0.133 (n=58)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0636 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.5217` → IC=+0.259 (n=52)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5217 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.141` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.141 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2991.1392` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2991.1392 (IC base=+0.095)

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

- **PATRÓN** `dist_vwap_pct` < `0.4088` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.4088 (IC base=+0.012)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0501` → IC=+0.152 (n=136)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.0501 (IC base=+0.107)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.161 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 6.0 (IC base=+0.107)

- **PATRÓN** `ibs_15` > `0.5556` → IC=+0.196 (n=123)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.5556 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.4521` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4521 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.422` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.422 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=119)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2489.2422` → IC=+0.161 (n=122)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2489.2422 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.107)

- **PATRÓN** `ibs_15` < `0.1304` → IC=+0.171 (n=162)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.1304 (IC base=+0.032)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.396 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.327)

- **PATRÓN** `drift_60min` |x|≤ `0.1155` → IC=+0.356 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1155 (IC base=+0.327)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.340 (n=129)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.327)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.342 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.327)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.326 (n=199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.327)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.372 (n=194)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.327)

- **PATRÓN** `dist_vwap_pct` > `0.156` → IC=+0.347 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.156 (IC base=+0.327)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.729` → IC=+0.326 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.729 (IC base=+0.327)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.888` → IC=+0.329 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.888 (IC base=+0.327)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.328 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.327)

- **PATRÓN** `libro_liquidez` > `11281.6823` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11281.6823 (IC base=+0.327)

- **PATRÓN** `ballena_activa_n` < `521.0` → IC=+0.378 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 521.0 (IC base=+0.327)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1204` → IC=+0.350 (n=38)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1204 (IC base=+0.316)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.314 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.316)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.375 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.316)

- **PATRÓN** `drift_60min` |x|≤ `0.162` → IC=+0.333 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.162 (IC base=+0.316)

- **PATRÓN** `drift_15min` |x|≤ `0.4136` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4136 (IC base=+0.316)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0919` → IC=+0.316 (n=101)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0919 (IC base=+0.316)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.345 (n=121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.316)

- **PATRÓN** `ibs_15` > `0.9234` → IC=+0.383 (n=75)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9234 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` > `0.2747` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2747 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.509` → IC=+0.332 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.509 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `11333.8932` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11333.8932 (IC base=+0.316)

- **PATRÓN** `ballena_activa_n` < `613.0` → IC=+0.424 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 613.0 (IC base=+0.316)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.342 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.372 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.377 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.355 (n=81)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2105` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2105 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.335 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.336)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.346 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.7785` → IC=+0.404 (n=81)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7785 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` < `0.3445` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3445 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` < `20.548` → IC=+0.337 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 20.548 (IC base=+0.336)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `2812.5928` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2812.5928 (IC base=+0.336)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.206 (n=335)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=1006)

- **FILTRO** `ibs_15` < `0.4909` → IC=-0.223 (n=117)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4909
  - _Potencial_: sin este filtro IC_bueno=+0.183 (n=351)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=345)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=996)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.297` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.297 (IC base=-0.070)

- **PATRÓN** `ibs_15` > `0.4909` → IC=+0.183 (n=351)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.4909 (IC base=-0.070)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1246` → IC=+0.236 (n=294)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1246 (IC base=-0.065)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1028` → IC=+0.249 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1028 (IC base=-0.065)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.268 (n=441)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.484` → IC=+0.216 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.484 (IC base=-0.065)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.220 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=-0.065)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_15` < `0.6975` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6975
  - _Potencial_: sin este filtro IC_bueno=+0.291 (n=41)

- **FILTRO** `sigma_h` > `0.0075` → IC=-0.239 (n=224)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=676)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.232 (n=297)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=603)

- **FILTRO** `drift_15min` |x|> `0.7406` → IC=-0.203 (n=224)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7406
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=676)

- **FILTRO** `sigma_ewma_delta_pct` > `19.563` → IC=-0.252 (n=163)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.563
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=737)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1731` → IC=+0.152 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1731 (IC base=+0.018)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1355` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1355 (IC base=+0.018)

- **PATRÓN** `ibs_15` > `0.6975` → IC=+0.291 (n=41)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6975 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` > `0.1982` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1982 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` < `0.3651` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3651 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `435.0` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 435.0 (IC base=+0.018)

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

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.247 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.211 (n=223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.4455` → IC=+0.220 (n=223)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4455 (IC base=+0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0918` → IC=+0.221 (n=199)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0918 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.225 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.270 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.209)

- **PATRÓN** `ibs_15` < `0.2963` → IC=+0.294 (n=197)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2963 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.2394` → IC=+0.220 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2394 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.4132` → IC=+0.209 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4132 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.326` → IC=+0.225 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.326 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `11493.267` → IC=+0.209 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11493.267 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `181.0` → IC=+0.208 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 181.0 (IC base=+0.209)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0104` → IC=-0.250 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0104
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=249)

- **FILTRO** `drift_60min` |x|> `0.1657` → IC=-0.184 (n=112)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1657
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=219)

- **FILTRO** `drift_15min` |x|> `0.8686` → IC=-0.262 (n=82)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8686
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=249)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.153 (n=119)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=212)

- **PATRÓN** `ibs_15` > `0.8182` → IC=+0.222 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8182 (IC base=-0.128)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1232` → IC=+0.167 (n=64)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.1232 (IC base=-0.048)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1809` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1809 (IC base=-0.048)

- **PATRÓN** `ibs_15` < `0.3814` → IC=+0.214 (n=96)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3814 (IC base=-0.048)

- **PATRÓN** `dist_vwap_pct` < `0.6071` → IC=+0.176 (n=100)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.6071 (IC base=-0.048)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 41.0 (IC base=-0.048)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0227` → IC=-0.252 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0227
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=241)

- **FILTRO** `drift_15min` |x|> `1.2` → IC=-0.250 (n=90)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=274)

- **FILTRO** `sigma_ewma_delta_pct` > `3.98` → IC=-0.174 (n=130)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.98
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=234)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.267 (n=41)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=323)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1618` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1618 (IC base=-0.059)

- **PATRÓN** `ibs_15` < `0.0514` → IC=+0.316 (n=36)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0514 (IC base=-0.059)

- **PATRÓN** `ibs_15` > `0.2737` → IC=+0.280 (n=48)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.2737 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.5815` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5815 (IC base=-0.059)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.289 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.059)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.085)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.085)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.287 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.303 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.323 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.302 (n=220)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8348` → IC=+0.319 (n=330)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8348 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.3131` → IC=+0.329 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3131 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.92` → IC=+0.287 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 18.92 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.289 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `12448.5931` → IC=+0.329 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12448.5931 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.297 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.305 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.1596` → IC=+0.298 (n=166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1596 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.311 (n=125)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.9689` → IC=+0.339 (n=85)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9689 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.3217` → IC=+0.352 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3217 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.121` → IC=+0.287 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.121 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `15285.027` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15285.027 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.293 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.292 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0682` → IC=+0.331 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0682 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1881` → IC=+0.321 (n=65)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1881 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2866` → IC=+0.319 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2866 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.321 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.846` → IC=+0.321 (n=143)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.846 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.0935` → IC=+0.309 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0935 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` < `0.4822` → IC=+0.288 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4822 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.791` → IC=+0.294 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.791 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.469` → IC=+0.297 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.469 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.286)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5787 sube el IC de +0.124 a +0.215 en UPDOWN_GBM#15min (n=520). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8791 sube el IC de +0.165 a +0.282 en UPDOWN_GBM#BTC#15min (n=99). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6314 sube el IC de +0.085 a +0.192 en UPDOWN_GBM#ETH#15min (n=131). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5217 sube el IC de +0.095 a +0.259 en UPDOWN_GBM#SOL#15min (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5556 sube el IC de +0.107 a +0.196 en UPDOWN_GBM#XRP#15min (n=123). Ya aplicado como kelly_boost=+0.98€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1304 sube el IC de +0.032 a +0.171 en UPDOWN_GBM#XRP#15min (n=162). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#60min**: dentro de BUY_YES, IBS > 0.9606 sube el IC de +0.011 a +0.151 en UPDOWN_GBM#BTC#60min (n=41). Ya aplicado como kelly_boost=+0.76€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.4909 sube el IC de -0.070 a +0.183 en UPDOWN_GBM_15M_TARDIO (n=351). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3696 sube el IC de -0.065 a +0.268 en UPDOWN_GBM_15M_TARDIO (n=441). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.6975 sube el IC de +0.018 a +0.291 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=41). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5457 sube el IC de +0.079 a +0.208 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=166). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2963 sube el IC de +0.209 a +0.294 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=197). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8182 sube el IC de -0.128 a +0.222 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3814 sube el IC de -0.048 a +0.214 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=96). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.0514 sube el IC de -0.059 a +0.316 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=36). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS > 0.2737 sube el IC de -0.059 a +0.280 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=48). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8348 sube el IC de +0.285 a +0.319 en UPDOWN_GBM_IBS_ALTO (n=330). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9689 sube el IC de +0.282 a +0.339 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=85). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.846 sube el IC de +0.286 a +0.321 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=143). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.327 a +0.372 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=194). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.9234 sube el IC de +0.316 a +0.383 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=75). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7785 sube el IC de +0.336 a +0.404 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=81). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.365 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.365 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `BALLENAS_CONFIRMADAS_15M#XRP#15min` — IC=+0.129 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `BALLENAS_CONFIRMADAS_15M#XRP` — IC=+0.129 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 801 | +0.087 | +44.29€ | 2 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 801 | +0.087 | +44.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 23 | +0.060 | +0.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 23 | +0.060 | +0.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 523 | +0.106 | +36.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 523 | +0.106 | +36.75€ | 2 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 33 | +0.129 | +7.38€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 33 | +0.129 | +7.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 14741 | -0.111 | -2486.94€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 954 | -0.009 | -140.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 13787 | -0.118 | -2346.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1913 | -0.090 | -417.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1913 | -0.090 | -417.54€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 954 | -0.009 | -140.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 954 | -0.009 | -140.48€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1960 | -0.167 | -529.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1960 | -0.167 | -529.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 3944 | -0.049 | -364.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 3944 | -0.049 | -364.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 3274 | -0.128 | -288.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 3274 | -0.128 | -288.35€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2696 | -0.194 | -746.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2696 | -0.194 | -746.52€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 4035 | -0.072 | +1809.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 1149 | -0.009 | +854.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 2886 | -0.097 | +955.67€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 4035 | -0.072 | +1809.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 1149 | -0.009 | +854.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 2886 | -0.097 | +955.67€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 87 | -0.073 | -15.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 87 | -0.073 | -15.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 87 | -0.073 | -15.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 87 | -0.073 | -15.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 47507 | +0.113 | -3014.35€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 7946 | +0.184 | -276.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 162 | -0.110 | -54.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 35659 | +0.098 | -2614.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3740 | +0.117 | -70.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 5991 | +0.081 | -811.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 26 | -0.107 | +5.05€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 5950 | +0.083 | -804.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 9525 | +0.132 | -228.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2338 | +0.197 | -113.96€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 5888 | +0.109 | -143.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1257 | +0.127 | +50.51€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 6006 | +0.081 | -770.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 28 | +0.033 | +3.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#240min | 9 | -0.143 | -7.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 5969 | +0.082 | -767.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 10279 | +0.127 | -155.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2961 | +0.172 | -13.65€ | 1 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 5928 | +0.112 | -94.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1378 | +0.096 | -39.04€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 9718 | +0.125 | -629.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2573 | +0.192 | -159.26€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 79 | -0.006 | -2.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 5961 | +0.097 | -385.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1105 | +0.131 | -81.51€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 5988 | +0.104 | -418.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 20 | +0.000 | +1.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 5 | -0.018 | -1.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 5963 | +0.105 | -418.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 7906 | +0.177 | -616.97€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 7906 | +0.177 | -616.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2017 | +0.165 | -227.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2017 | +0.165 | -227.25€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 146 | -0.135 | -1.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 146 | -0.135 | -1.74€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1971 | +0.169 | -209.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1971 | +0.169 | -209.27€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1766 | +0.238 | -38.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1766 | +0.238 | -38.03€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1927 | +0.182 | -154.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1927 | +0.182 | -154.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 396 | +0.447 | +4.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 396 | +0.447 | +4.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 149 | +0.440 | +0.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 149 | +0.440 | +0.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 154 | +0.442 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 154 | +0.442 | +1.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 89 | +0.445 | +2.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 89 | +0.445 | +2.27€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 25324 | +0.188 | -2403.33€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 25324 | +0.188 | -2403.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 4514 | +0.146 | -728.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 4514 | +0.146 | -728.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 3949 | +0.226 | -138.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 3949 | +0.226 | -138.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 4386 | +0.161 | -604.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 4386 | +0.161 | -604.57€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 4022 | +0.220 | -162.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 4022 | +0.220 | -162.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 4185 | +0.199 | -317.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 4185 | +0.199 | -317.11€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 4268 | +0.183 | -452.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 4268 | +0.183 | -452.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 9201 | +0.132 | +338.17€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 9201 | +0.132 | +338.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 4571 | +0.137 | +207.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 4571 | +0.137 | +207.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 4630 | +0.127 | +130.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 4630 | +0.127 | +130.86€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 946 | +0.294 | -5.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 946 | +0.294 | -5.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 409 | +0.276 | -13.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 409 | +0.276 | -13.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 445 | +0.301 | +9.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 445 | +0.301 | +9.14€ | 0 | 5 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 464 | +0.103 | +2.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 155 | +0.099 | -3.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 309 | +0.104 | +5.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 26 | +0.143 | +2.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 26 | +0.143 | +2.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 367 | +0.113 | +10.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 58 | +0.150 | +5.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 309 | +0.104 | +5.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 71 | +0.034 | -11.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 71 | +0.034 | -11.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 13790 | +0.094 | -539.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1243 | +0.071 | -33.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 12547 | +0.096 | -505.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 8315 | +0.097 | -198.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1243 | +0.071 | -33.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 7072 | +0.101 | -164.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 1695 | +0.119 | +39.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 1695 | +0.119 | +39.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 3780 | +0.076 | -379.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 3780 | +0.076 | -379.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 556 | +0.265 | -60.19€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 556 | +0.265 | -60.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 556 | +0.265 | -60.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 556 | +0.265 | -60.19€ | 0 | 4 |
| ✅ GBM_LATE_15M | 11910 | +0.057 | +5038.41€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 11910 | +0.057 | +5038.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1809 | +0.195 | +1319.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1809 | +0.195 | +1319.75€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 1786 | +0.174 | +1191.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1786 | +0.174 | +1191.04€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 1851 | +0.196 | +1351.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1851 | +0.196 | +1351.20€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 1861 | -0.037 | +103.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1861 | -0.037 | +103.06€ | 3 | 12 |
| ✅ GBM_LATE_15M#SOL | 1943 | -0.048 | +468.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1943 | -0.048 | +468.91€ | 5 | 5 |
| ✅ GBM_LATE_15M#XRP | 2660 | -0.069 | +604.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2660 | -0.069 | +604.44€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 12656 | +0.061 | +6614.87€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 12656 | +0.061 | +6614.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 2176 | -0.005 | +1689.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 2176 | -0.005 | +1689.21€ | 2 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2755 | -0.022 | +412.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2755 | -0.022 | +412.20€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1646 | +0.258 | +1628.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1646 | +0.258 | +1628.49€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1944 | -0.048 | +58.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1944 | -0.048 | +58.12€ | 8 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2099 | -0.014 | +747.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2099 | -0.014 | +747.09€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2036 | +0.265 | +2079.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2036 | +0.265 | +2079.77€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 9815 | +0.170 | +6972.59€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 9815 | +0.170 | +6972.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 1388 | +0.197 | +1050.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 1388 | +0.197 | +1050.18€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1623 | +0.160 | +1161.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1623 | +0.160 | +1161.52€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 1410 | +0.200 | +1081.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 1410 | +0.200 | +1081.57€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1609 | +0.146 | +998.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1609 | +0.146 | +998.01€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1823 | +0.123 | +1136.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1823 | +0.123 | +1136.18€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1962 | +0.202 | +1545.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1962 | +0.202 | +1545.13€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 2148 | +0.103 | +695.73€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 2148 | +0.103 | +695.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 68 | +0.071 | +21.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 68 | +0.071 | +21.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 533 | +0.076 | +149.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 533 | +0.076 | +149.97€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 322 | +0.148 | +158.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 322 | +0.148 | +158.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 458 | +0.172 | +197.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 458 | +0.172 | +197.95€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 394 | +0.003 | +26.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 394 | +0.003 | +26.69€ | 4 | 4 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 373 | +0.127 | +140.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 373 | +0.127 | +140.76€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO | 11723 | +0.176 | +8509.67€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 11723 | +0.176 | +8509.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1738 | +0.221 | +1467.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1738 | +0.221 | +1467.27€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1912 | +0.161 | +1368.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1912 | +0.161 | +1368.84€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1755 | +0.224 | +1500.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1755 | +0.224 | +1500.84€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1808 | +0.141 | +1115.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1808 | +0.141 | +1115.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 2071 | +0.105 | +1134.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 2071 | +0.105 | +1134.72€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2439 | +0.206 | +1922.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2439 | +0.206 | +1922.36€ | 0 | 22 |
| ✅ GBM_LATE_5M | 3719 | +0.123 | +1694.03€ | 1 | 23 |
| ✅ GBM_LATE_5M#5min | 3719 | +0.123 | +1694.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 235 | +0.171 | +149.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 235 | +0.171 | +149.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1028 | +0.110 | +478.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1028 | +0.110 | +478.55€ | 1 | 15 |
| ✅ GBM_LATE_5M#DOGE | 463 | +0.147 | +246.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 463 | +0.147 | +246.88€ | 0 | 11 |
| ✅ GBM_LATE_5M#ETH | 1275 | +0.141 | +628.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1275 | +0.141 | +628.47€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 161 | -0.003 | +5.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 161 | -0.003 | +5.40€ | 1 | 1 |
| ✅ GBM_LATE_5M#XRP | 557 | +0.103 | +184.74€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 557 | +0.103 | +184.74€ | 0 | 0 |
| ✅ GBM_LATE_60M | 688 | +0.029 | +228.77€ | 3 | 13 |
| ✅ GBM_LATE_60M#60min | 688 | +0.029 | +228.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 230 | +0.065 | +66.79€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 230 | +0.065 | +66.79€ | 1 | 10 |
| ✅ GBM_LATE_60M#ETH | 254 | +0.062 | +116.33€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 254 | +0.062 | +116.33€ | 2 | 12 |
| ✅ GBM_LATE_60M#SOL | 204 | -0.053 | +45.64€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 204 | -0.053 | +45.64€ | 3 | 8 |
| 🚫 GBM_LATE_60M_FADE | 212 | -0.299 | -35.59€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 212 | -0.299 | -35.59€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 85 | -0.247 | -8.22€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 85 | -0.247 | -8.22€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 68 | -0.357 | -20.58€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 68 | -0.357 | -20.58€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 59 | -0.287 | -6.78€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 59 | -0.287 | -6.78€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 432 | +0.046 | +34.04€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 432 | +0.046 | +34.04€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 187 | +0.045 | +25.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 187 | +0.045 | +25.52€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 107 | +0.069 | +0.62€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 107 | +0.069 | +0.62€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 138 | +0.029 | +7.90€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 138 | +0.029 | +7.90€ | 3 | 3 |
| ✅ LATE_WINDOW_5MIN | 42 | +0.204 | +15.02€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 42 | +0.204 | +15.02€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 42 | +0.204 | +15.02€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 42 | +0.204 | +15.02€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 548 | +0.102 | +134.27€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 548 | +0.102 | +134.27€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 548 | +0.102 | +134.27€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 548 | +0.102 | +134.27€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 312 | -0.092 | -35.36€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 312 | -0.092 | -35.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 71 | -0.103 | -9.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 71 | -0.103 | -9.18€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 94 | -0.010 | -2.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 94 | -0.010 | -2.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 1242 | -0.013 | -22.17€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1242 | -0.013 | -22.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 70 | -0.014 | -3.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 70 | -0.014 | -3.67€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 148 | -0.033 | -4.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 148 | -0.033 | -4.86€ | 3 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 96 | -0.061 | -6.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 96 | -0.061 | -6.98€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 394 | +0.010 | +6.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 394 | +0.010 | +6.87€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 444 | -0.004 | -7.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 444 | -0.004 | -7.56€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 90 | -0.065 | -5.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 90 | -0.065 | -5.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M | 620 | -0.011 | +0.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 620 | -0.011 | +0.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 185 | -0.029 | -8.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 185 | -0.029 | -8.28€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 187 | +0.013 | +5.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 187 | +0.013 | +5.65€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 248 | -0.016 | +3.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 248 | -0.016 | +3.59€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 7315 | -0.003 | -93.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 7315 | -0.003 | -93.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 541 | -0.003 | +3.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 541 | -0.003 | +3.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 668 | -0.013 | -10.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 668 | -0.013 | -10.86€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1728 | +0.007 | -17.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1728 | +0.007 | -17.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1585 | +0.001 | +1.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1585 | +0.001 | +1.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 1317 | -0.013 | -37.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 1317 | -0.013 | -37.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1476 | -0.005 | -32.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1476 | -0.005 | -32.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 11805 | -0.032 | +609.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 11805 | -0.032 | +609.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1938 | -0.022 | +320.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1938 | -0.022 | +320.25€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 2042 | -0.030 | -9.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 2042 | -0.030 | -9.22€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1957 | -0.035 | +176.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1957 | -0.035 | +176.61€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1959 | -0.041 | -22.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1959 | -0.041 | -22.71€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1981 | -0.037 | +74.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1981 | -0.037 | +74.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1928 | -0.029 | +70.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1928 | -0.029 | +70.20€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 661 | -0.085 | -44.60€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 661 | -0.085 | -44.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 105 | -0.033 | -4.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 105 | -0.033 | -4.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 105 | -0.154 | -13.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 105 | -0.154 | -13.43€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 139 | -0.138 | -12.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 139 | -0.138 | -12.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 175 | -0.048 | -2.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 175 | -0.048 | -2.15€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 31962 | -0.077 | +627.32€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 31962 | -0.077 | +627.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 5160 | -0.088 | +443.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 5160 | -0.088 | +443.83€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 5295 | -0.078 | -115.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 5295 | -0.078 | -115.18€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 5286 | -0.081 | +172.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 5286 | -0.081 | +172.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 4810 | -0.098 | -237.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 4810 | -0.098 | -237.95€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 5986 | -0.054 | +99.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 5986 | -0.054 | +99.90€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 5425 | -0.067 | +264.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 5425 | -0.067 | +264.15€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6194 | -0.012 | -108.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6194 | -0.012 | -108.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 994 | -0.018 | -21.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 994 | -0.018 | -21.35€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1289 | -0.004 | -11.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1289 | -0.004 | -11.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1345 | -0.003 | -7.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1345 | -0.003 | -7.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 828 | -0.016 | -13.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 828 | -0.016 | -13.66€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 715 | +0.114 | +239.57€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 579 | +0.127 | +226.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 137 | +0.119 | +56.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 137 | +0.119 | +56.78€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 115 | +0.090 | +23.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 115 | +0.090 | +23.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 111 | +0.111 | +40.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 111 | +0.111 | +40.27€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 100 | +0.196 | +68.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 100 | +0.196 | +68.63€ | 0 | 4 |
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
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 127 | -0.159 | -8.93€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 24 | -0.231 | -1.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 128 | -0.269 | -18.83€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 106 | -0.287 | -23.22€ | 4 | 0 |
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
| ✅ STREAK_FADE_5M | 1879 | -0.023 | -82.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1879 | -0.023 | -82.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 779 | -0.013 | -22.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 779 | -0.013 | -22.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 553 | -0.026 | -25.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 553 | -0.026 | -25.13€ | 2 | 0 |
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
| ✅ STREAK_MOM_5M | 3806 | +0.025 | +71.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 3806 | +0.025 | +71.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1248 | +0.027 | +18.78€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1248 | +0.027 | +18.78€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 768 | +0.044 | +36.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 768 | +0.044 | +36.58€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 1127 | +0.013 | +0.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1127 | +0.013 | +0.07€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 663 | +0.020 | +16.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 663 | +0.020 | +16.04€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 4173 | +0.009 | -33.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 4173 | +0.009 | -33.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1600 | +0.009 | -14.86€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1600 | +0.009 | -14.86€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1655 | +0.017 | -0.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1655 | +0.017 | -0.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 918 | -0.004 | -18.10€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 918 | -0.004 | -18.10€ | 2 | 0 |
| ✅ UPDOWN_GBM | 9616 | +0.008 | +263.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3393 | +0.036 | +313.37€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 413 | +0.008 | +6.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 5155 | -0.007 | -55.58€ | 1 | 0 |
| ✅ UPDOWN_GBM#60min | 608 | +0.000 | -0.30€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 276 | +0.065 | +39.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 181 | +0.123 | +45.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 9 | -0.061 | -1.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 86 | -0.034 | -4.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1879 | +0.015 | +97.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 382 | +0.065 | +68.78€ | 2 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 123 | +0.052 | +8.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1133 | -0.000 | +19.81€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 223 | +0.002 | -1.30€ | 1 | 2 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 1087 | +0.001 | +0.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 127 | +0.089 | +26.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 10 | +0.042 | +0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 950 | -0.013 | -27.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 2050 | -0.002 | +10.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 991 | +0.021 | +32.91€ | 1 | 2 |
| ✅ UPDOWN_GBM#ETH#240min | 116 | +0.034 | +7.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 670 | -0.036 | -30.17€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 258 | +0.000 | +0.13€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 2782 | +0.005 | +13.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 885 | +0.002 | +6.50€ | 1 | 4 |
| ✅ UPDOWN_GBM#SOL#240min | 109 | -0.004 | -2.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1649 | +0.010 | +8.77€ | 3 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 127 | -0.004 | +0.87€ | 1 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 1540 | +0.014 | +103.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 827 | +0.049 | +133.36€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 46 | -0.125 | -6.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 667 | -0.019 | -22.75€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 258 | +0.327 | +63.67€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 258 | +0.327 | +63.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 150 | +0.316 | +28.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 150 | +0.316 | +28.57€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 108 | +0.336 | +35.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 108 | +0.336 | +35.10€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 5579 | -0.066 | +1278.61€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 5579 | -0.066 | +1278.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 307 | -0.050 | +341.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 307 | -0.050 | +341.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1153 | -0.154 | -58.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1153 | -0.154 | -58.15€ | 5 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 80 | +0.049 | +9.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 80 | +0.049 | +9.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 518 | +0.154 | +247.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 518 | +0.154 | +247.57€ | 2 | 16 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1815 | -0.062 | +371.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1815 | -0.062 | +371.95€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1706 | -0.084 | +365.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1706 | -0.084 | +365.86€ | 4 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 50 | +0.058 | +0.88€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 50 | +0.058 | +0.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 50 | +0.058 | +0.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 50 | +0.058 | +0.88€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 440 | +0.285 | +346.58€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 440 | +0.285 | +346.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 250 | +0.282 | +194.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 250 | +0.282 | +194.11€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 190 | +0.286 | +152.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 190 | +0.286 | +152.48€ | 0 | 14 |
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
  - _Estado_: Spread bajo (0.086) — sin ventaja clara. oversold(IBS<0.3): IC=+0.026 n=3422 | neutral: IC=+0.002 n=3749 | overbought(IBS>0.7): IC=+0.088 n=3750
  - _Datos_: n=11357 IC=+0.040 PNL=+1142.66€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 598s) 177 celda(s) GATE OK de 2462 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.002 < 0.08 — monitorear
  - _Datos_: n=885 IC=+0.002 PNL=+6.50€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=454/15 IC=+0.274 PNL=+132.22€ | BTC: n=440/15 IC=+0.224 PNL=+21.91€ | SOL: n=485/15 IC=+0.373 PNL=+449.93€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.067 n=152795 | tras_1loss IC=+0.051 n=120184 | tras_2loss IC=+0.015 n=53941/40 | gap=+0.052 (umbral 0.05)

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
  - _Estado_: 9554 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.090 n=59/60 | contraria IC=+0.134 n=39 | gap=-0.044 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=146, boost estimado=+0.012. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 100 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=258/40 IC=+0.000 PNL=+0.13€ | BTC#60min: n=223/40 IC=+0.002 PNL=-1.30€ | SOL#60min: n=127/40 IC=-0.004 PNL=+0.87€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.001 n=907 | contrario_BTC IC=-0.011 n=787/40 | gap=-0.011 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: 26/30 ops en el filtro definido (IC actual=+0.214 PNL=+19.08€)
  - _Datos_: n=26 IC=+0.214 PNL=+19.08€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=9339 IC=+0.006 PNL=+209.77€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=9339 IC=+0.006 PNL=+209.77€

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
  - _Estado_: n=492 IC=+0.010 PNL=+3.85€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=492 IC=+0.010 PNL=+3.85€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=116 IC=-0.042 PNL=-4.15€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=116 IC=-0.042 PNL=-4.15€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.1 con n=693 PNL=+206.55€
  - _Datos_: n=693 IC=+0.124 PNL=+206.55€

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
  - _Estado_: n=382 IC=+0.065 PNL=+68.78€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=382 IC=+0.065 PNL=+68.78€

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
  - _Estado_: n=1980 IC=+0.028 PNL=+164.36€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1980 IC=+0.028 PNL=+164.36€

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
  - _Estado_: n=109 IC=-0.013 PNL=+8.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=109 IC=-0.013 PNL=+8.45€

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
  - _Estado_: n=2559 IC=-0.019 PNL=-50.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2559 IC=-0.019 PNL=-50.02€

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
  - _Estado_: n=2515 IC=+0.013 PNL=+99.98€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2515 IC=+0.013 PNL=+99.98€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=684 IC=+0.031 PNL=+18.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=684 IC=+0.031 PNL=+18.26€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.110 > 0.08 con n=208 PNL=+57.03€
  - _Datos_: n=208 IC=+0.110 PNL=+57.03€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.08 con n=168 PNL=+13.09€
  - _Datos_: n=168 IC=+0.106 PNL=+13.09€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.135 > 0.08 con n=154 PNL=+50.60€
  - _Datos_: n=154 IC=+0.135 PNL=+50.60€

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
  - _Estado_: n=1330 IC=+0.028 PNL=+70.36€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1330 IC=+0.028 PNL=+70.36€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=393 PNL=+143.19€
  - _Datos_: n=393 IC=+0.128 PNL=+143.19€

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
  - _Estado_: n=2333 IC=+0.029 PNL=+175.89€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=2333 IC=+0.029 PNL=+175.89€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.1 con n=1027 PNL=+384.17€
  - _Datos_: n=1027 IC=+0.162 PNL=+384.17€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.200 < -0.1 con n=58 PNL=-0.76€
  - _Datos_: n=58 IC=-0.200 PNL=-0.76€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=646 IC=+0.032 PNL=+68.33€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=646 IC=+0.032 PNL=+68.33€

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
  - _Estado_: n=7610 IC=-0.142 PNL=+381.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7610 IC=-0.142 PNL=+381.44€

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
  - _Estado_: n=933 IC=+0.139 PNL=+479.63€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=933 IC=+0.139 PNL=+479.63€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.08 con n=655 PNL=+192.19€
  - _Datos_: n=655 IC=+0.126 PNL=+192.19€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.163 > 0.08 con n=197 PNL=+71.37€
  - _Datos_: n=197 IC=+0.163 PNL=+71.37€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.234 < -0.1 con n=846 PNL=-93.57€
  - _Datos_: n=846 IC=-0.234 PNL=-93.57€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=2180 IC=+0.138 PNL=+1256.31€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=2180 IC=+0.138 PNL=+1256.31€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=47 PNL=+16.97€
  - _Datos_: n=47 IC=+0.112 PNL=+16.97€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=947 IC=-0.009 PNL=+90.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=947 IC=-0.009 PNL=+90.74€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.183 > 0.08 con n=844 PNL=+561.76€
  - _Datos_: n=844 IC=+0.183 PNL=+561.76€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1408 IC=-0.061 PNL=+310.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1408 IC=-0.061 PNL=+310.24€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.08 con n=2017 PNL=-214.61€
  - _Datos_: n=2017 IC=+0.227 PNL=-214.61€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.103 n=303) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=303 IC=+0.103 PNL=+77.34€

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
  - _Estado_: n=4514 IC=+0.146 PNL=-728.14€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=4514 IC=+0.146 PNL=-728.14€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.250 > 0.1 con n=62 PNL=+44.39€
  - _Datos_: n=62 IC=+0.250 PNL=+44.39€
