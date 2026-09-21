# Hipótesis automáticas — 2026-09-21 02:13 UTC
_Generado por shadow_postmortem.py sobre 534936 resoluciones (PNL=+59349.57€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=474)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=446)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.252 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.131)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.220 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.131)

- **PATRÓN** `banda_hit_calibrado` > `0.804` → IC=+0.257 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.804 (IC base=+0.131)

- **PATRÓN** `banda_z` > `9.958` → IC=+0.223 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.958 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.145 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=542)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.131)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.260 (n=373)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=319)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.260 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.141)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.226 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.141)

- **PATRÓN** `banda_hit_calibrado` > `0.802` → IC=+0.272 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.802 (IC base=+0.141)

- **PATRÓN** `banda_z` > `11.154` → IC=+0.228 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.154 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.143 (n=289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 12.0 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=457)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.141 (n=115)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 96.0 (IC base=+0.039)

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
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `banda_z` > `3.13` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 3.13 (IC base=+0.154)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.705` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ballenas_wallet_edge_medio` > 0.705 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2784.9288` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2784.9288 (IC base=+0.154)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `145.1` → IC=-0.236 (n=6472)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.1
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=19419)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `140.57` → IC=-0.242 (n=882)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.57
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=2647)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `494.42` → IC=-0.152 (n=346)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 494.42
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1040)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `133.45` → IC=-0.276 (n=776)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.45
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=2331)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `160.64` → IC=-0.232 (n=1526)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.64
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4581)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `121.81` → IC=-0.364 (n=1282)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.81
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=3849)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.244 (n=334)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=381)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.179 (n=216)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=448)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.264 (n=163)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=169)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.214 (n=75)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=227)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.300 (n=63)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=130)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.187 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=137)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=152)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.198 (n=13004)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.69 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3251)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `5474.7679` → IC=+0.173 (n=2069)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5474.7679 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=10359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=12478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.235 (n=9945)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=5315)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `1663.3165` → IC=+0.158 (n=5992)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1663.3165 (IC base=+0.130)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=1342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.349 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `15620.9367` → IC=+0.234 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15620.9367 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.262 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=1982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `15398.3905` → IC=+0.206 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15398.3905 (IC base=+0.198)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.179 (n=303)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.62 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.144 (n=234)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4624.034 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=323)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.116)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.149 (n=785)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.44 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=555)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `5859.5725` → IC=+0.165 (n=219)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5859.5725 (IC base=+0.116)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=2599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=2217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.334 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.235)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.358 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.242 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.235)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.141 (n=608)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.223 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=698)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `1296.7944` → IC=+0.146 (n=606)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1296.7944 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.231 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.428 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=1027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.311 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=699)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.166)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.361 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=184)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `1271.2794` → IC=+0.159 (n=221)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1271.2794 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.214 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.117)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=10429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=9966)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.224 (n=3600)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=2435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=2566)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.169)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.275 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.259 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.256)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.327 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.256)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=2378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=2394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=2457)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.187 (n=1105)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.73 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.240)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.323 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.240)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=2436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.192 (n=2343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.192 (n=1765)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.434 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.431 (n=502)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.939` → IC=+0.469 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.939 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `2060.1801` → IC=+0.437 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2060.1801 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.432 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.431 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.451 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.436 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.469 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.435 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `3299.2146` → IC=+0.442 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3299.2146 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.405 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.408 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.404)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.412 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.404)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.405 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.404)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `libro_liquidez` < `6836.9618` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 6836.9618
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=30964)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.240 (n=11597)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=6301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=5315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=5761)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=5533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=5504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=1994)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=2991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=5696)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.173)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=2793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=2097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.263 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=5124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.252 (n=2586)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=5180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=5137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.200 (n=4750)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.12` → IC=+0.130 (n=4357)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` < 4.12 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.145 (n=4543)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.133 (n=6425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 8.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.18` → IC=+0.145 (n=4333)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.18 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=2399)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.06` → IC=+0.132 (n=2149)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.06 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2240)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.140 (n=3173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 8.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.53` → IC=+0.146 (n=2146)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.53 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=2351)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.126 (n=2177)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.16 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=2311)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.34` → IC=+0.145 (n=2178)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.34 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=730)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1573.916` → IC=+0.295 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1573.916 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.294 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.273)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.338 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `4195.4603` → IC=+0.291 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4195.4603 (IC base=+0.273)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.334 (n=348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.397 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `1467.8527` → IC=+0.313 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1467.8527 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.345 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.338)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.361 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.338)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.338)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.338)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.338)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.443 (n=404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `2547.1781` → IC=+0.437 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2547.1781 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.444 (n=196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.443 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `2057.1892` → IC=+0.459 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2057.1892 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.381)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.72` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.315 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.274 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.72` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.315 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.274 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.3549` → IC=+0.126 (n=6357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.3549 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.240 (n=2410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` < `0.5992` → IC=+0.245 (n=2014)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5992 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.923` → IC=+0.175 (n=2786)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 5.923 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `1.2124` → IC=+0.244 (n=1912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2124 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `1.0513` → IC=+0.246 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0513 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.3081` → IC=+0.211 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3081 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` > `1.9183` → IC=+0.204 (n=3255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9183 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.571` → IC=+0.132 (n=8724)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.571 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.5691` → IC=+0.200 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5691 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` < `0.1425` → IC=+0.172 (n=2709)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1425 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` < `0.7035` → IC=+0.177 (n=1311)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.7035 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` > `0.8712` → IC=+0.173 (n=1985)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.8712 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.1683` → IC=+0.225 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1683 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` > `1.5849` → IC=+0.201 (n=4426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5849 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.211 (n=4735)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.062)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.178 (n=547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.005 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.173 (n=548)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0081 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.3416` → IC=+0.168 (n=1639)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3416 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=619)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.067` → IC=+0.275 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.067 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.205 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.166 (n=1524)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.248 (n=1070)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.291 (n=400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.245 (n=823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0613` → IC=+0.298 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0613 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.39` → IC=+0.249 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.39 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.274 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6473` → IC=+0.257 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6473 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1772.5987` → IC=+0.245 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1772.5987 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.236 (n=547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.1134` → IC=+0.248 (n=546)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1134 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=1302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.212 (n=1259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.7274` → IC=+0.244 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7274 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.211 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.5634` → IC=+0.216 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5634 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.867` → IC=+0.245 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.867 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2554` → IC=+0.218 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2554 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.8746` → IC=+0.214 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8746 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.0746` → IC=+0.223 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0746 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.403` → IC=+0.222 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.403 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.3839` → IC=+0.214 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3839 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `15816.3726` → IC=+0.223 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15816.3726 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.176 (n=439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.157 (n=435)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.168 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6835` → IC=+0.167 (n=1300)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6835 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.6791` → IC=+0.137 (n=221)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.6791 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1254` → IC=+0.152 (n=1165)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1254 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.325` → IC=+0.159 (n=212)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.325 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.189` → IC=+0.136 (n=1173)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.189 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.146 (n=1300)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2089 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.136 (n=1299)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6201 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.173 (n=347)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4453` → IC=+0.146 (n=1190)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4453 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7721` → IC=+0.146 (n=793)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7721 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.145 (n=1107)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 411.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.202 (n=1061)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=1592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.596` → IC=+0.239 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.596 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.2145` → IC=+0.188 (n=1576)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2145 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.3689` → IC=+0.192 (n=206)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.3689 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.9269` → IC=+0.206 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9269 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=1060)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.223 (n=1359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.220 (n=1214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0065 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.256 (n=453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.3824` → IC=+0.232 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3824 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.55` → IC=+0.238 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.55 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.394` → IC=+0.218 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.394 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3606` → IC=+0.276 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3606 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.8365` → IC=+0.207 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8365 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.2771` → IC=+0.226 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2771 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.230 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1861.06` → IC=+0.230 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1861.06 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.225 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=92)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2007)

- **PATRÓN** `ibs_20min` > `0.9396` → IC=+0.198 (n=326)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.9396 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.3544` → IC=+0.344 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3544 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.7239` → IC=+0.326 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7239 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.643` → IC=+0.151 (n=637)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.643 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.6017` → IC=+0.345 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6017 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.333 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1929 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.1687` → IC=+0.327 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1687 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.338 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4007` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4007 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.325 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.339 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 165.0 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.3104` → IC=+0.168 (n=230)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.3104 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.155 (n=482)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.856 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2258` → IC=+0.235 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2258 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.176 (n=597)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.010)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.155 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=292)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.197 (n=87)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=261)

- **FILTRO** `ibs_20min` > `0.2632` → IC=-0.128 (n=1987)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2632
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=986)

- **FILTRO** `sigma_ewma_delta_pct` > `8.642` → IC=-0.205 (n=323)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.642
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2650)

- **PATRÓN** `drift_60min` |x|≤ `0.1707` → IC=+0.167 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1707 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.235 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7647 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `1.6268` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6268 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.5528` → IC=+0.272 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5528 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.6528` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6528 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `1.1487` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1487 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` < `0.1494` → IC=+0.300 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1494 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `2.2264` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2264 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.5504` → IC=+0.266 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5504 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.304 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.2632` → IC=+0.124 (n=986)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.2632 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.6436` → IC=+0.315 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6436 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` < `1.0999` → IC=+0.235 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0999 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1012` → IC=+0.230 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1012 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.1501` → IC=+0.265 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1501 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` < `2.4353` → IC=+0.271 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4353 (IC base=-0.044)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.638` → IC=-0.192 (n=505)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.638
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1516)

- **FILTRO** `ibs_20min` < `0.6944` → IC=-0.159 (n=1333)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6944
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=688)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.196 (n=396)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=1625)

- **FILTRO** `ibs_20min` > `0.7734` → IC=-0.201 (n=751)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7734
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=2255)

- **PATRÓN** `dist_vwap_pct` > `0.9672` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9672 (IC base=-0.077)

- **PATRÓN** `dist_vwap_pct` < `0.2585` → IC=+0.316 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2585 (IC base=-0.077)

- **PATRÓN** `volumen_regimen` > `0.616` → IC=+0.300 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.616 (IC base=-0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.0753` → IC=+0.293 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0753 (IC base=-0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.4081` → IC=+0.293 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4081 (IC base=-0.077)

- **PATRÓN** `volumen_spike_ratio` > `1.8611` → IC=+0.297 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8611 (IC base=-0.077)

- **PATRÓN** `dist_vwap_pct` > `0.9919` → IC=+0.318 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9919 (IC base=-0.023)

- **PATRÓN** `volumen_regimen` < `0.7389` → IC=+0.256 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7389 (IC base=-0.023)

- **PATRÓN** `volumen_regimen` > `1.0812` → IC=+0.293 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0812 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1058` → IC=+0.283 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1058 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.2166` → IC=+0.256 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2166 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5844` → IC=+0.249 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5844 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.190 (n=3001)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0094 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4684` → IC=+0.185 (n=8036)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4684 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `1.013` → IC=+0.290 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.013 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.556` → IC=+0.152 (n=4274)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.556 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `1.1748` → IC=+0.230 (n=3150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1748 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` > `0.6824` → IC=+0.241 (n=2815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6824 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2993` → IC=+0.259 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2993 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.4763` → IC=+0.242 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4763 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` > `2.7163` → IC=+0.240 (n=1706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7163 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.269 (n=4617)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.147 (n=3042)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0088 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.5517` → IC=+0.149 (n=8016)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5517 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.6787` → IC=+0.242 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6787 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.1703` → IC=+0.236 (n=2359)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1703 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.7178` → IC=+0.237 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7178 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2028` → IC=+0.242 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2028 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2479` → IC=+0.307 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2479 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4914` → IC=+0.253 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4914 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.3584` → IC=+0.260 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3584 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.264 (n=3267)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 81.0 (IC base=+0.070)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.503` → IC=-0.163 (n=485)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.503
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1628)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.266 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.202 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.268 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.4469` → IC=+0.182 (n=256)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4469 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` > `2.185` → IC=+0.193 (n=347)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.185 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.188 (n=325)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 15.0 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.817` → IC=-0.146 (n=657)

  - _Acción_: SKIP cuando `ibs_20min` > 0.817
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1973)

- **PATRÓN** `ibs_20min` > `0.86` → IC=+0.152 (n=605)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.86 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.295` → IC=+0.156 (n=321)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.295 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `1.0445` → IC=+0.143 (n=720)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0445 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` > `0.6606` → IC=+0.148 (n=731)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6606 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.194 (n=266)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `249.0` → IC=+0.189 (n=348)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 249.0 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` > `0.6013` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6013 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` < `0.1515` → IC=+0.211 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1515 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `0.6047` → IC=+0.207 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6047 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.4584` → IC=+0.213 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4584 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1954` → IC=+0.219 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1954 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `483.0` → IC=+0.208 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 483.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.286 (n=954)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.1057` → IC=+0.245 (n=477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1057 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.256 (n=534)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.578` → IC=+0.279 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.578 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.1395` → IC=+0.259 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1395 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.9594` → IC=+0.262 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9594 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.255 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1928.9792` → IC=+0.253 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1928.9792 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.265 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.244)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.328 (n=515)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.327 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.3388` → IC=+0.290 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3388 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.883` → IC=+0.303 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.883 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.315 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `1.6234` → IC=+0.292 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6234 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.2073` → IC=+0.288 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2073 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.297 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `1912.5061` → IC=+0.315 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.5061 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.290 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.285)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2702` → IC=-0.196 (n=432)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2702
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=1299)

- **FILTRO** `ibs_20min` > `0.7848` → IC=-0.175 (n=537)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7848
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1615)

- **PATRÓN** `ibs_20min` > `0.8048` → IC=+0.155 (n=589)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.8048 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` > `0.4461` → IC=+0.231 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4461 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `1.0974` → IC=+0.224 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0974 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.212 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2672` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2672 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.1059` → IC=+0.244 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1059 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.266 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` > `0.1468` → IC=+0.200 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1468 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` < `0.4933` → IC=+0.180 (n=370)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.4933 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` < `1.1615` → IC=+0.192 (n=345)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.1615 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `0.6698` → IC=+0.180 (n=345)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6698 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.8288` → IC=+0.230 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8288 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.1518` → IC=+0.257 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1518 (IC base=-0.009)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.236 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7059` → IC=-0.204 (n=958)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=959)

- **FILTRO** `ibs_20min` > `0.6923` → IC=-0.232 (n=501)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6923
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=1512)

- **FILTRO** `sigma_ewma_delta_pct` > `4.685` → IC=-0.176 (n=449)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.685
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=1564)

- **PATRÓN** `ibs_20min` > `0.7059` → IC=+0.269 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7059 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.815` → IC=+0.344 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.815 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.157 (n=301)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.296 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `0.6366` → IC=+0.286 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6366 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.1049` → IC=+0.288 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1049 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.298 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.7981` → IC=+0.304 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7981 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.314 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.209 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.2075` → IC=+0.221 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2075 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `0.7129` → IC=+0.266 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7129 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.209 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `2.5185` → IC=+0.223 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5185 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.234 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.012)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.016` → IC=+0.318 (n=783)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.016 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.289 (n=548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` > `0.9097` → IC=+0.345 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9097 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` > `0.1916` → IC=+0.314 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1916 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.483` → IC=+0.297 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.483 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` > `1.0362` → IC=+0.302 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0362 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.311 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` < `1.4418` → IC=+0.280 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4418 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `2.5388` → IC=+0.288 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5388 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.278 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `2599.3337` → IC=+0.286 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2599.3337 (IC base=+0.274)

- **PATRÓN** `sigma_h` > `0.0147` → IC=+0.299 (n=865)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0147 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.280 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.3976` → IC=+0.304 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3976 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.5397` → IC=+0.286 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5397 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.471` → IC=+0.290 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.471 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.272 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `1.2432` → IC=+0.311 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2432 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2407` → IC=+0.339 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2407 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `2.5387` → IC=+0.266 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5387 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `2.1751` → IC=+0.271 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1751 (IC base=+0.271)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.272 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2583.0856` → IC=+0.277 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2583.0856 (IC base=+0.271)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.170 (n=2376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.201 (n=2367)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0888` → IC=+0.185 (n=2365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0888 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=7400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.5808` → IC=+0.217 (n=7091)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5808 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1693` → IC=+0.194 (n=3092)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1693 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.232` → IC=+0.258 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.232 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2161` → IC=+0.160 (n=4688)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2161 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.157 (n=4689)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6258 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2466` → IC=+0.192 (n=1422)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2466 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5656` → IC=+0.171 (n=2982)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5656 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6497` → IC=+0.175 (n=2259)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6497 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2375.6564` → IC=+0.167 (n=4727)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2375.6564 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.180 (n=6005)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 118.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.182 (n=4511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0065 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.203 (n=2255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.208 (n=2299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.4762` → IC=+0.225 (n=6762)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4762 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.2249` → IC=+0.158 (n=4946)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2249 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.238` → IC=+0.195 (n=1147)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.238 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.181` → IC=+0.152 (n=4932)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.181 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.225 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5744` → IC=+0.165 (n=2682)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5744 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.2831` → IC=+0.173 (n=2764)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.2831 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.171 (n=5730)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 120.0 (IC base=+0.167)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.222 (n=408)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.189 (n=555)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0075 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.3381` → IC=+0.207 (n=1221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3381 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.200 (n=602)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.073` → IC=+0.309 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.073 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.236 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.181 (n=1122)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.244 (n=752)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.252 (n=764)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1823` → IC=+0.292 (n=570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1823 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=412)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3455` → IC=+0.264 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3455 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.049` → IC=+0.253 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.049 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0955` → IC=+0.233 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0955 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.272 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4211` → IC=+0.248 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4211 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.6473` → IC=+0.240 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6473 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1777.62` → IC=+0.252 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1777.62 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.247 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.204 (n=350)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=1104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.4138` → IC=+0.226 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4138 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.1987` → IC=+0.212 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1987 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.235 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.686` → IC=+0.178 (n=461)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.686 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2334` → IC=+0.194 (n=230)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2334 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.414` → IC=+0.203 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.414 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `15752.6972` → IC=+0.171 (n=475)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 15752.6972 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.194 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0025 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.2883` → IC=+0.154 (n=1152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.2883 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.153 (n=1060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5531` → IC=+0.184 (n=1152)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5531 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.13` → IC=+0.160 (n=1156)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.13 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.882` → IC=+0.209 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.882 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.154 (n=1152)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2129 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1573` → IC=+0.157 (n=354)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1573 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.449` → IC=+0.145 (n=1042)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.449 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7597` → IC=+0.137 (n=694)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.7597 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.151 (n=322)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 221.0 (IC base=+0.136)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.227 (n=537)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.2078` → IC=+0.214 (n=789)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2078 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.783` → IC=+0.276 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.783 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.2133` → IC=+0.195 (n=1142)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.2133 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.135` → IC=+0.193 (n=461)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.135 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.9343` → IC=+0.209 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9343 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.208 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `1932.8384` → IC=+0.205 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1932.8384 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.236 (n=976)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.0916` → IC=+0.253 (n=326)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0916 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.279 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.3521` → IC=+0.253 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3521 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.729` → IC=+0.273 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.729 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.3597` → IC=+0.275 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3597 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.6422` → IC=+0.224 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6422 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.2601` → IC=+0.233 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2601 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `1917.241` → IC=+0.226 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.241 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.230 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.223)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.169 (n=1128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0077 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.163 (n=1126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.163 (n=1126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3938` → IC=+0.202 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3938 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.153` → IC=+0.185 (n=756)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.153 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.246 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.0496` → IC=+0.155 (n=991)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0496 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.6345` → IC=+0.152 (n=1126)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6345 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.227 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4219` → IC=+0.159 (n=367)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4219 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.5331` → IC=+0.177 (n=367)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.5331 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `6913.8034` → IC=+0.185 (n=751)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 6913.8034 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.150 (n=1064)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 168.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.158 (n=1186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0072 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.141 (n=1186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.187 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6149` → IC=+0.171 (n=1186)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6149 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.344` → IC=+0.137 (n=1275)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.344 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.926` → IC=+0.175 (n=420)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 6.926 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.144 (n=791)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8554 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.209 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.489` → IC=+0.142 (n=356)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.489 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `9966.3147` → IC=+0.159 (n=538)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 9966.3147 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.5652` → IC=-0.182 (n=435)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5652
  - _Potencial_: sin este filtro IC_bueno=+0.207 (n=1308)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.159 (n=585)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.01 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=1323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.5156` → IC=+0.203 (n=1289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5156 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.0671` → IC=+0.219 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0671 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.569` → IC=+0.251 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.569 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.2243` → IC=+0.127 (n=1290)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2243 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.1664` → IC=+0.129 (n=1287)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1664 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.8114` → IC=+0.133 (n=828)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8114 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1343)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2881.368` → IC=+0.195 (n=585)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2881.368 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.133 (n=960)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 49.0 (IC base=+0.115)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.150 (n=578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.006 (IC base=+0.110)

- **PATRÓN** `drift_60min` |x|≤ `0.1029` → IC=+0.139 (n=436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.1029 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=1329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.207 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `0.9627` → IC=+0.142 (n=171)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.9627 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.1939` → IC=+0.134 (n=1194)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1939 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.434` → IC=+0.154 (n=273)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 7.434 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `1.0465` → IC=+0.122 (n=1151)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0465 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.167 (n=160)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.4572` → IC=+0.133 (n=388)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4572 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` > `2.173` → IC=+0.124 (n=527)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.173 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `3066.2091` → IC=+0.158 (n=436)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3066.2091 (IC base=+0.110)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0184` → IC=+0.207 (n=818)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0184 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.1289` → IC=+0.198 (n=409)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1289 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=1274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.7333` → IC=+0.255 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7333 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `1.2245` → IC=+0.223 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2245 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.442` → IC=+0.241 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.442 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `1.209` → IC=+0.199 (n=1227)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.209 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` > `0.8588` → IC=+0.215 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8588 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2353` → IC=+0.273 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2353 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `2.1696` → IC=+0.207 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1696 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.8094` → IC=+0.201 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8094 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.197 (n=1283)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.237 (n=431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.218 (n=584)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.218 (n=431)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=589)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.4426` → IC=+0.246 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4426 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1146` → IC=+0.232 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1146 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.374` → IC=+0.245 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.374 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6302` → IC=+0.216 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6302 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.283 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2447` → IC=+0.196 (n=1011)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2447 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4601` → IC=+0.198 (n=1149)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4601 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2559.8293` → IC=+0.210 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2559.8293 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.159 (n=555)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0038 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.173 (n=555)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0089 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.154 (n=733)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.180 (n=1663)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.3706` → IC=+0.182 (n=492)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.3706 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.719` → IC=+0.177 (n=775)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.719 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.164 (n=961)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8725 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.206` → IC=+0.151 (n=480)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.206 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1642` → IC=+0.175 (n=460)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1642 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4378` → IC=+0.158 (n=533)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4378 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5597` → IC=+0.174 (n=532)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5597 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=1867)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2477.0811` → IC=+0.149 (n=1486)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2477.0811 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.165 (n=1441)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 165.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.126 (n=1170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0057 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.122 (n=1174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.6556` → IC=+0.133 (n=1751)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6556 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3431` → IC=+0.129 (n=410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3431 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.144 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 9.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.2513` → IC=+0.146 (n=410)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.2513 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.2868` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.2868 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.328` → IC=+0.136 (n=185)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.328 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `0.7069` → IC=+0.145 (n=181)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.7069 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `12265.8595` → IC=+0.136 (n=366)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 12265.8595 (IC base=+0.106)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.204 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3374` → IC=+0.138 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3374 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.143 (n=494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6012` → IC=+0.175 (n=484)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6012 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2809` → IC=+0.146 (n=588)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2809 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.406` → IC=+0.148 (n=214)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 4.406 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.7202` → IC=+0.140 (n=492)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.7202 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.203 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.1128` → IC=+0.148 (n=476)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1128 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.137 (n=540)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `336.0` → IC=+0.138 (n=457)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 336.0 (IC base=+0.124)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.267 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.213 (n=162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.213 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.257 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.4315` → IC=+0.247 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4315 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.367` → IC=+0.253 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.367 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.047` → IC=+0.242 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.047 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.8407` → IC=+0.215 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8407 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.220 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2555` → IC=+0.333 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2555 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.3839` → IC=+0.235 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3839 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.3941` → IC=+0.276 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3941 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.0725` → IC=+0.171 (n=150)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.0725 (IC base=+0.074)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4286` → IC=-0.124 (n=163)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4286
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=319)

- **FILTRO** `dist_vwap_pct` > `0.3414` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3414
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=448)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.145 (n=246)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0069 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.147 (n=344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.245 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.8398` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.8398 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.0671` → IC=+0.133 (n=325)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.0671 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.7231` → IC=+0.131 (n=329)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.7231 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.2136` → IC=+0.152 (n=159)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.2136 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3064.7088` → IC=+0.204 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3064.7088 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.158 (n=115)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 21.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.4286` → IC=+0.157 (n=319)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4286 (IC base=+0.062)

- **PATRÓN** `volumen_spike_ratio` < `1.6051` → IC=+0.162 (n=149)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.6051 (IC base=+0.062)

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

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.181 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.022 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.178` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.178 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.576` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.576 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8853` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8853 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.136 (n=201)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6515 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1187` → IC=+0.130 (n=179)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1187 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.6848` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.6848 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.8185` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.8185 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 17.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.198 (n=3006)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0109 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=9418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.214 (n=9023)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.9038` → IC=+0.196 (n=1236)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.9038 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.605` → IC=+0.226 (n=4398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.605 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8816` → IC=+0.164 (n=4023)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8816 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.195 (n=1681)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.6257` → IC=+0.187 (n=2879)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6257 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2325.81` → IC=+0.168 (n=6011)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2325.81 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.193 (n=6732)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 89.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.191 (n=5461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0069 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1442` → IC=+0.185 (n=3604)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1442 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5657` → IC=+0.238 (n=8188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5657 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2368` → IC=+0.161 (n=5108)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2368 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.91` → IC=+0.197 (n=1161)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.91 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.706` → IC=+0.182 (n=7939)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.706 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7057` → IC=+0.158 (n=2496)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7057 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.246 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.8753` → IC=+0.187 (n=4966)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8753 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.188 (n=4748)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 49.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.208 (n=512)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.209 (n=1025)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3429` → IC=+0.191 (n=1536)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3429 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.195 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=1030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.318 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.472` → IC=+0.349 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.472 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.251 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.5813` → IC=+0.208 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5813 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=854)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.256 (n=1171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.262 (n=1044)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.127` → IC=+0.291 (n=515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.127 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.266 (n=1063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=1063)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.3485` → IC=+0.289 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3485 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.427` → IC=+0.266 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.427 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.303 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `1.8751` → IC=+0.278 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8751 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1772.5987` → IC=+0.271 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1772.5987 (IC base=+0.256)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.192 (n=482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.165 (n=633)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=1502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.3102` → IC=+0.200 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3102 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1241` → IC=+0.181 (n=814)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1241 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.168 (n=332)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.271` → IC=+0.150 (n=1289)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.271 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.6272` → IC=+0.180 (n=480)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6272 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2695` → IC=+0.189 (n=207)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2695 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.1195` → IC=+0.157 (n=1218)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1195 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.5017` → IC=+0.152 (n=1237)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5017 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `13656.0542` → IC=+0.151 (n=959)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 13656.0542 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `481.0` → IC=+0.154 (n=1316)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 481.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3181` → IC=+0.158 (n=1255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3181 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.178 (n=426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6459` → IC=+0.191 (n=1255)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6459 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6776` → IC=+0.167 (n=202)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6776 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1283` → IC=+0.164 (n=1140)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1283 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.516` → IC=+0.165 (n=216)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.516 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.160 (n=1255)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1954 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.194 (n=338)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.158 (n=1157)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7548` → IC=+0.161 (n=771)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7548 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `429.0` → IC=+0.154 (n=934)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 429.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.240 (n=657)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=1519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.221 (n=1469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.6721` → IC=+0.256 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6721 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.741` → IC=+0.291 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.741 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.2162` → IC=+0.222 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2162 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.9235` → IC=+0.247 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9235 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.227 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `1931.8584` → IC=+0.222 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1931.8584 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.242 (n=1350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.242 (n=901)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.157` → IC=+0.240 (n=594)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.157 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.267 (n=517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3653` → IC=+0.269 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3653 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.748` → IC=+0.279 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.748 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.295 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.791` → IC=+0.234 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.791 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.2335` → IC=+0.236 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2335 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.252 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1862.661` → IC=+0.251 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1862.661 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.243 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.237)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.180 (n=517)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0034 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4338` → IC=+0.143 (n=1540)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4338 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=1612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.8796` → IC=+0.260 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8796 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.3602` → IC=+0.171 (n=611)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.3602 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.318` → IC=+0.168 (n=254)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.318 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8772` → IC=+0.159 (n=1027)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8772 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2793` → IC=+0.235 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2793 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5228` → IC=+0.151 (n=655)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5228 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.4714` → IC=+0.151 (n=496)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.4714 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `8151.5866` → IC=+0.230 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8151.5866 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.152 (n=475)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 81.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.154 (n=1251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0076 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4396` → IC=+0.150 (n=1251)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4396 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.6915` → IC=+0.186 (n=1251)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6915 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.362` → IC=+0.140 (n=1248)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.362 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.109` → IC=+0.186 (n=189)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.109 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.146 (n=551)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6973 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.1852` → IC=+0.140 (n=417)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.1852 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.255 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.150 (n=1180)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `10998.3764` → IC=+0.209 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10998.3764 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `183.0` → IC=+0.140 (n=1173)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 183.0 (IC base=+0.135)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.133 (n=1019)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0079 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.4695` → IC=+0.186 (n=1529)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4695 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `1.048` → IC=+0.199 (n=290)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 1.048 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.414` → IC=+0.230 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.414 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=1062)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2904.4304` → IC=+0.242 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2904.4304 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.127 (n=1165)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 54.0 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.132 (n=1501)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0109 (IC base=+0.110)

- **PATRÓN** `drift_60min` |x|≤ `0.1286` → IC=+0.150 (n=501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1286 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=1554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.205 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.2141` → IC=+0.128 (n=1214)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.2141 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.437` → IC=+0.125 (n=1450)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.437 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.7205` → IC=+0.153 (n=661)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7205 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.2238` → IC=+0.174 (n=234)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2238 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.4566` → IC=+0.138 (n=448)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4566 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2844.2019` → IC=+0.159 (n=500)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2844.2019 (IC base=+0.110)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0187` → IC=+0.213 (n=1018)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0187 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=1594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=1362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.5111` → IC=+0.243 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5111 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.188` → IC=+0.225 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.188 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.164` → IC=+0.262 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.164 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.0764` → IC=+0.203 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0764 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.635` → IC=+0.210 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.635 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.236` → IC=+0.238 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.236 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.5326` → IC=+0.232 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5326 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.210 (n=1576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2591.9144` → IC=+0.208 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2591.9144 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.233 (n=556)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.220 (n=556)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.201 (n=1757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.257 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.8402` → IC=+0.203 (n=1859)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8402 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.807` → IC=+0.262 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.807 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.238 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.255 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.2198` → IC=+0.197 (n=1306)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2198 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4437` → IC=+0.201 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4437 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2568.8002` → IC=+0.202 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2568.8002 (IC base=+0.201)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=2801)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.158 (n=2383)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0092 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.5214` → IC=+0.161 (n=2708)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5214 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.157 (n=908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.171 (n=945)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.9392` → IC=+0.210 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9392 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1884` → IC=+0.163 (n=954)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1884 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.4988` → IC=+0.141 (n=1599)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.4988 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.152` → IC=+0.179 (n=444)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.152 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.9039` → IC=+0.163 (n=1134)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.9039 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1732` → IC=+0.184 (n=741)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1732 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.459` → IC=+0.157 (n=893)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.459 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8927` → IC=+0.162 (n=1786)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8927 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=1792)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `2753.9412` → IC=+0.154 (n=2419)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2753.9412 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.192 (n=705)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0037 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.4792` → IC=+0.153 (n=2114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4792 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.158 (n=715)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 4.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.1769` → IC=+0.162 (n=930)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1769 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.9113` → IC=+0.142 (n=314)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.9113 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.4316` → IC=+0.125 (n=2092)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.4316 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.241` → IC=+0.140 (n=2098)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 6.241 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.9021` → IC=+0.147 (n=1341)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.9021 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.148 (n=994)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.5338` → IC=+0.137 (n=921)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5338 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.8153` → IC=+0.141 (n=1394)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8153 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=2801)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `7398.1841` → IC=+0.145 (n=1887)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 7398.1841 (IC base=+0.132)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.175 (n=312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0056 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.176 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0033 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.192 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.5204` → IC=+0.202 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5204 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.2197` → IC=+0.185 (n=163)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.2197 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` < `0.4014` → IC=+0.166 (n=348)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.4014 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.301` → IC=+0.174 (n=381)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 2.301 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `0.8476` → IC=+0.198 (n=236)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.8476 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.3101` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3101 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.4501` → IC=+0.192 (n=118)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4501 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `2.7022` → IC=+0.208 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7022 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `12565.4829` → IC=+0.201 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12565.4829 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.211 (n=400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1108` → IC=+0.171 (n=399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1108 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.172 (n=400)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1409 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.142 (n=412)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6091 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.7021` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.7021 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.2218` → IC=+0.136 (n=932)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2218 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.06` → IC=+0.150 (n=990)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 9.06 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8811` → IC=+0.182 (n=605)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8811 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0696` → IC=+0.162 (n=427)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0696 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4214` → IC=+0.141 (n=302)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4214 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.143 (n=603)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `11328.3365` → IC=+0.147 (n=907)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 11328.3365 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `712.0` → IC=+0.142 (n=862)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 712.0 (IC base=+0.134)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.5715` → IC=+0.174 (n=623)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.5715 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.8576` → IC=+0.167 (n=547)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.8576 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.165)

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

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.160 (n=835)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0087 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.159 (n=834)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4866` → IC=+0.161 (n=835)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4866 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5456` → IC=+0.157 (n=557)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5456 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.1886` → IC=+0.159 (n=834)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.1886 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `1.006` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 1.006 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.4256` → IC=+0.163 (n=772)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4256 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.161 (n=835)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.0946` → IC=+0.159 (n=734)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0946 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.7181` → IC=+0.156 (n=746)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7181 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.1126` → IC=+0.153 (n=771)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.1126 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1724` → IC=+0.168 (n=245)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1724 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.5244` → IC=+0.159 (n=819)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.5244 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5194` → IC=+0.153 (n=731)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5194 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=813)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.152 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0084 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.139 (n=619)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0047 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4905` → IC=+0.165 (n=691)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4905 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.152 (n=242)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 4.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.0983` → IC=+0.152 (n=691)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.0983 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6358` → IC=+0.167 (n=163)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6358 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.3867` → IC=+0.143 (n=692)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3867 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.906` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.906 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.261` → IC=+0.139 (n=622)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.261 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.0954` → IC=+0.151 (n=608)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0954 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.7253` → IC=+0.145 (n=618)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7253 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.177 (n=298)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.151 (n=597)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.7743` → IC=+0.161 (n=452)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7743 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7641.8774` → IC=+0.161 (n=691)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7641.8774 (IC base=+0.139)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 1.0 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.32` → IC=+0.144 (n=85)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 2.32 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.057)

- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.148 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0137 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.2105` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.2105 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `0.5969` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.5969 (IC base=+0.051)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.218 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=326)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.235 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=338)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.213 (n=347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.5789` → IC=+0.198 (n=696)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5789 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.1931` → IC=+0.162 (n=347)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1931 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.528` → IC=+0.208 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.528 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `2.1222` → IC=+0.153 (n=517)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1222 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=566)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2435.8886` → IC=+0.148 (n=305)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2435.8886 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.277 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.0664` → IC=+0.201 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0664 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `2.6357` → IC=+0.132 (n=191)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.6357 (IC base=-0.011)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.174 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0059 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.5656` → IC=+0.198 (n=240)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5656 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.167 (n=124)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.0529` → IC=+0.129 (n=211)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0529 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.067` → IC=+0.139 (n=178)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.067 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2625` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2625 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.193 (n=177)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.4946` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.4946 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.6802` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6802 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.0664` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0664 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.4111` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4111 (IC base=+0.043)

- **PATRÓN** `libro_liquidez` > `3545.1926` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3545.1926 (IC base=+0.043)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.271 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=100)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.243 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=100)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.179 (n=182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.143 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.557` → IC=+0.223 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.557 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.5279` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.5279 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.217` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.217 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8141` → IC=+0.148 (n=160)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8141 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6396` → IC=+0.143 (n=214)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.6396 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.3075` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3075 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.7779` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.7779 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `1.4062` → IC=+0.149 (n=189)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4062 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=253)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `1108.9201` → IC=+0.170 (n=210)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1108.9201 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1103` → IC=+0.189 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1103 (IC base=-0.041)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=-0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.967` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 2.967 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=-0.041)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.0882` → IC=-0.278 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0882
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=44)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.122 (n=109)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.006 (IC base=+0.075)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.143 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 14.0 (IC base=+0.075)

- **PATRÓN** `ibs_20min` > `0.6923` → IC=+0.190 (n=195)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.6923 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1948` → IC=+0.146 (n=125)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1948 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.244` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.244 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0588` → IC=+0.153 (n=73)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.0588 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.0856` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0856 (IC base=+0.075)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.127 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0075 (IC base=-0.054)

- **PATRÓN** `ibs_20min` < `0.0882` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0882 (IC base=-0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.174` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 2.174 (IC base=-0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.1383` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1383 (IC base=-0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.9854` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.9854 (IC base=-0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4444 (IC base=-0.054)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `10.0` → IC=-0.409 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=136)

- **FILTRO** `dist_vwap_pct` > `0.2334` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2334
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=162)

- **FILTRO** `volumen_regimen` < `0.7296` → IC=-0.350 (n=58)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7296
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=120)

- **FILTRO** `drift_60min` |x|> `0.2212` → IC=-0.346 (n=37)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2212
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=112)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=135)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=125)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.282 (n=53)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=46)

- **FILTRO** `volumen_regimen` < `0.7431` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7431
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=46)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.283 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=44)

- **FILTRO** `drift_60min` |x|> `0.1778` → IC=-0.324 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1778
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=48)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.333 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=43)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8396` → IC=-0.429 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8396
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.333 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=27)

- **FILTRO** `ibs_20min` > `0.6482` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6482
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=25)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

- **FILTRO** `dist_vwap_pct` > `0.0767` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0767
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=40)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=20)

- **FILTRO** `volumen_regimen` < `1.0683` → IC=-0.431 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0683
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2075` → IC=-0.135 (n=113)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2075
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=221)

- **FILTRO** `dist_vwap_pct` > `0.6296` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6296
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=308)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.124 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.078)

- **PATRÓN** `ibs_20min` > `0.6592` → IC=+0.160 (n=230)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6592 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.2075` → IC=+0.128 (n=221)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.2075 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.105` → IC=+0.145 (n=105)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 6.105 (IC base=+0.039)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.039)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=84)

- **FILTRO** `ibs_20min` < `0.557` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.557
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=75)

- **FILTRO** `volumen_regimen` < `0.7797` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7797
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=75)

- **PATRÓN** `ibs_20min` > `0.6592` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.6592 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.4745` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4745 (IC base=-0.020)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1361 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` < `0.1782` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1782 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `2.8706` → IC=+0.123 (n=83)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.8706 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3566.36` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3566.36 (IC base=+0.097)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.8361` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8361
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=55)

- **FILTRO** `ibs_20min` > `0.3115` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3115
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=81)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.156 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0042 (IC base=+0.059)

- **PATRÓN** `drift_60min` |x|≤ `0.2855` → IC=+0.125 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.2855 (IC base=+0.059)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.239 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.8361` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8361 (IC base=+0.059)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `1549.4073` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1549.4073 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.005)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0772` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0772
  - _Potencial_: sin este filtro IC_bueno=+0.262 (n=19)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.206 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.167 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0079 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.170 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.7143` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7143 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.6353` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6353 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.0976` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0976 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5586` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5586 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.03 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.033)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.138 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 16.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=594)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2844.5756` → IC=+0.168 (n=203)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2844.5756 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.138 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 16.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=594)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2844.5756` → IC=+0.168 (n=203)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2844.5756 (IC base=+0.107)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=76)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.176 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=110)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=129)

- **FILTRO** `libro_liquidez` < `2453.3967` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `libro_liquidez` < 2453.3967
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=109)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=201)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=187)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1528)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=49)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=59)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `36073.08` → IC=-0.147 (n=49)

  - _Acción_: SKIP cuando `liq_usd_total` < 36073.08
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=100)

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

- **PATRÓN** `liq_n` > `17.0` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `liq_n` > 17.0 (IC base=+0.030)

- **PATRÓN** `liq_usd_total` > `68754.71` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `liq_usd_total` > 68754.71 (IC base=+0.030)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9666` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9666
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=89)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=685)

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
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=422)

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
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=110)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.7565` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.7565
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=95)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=464)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=307)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=307)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.134 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=169)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=169)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=106)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.138 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=139)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=69)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=85)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=182)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=69)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=72)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=226)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=226)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=113)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7227)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.178 (n=3041)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=9549)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.172 (n=3180)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=9861)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.219 (n=518)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1649)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.172 (n=547)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=1781)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.123 (n=1453)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.495 (IC base=+0.023)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.203 (n=546)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1656)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.201 (n=576)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1743)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.164 (n=567)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1752)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.475` → IC=-0.189 (n=531)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=1610)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.190 (n=556)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1765)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=2610)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=2748)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=2754)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.160 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=342)

- **FILTRO** `ibs_20min` > `0.1763` → IC=-0.142 (n=107)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1763
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=327)

- **FILTRO** `libro_liquidez` < `16798.6123` → IC=-0.148 (n=208)

  - _Acción_: SKIP cuando `libro_liquidez` < 16798.6123
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=626)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=220)

- **FILTRO** `ibs_20min` < `0.0992` → IC=-0.243 (n=72)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0992
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=216)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.188 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=189)

- **FILTRO** `drift_20min_pct` |x|> `0.1486` → IC=-0.159 (n=89)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1486
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=175)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=714)

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

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.032)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=8949)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=20154)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.277 (n=7013)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=22090)

- **FILTRO** `ibs_7min` < `0.2935` → IC=-0.236 (n=7275)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2935
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=21828)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.159 (n=9831)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=19272)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9080)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=27369)

- **FILTRO** `ibs_7min` > `0.2942` → IC=-0.179 (n=9112)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2942
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27337)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=1136)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3631)

- **FILTRO** `ibs_7min` < `0.7093` → IC=-0.254 (n=1573)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7093
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3194)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.180 (n=1144)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3623)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.152 (n=4225)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=2061)

- **FILTRO** `drift_7min_pct` |x|> `0.1117` → IC=-0.127 (n=2129)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1117
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4157)

- **FILTRO** `ibs_7min` > `0.7928` → IC=-0.205 (n=1571)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7928
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4715)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3874)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=1220)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3831)

- **FILTRO** `ibs_7min` < `0.7518` → IC=-0.188 (n=1262)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7518
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3789)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.173 (n=1260)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=3791)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.257 (n=1260)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=3855)

- **FILTRO** `ibs_7min` > `0.2588` → IC=-0.172 (n=1277)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2588
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3838)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.185 (n=1275)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3840)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.172 (n=1105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3399)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.310 (n=1092)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=3412)

- **FILTRO** `ibs_7min` < `0.1972` → IC=-0.258 (n=1126)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1972
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=3378)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.213 (n=1090)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=3414)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.238 (n=1557)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=5123)

- **FILTRO** `ibs_7min` > `0.759` → IC=-0.177 (n=1668)

  - _Acción_: SKIP cuando `ibs_7min` > 0.759
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=5012)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1526)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=3254)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.246 (n=1171)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3609)

- **FILTRO** `ibs_7min` < `0.7427` → IC=-0.181 (n=1194)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7427
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=3586)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.178 (n=1194)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3586)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=1224)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=3689)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.172 (n=1228)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3685)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.191 (n=1195)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3718)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.265 (n=1201)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=3930)

- **FILTRO** `ibs_7min` < `0.7037` → IC=-0.229 (n=1282)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3849)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=1674)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=5238)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.279 (n=1132)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3738)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.232 (n=1216)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3654)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.212 (n=1171)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3699)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.204 (n=1618)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=4925)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1031)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=514)

- **FILTRO** `libro_liquidez` < `10550.0548` → IC=-0.148 (n=140)

  - _Acción_: SKIP cuando `libro_liquidez` < 10550.0548
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=420)

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
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=541)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.129 (n=705)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.151 (n=236)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 459.6089 (IC base=+0.115)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `417.524` → IC=+0.141 (n=143)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 417.524 (IC base=+0.138)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.121 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 13.0 (IC base=+0.096)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.170 (n=95)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.092)

- **PATRÓN** `total_vol_5m` < `391.8444` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 391.8444 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 69.0 (IC base=+0.092)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.180 (n=123)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.185 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 11.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.167 (n=109)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 6300.756 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 37.0 (IC base=+0.139)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.151 (n=124)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.141 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 13.0 (IC base=+0.104)

- **PATRÓN** `total_vol_5m` < `257344.8` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 257344.8 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `3728.9067` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3728.9067 (IC base=+0.104)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.339 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=216)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.365 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=51)

- **FILTRO** `T_h` > `87.9957` → IC=-0.463 (n=25)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=76)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.222 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.141)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0142` → IC=-0.206 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.6199` → IC=-0.267 (n=114)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.6199
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=226)

- **FILTRO** `pct_vs_K` |x|> `3.5279` → IC=-0.438 (n=95)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.5279
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=186)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `81.2732` → IC=-0.175 (n=81)

  - _Acción_: SKIP cuando `T_h` > 81.2732
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=41)

- **FILTRO** `pct_vs_K` |x|> `2.7217` → IC=-0.337 (n=41)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7217
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=81)

- **FILTRO** `sigma_h` < `0.0071` → IC=-0.305 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=25)

- **FILTRO** `T_h` > `144.6113` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` > 144.6113
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=77)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.4552` → IC=-0.378 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4552
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **FILTRO** `sigma_h` > `0.0095` → IC=-0.300 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=72)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.380 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=72)

- **FILTRO** `T_h` > `64.7514` → IC=-0.331 (n=63)

  - _Acción_: SKIP cuando `T_h` > 64.7514
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0146` → IC=-0.167 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0146
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=61)

- **FILTRO** `T_h` > `135.1308` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `T_h` > 135.1308
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `pct_vs_K` |x|> `5.0364` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.0364
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=61)

- **FILTRO** `sigma_h` < `0.0142` → IC=-0.360 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **FILTRO** `T_h` > `63.9197` → IC=-0.384 (n=41)

  - _Acción_: SKIP cuando `T_h` > 63.9197
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.462 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.386)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.472 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.386)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.444 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.386)

- **PATRÓN** `dist_50` > `0.4444` → IC=+0.472 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.386)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.464 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.386)

- **PATRÓN** `edge` > `0.1023` → IC=+0.452 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.414)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.447 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.414)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.414)

- **PATRÓN** `dist_50` > `0.3792` → IC=+0.471 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3792 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.439 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.414)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.2825` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2825 (IC base=+0.480)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.469 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.480)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.460 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.480)

- **PATRÓN** `T_h` > `1.1094` → IC=+0.460 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1094 (IC base=+0.480)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.480)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.462 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.480)

- **PATRÓN** `edge` > `0.115` → IC=+0.472 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.115 (IC base=+0.472)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.472 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.472)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.469 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.472)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.485 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.472)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.462 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.472)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.461 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.472)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=149)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=257)

- **FILTRO** `streak_estiramiento` > `0.8365` → IC=-0.173 (n=53)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8365
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=163)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `streak_estiramiento` < 0.4576 (IC base=+0.030)

- **PATRÓN** `streak_estiramiento` < `0.7314` → IC=+0.128 (n=143)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.7314 (IC base=+0.039)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `ballena_activa_n` > `52.0` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 52.0
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=33)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_racha` < 990711.2 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 52.0 (IC base=+0.000)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=77)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=87)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=671)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=677)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=365)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `2389.5844` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2389.5844
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=536)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1069)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=651)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=656)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2660)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1367)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=1375)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.187 (n=461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0042 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.217 (n=626)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1625` → IC=+0.193 (n=1216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1625 (IC base=+0.185)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2175` → IC=+0.190 (n=462)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio_macro` |x|> 0.2175 (IC base=+0.185)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1305` → IC=+0.229 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1305 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.198 (n=980)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 11.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.186 (n=1388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 16.0 (IC base=+0.185)

- **PATRÓN** `ibs_15` > `0.6129` → IC=+0.260 (n=1382)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6129 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.4454` → IC=+0.187 (n=327)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.4454 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.5623` → IC=+0.174 (n=1360)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.5623 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.122` → IC=+0.270 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.122 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2965.5726` → IC=+0.192 (n=921)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2965.5726 (IC base=+0.185)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=471)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.224 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.205 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.286 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.206)

- **PATRÓN** `drift_15min` |x|≤ `0.3806` → IC=+0.214 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3806 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.232 (n=110)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.206)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1492` → IC=+0.281 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1492 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.267 (n=328)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.281 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.575` → IC=+0.257 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.575 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `15855.155` → IC=+0.250 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15855.155 (IC base=+0.206)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `25.228` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 25.228
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=303)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.164 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0034 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.164 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0057 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0692` → IC=+0.167 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0692 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1407` → IC=+0.159 (n=215)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.1407 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.258` → IC=+0.170 (n=222)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.258 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.164 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.141 (n=324)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 16.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.6213` → IC=+0.223 (n=323)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6213 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1542` → IC=+0.160 (n=248)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1542 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.218 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `9475.4181` → IC=+0.151 (n=147)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 9475.4181 (IC base=+0.141)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` < `4.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=73)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.152 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=69)

- **FILTRO** `ibs_15` > `0.2175` → IC=-0.250 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2175
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=68)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.229 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1498` → IC=+0.199 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1498 (IC base=+0.157)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.197 (n=153)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.157)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2836` → IC=+0.208 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2836 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.192 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 11.0 (IC base=+0.157)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.241 (n=172)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.116` → IC=+0.163 (n=99)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.116 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.4684` → IC=+0.163 (n=188)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.4684 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.532` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.532 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=136)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `3004.2322` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3004.2322 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.210 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.157)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5688` → IC=-0.142 (n=118)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5688
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=736)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.943` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.943 (IC base=+0.016)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0235` → IC=+0.240 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0235 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.191 (n=166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.177)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0401` → IC=+0.187 (n=375)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.0401 (IC base=+0.177)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.240 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_15` > `0.5429` → IC=+0.272 (n=375)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5429 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1268` → IC=+0.194 (n=227)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1268 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.6263` → IC=+0.181 (n=437)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.6263 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.303` → IC=+0.229 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.303 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.952` → IC=+0.177 (n=317)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 5.952 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2843.9766` → IC=+0.256 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2843.9766 (IC base=+0.177)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.164 (n=418)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` < 0.1176 (IC base=+0.046)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.377 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.340)

- **PATRÓN** `drift_60min` |x|≤ `0.1089` → IC=+0.351 (n=247)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1089 (IC base=+0.340)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.363 (n=247)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.340)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.392 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.340)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.363 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.340)

- **PATRÓN** `ibs_15` > `0.7856` → IC=+0.382 (n=370)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7856 (IC base=+0.340)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.384 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.143` → IC=+0.351 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.143 (IC base=+0.340)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.346 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.357 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.340)

- **PATRÓN** `ballena_activa_n` < `475.0` → IC=+0.363 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 475.0 (IC base=+0.340)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.349 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.346)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.389 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.346)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.355 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.346)

- **PATRÓN** `drift_15min` |x|≤ `0.4202` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4202 (IC base=+0.346)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.365 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.346)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.414 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.346)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.372 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.346)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.346 (n=219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.346)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.377 (n=209)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.346)

- **PATRÓN** `dist_vwap_pct` > `0.4001` → IC=+0.418 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4001 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.597` → IC=+0.354 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.597 (IC base=+0.346)

- **PATRÓN** `libro_liquidez` > `15484.5662` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15484.5662 (IC base=+0.346)

- **PATRÓN** `ballena_activa_n` < `582.0` → IC=+0.401 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 582.0 (IC base=+0.346)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.370 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.330)

- **PATRÓN** `drift_60min` |x|≤ `0.1039` → IC=+0.345 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1039 (IC base=+0.330)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0624` → IC=+0.342 (n=162)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0624 (IC base=+0.330)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.358 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.330)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.383 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.330)

- **PATRÓN** `ibs_15` > `0.7401` → IC=+0.390 (n=162)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7401 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` > `0.4449` → IC=+0.349 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4449 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` < `0.1109` → IC=+0.344 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1109 (IC base=+0.330)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.275` → IC=+0.362 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.275 (IC base=+0.330)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.342 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `3507.1457` → IC=+0.354 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3507.1457 (IC base=+0.330)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.013` → IC=-0.212 (n=598)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1796)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.189 (n=775)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1619)

- **FILTRO** `libro_liquidez` < `3905.4186` → IC=-0.133 (n=1580)

  - _Acción_: SKIP cuando `libro_liquidez` < 3905.4186
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=814)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.138` → IC=+0.266 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.138 (IC base=-0.059)

- **PATRÓN** `ibs_15` > `0.6324` → IC=+0.268 (n=589)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6324 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1102` → IC=+0.186 (n=361)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1102 (IC base=-0.059)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1175` → IC=+0.239 (n=968)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1175 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1786` → IC=+0.241 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1786 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.356` → IC=+0.281 (n=1451)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.356 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.8693` → IC=+0.275 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8693 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.218 (n=360)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1083)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.226 (n=476)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=967)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.207 (n=914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=529)

- **FILTRO** `sigma_ewma_delta_pct` > `19.716` → IC=-0.244 (n=256)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.716
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1187)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.186 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0027 (IC base=+0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.275 (n=69)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.7413` → IC=+0.331 (n=152)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7413 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1319` → IC=+0.296 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1319 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.5257` → IC=+0.283 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5257 (IC base=+0.086)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6625` → IC=-0.205 (n=93)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6625
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=282)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=358)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.174 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.005 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.214 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.142)

- **PATRÓN** `drift_15min` |x|≤ `0.4193` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.4193 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1323` → IC=+0.153 (n=188)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1323 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.240 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.6625` → IC=+0.257 (n=282)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6625 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1135` → IC=+0.182 (n=199)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1135 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.878` → IC=+0.154 (n=241)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 8.878 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=358)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `10911.5134` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 10911.5134 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.238 (n=589)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.225)

- **PATRÓN** `drift_15min` |x|≤ `0.774` → IC=+0.233 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.774 (IC base=+0.225)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2005` → IC=+0.255 (n=267)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2005 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.241 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.225)

- **PATRÓN** `ibs_15` < `0.273` → IC=+0.279 (n=518)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.273 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.7277` → IC=+0.279 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7277 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.01` → IC=+0.243 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.01 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.262` → IC=+0.229 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.262 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `3504.653` → IC=+0.229 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3504.653 (IC base=+0.225)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1671` → IC=-0.223 (n=193)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1671
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=377)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.257 (n=142)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=428)

- **FILTRO** `sigma_ewma_delta_pct` > `18.012` → IC=-0.133 (n=300)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.012
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2405)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.161)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.161)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0746` → IC=+0.217 (n=242)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0746 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.3636` → IC=+0.258 (n=271)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3636 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` < `0.1869` → IC=+0.214 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1869 (IC base=-0.045)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0196` → IC=-0.262 (n=360)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0196
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=361)

- **FILTRO** `drift_15min` |x|> `1.2` → IC=-0.242 (n=180)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=541)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.260 (n=181)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=540)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1526` → IC=+0.272 (n=134)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1526 (IC base=-0.044)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1035` → IC=+0.375 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1035 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.312 (n=403)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `1.0728` → IC=+0.402 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0728 (IC base=-0.044)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.2378` → IC=+0.160 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2378 (IC base=+0.077)

- **PATRÓN** `drift_15min` |x|≤ `0.5874` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `drift_15min` |x|≤ 0.5874 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.077)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.2378` → IC=+0.160 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2378 (IC base=+0.077)

- **PATRÓN** `drift_15min` |x|≤ `0.5874` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `drift_15min` |x|≤ 0.5874 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.077)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.299 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.301 (n=275)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.319 (n=202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1428` → IC=+0.300 (n=404)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1428 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.329 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.331 (n=606)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2727` → IC=+0.333 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2727 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.164` → IC=+0.332 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.164 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.294 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `14408.9622` → IC=+0.304 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14408.9622 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.310 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.295 (n=154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.335 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.284)

- **PATRÓN** `drift_15min` |x|≤ `0.3892` → IC=+0.283 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3892 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.291 (n=113)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1428` → IC=+0.326 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1428 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.304 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.312 (n=339)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.365 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.359 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `15942.3752` → IC=+0.326 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15942.3752 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.311 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.310 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.302)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1481` → IC=+0.322 (n=178)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1481 (IC base=+0.302)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.346 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.346 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.302)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.344 (n=267)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.302)

- **PATRÓN** `dist_vwap_pct` > `0.612` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.612 (IC base=+0.302)

- **PATRÓN** `dist_vwap_pct` < `0.1658` → IC=+0.304 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1658 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.335 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.302)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.309 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.302)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2669` → IC=-0.181 (n=67)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2669
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=202)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1129` → IC=-0.181 (n=67)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1129
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=202)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.121` → IC=-0.164 (n=105)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.121
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=327)

- **FILTRO** `drift_15min` |x|> `0.4386` → IC=-0.135 (n=146)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4386
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=286)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1958` → IC=-0.120 (n=77)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1958
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=78)

- **FILTRO** `drift_60min` |x|> `0.1544` → IC=-0.214 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1544
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1066` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1066
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `79.3918` → IC=+0.177 (n=255)

  - _Acción_: Kelly boost +0.89€ cuando `T_h` > 79.3918 (IC base=+0.168)

- **PATRÓN** `ratio` < `0.973` → IC=+0.462 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.168)

- **PATRÓN** `T_h` > `145.8408` → IC=+0.406 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8408 (IC base=+0.345)

- **PATRÓN** `ratio` > `1.01` → IC=+0.369 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.01 (IC base=+0.345)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.4275` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `T_h` > 144.4275 (IC base=+0.136)

- **PATRÓN** `ratio` < `0.9934` → IC=+0.286 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9934 (IC base=+0.136)

- **PATRÓN** `T_h` > `97.9834` → IC=+0.311 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 97.9834 (IC base=+0.299)

- **PATRÓN** `ratio` > `1.0422` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0422 (IC base=+0.299)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `81.6124` → IC=+0.236 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6124 (IC base=+0.217)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.401 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.217)

- **PATRÓN** `T_h` > `102.672` → IC=+0.347 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 102.672 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.376 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1402` → IC=+0.455 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1402 (IC base=+0.404)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6129 sube el IC de +0.185 a +0.260 en UPDOWN_GBM#15min (n=1382). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.206 a +0.267 en UPDOWN_GBM#BTC#15min (n=328). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6213 sube el IC de +0.141 a +0.223 en UPDOWN_GBM#ETH#15min (n=323). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.157 a +0.241 en UPDOWN_GBM#SOL#15min (n=172). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5429 sube el IC de +0.177 a +0.272 en UPDOWN_GBM#XRP#15min (n=375). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.046 a +0.164 en UPDOWN_GBM#XRP#15min (n=418). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6324 sube el IC de -0.059 a +0.268 en UPDOWN_GBM_15M_TARDIO (n=589). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.356 sube el IC de -0.039 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1451). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7413 sube el IC de +0.086 a +0.331 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=152). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6625 sube el IC de +0.142 a +0.257 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=282). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.273 sube el IC de +0.225 a +0.279 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=518). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.161 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3636 sube el IC de -0.045 a +0.258 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=271). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.044 a +0.312 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=403). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.292 a +0.331 en UPDOWN_GBM_IBS_ALTO (n=606). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.284 a +0.312 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=339). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.302 a +0.344 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=267). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7856 sube el IC de +0.340 a +0.382 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=370). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.346 a +0.377 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=209). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7401 sube el IC de +0.330 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=162). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1234 | +0.090 | +152.68€ | 2 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1234 | +0.090 | +152.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 906 | +0.099 | +129.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 906 | +0.099 | +129.33€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 242 | +0.045 | +4.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 242 | +0.045 | +4.70€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 23158 | -0.092 | -3068.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1386 | -0.045 | -208.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 21772 | -0.095 | -2859.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3529 | -0.088 | -572.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3529 | -0.088 | -572.68€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1386 | -0.045 | -208.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1386 | -0.045 | -208.83€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6631 | -0.033 | -599.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6631 | -0.033 | -599.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6107 | -0.095 | -434.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6107 | -0.095 | -434.65€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5131 | -0.179 | -1092.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5131 | -0.179 | -1092.38€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 15516 | -0.033 | +4123.46€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4088 | -0.002 | +1824.39€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 11428 | -0.044 | +2299.07€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 15516 | -0.033 | +4123.46€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4088 | -0.002 | +1824.39€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 11428 | -0.044 | +2299.07€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1379 | -0.102 | -183.33€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 152 | -0.045 | -16.27€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1227 | -0.109 | -167.06€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 762 | -0.090 | -94.78€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 128 | -0.038 | -11.04€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 634 | -0.101 | -83.73€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 419 | -0.130 | -74.67€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 395 | -0.132 | -69.45€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 84639 | +0.113 | -4308.12€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 12992 | +0.183 | -430.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 334 | -0.104 | -47.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 65676 | +0.100 | -3644.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5637 | +0.110 | -184.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 10931 | +0.097 | -974.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 43 | -0.167 | -2.82€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 10873 | +0.099 | -959.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 17122 | +0.132 | -344.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4047 | +0.201 | -140.84€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 10884 | +0.112 | -162.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2149 | +0.109 | -19.55€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 10971 | +0.088 | -1067.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 50 | -0.077 | -4.56€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 10906 | +0.089 | -1051.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 18063 | +0.124 | -346.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5023 | +0.175 | -80.95€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 10994 | +0.106 | -207.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2034 | +0.098 | -49.47€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 16604 | +0.115 | -941.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3786 | +0.187 | -209.66€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 237 | -0.065 | +6.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11127 | +0.093 | -622.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1454 | +0.130 | -115.41€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 10948 | +0.102 | -634.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 43 | -0.033 | +7.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 10892 | +0.103 | -642.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 13407 | +0.191 | -892.96€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 13407 | +0.191 | -892.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3241 | +0.169 | -342.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3241 | +0.169 | -342.35€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 963 | +0.193 | -2.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 963 | +0.193 | -2.72€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3170 | +0.181 | -271.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3170 | +0.181 | -271.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2840 | +0.240 | -84.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2840 | +0.240 | -84.00€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3114 | +0.189 | -205.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3114 | +0.189 | -205.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 631 | +0.429 | -18.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 631 | +0.429 | -18.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 241 | +0.430 | -5.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 241 | +0.430 | -5.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 238 | +0.438 | -1.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 238 | +0.438 | -1.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 144 | +0.404 | -9.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 144 | +0.404 | -9.92€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 45982 | +0.197 | -3651.29€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 45982 | +0.197 | -3651.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 7984 | +0.175 | -951.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 7984 | +0.175 | -951.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7326 | +0.224 | -265.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7326 | +0.224 | -265.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 7943 | +0.173 | -958.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 7943 | +0.173 | -958.53€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7418 | +0.219 | -288.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7418 | +0.219 | -288.15€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 7593 | +0.204 | -494.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 7593 | +0.204 | -494.85€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 7718 | +0.193 | -692.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 7718 | +0.193 | -692.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 17280 | +0.120 | +196.64€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 17280 | +0.120 | +196.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 8574 | +0.124 | +149.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 8574 | +0.124 | +149.58€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 8706 | +0.116 | +47.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 8706 | +0.116 | +47.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1371 | +0.289 | -17.56€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1371 | +0.289 | -17.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 610 | +0.273 | -23.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 610 | +0.273 | -23.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 658 | +0.295 | +5.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 658 | +0.295 | +5.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 103 | +0.338 | +1.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 103 | +0.338 | +1.04€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 602 | +0.437 | -1.01€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 602 | +0.437 | -1.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 282 | +0.437 | -1.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 282 | +0.437 | -1.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 280 | +0.440 | +0.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 280 | +0.440 | +0.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 40 | +0.381 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 40 | +0.381 | -0.11€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 999 | +0.075 | -39.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 348 | +0.060 | -28.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 651 | +0.084 | -11.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 59 | +0.139 | +5.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 59 | +0.139 | +5.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 785 | +0.085 | -12.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 134 | +0.088 | -1.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 651 | +0.084 | -11.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 155 | +0.003 | -32.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 155 | +0.003 | -32.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 31399 | +0.099 | -937.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2612 | +0.091 | +24.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 28787 | +0.099 | -962.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 17734 | +0.103 | -264.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2612 | +0.091 | +24.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 15122 | +0.105 | -289.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 5730 | +0.110 | -12.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 5730 | +0.110 | -12.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 7935 | +0.081 | -660.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 7935 | +0.081 | -660.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 762 | +0.226 | -93.34€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 762 | +0.226 | -93.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 762 | +0.226 | -93.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 762 | +0.226 | -93.34€ | 1 | 4 |
| ✅ GBM_LATE_15M | 22845 | +0.079 | +10621.70€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 22845 | +0.079 | +10621.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3780 | +0.192 | +2732.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3780 | +0.192 | +2732.54€ | 0 | 17 |
| ✅ GBM_LATE_15M#BTC | 3384 | +0.173 | +2278.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3384 | +0.173 | +2278.44€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 3931 | +0.200 | +2952.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3931 | +0.200 | +2952.69€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 3402 | +0.014 | +621.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3402 | +0.014 | +621.81€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3321 | -0.034 | +770.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3321 | -0.034 | +770.02€ | 4 | 16 |
| ✅ GBM_LATE_15M#XRP | 5027 | -0.045 | +1266.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5027 | -0.045 | +1266.21€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 24138 | +0.082 | +12617.24€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 24138 | +0.082 | +12617.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4573 | +0.016 | +2583.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4573 | +0.016 | +2583.25€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5049 | +0.009 | +992.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5049 | +0.009 | +992.66€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3409 | +0.262 | +3432.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3409 | +0.262 | +3432.58€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3883 | -0.003 | +684.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3883 | -0.003 | +684.04€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3930 | +0.022 | +1457.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3930 | +0.022 | +1457.13€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3294 | +0.272 | +3467.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3294 | +0.272 | +3467.56€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 18469 | +0.167 | +13524.99€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 18469 | +0.167 | +13524.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2766 | +0.206 | +2190.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2766 | +0.206 | +2190.93€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2931 | +0.148 | +2073.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2931 | +0.148 | +2073.11€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2878 | +0.209 | +2297.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2878 | +0.209 | +2297.12€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3081 | +0.135 | +2075.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3081 | +0.135 | +2075.13€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3461 | +0.113 | +2284.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3461 | +0.113 | +2284.76€ | 1 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3352 | +0.200 | +2603.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3352 | +0.200 | +2603.93€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4551 | +0.122 | +1825.54€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4551 | +0.122 | +1825.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1279 | +0.117 | +532.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1279 | +0.117 | +532.42€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1242 | +0.141 | +546.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1242 | +0.141 | +546.83€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 973 | +0.088 | +272.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 973 | +0.088 | +272.59€ | 2 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 22938 | +0.173 | +16725.99€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 22938 | +0.173 | +16725.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3605 | +0.219 | +3018.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3605 | +0.219 | +3018.10€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3590 | +0.147 | +2313.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3590 | +0.147 | +2313.42€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3729 | +0.226 | +3221.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3729 | +0.226 | +3221.59€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3720 | +0.136 | +2452.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3720 | +0.136 | +2452.02€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4038 | +0.107 | +2428.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4038 | +0.107 | +2428.42€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4256 | +0.202 | +3292.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4256 | +0.202 | +3292.45€ | 0 | 25 |
| ✅ GBM_LATE_5M | 6425 | +0.143 | +3549.84€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 6425 | +0.143 | +3549.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 589 | +0.185 | +410.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 589 | +0.185 | +410.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1680 | +0.142 | +1079.05€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1680 | +0.142 | +1079.05€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 2033 | +0.147 | +1105.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2033 | +0.147 | +1105.95€ | 0 | 33 |
| ✅ GBM_LATE_5M#SOL | 415 | +0.054 | +73.25€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 415 | +0.054 | +73.25€ | 1 | 6 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1484 | +0.068 | +654.77€ | 2 | 12 |
| ✅ GBM_LATE_60M#60min | 1484 | +0.068 | +654.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 533 | +0.085 | +220.18€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 533 | +0.085 | +220.18€ | 0 | 12 |
| ✅ GBM_LATE_60M#ETH | 493 | +0.076 | +270.47€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 493 | +0.076 | +270.47€ | 2 | 17 |
| ✅ GBM_LATE_60M#SOL | 458 | +0.039 | +164.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 458 | +0.039 | +164.12€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 333 | -0.264 | -26.90€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 333 | -0.264 | -26.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 126 | -0.219 | -9.14€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 126 | -0.219 | -9.14€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 110 | -0.277 | -10.45€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 110 | -0.277 | -10.45€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 97 | -0.298 | -7.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 97 | -0.298 | -7.31€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 640 | +0.058 | +124.47€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 640 | +0.058 | +124.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 252 | +0.051 | +43.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 252 | +0.051 | +43.22€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 189 | +0.029 | -3.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 189 | +0.029 | -3.13€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 199 | +0.092 | +84.38€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 199 | +0.092 | +84.38€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN | 80 | +0.268 | +63.49€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 80 | +0.268 | +63.49€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 80 | +0.268 | +63.49€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 80 | +0.268 | +63.49€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1692 | +0.100 | +459.06€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1692 | +0.100 | +459.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1692 | +0.100 | +459.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1692 | +0.100 | +459.06€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 367 | -0.080 | -33.57€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 367 | -0.080 | -33.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 94 | -0.062 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 94 | -0.062 | -5.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 125 | -0.020 | -3.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 125 | -0.020 | -3.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1726 | +0.004 | +6.00€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1726 | +0.004 | +6.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 88 | -0.022 | -4.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 88 | -0.022 | -4.85€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 183 | -0.008 | +6.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 183 | -0.008 | +6.48€ | 5 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 122 | -0.040 | -6.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 122 | -0.040 | -6.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 732 | +0.034 | +26.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 732 | +0.034 | +26.69€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 462 | -0.006 | -8.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 462 | -0.006 | -8.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 139 | -0.053 | -7.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 139 | -0.053 | -7.93€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 994 | -0.048 | -29.93€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 994 | -0.048 | -29.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 284 | -0.045 | -13.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 284 | -0.045 | -13.00€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 326 | -0.037 | -4.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 326 | -0.037 | -4.81€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 384 | -0.060 | -12.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 384 | -0.060 | -12.11€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 14091 | -0.012 | -210.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14091 | -0.012 | -210.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2808 | -0.024 | -64.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2808 | -0.024 | -64.01€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 25631 | -0.009 | +1145.62€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 25631 | -0.009 | +1145.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4495 | +0.014 | +564.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4495 | +0.014 | +564.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4043 | -0.026 | -34.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4043 | -0.026 | -34.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4521 | +0.011 | +391.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4521 | +0.011 | +391.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3823 | -0.051 | -134.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3823 | -0.051 | -134.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4287 | -0.012 | +169.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4287 | -0.012 | +169.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4462 | +0.004 | +188.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4462 | +0.004 | +188.38€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5459 | -0.052 | -133.05€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5459 | -0.052 | -133.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1268 | -0.072 | -34.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1268 | -0.072 | -34.53€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 552 | -0.119 | -21.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 552 | -0.119 | -21.71€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1546 | -0.070 | -30.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1546 | -0.070 | -30.14€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 847 | -0.016 | -25.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 847 | -0.016 | -25.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 65552 | -0.074 | +1425.03€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 65552 | -0.074 | +1425.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 11053 | -0.080 | +625.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 11053 | -0.080 | +625.17€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10166 | -0.092 | -440.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10166 | -0.092 | -440.77€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 11184 | -0.070 | +579.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 11184 | -0.070 | +579.68€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 9693 | -0.094 | -177.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 9693 | -0.094 | -177.18€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 12043 | -0.050 | +339.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 12043 | -0.050 | +339.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 11413 | -0.064 | +498.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 11413 | -0.064 | +498.53€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6897 | -0.023 | -102.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6897 | -0.023 | -102.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1606 | -0.025 | -4.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1606 | -0.025 | -4.26€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1534 | -0.019 | -8.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1534 | -0.019 | -8.45€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1021 | -0.039 | -15.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1021 | -0.039 | -15.67€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1076 | +0.108 | +357.61€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 940 | +0.115 | +345.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 216 | +0.138 | +107.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 216 | +0.138 | +107.57€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 186 | +0.096 | +44.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 186 | +0.096 | +44.24€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 189 | +0.092 | +58.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 189 | +0.092 | +58.12€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 164 | +0.139 | +78.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 164 | +0.139 | +78.91€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 185 | +0.104 | +56.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 185 | +0.104 | +56.17€ | 0 | 5 |
| ✅ PRICE_TARGET_GBM | 504 | -0.091 | -20.76€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 227 | -0.138 | -42.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 185 | -0.174 | -45.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 177 | -0.081 | +2.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 135 | -0.091 | -3.97€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 100 | +0.000 | +19.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 80 | -0.012 | +13.30€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 400 | -0.114 | -36.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 621 | -0.213 | -44.19€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 254 | -0.199 | -34.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 222 | -0.192 | -32.62€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 218 | -0.232 | -25.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 191 | -0.241 | -29.15€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 149 | -0.202 | +15.78€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 135 | -0.201 | +12.72€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 548 | -0.213 | -49.05€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 238 | +0.408 | +183.41€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 58 | +0.383 | +47.57€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 58 | +0.383 | +47.57€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 152 | +0.480 | +140.60€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 152 | +0.480 | +140.60€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#sniper | 238 | +0.408 | +183.41€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 444 | +0.036 | +19.40€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 444 | +0.036 | +19.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 210 | +0.038 | +7.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 210 | +0.038 | +7.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 48 | -0.020 | -3.52€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 48 | -0.020 | -3.52€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 160 | +0.037 | +11.48€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 160 | +0.037 | +11.48€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 2620 | -0.025 | -114.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2620 | -0.025 | -114.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 565 | -0.022 | -22.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 565 | -0.022 | -22.81€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1096 | -0.027 | -50.23€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1096 | -0.027 | -50.23€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 65 | -0.037 | -4.30€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 65 | -0.037 | -4.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 1 | 0 |
| ✅ STREAK_FADE_60M#SOL | 28 | +0.033 | -0.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 28 | +0.033 | -0.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7197 | +0.023 | +109.89€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7197 | +0.023 | +109.89€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1553 | +0.034 | +46.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1553 | +0.034 | +46.36€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2174 | +0.013 | +4.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2174 | +0.013 | +4.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1349 | +0.032 | +37.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1349 | +0.032 | +37.83€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6721 | +0.010 | -50.67€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6721 | +0.010 | -50.67€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2679 | +0.016 | -6.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2679 | +0.016 | -6.65€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2643 | +0.011 | -18.23€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2643 | +0.011 | -18.23€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1399 | -0.003 | -25.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1399 | -0.003 | -25.79€ | 2 | 0 |
| ✅ UPDOWN_GBM | 31823 | +0.031 | +1882.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 8554 | +0.062 | +1479.67€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1175 | +0.005 | +8.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 20055 | +0.022 | +378.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1916 | +0.006 | +16.19€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2996 | +0.071 | +330.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 462 | +0.153 | +187.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 23 | -0.020 | -0.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2511 | +0.057 | +144.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 5915 | +0.032 | +388.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1066 | +0.080 | +242.51€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 326 | +0.021 | +7.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3618 | +0.028 | +124.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 858 | +0.002 | +13.86€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 47 | -0.112 | +0.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3757 | +0.039 | +211.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 434 | +0.144 | +164.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 18 | +0.000 | -0.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3305 | +0.026 | +46.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 6703 | +0.020 | +280.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2248 | +0.044 | +248.22€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 314 | +0.006 | +7.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3440 | +0.011 | +22.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 661 | +0.005 | -1.31€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 40 | -0.143 | +3.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 7779 | +0.016 | +196.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2176 | +0.021 | +129.66€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 308 | -0.006 | -2.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4864 | +0.017 | +68.61€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 397 | +0.014 | +3.65€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 34 | -0.167 | -2.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4671 | +0.035 | +476.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2168 | +0.076 | +506.93€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 186 | -0.005 | -3.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2317 | -0.002 | -27.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 121 | -0.142 | +1.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 493 | +0.340 | +148.24€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 493 | +0.340 | +148.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 278 | +0.346 | +83.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 278 | +0.346 | +83.14€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 215 | +0.330 | +65.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 215 | +0.330 | +65.10€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 10587 | -0.043 | +2249.31€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 10587 | -0.043 | +2249.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 626 | -0.045 | +333.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 626 | -0.045 | +333.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1979 | -0.121 | +56.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1979 | -0.121 | +56.37€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 265 | +0.163 | +157.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 265 | +0.163 | +157.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1159 | +0.199 | +658.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1159 | +0.199 | +658.99€ | 2 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3275 | -0.065 | +507.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3275 | -0.065 | +507.37€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3283 | -0.077 | +536.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3283 | -0.077 | +536.40€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 122 | +0.057 | +11.27€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 122 | +0.057 | +11.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 122 | +0.057 | +11.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 122 | +0.057 | +11.27€ | 2 | 4 |
| ✅ UPDOWN_GBM_IBS_ALTO | 807 | +0.292 | +664.46€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 807 | +0.292 | +664.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 451 | +0.284 | +342.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 451 | +0.284 | +342.51€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 356 | +0.302 | +321.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 356 | +0.302 | +321.94€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 701 | -0.107 | -79.88€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 701 | -0.107 | -79.88€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 194 | -0.066 | -11.97€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 194 | -0.066 | -11.97€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 69 | -0.162 | -8.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 69 | -0.162 | -8.81€ | 3 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 60 | -0.210 | -9.56€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 60 | -0.210 | -9.56€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2141 | +0.305 | +1101.63€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 724 | +0.253 | +111.31€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 784 | +0.295 | +332.29€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 633 | +0.376 | +658.04€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.061) — sin ventaja clara. oversold(IBS<0.3): IC=+0.048 n=11128 | neutral: IC=+0.027 n=12025 | overbought(IBS>0.7): IC=+0.088 n=11390
  - _Datos_: n=35820 IC=+0.054 PNL=+4315.83€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 496 celda(s) pasan gate riguroso completo de 2127 evaluadas (n>=40) y 3137 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.021 < 0.08 — monitorear
  - _Datos_: n=2172 IC=+0.021 PNL=+128.71€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=784/15 IC=+0.295 PNL=+332.29€ | BTC: n=724/15 IC=+0.253 PNL=+111.31€ | SOL: n=633/15 IC=+0.376 PNL=+658.04€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 29 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: 31692 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.101 n=241/60 | contraria IC=+0.148 n=228 | gap=-0.047 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=266, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 164 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=660/40 IC=+0.006 PNL=-0.80€ | BTC#60min: n=856/40 IC=+0.002 PNL=+13.87€ | SOL#60min: n=396/40 IC=+0.015 PNL=+4.16€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.052 n=300195 | tras_1loss IC=+0.075 n=233799 | tras_2loss IC=+0.044 n=99272/40 | gap=+0.008 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.021 n=3579 | contrario_BTC IC=+0.022 n=3144/40 | gap=+0.001 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.08 con n=279 PNL=+189.48€
  - _Datos_: n=279 IC=+0.187 PNL=+189.48€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.212 > 0.08 con n=335 PNL=+234.80€
  - _Datos_: n=335 IC=+0.212 PNL=+234.80€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.269 > 0.08 con n=37 PNL=+31.71€
  - _Datos_: n=37 IC=+0.269 PNL=+31.71€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.339 > 0.1 con n=1779 PNL=+1066.54€
  - _Datos_: n=1779 IC=+0.339 PNL=+1066.54€

**🟡 H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=250 PNL=+33.14€
  - _Datos_: n=250 IC=+0.083 PNL=+33.14€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=49 IC=+0.186 PNL=+32.29€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=49 IC=+0.186 PNL=+32.29€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=30412 IC=+0.030 PNL=+1783.08€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=30412 IC=+0.030 PNL=+1783.08€

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
  - _Estado_: n=1388 IC=+0.012 PNL=+5.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1388 IC=+0.012 PNL=+5.60€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=524 IC=-0.009 PNL=+11.62€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=524 IC=-0.009 PNL=+11.62€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=430 IC=+0.023 PNL=+23.10€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=430 IC=+0.023 PNL=+23.10€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.1 con n=1838 PNL=+1144.89€
  - _Datos_: n=1838 IC=+0.186 PNL=+1144.89€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=968 IC=+0.044 PNL=+70.57€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=968 IC=+0.044 PNL=+70.57€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1062 IC=+0.080 PNL=+244.12€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1062 IC=+0.080 PNL=+244.12€

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
  - _Estado_: n=4916 IC=+0.068 PNL=+1053.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4916 IC=+0.068 PNL=+1053.26€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=131 IC=-0.244 PNL=-6.49€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=131 IC=-0.244 PNL=-6.49€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=218 IC=-0.014 PNL=+12.64€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=218 IC=-0.014 PNL=+12.64€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=470 IC=+0.015 PNL=+35.03€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=470 IC=+0.015 PNL=+35.03€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=40 IC=+0.024 PNL=+0.32€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=40 IC=+0.024 PNL=+0.32€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=4795 IC=-0.004 PNL=-10.86€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4795 IC=-0.004 PNL=-10.86€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.176 > 0.08 con n=66 PNL=+18.24€
  - _Datos_: n=66 IC=+0.176 PNL=+18.24€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.265 n=79) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=79 IC=+0.265 PNL=+61.57€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=6063 IC=+0.028 PNL=+311.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=6063 IC=+0.028 PNL=+311.99€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=1937 IC=+0.051 PNL=+229.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1937 IC=+0.051 PNL=+229.11€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=335 PNL=+94.70€
  - _Datos_: n=335 IC=+0.105 PNL=+94.70€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.140 > 0.08 con n=520 PNL=+125.90€
  - _Datos_: n=520 IC=+0.140 PNL=+125.90€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.08 con n=411 PNL=+203.29€
  - _Datos_: n=411 IC=+0.127 PNL=+203.29€

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
  - _Estado_: n=4601 IC=+0.038 PNL=+337.68€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4601 IC=+0.038 PNL=+337.68€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=617 PNL=+238.86€
  - _Datos_: n=617 IC=+0.124 PNL=+238.86€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=140 IC=-0.056 PNL=+31.39€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=140 IC=-0.056 PNL=+31.39€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.451 > 0.1 con n=1053 PNL=+1068.65€
  - _Datos_: n=1053 IC=+0.451 PNL=+1068.65€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=10905 IC=+0.055 PNL=+1350.02€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=10905 IC=+0.055 PNL=+1350.02€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.200 > 0.1 con n=2932 PNL=+1591.85€
  - _Datos_: n=2932 IC=+0.200 PNL=+1591.85€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.165 < -0.1 con n=201 PNL=+16.12€
  - _Datos_: n=201 IC=-0.165 PNL=+16.12€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1664 IC=+0.046 PNL=+176.37€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1664 IC=+0.046 PNL=+176.37€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=65 IC=-0.127 PNL=+3.73€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=65 IC=-0.127 PNL=+3.73€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.1 con n=343 PNL=+105.98€
  - _Datos_: n=343 IC=+0.132 PNL=+105.98€

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
  - _Estado_: n=15774 IC=-0.138 PNL=+1063.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=15774 IC=-0.138 PNL=+1063.94€

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
  - _Estado_: n=1729 IC=+0.135 PNL=+908.05€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1729 IC=+0.135 PNL=+908.05€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=1799 PNL=+1132.26€
  - _Datos_: n=1799 IC=+0.189 PNL=+1132.26€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=3237 IC=+0.016 PNL=+97.75€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3237 IC=+0.016 PNL=+97.75€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=1820 PNL=+936.74€
  - _Datos_: n=1820 IC=+0.083 PNL=+936.74€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.08 con n=435 PNL=+220.66€
  - _Datos_: n=435 IC=+0.207 PNL=+220.66€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.242 < -0.1 con n=1565 PNL=-195.36€
  - _Datos_: n=1565 IC=-0.242 PNL=-195.36€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=4615 IC=+0.159 PNL=+2938.59€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=4615 IC=+0.159 PNL=+2938.59€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.08 con n=71 PNL=+29.16€
  - _Datos_: n=71 IC=+0.116 PNL=+29.16€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=1791 IC=+0.056 PNL=+439.48€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1791 IC=+0.056 PNL=+439.48€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.176 > 0.08 con n=1620 PNL=+1082.40€
  - _Datos_: n=1620 IC=+0.176 PNL=+1082.40€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=2637 IC=-0.034 PNL=+689.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2637 IC=-0.034 PNL=+689.76€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.081 > 0.08 con n=518 PNL=-54.52€
  - _Datos_: n=518 IC=+0.081 PNL=-54.52€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.232 > 0.08 con n=3051 PNL=-295.38€
  - _Datos_: n=3051 IC=+0.232 PNL=-295.38€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 33/40 ops en el filtro definido (IC actual=-0.043 PNL=+2.97€)
  - _Datos_: n=33 IC=-0.043 PNL=+2.97€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.093 n=880) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=880 IC=+0.093 PNL=+210.21€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.341 > 0.08 con n=231 PNL=+88.58€
  - _Datos_: n=231 IC=+0.341 PNL=+88.58€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=421) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=421 IC=+0.410 PNL=+589.92€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=7974 IC=+0.174 PNL=-951.01€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=7974 IC=+0.174 PNL=-951.01€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.205 > 0.1 con n=127 PNL=+76.45€
  - _Datos_: n=127 IC=+0.205 PNL=+76.45€
