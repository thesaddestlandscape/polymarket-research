# Hipótesis automáticas — 2026-09-13 07:39 UTC
_Generado por shadow_postmortem.py sobre 416620 resoluciones (PNL=+43977.57€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.385` → IC=-0.148 (n=194)

  - _Acción_: SKIP cuando `py_entrada` < 0.385
  - _Potencial_: sin este filtro IC_bueno=+0.242 (n=397)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=397)

- **PATRÓN** `py_entrada` > `0.385` → IC=+0.242 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.385 (IC base=+0.114)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.206 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.114)

- **PATRÓN** `banda_hit_calibrado` > `0.806` → IC=+0.265 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.806 (IC base=+0.114)

- **PATRÓN** `banda_z` > `10.773` → IC=+0.227 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.773 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.130 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 11.0 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=467)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.114)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=397)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.128 (n=127)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 98.0 (IC base=+0.036)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.375` → IC=-0.129 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.234 (n=314)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=288)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=313)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.234 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.121)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.192 (n=232)

  - _Acción_: Kelly boost +0.96€ cuando `n_total_lado` > 58.0 (IC base=+0.121)

- **PATRÓN** `banda_hit_calibrado` > `0.8049` → IC=+0.265 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8049 (IC base=+0.121)

- **PATRÓN** `banda_z` > `11.589` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.589 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=384)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 87.0 (IC base=+0.032)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=96)

- **FILTRO** `banda_hit_calibrado` < `0.6329` → IC=-0.214 (n=40)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6329
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=84)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=79)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=89)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.244 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.51 (IC base=+0.095)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.244 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.095)

- **PATRÓN** `banda_z` > `8.441` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.441 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=100)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `963.9705` → IC=+0.128 (n=84)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 963.9705 (IC base=+0.095)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.191)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.382 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `146.3` → IC=-0.263 (n=5316)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.3
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=15950)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `n_ballenas` < `4.0` → IC=-0.124 (n=1833)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=1139)

- **FILTRO** `restante_s_al_confirmar` < `140.79` → IC=-0.283 (n=743)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.79
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=2229)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `132.89` → IC=-0.291 (n=676)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.89
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2031)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `144.43` → IC=-0.162 (n=1374)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.43
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4125)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `157.46` → IC=-0.254 (n=1220)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.46
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3665)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.06` → IC=-0.347 (n=1341)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.06
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=2725)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.31` → IC=-0.295 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=133)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.189 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=77)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=84)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.52 (IC base=+0.022)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=20)

- **FILTRO** `py_entrada` > `0.3` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=27)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.200 (n=9914)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=2688)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `11044.8547` → IC=+0.193 (n=858)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 11044.8547 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=8111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=9786)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.245 (n=7225)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.173 (n=5305)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `6996.6608` → IC=+0.176 (n=1683)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 6996.6608 (IC base=+0.136)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.354 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `14488.4893` → IC=+0.214 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14488.4893 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=1134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.214 (n=1249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.270 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `12677.5597` → IC=+0.208 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12677.5597 (IC base=+0.205)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.177 (n=264)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.615 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=280)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `4690.1012` → IC=+0.152 (n=225)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4690.1012 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.191 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.165 (n=538)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.425 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=533)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `3889.9068` → IC=+0.163 (n=411)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3889.9068 (IC base=+0.137)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=1843)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.331 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` < `0.305` → IC=+0.328 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.305 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.238 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `4383.8031` → IC=+0.244 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4383.8031 (IC base=+0.238)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.223 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=595)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `1510.4431` → IC=+0.150 (n=447)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1510.4431 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `4449.086` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4449.086 (IC base=+0.086)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.213 (n=489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.196 (n=1012)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 12.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.426 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.279 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.187 (n=1054)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.03 (IC base=+0.181)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.325 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3435.4625` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3435.4625 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.138 (n=645)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.121)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.224 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=316)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.121)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=104)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.344 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=8322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=7071)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.218 (n=3012)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.340 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `5339.6996` → IC=+0.344 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5339.6996 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.178 (n=2009)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.180 (n=2102)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.168)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.377 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.338)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.362 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.338)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=2087)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=1760)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.185 (n=1330)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.72 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=1859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=1586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.326 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.237)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.191 (n=1054)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.7 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.190 (n=856)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.445 (n=346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.449 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `9523.4542` → IC=+0.461 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9523.4542 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.442 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.458 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `11651.323` → IC=+0.460 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11651.323 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.454 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.460 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.442 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `3923.6329` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3923.6329 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.422 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.433 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.429 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.429 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` < `12.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `libro_liquidez` < `5005.2013` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 5005.2013
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=28956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.236 (n=9468)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=5044)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.172 (n=3449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 12.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=4503)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.165)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=4352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=4349)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=1582)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=1838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4506)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.167)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=2209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.206 (n=1517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=4036)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.251 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4866)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=3307)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.246 (n=1688)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.189)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=3721)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.05` → IC=+0.137 (n=3407)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.05 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.146 (n=3715)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.94 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=4516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.41` → IC=+0.151 (n=3408)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.41 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=1861)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.130)

- **PATRÓN** `restante_min` < `3.99` → IC=+0.142 (n=1690)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` < 3.99 (IC base=+0.130)

- **PATRÓN** `restante_min` > `4.89` → IC=+0.145 (n=2340)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.89 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=2223)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `lag_apertura_s` < `6.5` → IC=+0.147 (n=2225)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 6.5 (IC base=+0.130)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=1860)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.47` → IC=+0.126 (n=2275)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.47 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.149 (n=1873)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.96` → IC=+0.147 (n=1717)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 2.96 (IC base=+0.118)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1640.8166` → IC=+0.298 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1640.8166 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.301 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.276)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.328 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `5128.7219` → IC=+0.294 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5128.7219 (IC base=+0.276)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.329 (n=290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.382 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1497.524` → IC=+0.311 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1497.524 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.335 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.328)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.357 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.328)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.328)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.366 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.328)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.436 (n=343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.432 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.430 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `1890.5013` → IC=+0.437 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1890.5013 (IC base=+0.428)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.433 (n=163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.434 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `5265.735` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5265.735 (IC base=+0.429)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.434 (n=181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.445 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.430 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `2133.31` → IC=+0.452 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2133.31 (IC base=+0.429)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.372)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.372)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.263)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.399 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.286 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `1390.7824` → IC=+0.287 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1390.7824 (IC base=+0.263)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.263)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.399 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.286 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `1390.7824` → IC=+0.287 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1390.7824 (IC base=+0.263)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9744` → IC=+0.229 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9744 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.2046` → IC=+0.243 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2046 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.829` → IC=+0.167 (n=2136)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.829 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6121` → IC=+0.254 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6121 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `1.0681` → IC=+0.241 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0681 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.1757` → IC=+0.191 (n=3714)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1757 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.1105` → IC=+0.194 (n=1388)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1105 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `2.8549` → IC=+0.191 (n=3580)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.8549 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.472` → IC=+0.193 (n=3580)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.472 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.5754` → IC=+0.124 (n=6815)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.5754 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.1278` → IC=+0.164 (n=2022)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1278 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `1.2013` → IC=+0.161 (n=2113)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2013 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` > `0.8681` → IC=+0.164 (n=1409)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.8681 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.1691` → IC=+0.226 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1691 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.4629` → IC=+0.194 (n=3516)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4629 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.204 (n=3279)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 165.0 (IC base=+0.056)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.190 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.184 (n=565)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.007 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3245` → IC=+0.170 (n=1243)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3245 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=830)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.032` → IC=+0.285 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.032 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.193 (n=161)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.6298` → IC=+0.158 (n=1137)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.6298 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.162 (n=1137)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.183 (n=1322)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.06 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.190 (n=903)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 64.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.256 (n=826)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.280 (n=616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.253 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.063` → IC=+0.287 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.063 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.363` → IC=+0.250 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.363 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.234 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2878` → IC=+0.293 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2878 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.7073` → IC=+0.268 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7073 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1576.15` → IC=+0.251 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1576.15 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.233 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.238 (n=414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.238 (n=414)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=983)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9263` → IC=+0.253 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9263 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.217 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.231 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2629` → IC=+0.224 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2629 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.8783` → IC=+0.212 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8783 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.1007` → IC=+0.212 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1007 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4925` → IC=+0.228 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4925 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.4189` → IC=+0.217 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4189 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.229 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.161 (n=884)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0048 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3183` → IC=+0.147 (n=1004)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3183 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.160 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.175 (n=1004)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6789 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.426` → IC=+0.178 (n=175)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.426 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.149 (n=1004)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2025 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1561` → IC=+0.202 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1561 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4143` → IC=+0.155 (n=895)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4143 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4133` → IC=+0.151 (n=895)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4133 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `12789.0736` → IC=+0.151 (n=669)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 12789.0736 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.169 (n=273)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 220.0 (IC base=+0.140)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.188 (n=1211)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0058 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=1277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.255 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.358` → IC=+0.231 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.358 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.183 (n=1015)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.3774` → IC=+0.177 (n=159)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.3774 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.6649` → IC=+0.183 (n=1125)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.6649 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.191 (n=1362)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.195 (n=313)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 16.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.218 (n=1044)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1461` → IC=+0.214 (n=460)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1461 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.3919` → IC=+0.230 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3919 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.234 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.393` → IC=+0.212 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.393 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.273 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.8456` → IC=+0.200 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8456 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.3042` → IC=+0.218 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3042 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1888.9584` → IC=+0.226 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1888.9584 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.210 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.211)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=87)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1534)

- **PATRÓN** `ibs_20min` > `0.9296` → IC=+0.158 (n=261)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.9296 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` < `0.1735` → IC=+0.337 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1735 (IC base=+0.007)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.23` → IC=+0.129 (n=483)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 4.23 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.6044` → IC=+0.409 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6044 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.1897` → IC=+0.348 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1897 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `2.4241` → IC=+0.337 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4241 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.1031` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1031 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.339 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.1485` → IC=+0.184 (n=150)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1485 (IC base=-0.008)

- **PATRÓN** `volumen_regimen` < `1.0344` → IC=+0.146 (n=408)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0344 (IC base=-0.008)

- **PATRÓN** `volumen_regimen` > `0.6164` → IC=+0.137 (n=464)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6164 (IC base=-0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2615` → IC=+0.205 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2615 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.4999` → IC=+0.167 (n=370)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4999 (IC base=-0.008)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=220)

- **FILTRO** `ibs_20min` < `0.2424` → IC=-0.176 (n=66)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2424
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=200)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.126 (n=1587)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=791)

- **FILTRO** `sigma_ewma_delta_pct` > `8.607` → IC=-0.198 (n=263)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.607
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2115)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` > `1.1487` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1487 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.338 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `3.0656` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0656 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.6425` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6425 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` < `0.6485` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6485 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` > `0.9331` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.9331 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.0864` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0864 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.209 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.048)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.245 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=-0.048)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.627` → IC=-0.188 (n=389)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.627
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1169)

- **FILTRO** `ibs_20min` < `0.641` → IC=-0.157 (n=1028)

  - _Acción_: SKIP cuando `ibs_20min` < 0.641
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=530)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.185 (n=319)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1239)

- **FILTRO** `ibs_20min` > `0.7778` → IC=-0.194 (n=590)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1776)

- **PATRÓN** `dist_vwap_pct` > `0.8527` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8527 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.290 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.088)

- **PATRÓN** `volumen_regimen` > `0.6107` → IC=+0.275 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6107 (IC base=-0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.289 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.088)

- **PATRÓN** `volumen_spike_ratio` < `2.5191` → IC=+0.256 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5191 (IC base=-0.088)

- **PATRÓN** `volumen_spike_ratio` > `1.8262` → IC=+0.276 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8262 (IC base=-0.088)

- **PATRÓN** `dist_vwap_pct` > `0.6876` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6876 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.2345` → IC=+0.231 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2345 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.285 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.1062` → IC=+0.247 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1062 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.224` → IC=+0.246 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.224 (IC base=-0.031)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.225 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=-0.031)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.168 (n=2302)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0091 (IC base=+0.084)

- **PATRÓN** `ibs_20min` > `0.4563` → IC=+0.171 (n=6164)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.4563 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.694` → IC=+0.273 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.694 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.492` → IC=+0.137 (n=3274)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.492 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `0.6742` → IC=+0.226 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6742 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.2492` → IC=+0.250 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2492 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `1.4809` → IC=+0.234 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4809 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `2.8039` → IC=+0.230 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8039 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.275 (n=3152)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 104.0 (IC base=+0.084)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.136 (n=2376)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0084 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.5625` → IC=+0.146 (n=6272)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5625 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.6504` → IC=+0.243 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6504 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` > `1.1948` → IC=+0.255 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1948 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.2505` → IC=+0.323 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2505 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.6177` → IC=+0.251 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6177 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` > `2.3783` → IC=+0.257 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3783 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.255 (n=2236)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.065)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.35` → IC=-0.123 (n=616)

  - _Acción_: SKIP cuando `ibs_20min` < 0.35
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=1252)

- **FILTRO** `sigma_ewma_delta_pct` > `4.322` → IC=-0.157 (n=362)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.322
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1192)

- **PATRÓN** `ibs_20min` > `0.8553` → IC=+0.253 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8553 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.0` → IC=+0.161 (n=491)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 5.0 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2195` → IC=+0.294 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2195 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.8686` → IC=+0.198 (n=306)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.8686 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` > `2.6757` → IC=+0.190 (n=153)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6757 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.220 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1791` → IC=+0.470 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1791 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4617` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4617 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.3568` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3568 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8349` → IC=-0.150 (n=529)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8349
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=1590)

- **PATRÓN** `dist_vwap_pct` > `0.1102` → IC=+0.124 (n=312)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1102 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `0.6566` → IC=+0.124 (n=530)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6566 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.4206` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4206 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.179 (n=191)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 236.0 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.1336` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1336 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.763` → IC=+0.225 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.763 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1523` → IC=+0.216 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1523 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `515.0` → IC=+0.210 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 515.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.267 (n=985)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0951` → IC=+0.243 (n=368)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0951 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.252 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.569` → IC=+0.280 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.569 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1115` → IC=+0.256 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1115 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `2.359` → IC=+0.237 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.359 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.6881` → IC=+0.241 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6881 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.296 (n=872)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.315 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` < `0.3357` → IC=+0.286 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3357 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.885` → IC=+0.303 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.885 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.612` → IC=+0.279 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.612 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.3458` → IC=+0.312 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3458 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` < `3.3816` → IC=+0.273 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.3816 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `2.2342` → IC=+0.285 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2342 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `1878.6984` → IC=+0.299 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1878.6984 (IC base=+0.279)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.275 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.279)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2234` → IC=-0.210 (n=302)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2234
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=908)

- **FILTRO** `ibs_20min` > `0.8296` → IC=-0.179 (n=412)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8296
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1238)

- **PATRÓN** `ibs_20min` > `0.7998` → IC=+0.130 (n=412)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.7998 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.4514` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4514 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.9313` → IC=+0.198 (n=213)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.9313 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `0.6044` → IC=+0.171 (n=217)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.6044 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2693` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2693 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.2948` → IC=+0.224 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2948 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.225 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1026` → IC=+0.157 (n=68)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1026 (IC base=-0.029)

- **PATRÓN** `volumen_regimen` < `1.0874` → IC=+0.153 (n=165)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0874 (IC base=-0.029)

- **PATRÓN** `volumen_regimen` > `0.6828` → IC=+0.141 (n=165)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6828 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1922` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1922 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.7071` → IC=+0.229 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7071 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.5015` → IC=+0.226 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5015 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.222 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6634` → IC=-0.195 (n=753)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6634
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=753)

- **FILTRO** `ibs_20min` > `0.7241` → IC=-0.234 (n=401)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7241
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1205)

- **FILTRO** `sigma_ewma_delta_pct` > `4.748` → IC=-0.161 (n=387)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.748
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1219)

- **PATRÓN** `ibs_20min` > `0.6634` → IC=+0.244 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6634 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1794` → IC=+0.308 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1794 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.8618` → IC=+0.277 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8618 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `1.1627` → IC=+0.276 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1627 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.267 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4442` → IC=+0.316 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4442 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.309 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.2063` → IC=+0.167 (n=530)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.2063 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` > `0.5114` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.5114 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` < `0.1563` → IC=+0.184 (n=264)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1563 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.0893` → IC=+0.201 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0893 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.1007` → IC=+0.188 (n=254)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1007 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2193` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2193 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.629` → IC=+0.200 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.629 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.526` → IC=+0.184 (n=264)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.526 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.214 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0145` → IC=+0.319 (n=646)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0145 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.276 (n=458)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` > `0.8982` → IC=+0.329 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8982 (IC base=+0.260)

- **PATRÓN** `dist_vwap_pct` > `0.1796` → IC=+0.307 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1796 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.339` → IC=+0.287 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.339 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.737` → IC=+0.260 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.737 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `0.85` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.85 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` < `0.1112` → IC=+0.264 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1112 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.296 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.552` → IC=+0.273 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.552 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.266 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `2426.1788` → IC=+0.264 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2426.1788 (IC base=+0.260)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.276 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.291 (n=701)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.3913` → IC=+0.302 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3913 (IC base=+0.268)

- **PATRÓN** `dist_vwap_pct` > `0.5126` → IC=+0.291 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5126 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.385` → IC=+0.282 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.385 (IC base=+0.268)

- **PATRÓN** `volumen_regimen` > `1.2419` → IC=+0.313 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2419 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2407` → IC=+0.347 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2407 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `2.5474` → IC=+0.264 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5474 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.17` → IC=+0.267 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.17 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.268 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `2554.1268` → IC=+0.278 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2554.1268 (IC base=+0.268)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.179 (n=1856)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0047 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.201 (n=1844)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3326` → IC=+0.174 (n=4867)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3326 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=5775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.6949` → IC=+0.229 (n=4940)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6949 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1595` → IC=+0.196 (n=2418)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1595 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.217` → IC=+0.250 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.217 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.2196` → IC=+0.162 (n=3699)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2196 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6224` → IC=+0.159 (n=3700)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6224 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1069` → IC=+0.188 (n=2160)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1069 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `2.313` → IC=+0.169 (n=4606)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.313 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `3825.7125` → IC=+0.174 (n=1844)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3825.7125 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.185 (n=4448)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 127.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.187 (n=3550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0063 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.204 (n=1778)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=2583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.4545` → IC=+0.225 (n=5320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4545 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.734` → IC=+0.189 (n=2208)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.734 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.1842` → IC=+0.156 (n=3898)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1842 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6252` → IC=+0.152 (n=3897)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6252 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.291` → IC=+0.228 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.291 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.8769` → IC=+0.169 (n=3117)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.8769 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6358` → IC=+0.175 (n=1558)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6358 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `131.0` → IC=+0.170 (n=4287)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 131.0 (IC base=+0.170)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.224 (n=310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.204 (n=421)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3182` → IC=+0.209 (n=926)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3182 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=408)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.044` → IC=+0.311 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.044 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2282` → IC=+0.236 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2282 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.2511` → IC=+0.179 (n=734)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.2511 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `1.4401` → IC=+0.182 (n=834)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4401 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.206 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.245 (n=582)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.252 (n=591)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.297 (n=441)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.244 (n=662)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.109` → IC=+0.268 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.109 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.936` → IC=+0.250 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.936 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0697` → IC=+0.234 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0697 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.260 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8745` → IC=+0.252 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8745 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.234 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1577.6848` → IC=+0.254 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1577.6848 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.237 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.247 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.3628` → IC=+0.175 (n=799)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3628 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4506` → IC=+0.221 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4506 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.2079` → IC=+0.213 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2079 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.697` → IC=+0.237 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.697 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.2773` → IC=+0.177 (n=799)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.2773 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.191 (n=173)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.205 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `11247.6748` → IC=+0.190 (n=713)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 11247.6748 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `412.0` → IC=+0.163 (n=633)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 412.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.180 (n=800)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0049 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.2865` → IC=+0.170 (n=909)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.2865 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.168 (n=835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5111` → IC=+0.194 (n=909)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5111 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.118` → IC=+0.220 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.118 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.167 (n=909)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2025 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.199 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.163 (n=800)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.4122` → IC=+0.155 (n=801)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4122 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `237.0` → IC=+0.163 (n=238)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 237.0 (IC base=+0.151)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.198 (n=906)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0058 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1945` → IC=+0.197 (n=605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1945 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.219 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=426)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.541` → IC=+0.271 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.541 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.1074` → IC=+0.185 (n=737)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1074 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.1357` → IC=+0.184 (n=352)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1357 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `3.6503` → IC=+0.200 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6503 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.204 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.204 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.233 (n=762)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.219)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.224 (n=346)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.242 (n=254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.265 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.3548` → IC=+0.249 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3548 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.677` → IC=+0.269 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.677 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.272 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.2531` → IC=+0.229 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2531 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1887.358` → IC=+0.234 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.358 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.200 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.219)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.207 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.4222` → IC=+0.170 (n=865)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.4222 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.4164` → IC=+0.207 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4164 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1317` → IC=+0.189 (n=574)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1317 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.299` → IC=+0.252 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.299 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.8664` → IC=+0.167 (n=577)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8664 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.2029` → IC=+0.184 (n=289)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.2029 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.241 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.175 (n=281)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4142 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.5331` → IC=+0.185 (n=281)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.5331 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `7552.1408` → IC=+0.196 (n=577)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 7552.1408 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.168 (n=705)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 158.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.159 (n=819)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.006 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3707` → IC=+0.147 (n=930)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3707 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.185 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.5951` → IC=+0.177 (n=930)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5951 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1459` → IC=+0.139 (n=929)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1459 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.147` → IC=+0.196 (n=182)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 12.147 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8624` → IC=+0.140 (n=620)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8624 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.6141` → IC=+0.133 (n=930)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.6141 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.168 (n=368)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.7855` → IC=+0.133 (n=545)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.7855 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `9883.3938` → IC=+0.151 (n=422)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 9883.3938 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.147 (n=698)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0077 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=1075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5111` → IC=+0.196 (n=1044)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5111 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0126` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0126 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.371` → IC=+0.256 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.371 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2243` → IC=+0.121 (n=1046)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2243 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.7951` → IC=+0.124 (n=669)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7951 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1061)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2908.3422` → IC=+0.200 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2908.3422 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.137 (n=747)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 49.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.154 (n=339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0052 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.5273` → IC=+0.204 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5273 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.33` → IC=+0.154 (n=212)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 7.33 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.041` → IC=+0.127 (n=889)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.041 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2729` → IC=+0.180 (n=120)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2729 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.5679` → IC=+0.123 (n=383)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.5679 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.144` → IC=+0.142 (n=395)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.144 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `3090.3968` → IC=+0.155 (n=337)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3090.3968 (IC base=+0.115)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.209 (n=661)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.1645` → IC=+0.213 (n=437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1645 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=1030)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.250 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.72 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `1.2054` → IC=+0.239 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2054 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.289` → IC=+0.234 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.289 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `1.2034` → IC=+0.200 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2034 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` > `0.8476` → IC=+0.215 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8476 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.169` → IC=+0.254 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.169 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `2.2071` → IC=+0.214 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2071 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.4272` → IC=+0.203 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4272 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.199 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.239 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.205 (n=476)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.022 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.220 (n=352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.211 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.210 (n=488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.431` → IC=+0.235 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.431 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `1.1088` → IC=+0.208 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1088 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.699` → IC=+0.224 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.699 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.213 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6258 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.286 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2458` → IC=+0.195 (n=807)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2458 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4604` → IC=+0.187 (n=917)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4604 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2515.4602` → IC=+0.209 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2515.4602 (IC base=+0.200)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.146 (n=430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0038 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.153 (n=583)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0071 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0939` → IC=+0.152 (n=429)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0939 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.4087` → IC=+0.169 (n=1285)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.4087 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.7813` → IC=+0.190 (n=172)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.7813 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.713` → IC=+0.179 (n=581)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 3.713 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8626` → IC=+0.162 (n=732)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8626 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.141 (n=366)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.2084 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1672` → IC=+0.165 (n=353)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1672 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.2547` → IC=+0.143 (n=1078)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.2547 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.8243` → IC=+0.153 (n=816)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.8243 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=1418)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `8101.5764` → IC=+0.177 (n=583)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 8101.5764 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.163 (n=363)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 20.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.140 (n=443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0036 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.3044` → IC=+0.158 (n=884)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.3044 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.824` → IC=+0.127 (n=526)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 3.824 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.144 (n=338)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `2.2271` → IC=+0.124 (n=1108)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.2271 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.136 (n=399)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 20.0 (IC base=+0.102)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.142 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0037 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1032` → IC=+0.164 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1032 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.169 (n=264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 10.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5377` → IC=+0.154 (n=255)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.5377 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.2999` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2999 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.328` → IC=+0.191 (n=134)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.328 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.5894` → IC=+0.204 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5894 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `1.5129` → IC=+0.130 (n=244)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.5129 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `9633.8027` → IC=+0.159 (n=285)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9633.8027 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 148.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.195 (n=195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.003 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.2718` → IC=+0.136 (n=385)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.2718 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.6123` → IC=+0.167 (n=385)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6123 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.351` → IC=+0.132 (n=180)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 4.351 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` > `1.0596` → IC=+0.150 (n=198)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0596 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.1552` → IC=+0.199 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1552 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `2.4085` → IC=+0.136 (n=427)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.4085 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `260.0` → IC=+0.139 (n=272)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 260.0 (IC base=+0.111)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.254 (n=173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.229 (n=131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.239 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.2763` → IC=+0.249 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2763 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.3645` → IC=+0.246 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3645 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.252 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.6827` → IC=+0.231 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6827 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.1711` → IC=+0.244 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1711 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.3686` → IC=+0.218 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3686 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.0232` → IC=+0.270 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0232 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `12495.4243` → IC=+0.229 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12495.4243 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.129 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0047 (IC base=+0.082)

- **PATRÓN** `drift_60min` |x|≤ `0.0962` → IC=+0.152 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0962 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.3259` → IC=+0.134 (n=219)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.3259 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.985` → IC=+0.133 (n=118)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 3.985 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.128 (n=76)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.207 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.151 (n=124)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.067)

- **PATRÓN** `libro_liquidez` > `2775.0073` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2775.0073 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.4524` → IC=+0.153 (n=246)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.4524 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.8782` → IC=+0.142 (n=149)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.8782 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.128 (n=189)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 45.0 (IC base=+0.071)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0226` → IC=+0.146 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0226 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.174 (n=142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0061 (IC base=+0.134)

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

- **PATRÓN** `volumen_pendiente_norm` < `0.2672` → IC=+0.159 (n=136)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.2672 (IC base=+0.134)

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

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.129 (n=149)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.6 (IC base=+0.125)

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
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.191 (n=3150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0086 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=7249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.475` → IC=+0.212 (n=6940)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.475 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.8871` → IC=+0.199 (n=920)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.8871 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.576` → IC=+0.221 (n=3408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.576 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8832` → IC=+0.164 (n=3134)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8832 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1701` → IC=+0.183 (n=1909)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1701 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.6497` → IC=+0.177 (n=2195)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6497 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.170 (n=8240)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.04 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3787.3248` → IC=+0.173 (n=2313)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3787.3248 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.192 (n=4904)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 98.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.197 (n=4238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0067 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.4735` → IC=+0.185 (n=6354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4735 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=2432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=2949)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.237 (n=6354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5588 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.763` → IC=+0.200 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.763 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.688` → IC=+0.182 (n=6134)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.688 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.0558` → IC=+0.157 (n=3862)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0558 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `1.1975` → IC=+0.158 (n=1464)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1975 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2363` → IC=+0.245 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2363 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.2962` → IC=+0.189 (n=2552)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.2962 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.178 (n=5230)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 130.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.224 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.231 (n=526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.322` → IC=+0.197 (n=1158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.322 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.214 (n=781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.79` → IC=+0.327 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.79 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.0945` → IC=+0.224 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0945 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `1.559` → IC=+0.200 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.559 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.5831` → IC=+0.191 (n=357)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5831 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.225 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.232 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.267 (n=804)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.272 (n=817)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.2035` → IC=+0.288 (n=608)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2035 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.0669` → IC=+0.309 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0669 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.621` → IC=+0.270 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.621 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2279` → IC=+0.318 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2279 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `1.9123` → IC=+0.280 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9123 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1576.58` → IC=+0.270 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1576.58 (IC base=+0.260)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.260 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.190 (n=366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0027 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1824` → IC=+0.155 (n=732)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1824 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.695` → IC=+0.242 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.695 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.3348` → IC=+0.198 (n=422)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3348 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.887` → IC=+0.168 (n=257)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.887 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.367` → IC=+0.154 (n=973)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.367 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.187 (n=483)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6973 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.181 (n=305)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.162 (n=1044)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7709` → IC=+0.161 (n=696)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7709 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `10653.1142` → IC=+0.171 (n=980)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 10653.1142 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `499.0` → IC=+0.166 (n=973)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 499.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.195 (n=326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0024 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.3244` → IC=+0.172 (n=978)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3244 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.172 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.6433` → IC=+0.206 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6433 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.3` → IC=+0.178 (n=486)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 3.3 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.168 (n=978)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1856 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1498` → IC=+0.227 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1498 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.4046` → IC=+0.173 (n=881)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.4046 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `289.0` → IC=+0.173 (n=261)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 289.0 (IC base=+0.158)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.225 (n=1085)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=1137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.217 (n=968)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.6717` → IC=+0.249 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6717 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.805` → IC=+0.294 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.805 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.2192` → IC=+0.220 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2192 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.6898` → IC=+0.219 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6898 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.236 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.238 (n=353)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.230 (n=944)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1455` → IC=+0.228 (n=464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1455 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.237 (n=389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` < `0.3839` → IC=+0.266 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3839 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.693` → IC=+0.274 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.693 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.3614` → IC=+0.287 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3614 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.9676` → IC=+0.216 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9676 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.256` → IC=+0.227 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.256 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `1892.3107` → IC=+0.229 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1892.3107 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.219 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.227)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.171 (n=515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0038 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0928` → IC=+0.140 (n=390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0928 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=1222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.238 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7143 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.3355` → IC=+0.179 (n=450)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3355 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.356` → IC=+0.172 (n=510)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.356 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8826` → IC=+0.160 (n=780)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8826 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.2022` → IC=+0.140 (n=390)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.2022 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.237 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7499` → IC=+0.160 (n=747)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7499 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=1270)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `9026.9243` → IC=+0.237 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9026.9243 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.146 (n=920)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 169.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.190 (n=314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0031 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.4225` → IC=+0.150 (n=937)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4225 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6933` → IC=+0.183 (n=938)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6933 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1942` → IC=+0.137 (n=866)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1942 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.13` → IC=+0.190 (n=140)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.13 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8529` → IC=+0.140 (n=625)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8529 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.1684` → IC=+0.144 (n=313)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1684 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.250 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.5565` → IC=+0.140 (n=384)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5565 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `2.1232` → IC=+0.163 (n=395)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.1232 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `11093.2268` → IC=+0.176 (n=313)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 11093.2268 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `199.0` → IC=+0.134 (n=863)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 199.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.175 (n=1212)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.4615 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `1.0011` → IC=+0.171 (n=214)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 1.0011 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.403` → IC=+0.214 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.403 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=833)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2933.8625` → IC=+0.249 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2933.8625 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.179 (n=378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0054 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1197` → IC=+0.150 (n=378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1197 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.156 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.619` → IC=+0.209 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.619 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.189` → IC=+0.138 (n=924)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.189 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.344` → IC=+0.128 (n=1087)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.344 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.152 (n=498)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.7144 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2176` → IC=+0.178 (n=175)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2176 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4671` → IC=+0.152 (n=326)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4671 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.2089` → IC=+0.135 (n=442)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.2089 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2953.4428` → IC=+0.160 (n=377)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2953.4428 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.027` → IC=+0.217 (n=408)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.027 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=1089)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.237 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.1738` → IC=+0.235 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1738 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.534` → IC=+0.236 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.534 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2386` → IC=+0.205 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2386 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.205 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6199 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.230 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.6094` → IC=+0.227 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6094 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.209 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2556.6049` → IC=+0.207 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2556.6049 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.249 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0252` → IC=+0.222 (n=448)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0252 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.203 (n=1423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.250 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.4733` → IC=+0.205 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4733 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1792` → IC=+0.202 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1792 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.518` → IC=+0.264 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.518 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `0.6325` → IC=+0.212 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6325 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.256 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.2324` → IC=+0.191 (n=1027)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.2324 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.196 (n=1167)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2531.5711` → IC=+0.203 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2531.5711 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.182 (n=1072)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 37.0 (IC base=+0.199)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=2335)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.148 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0051 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4177` → IC=+0.140 (n=1878)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4177 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.155 (n=745)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.139 (n=720)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 4.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.9291` → IC=+0.200 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9291 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1845` → IC=+0.126 (n=723)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.1845 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.187` → IC=+0.146 (n=343)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.187 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `0.8969` → IC=+0.129 (n=920)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.8969 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.1732` → IC=+0.155 (n=592)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1732 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.4515` → IC=+0.153 (n=704)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4515 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.8862` → IC=+0.144 (n=1407)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8862 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `8804.4184` → IC=+0.149 (n=967)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8804.4184 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.194 (n=590)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.477` → IC=+0.162 (n=1763)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.477 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1851` → IC=+0.155 (n=776)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1851 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.153 (n=289)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.265` → IC=+0.147 (n=1742)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.265 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.9009` → IC=+0.154 (n=1115)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.9009 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.153 (n=828)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.5699` → IC=+0.144 (n=1745)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.5699 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8156` → IC=+0.150 (n=1163)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8156 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=2335)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `12047.0566` → IC=+0.158 (n=799)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12047.0566 (IC base=+0.139)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `4.986` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.986
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=342)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.163 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.158 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0035 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0932` → IC=+0.196 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0932 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.174 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 19.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.5162` → IC=+0.198 (n=180)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5162 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.2289` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.2289 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.986` → IC=+0.160 (n=342)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 4.986 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1969` → IC=+0.151 (n=270)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1969 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.8077` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8077 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.1087` → IC=+0.149 (n=300)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.1087 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2272` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2272 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.206 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.6405` → IC=+0.174 (n=90)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6405 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `12645.8095` → IC=+0.196 (n=241)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 12645.8095 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.200 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.170 (n=274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.168 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 5.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.157` → IC=+0.158 (n=361)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.157 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.142 (n=372)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6091 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.6094` → IC=+0.176 (n=106)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.6094 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.273` → IC=+0.156 (n=801)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.273 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8795` → IC=+0.178 (n=547)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8795 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0691` → IC=+0.156 (n=385)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0691 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.5652` → IC=+0.140 (n=817)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5652 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.804` → IC=+0.145 (n=545)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.804 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `12050.2084` → IC=+0.148 (n=733)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 12050.2084 (IC base=+0.133)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.191 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0104 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.294` → IC=+0.162 (n=297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.294 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.9885` → IC=+0.227 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9885 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.285` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.285 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.0958` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0958 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `3.4677` → IC=+0.170 (n=443)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 3.4677 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.8314` → IC=+0.158 (n=396)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.8314 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

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

- **PATRÓN** `libro_liquidez` > `2463.7708` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2463.7708 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.145 (n=694)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0088 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.139 (n=693)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0045 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4977` → IC=+0.144 (n=694)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4977 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.164 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.140 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 4.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.7971` → IC=+0.159 (n=315)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.7971 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.9872` → IC=+0.182 (n=152)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.9872 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4203` → IC=+0.144 (n=650)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4203 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.807` → IC=+0.145 (n=692)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.807 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1119` → IC=+0.144 (n=610)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1119 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.6457` → IC=+0.136 (n=693)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6457 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1754` → IC=+0.156 (n=210)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1754 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.161 (n=228)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=640)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8862.571` → IC=+0.154 (n=620)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8862.571 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.173 (n=488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0071 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.5081` → IC=+0.194 (n=553)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.5081 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.171 (n=378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.103` → IC=+0.169 (n=553)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.103 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.168 (n=254)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.3657` → IC=+0.160 (n=563)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.3657 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.089` → IC=+0.168 (n=263)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.089 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6473` → IC=+0.184 (n=185)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6473 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.7334` → IC=+0.159 (n=494)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.7334 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.184 (n=242)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.183` → IC=+0.169 (n=478)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.183 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.170 (n=543)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `8201.961` → IC=+0.169 (n=553)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 8201.961 (IC base=+0.155)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=129)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` > `0.6396` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6396 (IC base=+0.026)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0084` → IC=-0.247 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=257)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=261)

- **FILTRO** `dist_vwap_pct` > `0.1579` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1579
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=183)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.180 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.162 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.201 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6429 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.148 (n=251)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.218` → IC=+0.208 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.218 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.231 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `2.5266` → IC=+0.141 (n=382)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5266 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=390)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2445.5482` → IC=+0.160 (n=210)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2445.5482 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.0875` → IC=+0.281 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0875 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.1579` → IC=+0.127 (n=183)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1579 (IC base=-0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.902` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 3.902 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.7298` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.7298 (IC base=-0.038)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=-0.038)

- **PATRÓN** `libro_liquidez` > `2874.2912` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2874.2912 (IC base=-0.038)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.204 (n=174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.5857` → IC=+0.198 (n=167)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5857 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.739` → IC=+0.124 (n=107)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 3.739 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.0527` → IC=+0.124 (n=147)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.0527 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.0779` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0779 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `2.0198` → IC=+0.181 (n=114)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.0198 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2848.0904` → IC=+0.132 (n=153)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2848.0904 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.037` → IC=+0.273 (n=20)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.037 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.4723` → IC=+0.219 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4723 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.914` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 5.914 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.9643` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.9643 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `3.0527` → IC=+0.260 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0527 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `1.3279` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.3279 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `2556.9997` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2556.9997 (IC base=+0.035)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6404` → IC=-0.161 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6404
  - _Potencial_: sin este filtro IC_bueno=+0.223 (n=171)

- **FILTRO** `sigma_h` > `0.0066` → IC=-0.321 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=79)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=70)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.157 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0048 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.130 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.6404` → IC=+0.223 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6404 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1209` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1209 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.147` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.147 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.7859` → IC=+0.141 (n=115)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.7859 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `0.6191` → IC=+0.132 (n=153)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6191 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.7387` → IC=+0.155 (n=82)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.7387 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.4015` → IC=+0.140 (n=123)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4015 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=178)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `1343.31` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1343.31 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.1021` → IC=+0.210 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1021 (IC base=-0.061)

- **PATRÓN** `ibs_20min` < `0.1926` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1926 (IC base=-0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.069` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.069 (IC base=-0.061)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.412` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.412 (IC base=-0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.0562` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0562 (IC base=-0.061)

- **PATRÓN** `volumen_spike_ratio` > `1.3921` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.3921 (IC base=-0.061)

- **PATRÓN** `libro_liquidez` > `1059.8551` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1059.8551 (IC base=-0.061)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1429` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1429
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=36)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.167 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0059 (IC base=+0.069)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.127 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 14.0 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.191 (n=150)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.6757 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.8439` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.8439 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.59` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.59 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.0854` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.0854 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.5681` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.5681 (IC base=+0.069)

- **PATRÓN** `libro_liquidez` > `385.351` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 385.351 (IC base=+0.069)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1621` → IC=-0.389 (n=34)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1621
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=105)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.419 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `dist_vwap_pct` > `0.2306` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2306
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=125)

- **FILTRO** `volumen_pendiente_norm` > `0.1113` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1113
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=48)

- **FILTRO** `dist_vwap_pct` > `0.3468` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3468
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=111)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=37)

- **FILTRO** `volumen_spike_ratio` > `1.5066` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5066
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=28)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.6316` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.6316
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `sigma_h` < `0.0018` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=37)

- **FILTRO** `ibs_20min` > `0.4197` → IC=-0.289 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4197
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.357 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=25)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `volumen_regimen` < `1.0152` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0152
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `sigma_h` > `0.0073` → IC=-0.350 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=20)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.450 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.251` → IC=-0.129 (n=87)

  - _Acción_: SKIP cuando `ibs_20min` > 0.251
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=171)

- **PATRÓN** `ibs_20min` > `0.6438` → IC=+0.153 (n=191)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6438 (IC base=+0.059)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.149 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.251` → IC=+0.142 (n=171)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.251 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.866` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 5.866 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.0649` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.0649 (IC base=+0.050)

- **PATRÓN** `libro_liquidez` > `3703.4476` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3703.4476 (IC base=+0.050)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

- **FILTRO** `volumen_regimen` < `0.7102` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7102
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.149 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0028 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1622 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.217` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 14.217 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.1293` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1293 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `3.3907` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 3.3907 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `1.5879` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5879 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `3644.5187` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3644.5187 (IC base=+0.116)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=52)

- **FILTRO** `ibs_20min` < `0.6645` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6645
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=51)

- **FILTRO** `ibs_20min` > `0.3636` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3636
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=64)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.167 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0046 (IC base=+0.071)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.160 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.071)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.8265` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.8265 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.0901` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.0901 (IC base=+0.071)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `1624.9844` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1624.9844 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.023)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.5556` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5556
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=49)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=43)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3593` → IC=+0.139 (n=81)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3593 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.125 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.7692` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7692 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.5856` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.5856 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.1848` → IC=+0.148 (n=69)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1848 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.04 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `507.9911` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 507.9911 (IC base=+0.124)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.122 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2812.796` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2812.796 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2298.3744` → IC=+0.125 (n=462)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2298.3744 (IC base=+0.092)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.122 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2812.796` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2812.796 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2298.3744` → IC=+0.125 (n=462)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2298.3744 (IC base=+0.092)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `11.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=71)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=116)

- **FILTRO** `libro_liquidez` < `2359.8786` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `libro_liquidez` < 2359.8786
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=99)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=179)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.124 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=101)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=165)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `libro_liquidez` < `12409.8631` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 12409.8631
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `libro_liquidez` < `14445.5423` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 14445.5423
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1250)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=49)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=81)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=60)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `31327.3` → IC=-0.136 (n=42)

  - _Acción_: SKIP cuando `liq_usd_total` < 31327.3
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **PATRÓN** `liq_usd_total` > `54982.77` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `liq_usd_total` > 54982.77 (IC base=+0.019)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=73)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=507)

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
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=418)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.425` → IC=-0.140 (n=145)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=453)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=212)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=212)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=184)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=150)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=150)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=90)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.151 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=124)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=147)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=207)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=207)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=70)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=5694)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=976)

- **FILTRO** `libro_liquidez` < `15924.9923` → IC=-0.159 (n=247)

  - _Acción_: SKIP cuando `libro_liquidez` < 15924.9923
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=744)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1103)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.175 (n=2364)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=7097)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.166 (n=2448)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=7383)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.210 (n=381)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=1186)

- **FILTRO** `ibs_20min` < `0.748` → IC=-0.173 (n=390)

  - _Acción_: SKIP cuando `ibs_20min` < 0.748
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1177)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.200 (n=398)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=1241)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.218 (n=410)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=1306)

- **FILTRO** `ibs_20min` > `0.2875` → IC=-0.179 (n=428)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2875
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=1288)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.194 (n=380)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=1159)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.185 (n=427)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=1303)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2021)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1915)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=1921)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=200)

- **FILTRO** `ibs_20min` > `0.1507` → IC=-0.125 (n=94)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1507
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=189)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=175)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.318 (n=53)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=122)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=536)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `py_entrada` < `0.35` → IC=-0.273 (n=5536)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=17007)

- **FILTRO** `ibs_7min` < `0.7124` → IC=-0.231 (n=5635)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7124
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=16908)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.162 (n=7606)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=14937)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.220 (n=6942)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=21115)

- **FILTRO** `ibs_7min` > `0.2973` → IC=-0.174 (n=7012)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2973
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=21045)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=828)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2705)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.258 (n=1165)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=2368)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.203 (n=852)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=2681)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.146 (n=3292)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=1593)

- **FILTRO** `drift_7min_pct` |x|> `0.1089` → IC=-0.124 (n=1658)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1089
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=3227)

- **FILTRO** `ibs_7min` > `0.8` → IC=-0.203 (n=1219)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=3666)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.147 (n=917)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=3059)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.254 (n=988)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=2988)

- **FILTRO** `ibs_7min` < `0.7638` → IC=-0.183 (n=994)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7638
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=2982)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.171 (n=991)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=2985)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.259 (n=918)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3075)

- **FILTRO** `ibs_7min` > `0.25` → IC=-0.169 (n=998)

  - _Acción_: SKIP cuando `ibs_7min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2995)

- **FILTRO** `ballena_activa_n` > `113.0` → IC=-0.162 (n=1350)

  - _Acción_: SKIP cuando `ballena_activa_n` > 113.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=2643)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.180 (n=823)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=2513)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.320 (n=782)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=2554)

- **FILTRO** `ibs_7min` < `0.2091` → IC=-0.269 (n=834)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2091
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=2502)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.215 (n=773)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=2563)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.230 (n=1185)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=3932)

- **FILTRO** `ibs_7min` > `0.2667` → IC=-0.152 (n=1736)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=3381)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=1181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=2539)

- **FILTRO** `ibs_7min` < `0.7511` → IC=-0.187 (n=930)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7511
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=2790)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.184 (n=921)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=2799)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=920)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=2845)

- **FILTRO** `ibs_7min` > `0.2744` → IC=-0.174 (n=940)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2744
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2825)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.176 (n=937)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2828)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.232 (n=1037)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3135)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.201 (n=1040)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=3132)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.169 (n=1268)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=4034)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.280 (n=896)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2910)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.222 (n=949)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=2857)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.209 (n=880)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2926)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.194 (n=1193)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=3802)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=918)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=475)

- **FILTRO** `libro_liquidez` < `10498.4421` → IC=-0.157 (n=129)

  - _Acción_: SKIP cuando `libro_liquidez` < 10498.4421
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=389)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=514)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3984` → IC=+0.137 (n=650)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3984 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.131 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `314679.3` → IC=+0.136 (n=627)

  - _Acción_: Kelly boost +0.68€ cuando `total_vol_5m` < 314679.3 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.123 (n=308)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3597.1493` → IC=+0.144 (n=262)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3597.1493 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.205 (n=76)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.110)

- **PATRÓN** `total_vol_5m` < `495.741` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `total_vol_5m` < 495.741 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `9761.0798` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 9761.0798 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.110)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3997` → IC=+0.214 (n=103)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.3997 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.169)

- **PATRÓN** `total_vol_5m` < `7212.57` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `total_vol_5m` < 7212.57 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3606.826` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3606.826 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.187 (n=81)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 69.0 (IC base=+0.169)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.160 (n=104)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.129 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 13.0 (IC base=+0.109)

- **PATRÓN** `total_vol_5m` < `353208.2` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `total_vol_5m` < 353208.2 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.243 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 37.0 (IC base=+0.109)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.275` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.275
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=68)

- **FILTRO** `T_h` > `50.8821` → IC=-0.265 (n=168)

  - _Acción_: SKIP cuando `T_h` > 50.8821
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=84)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.207 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=-0.120)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.281 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=32)

- **FILTRO** `T_h` > `56.3892` → IC=-0.402 (n=39)

  - _Acción_: SKIP cuando `T_h` > 56.3892
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=40)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.094)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0087` → IC=-0.152 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0087
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `T_h` < `291.9853` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `T_h` < 291.9853
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `87.9936` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `T_h` < 87.9936
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=24)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.7615` → IC=-0.244 (n=88)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7615
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=171)

- **FILTRO** `T_h` > `144.6658` → IC=-0.363 (n=71)

  - _Acción_: SKIP cuando `T_h` > 144.6658
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=142)

- **FILTRO** `pct_vs_K` |x|> `4.555` → IC=-0.446 (n=53)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.555
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=160)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0036` → IC=-0.269 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=73)

- **FILTRO** `T_h` > `63.9918` → IC=-0.176 (n=72)

  - _Acción_: SKIP cuando `T_h` > 63.9918
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `T_h` > `144.5878` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `T_h` > 144.5878
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=51)

- **FILTRO** `pct_vs_K` |x|> `2.3742` → IC=-0.423 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3742
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=39)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.986` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 135.986
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=53)

- **FILTRO** `pct_vs_K` |x|> `4.5225` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.5225
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.385 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=50)

- **FILTRO** `T_h` > `71.0631` → IC=-0.325 (n=55)

  - _Acción_: SKIP cuando `T_h` > 71.0631
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `T_h` > `63.6677` → IC=-0.136 (n=42)

  - _Acción_: SKIP cuando `T_h` > 63.6677
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `sigma_h` > `0.0063` → IC=-0.357 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=10)

- **FILTRO** `T_h` > `95.1632` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### RESOLUTION_SNIPER
- **PATRÓN** `dist_50` > `0.4444` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.343)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.447 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.343)

- **PATRÓN** `edge` > `0.1072` → IC=+0.441 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.404)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.478 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.404)

- **PATRÓN** `T_h` > `0.7616` → IC=+0.441 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7616 (IC base=+0.404)

- **PATRÓN** `dist_50` > `0.3885` → IC=+0.485 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3885 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.440 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.404)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.2065` → IC=+0.470 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2065 (IC base=+0.487)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.477 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.487)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.477 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.487)

- **PATRÓN** `T_h` > `0.9332` → IC=+0.479 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9332 (IC base=+0.487)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.477 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.487)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.478 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.487)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=111)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=207)

- **FILTRO** `streak_estiramiento` > `0.7313` → IC=-0.138 (n=56)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.7313
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=110)

- **PATRÓN** `streak_estiramiento` < `0.4382` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.4382 (IC base=+0.023)

- **PATRÓN** `streak_estiramiento` < `0.4095` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4095 (IC base=+0.030)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `991078.0` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `volumen_racha` > 991078.0
  - _Potencial_: sin este filtro IC_bueno=+0.180 (n=23)

- **FILTRO** `libro_liquidez` < `2208.5143` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 2208.5143
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=69)

- **PATRÓN** `volumen_racha` < `991078.0` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_racha` < 991078.0 (IC base=-0.011)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=81)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=83)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=432)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=438)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=283)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=408)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=815)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=467)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=518)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2147)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1128)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1136)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.190 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.177 (n=323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0087 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.175 (n=327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.167)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0589` → IC=+0.172 (n=969)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.0589 (IC base=+0.167)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3447` → IC=+0.208 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3447 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.167 (n=1011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 4.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.189 (n=467)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.167)

- **PATRÓN** `ibs_15` > `0.6176` → IC=+0.239 (n=969)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6176 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.102` → IC=+0.172 (n=638)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.102 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.699` → IC=+0.242 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.699 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=860)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2975.1342` → IC=+0.179 (n=646)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2975.1342 (IC base=+0.167)

### UPDOWN_GBM#60min
- **FILTRO** `sigma_ewma_delta_pct` > `27.178` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 27.178
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=272)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=271)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.5868` → IC=-0.127 (n=124)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.5868
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=243)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.215 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0023` → IC=+0.195 (n=244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0023 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.0624` → IC=+0.250 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0624 (IC base=+0.194)

- **PATRÓN** `drift_15min` |x|≤ `0.374` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.374 (IC base=+0.194)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2384` → IC=+0.202 (n=82)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2384 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3853` → IC=+0.227 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3853 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.211 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.8791` → IC=+0.294 (n=163)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8791 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.099` → IC=+0.207 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.099 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.624` → IC=+0.257 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.624 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `13595.2872` → IC=+0.252 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13595.2872 (IC base=+0.194)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.698` → IC=-0.124 (n=99)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.698
  - _Potencial_: sin este filtro IC_bueno=+0.266 (n=203)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.155 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0061 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.148 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0055 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.167 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.138)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.167 (n=151)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.138)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2712` → IC=+0.171 (n=138)

  - _Acción_: Kelly boost +0.86€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2712 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.153 (n=237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_15` > `0.698` → IC=+0.266 (n=203)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.698 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.3919` → IC=+0.157 (n=240)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.3919 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.024` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.024 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=267)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.148 (n=103)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.138)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.1832` → IC=-0.190 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1832
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=29)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.167 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0047 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.172 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0076 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.1368` → IC=+0.172 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1368 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0657` → IC=+0.161 (n=122)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.0657 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3249` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3249 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.246 (n=136)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.2071` → IC=+0.159 (n=136)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2071 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.367` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.367 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `3092.4545` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3092.4545 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.139)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5798` → IC=-0.143 (n=113)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5798
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=483)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `8.191` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 8.191
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0222` → IC=+0.223 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0222 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.087` → IC=+0.175 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.087 (IC base=+0.158)

- **PATRÓN** `delta_ratio_macro` |x|> `0.047` → IC=+0.179 (n=275)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.047 (IC base=+0.158)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.217 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_15` > `0.5075` → IC=+0.247 (n=275)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5075 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1137` → IC=+0.175 (n=167)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1137 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.232` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.232 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.092` → IC=+0.159 (n=250)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 7.092 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.158 (n=296)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.03 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `2708.1108` → IC=+0.201 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2708.1108 (IC base=+0.158)

- **PATRÓN** `ibs_15` < `0.103` → IC=+0.170 (n=292)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.103 (IC base=+0.045)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.397 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.1549` → IC=+0.337 (n=250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1549 (IC base=+0.332)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.338 (n=189)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.332)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2203` → IC=+0.369 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2203 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.356 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.332)

- **PATRÓN** `ibs_15` > `0.8365` → IC=+0.391 (n=254)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8365 (IC base=+0.332)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.362 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.332)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `3925.9545` → IC=+0.344 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3925.9545 (IC base=+0.332)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1885` → IC=+0.326 (n=142)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1885 (IC base=+0.329)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.326 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.329)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.357 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1544` → IC=+0.333 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1544 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1017` → IC=+0.336 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1017 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.358 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.329)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.329 (n=168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.365 (n=161)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` > `0.4001` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4001 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.561` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.561 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.296` → IC=+0.343 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.296 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `8997.0825` → IC=+0.353 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8997.0825 (IC base=+0.329)

- **PATRÓN** `ballena_activa_n` < `611.0` → IC=+0.395 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 611.0 (IC base=+0.329)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.379 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.360 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.331)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.348 (n=123)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.331)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.349 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.331)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.348 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.331)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.396 (n=123)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.341 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.734` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.734 (IC base=+0.331)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.331)

- **PATRÓN** `libro_liquidez` > `3566.5529` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3566.5529 (IC base=+0.331)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=+0.331)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.197 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1490)

- **FILTRO** `ibs_15` < `0.5837` → IC=-0.183 (n=165)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5837
  - _Potencial_: sin este filtro IC_bueno=+0.245 (n=496)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=613)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1373)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.219 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=-0.056)

- **PATRÓN** `ibs_15` > `0.5837` → IC=+0.245 (n=496)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5837 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` < `0.2628` → IC=+0.173 (n=389)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2628 (IC base=-0.056)

- **PATRÓN** `delta_ratio_macro` |x|> `0.119` → IC=+0.229 (n=639)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.119 (IC base=-0.051)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.182` → IC=+0.232 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.182 (IC base=-0.051)

- **PATRÓN** `ibs_15` < `0.3542` → IC=+0.270 (n=959)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3542 (IC base=-0.051)

- **PATRÓN** `dist_vwap_pct` > `0.3779` → IC=+0.254 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3779 (IC base=-0.051)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.212 (n=293)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=881)

- **FILTRO** `sigma_h` < `0.0032` → IC=-0.229 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0032
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=881)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.214 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=425)

- **FILTRO** `sigma_ewma_delta_pct` > `20.169` → IC=-0.246 (n=215)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.169
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=959)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.167 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.003 (IC base=+0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2339` → IC=+0.250 (n=34)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2339 (IC base=+0.068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1145` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1145 (IC base=+0.068)

- **PATRÓN** `ibs_15` > `0.7695` → IC=+0.340 (n=92)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7695 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.1418` → IC=+0.260 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1418 (IC base=+0.068)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6395` → IC=-0.244 (n=80)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6395
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=240)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=303)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.154 (n=215)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0039 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.222 (n=106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.130)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0557` → IC=+0.132 (n=240)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0557 (IC base=+0.130)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.231 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.144 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.256 (n=240)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.165 (n=174)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.902` → IC=+0.140 (n=256)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 18.902 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=303)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.212 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.227 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3466` → IC=+0.227 (n=349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3466 (IC base=+0.213)

- **PATRÓN** `drift_15min` |x|≤ `0.4115` → IC=+0.218 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4115 (IC base=+0.213)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1958` → IC=+0.231 (n=180)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1958 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.241 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.213)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.259 (n=397)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.7133` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7133 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.251` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.251 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.936` → IC=+0.221 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.936 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `3672.3796` → IC=+0.214 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3672.3796 (IC base=+0.213)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1644` → IC=-0.208 (n=166)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1644
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=323)

- **FILTRO** `drift_15min` |x|> `0.8298` → IC=-0.242 (n=122)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8298
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=367)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0711` → IC=+0.202 (n=186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0711 (IC base=-0.045)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.194` → IC=+0.184 (n=134)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.194 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.248 (n=208)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` < `0.1449` → IC=+0.196 (n=192)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1449 (IC base=-0.045)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0188` → IC=-0.240 (n=294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0188
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=295)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.237 (n=154)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=435)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.374 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.050)

- **PATRÓN** `ibs_15` < `0.3273` → IC=+0.285 (n=273)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3273 (IC base=-0.050)

- **PATRÓN** `dist_vwap_pct` > `0.4185` → IC=+0.393 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4185 (IC base=-0.050)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.148 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0071 (IC base=+0.086)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.250 (n=18)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.086)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.1423` → IC=+0.125 (n=46)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.62€ cuando `ibs_15` > 0.1423 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1159` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1159 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.086)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.148 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0071 (IC base=+0.086)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.250 (n=18)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.086)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.1423` → IC=+0.125 (n=46)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.62€ cuando `ibs_15` > 0.1423 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1159` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1159 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.086)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.294 (n=323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.290 (n=483)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.337 (n=164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2315` → IC=+0.322 (n=161)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2315 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.319 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.304 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.331 (n=483)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.263` → IC=+0.322 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.263 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.491` → IC=+0.304 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.491 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `12383.1611` → IC=+0.315 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12383.1611 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.293 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.283 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.0602` → IC=+0.326 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0602 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `0.3839` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3839 (IC base=+0.278)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2389` → IC=+0.326 (n=90)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2389 (IC base=+0.278)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3796` → IC=+0.294 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3796 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.330 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.278)

- **PATRÓN** `ibs_15` > `0.8595` → IC=+0.311 (n=241)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8595 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.335 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.471` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.471 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `14264.9886` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14264.9886 (IC base=+0.278)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.301 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.298)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.301 (n=214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.337 (n=96)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.298)

- **PATRÓN** `drift_15min` |x|≤ `0.4139` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4139 (IC base=+0.298)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1458` → IC=+0.321 (n=143)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1458 (IC base=+0.298)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.339 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.320 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.298)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.347 (n=214)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.2764` → IC=+0.312 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2764 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` < `0.1597` → IC=+0.304 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1597 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.547` → IC=+0.324 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.547 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.311 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.308 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.298)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.309 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.298)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0857` → IC=-0.278 (n=61)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0857
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=186)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.241 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=164)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.161 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=321)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2171` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2171
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=65)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1771` → IC=-0.148 (n=69)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1771
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=69)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2179` → IC=-0.155 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2179
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1979` → IC=-0.382 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1979
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.239 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `83.3501` → IC=+0.126 (n=172)

  - _Acción_: Kelly boost +0.63€ cuando `T_h` > 83.3501 (IC base=+0.121)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.326 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.121)

- **PATRÓN** `T_h` > `145.8875` → IC=+0.411 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8875 (IC base=+0.348)

- **PATRÓN** `ratio` > `1.012` → IC=+0.360 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.348)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9922` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.083)

- **PATRÓN** `T_h` > `111.89` → IC=+0.299 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.89 (IC base=+0.297)

- **PATRÓN** `ratio` > `1.0047` → IC=+0.350 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0047 (IC base=+0.297)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9922` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9922 (IC base=+0.181)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.357 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.181)

- **PATRÓN** `T_h` > `87.9957` → IC=+0.345 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9957 (IC base=+0.326)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.326)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.406)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6176 sube el IC de +0.167 a +0.239 en UPDOWN_GBM#15min (n=969). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8791 sube el IC de +0.194 a +0.294 en UPDOWN_GBM#BTC#15min (n=163). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.698 sube el IC de +0.138 a +0.266 en UPDOWN_GBM#ETH#15min (n=203). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.139 a +0.246 en UPDOWN_GBM#SOL#15min (n=136). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5075 sube el IC de +0.158 a +0.247 en UPDOWN_GBM#XRP#15min (n=275). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.103 sube el IC de +0.045 a +0.170 en UPDOWN_GBM#XRP#15min (n=292). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5837 sube el IC de -0.056 a +0.245 en UPDOWN_GBM_15M_TARDIO (n=496). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3542 sube el IC de -0.051 a +0.270 en UPDOWN_GBM_15M_TARDIO (n=959). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7695 sube el IC de +0.068 a +0.340 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=92). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6395 sube el IC de +0.130 a +0.256 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=240). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3605 sube el IC de +0.213 a +0.259 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=397). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.144 a +0.333 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.045 a +0.248 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=208). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3273 sube el IC de -0.050 a +0.285 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=273). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.288 a +0.331 en UPDOWN_GBM_IBS_ALTO (n=483). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8595 sube el IC de +0.278 a +0.311 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=241). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.298 a +0.347 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=214). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8365 sube el IC de +0.332 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=254). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.329 a +0.365 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=161). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.331 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=123). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH#sniper` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1100 | +0.078 | +106.44€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1100 | +0.078 | +106.44€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 795 | +0.083 | +85.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 795 | +0.083 | +85.43€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 229 | +0.041 | +2.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 229 | +0.041 | +2.01€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 50 | +0.173 | +20.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 50 | +0.173 | +20.49€ | 0 | 4 |
| ✅ BALLENAS_TARDIAS | 21266 | -0.105 | -3189.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1137 | -0.028 | -192.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 20129 | -0.109 | -2996.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 2972 | -0.116 | -545.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 2972 | -0.116 | -545.40€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1137 | -0.028 | -192.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1137 | -0.028 | -192.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 2707 | -0.088 | -610.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 2707 | -0.088 | -610.87€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5499 | -0.062 | -514.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5499 | -0.062 | -514.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 4885 | -0.109 | -365.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 4885 | -0.109 | -365.44€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4066 | -0.182 | -960.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4066 | -0.182 | -960.39€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 10135 | -0.049 | +4306.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 2777 | -0.009 | +1857.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 7358 | -0.064 | +2448.42€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 10135 | -0.049 | +4306.22€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 2777 | -0.009 | +1857.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 7358 | -0.064 | +2448.42€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 324 | -0.098 | -55.76€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 5 | +0.018 | +0.75€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 319 | -0.101 | -56.51€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 16 | -0.089 | -0.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 16 | -0.089 | -0.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 195 | -0.043 | -19.95€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 195 | -0.043 | -19.95€ | 1 | 1 |
| 🚫 CANDIDATA9_BOT_CONSENSO#ETH | 92 | -0.202 | -33.15€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 5 | +0.018 | +0.75€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#ETH#5min | 87 | -0.219 | -33.90€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 6 | -0.113 | -6.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 6 | -0.113 | -6.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 15 | +0.022 | +4.34€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 15 | +0.022 | +4.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 67602 | +0.113 | -3669.86€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 10793 | +0.183 | -302.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 259 | -0.113 | -47.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 52086 | +0.099 | -3237.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 4464 | +0.116 | -82.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 8690 | +0.094 | -877.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 36 | -0.158 | -1.29€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 8639 | +0.096 | -864.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 13375 | +0.132 | -249.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3254 | +0.203 | -82.17€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 8632 | +0.109 | -179.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1447 | +0.118 | +34.30€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 8727 | +0.088 | -897.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 41 | -0.035 | -1.28€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 8671 | +0.089 | -884.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 14567 | +0.125 | -276.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4137 | +0.170 | -67.95€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 8690 | +0.109 | -162.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1728 | +0.101 | -38.24€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 13536 | +0.117 | -802.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3289 | +0.187 | -154.48€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 162 | -0.061 | +6.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 8796 | +0.091 | -575.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1289 | +0.135 | -78.45€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 8707 | +0.101 | -566.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 36 | -0.026 | +4.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 8658 | +0.102 | -571.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 10476 | +0.183 | -774.58€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 10476 | +0.183 | -774.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2674 | +0.168 | -289.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2674 | +0.168 | -289.17€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 149 | -0.136 | -0.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 149 | -0.136 | -0.83€ | 4 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2634 | +0.176 | -249.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2634 | +0.176 | -249.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2365 | +0.237 | -67.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2365 | +0.237 | -67.81€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2575 | +0.189 | -180.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2575 | +0.189 | -180.92€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 503 | +0.443 | +0.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 503 | +0.443 | +0.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 196 | +0.439 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 196 | +0.439 | -0.46€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 191 | +0.443 | +1.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 191 | +0.443 | +1.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 110 | +0.429 | -1.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 110 | +0.429 | -1.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 36669 | +0.193 | -3195.96€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 36669 | +0.193 | -3195.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 6412 | +0.165 | -857.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 6412 | +0.165 | -857.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 5781 | +0.224 | -218.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 5781 | +0.224 | -218.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 6358 | +0.167 | -827.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 6358 | +0.167 | -827.64€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 5884 | +0.217 | -253.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 5884 | +0.217 | -253.60€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6066 | +0.199 | -444.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6066 | +0.199 | -444.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 6168 | +0.189 | -594.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 6168 | +0.189 | -594.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 13600 | +0.124 | +261.78€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 13600 | +0.124 | +261.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 6734 | +0.130 | +197.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 6734 | +0.130 | +197.64€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 6866 | +0.118 | +64.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 6866 | +0.118 | +64.14€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1170 | +0.288 | -21.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1170 | +0.288 | -21.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 516 | +0.276 | -14.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 516 | +0.276 | -14.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 557 | +0.291 | -5.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 557 | +0.291 | -5.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 97 | +0.328 | -1.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 97 | +0.328 | -1.32€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 515 | +0.428 | -9.34€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 515 | +0.428 | -9.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 239 | +0.429 | -3.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 239 | +0.429 | -3.92€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 239 | +0.429 | -4.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 239 | +0.429 | -4.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 37 | +0.372 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 37 | +0.372 | -0.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 757 | +0.068 | -40.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 264 | +0.064 | -19.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 493 | +0.070 | -21.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 48 | +0.100 | +0.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 48 | +0.100 | +0.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 591 | +0.077 | -18.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 98 | +0.110 | +2.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 493 | +0.070 | -21.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 118 | +0.008 | -22.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 118 | +0.008 | -22.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 23440 | +0.098 | -757.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1992 | +0.094 | +30.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 21448 | +0.098 | -788.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 13475 | +0.102 | -220.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1992 | +0.094 | +30.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 11483 | +0.103 | -250.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 3903 | +0.114 | +26.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 3903 | +0.114 | +26.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 6062 | +0.077 | -564.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 6062 | +0.077 | -564.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 682 | +0.263 | -77.11€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 682 | +0.263 | -77.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 682 | +0.263 | -77.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 682 | +0.263 | -77.11€ | 0 | 4 |
| ✅ GBM_LATE_15M | 17713 | +0.073 | +7910.81€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 17713 | +0.073 | +7910.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 2887 | +0.198 | +2143.65€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 2887 | +0.198 | +2143.65€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 2591 | +0.174 | +1729.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2591 | +0.174 | +1729.13€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 3005 | +0.193 | +2169.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3005 | +0.193 | +2169.37€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 2662 | -0.002 | +371.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2662 | -0.002 | +371.59€ | 1 | 14 |
| ✅ GBM_LATE_15M#SOL | 2644 | -0.038 | +592.68€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2644 | -0.038 | +592.68€ | 4 | 11 |
| ✅ GBM_LATE_15M#XRP | 3924 | -0.053 | +904.39€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 3924 | -0.053 | +904.39€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 18692 | +0.074 | +9298.77€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 18692 | +0.074 | +9298.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3422 | +0.012 | +1926.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3422 | +0.012 | +1926.52€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 3974 | +0.000 | +708.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 3974 | +0.000 | +708.73€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2630 | +0.256 | +2577.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2630 | +0.256 | +2577.43€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2860 | -0.028 | +235.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2860 | -0.028 | +235.34€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3112 | +0.011 | +1101.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3112 | +0.011 | +1101.71€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2694 | +0.265 | +2749.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2694 | +0.265 | +2749.03€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 14465 | +0.169 | +10408.50€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 14465 | +0.169 | +10408.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2115 | +0.210 | +1708.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2115 | +0.210 | +1708.15€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2275 | +0.158 | +1589.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2275 | +0.158 | +1589.58€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2223 | +0.203 | +1720.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2223 | +0.203 | +1720.15€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2392 | +0.142 | +1548.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2392 | +0.142 | +1548.75€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2738 | +0.113 | +1740.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2738 | +0.113 | +1740.60€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2722 | +0.198 | +2101.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2722 | +0.198 | +2101.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 3479 | +0.121 | +1312.36€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 3479 | +0.121 | +1312.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 105 | +0.107 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 105 | +0.107 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 962 | +0.114 | +362.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 962 | +0.114 | +362.53€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 960 | +0.152 | +416.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 960 | +0.152 | +416.59€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 697 | +0.069 | +159.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 697 | +0.069 | +159.19€ | 0 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 387 | +0.130 | +151.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 387 | +0.130 | +151.73€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO | 17722 | +0.173 | +12664.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 17722 | +0.173 | +12664.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 2758 | +0.225 | +2365.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 2758 | +0.225 | +2365.74€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2765 | +0.153 | +1814.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2765 | +0.153 | +1814.78€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 2848 | +0.219 | +2377.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 2848 | +0.219 | +2377.61€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 2808 | +0.135 | +1755.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 2808 | +0.135 | +1755.17€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3123 | +0.105 | +1724.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3123 | +0.105 | +1724.12€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3420 | +0.201 | +2627.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3420 | +0.201 | +2627.30€ | 0 | 27 |
| ✅ GBM_LATE_5M | 5194 | +0.135 | +2670.65€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5194 | +0.135 | +2670.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 475 | +0.177 | +315.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 475 | +0.177 | +315.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1452 | +0.136 | +843.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1452 | +0.136 | +843.96€ | 1 | 27 |
| ✅ GBM_LATE_5M#DOGE | 651 | +0.166 | +399.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 651 | +0.166 | +399.72€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 1661 | +0.145 | +879.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1661 | +0.145 | +879.62€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 278 | +0.011 | +21.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 278 | +0.011 | +21.30€ | 2 | 2 |
| ✅ GBM_LATE_5M#XRP | 677 | +0.097 | +210.54€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 677 | +0.097 | +210.54€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1113 | +0.052 | +355.80€ | 3 | 16 |
| ✅ GBM_LATE_60M#60min | 1113 | +0.052 | +355.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 388 | +0.080 | +129.23€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 388 | +0.080 | +129.23€ | 0 | 18 |
| ✅ GBM_LATE_60M#ETH | 374 | +0.059 | +130.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 374 | +0.059 | +130.75€ | 3 | 19 |
| ✅ GBM_LATE_60M#SOL | 351 | +0.016 | +95.82€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 351 | +0.016 | +95.82€ | 1 | 8 |
| 🚫 GBM_LATE_60M_FADE | 278 | -0.282 | -36.90€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 278 | -0.282 | -36.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 106 | -0.222 | -7.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 106 | -0.222 | -7.71€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 92 | -0.340 | -23.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 92 | -0.340 | -23.29€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 80 | -0.281 | -5.89€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 80 | -0.281 | -5.89€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 512 | +0.054 | +86.96€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 512 | +0.054 | +86.96€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 189 | +0.050 | +25.61€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 189 | +0.050 | +25.61€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 152 | +0.045 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 152 | +0.045 | +1.62€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 171 | +0.067 | +59.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 171 | +0.067 | +59.73€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1179 | +0.097 | +309.45€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1179 | +0.097 | +309.45€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1179 | +0.097 | +309.45€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1179 | +0.097 | +309.45€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 332 | -0.096 | -37.71€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 332 | -0.096 | -37.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 78 | -0.100 | -9.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 78 | -0.100 | -9.01€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 107 | -0.032 | -4.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 107 | -0.032 | -4.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1448 | -0.006 | -11.53€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1448 | -0.006 | -11.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 163 | -0.021 | +0.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 163 | -0.021 | +0.58€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 101 | -0.053 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 101 | -0.053 | -6.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 554 | +0.022 | +14.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 554 | +0.022 | +14.28€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 458 | -0.006 | -8.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 458 | -0.006 | -8.22€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 97 | -0.066 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 97 | -0.066 | -6.47€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 825 | -0.045 | -24.18€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 825 | -0.045 | -24.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 242 | -0.066 | -17.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 242 | -0.066 | -17.41€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 261 | -0.021 | -0.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 261 | -0.021 | -0.15€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 322 | -0.049 | -6.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 322 | -0.049 | -6.62€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 11943 | -0.011 | -176.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 11943 | -0.011 | -176.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2046 | -0.021 | -43.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2046 | -0.021 | -43.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2559 | +0.008 | -17.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2559 | +0.008 | -17.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2196 | -0.019 | -17.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2196 | -0.019 | -17.87€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 2885 | -0.017 | -63.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 2885 | -0.017 | -63.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 19292 | -0.015 | +907.79€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 19292 | -0.015 | +907.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3316 | +0.008 | +479.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3316 | +0.008 | +479.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3137 | -0.026 | -19.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3137 | -0.026 | -19.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3355 | -0.002 | +275.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3355 | -0.002 | +275.14€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 2977 | -0.045 | -68.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 2977 | -0.045 | -68.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3238 | -0.018 | +143.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3238 | -0.018 | +143.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3269 | -0.009 | +97.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3269 | -0.009 | +97.78€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 4037 | -0.030 | -90.13€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 4037 | -0.030 | -90.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 872 | +0.001 | -13.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 872 | +0.001 | -13.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 737 | -0.035 | -17.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 737 | -0.035 | -17.58€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 41 | -0.128 | -5.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 41 | -0.128 | -5.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 369 | -0.120 | -13.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 369 | -0.120 | -13.62€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1172 | -0.030 | -14.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1172 | -0.030 | -14.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 846 | -0.015 | -25.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 846 | -0.015 | -25.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3186 | +0.004 | -3.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3186 | +0.004 | -3.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1163 | +0.008 | +8.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1163 | +0.008 | +8.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1387 | +0.007 | -0.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1387 | +0.007 | -0.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 50600 | -0.073 | +1060.43€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 50600 | -0.073 | +1060.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 8418 | -0.082 | +470.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 8418 | -0.082 | +470.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 7969 | -0.087 | -277.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 7969 | -0.087 | -277.22€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 8453 | -0.072 | +424.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 8453 | -0.072 | +424.12€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 7485 | -0.096 | -245.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 7485 | -0.096 | -245.69€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 9474 | -0.046 | +312.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 9474 | -0.046 | +312.90€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 8801 | -0.063 | +376.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 8801 | -0.063 | +376.11€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6607 | -0.020 | -116.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6607 | -0.020 | -116.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1451 | -0.019 | -16.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1451 | -0.019 | -16.75€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1451 | -0.012 | -10.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1451 | -0.012 | -10.62€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 970 | -0.033 | -14.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 970 | -0.033 | -14.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 904 | +0.110 | +302.98€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 768 | +0.119 | +290.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 174 | +0.119 | +72.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 174 | +0.119 | +72.95€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 151 | +0.088 | +31.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 151 | +0.088 | +31.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 152 | +0.110 | +56.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 152 | +0.110 | +56.66€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 137 | +0.169 | +81.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 137 | +0.169 | +81.36€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#XRP | 154 | +0.109 | +48.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 154 | +0.109 | +48.00€ | 0 | 5 |
| ✅ PRICE_TARGET_GBM | 421 | -0.098 | -14.07€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 185 | -0.147 | -36.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 151 | -0.186 | -37.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 34 | +0.028 | +0.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 151 | -0.088 | +3.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 113 | -0.100 | -2.79€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 38 | -0.050 | +6.62€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 85 | -0.006 | +18.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 66 | -0.029 | +11.86€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 19 | +0.068 | +6.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 330 | -0.127 | -28.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 91 | +0.005 | +14.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 472 | -0.219 | -34.47€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 199 | -0.202 | -29.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 173 | -0.191 | -26.93€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 26 | -0.250 | -2.30€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 166 | -0.244 | -20.73€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 143 | -0.252 | -24.60€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 23 | -0.180 | +3.88€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 107 | -0.206 | +15.48€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 93 | -0.205 | +12.42€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 409 | -0.218 | -39.11€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 63 | -0.223 | +4.64€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 161 | +0.390 | +110.48€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#BTC | 21 | -0.022 | -5.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 21 | -0.022 | -5.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 37 | +0.321 | +34.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 37 | +0.321 | +34.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 103 | +0.490 | +81.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 103 | +0.490 | +81.46€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#sniper | 161 | +0.390 | +110.48€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 356 | +0.028 | +5.61€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 356 | +0.028 | +5.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 155 | +0.041 | +2.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 155 | +0.041 | +2.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 24 | +0.077 | +2.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 24 | +0.077 | +2.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 40 | -0.048 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 40 | -0.048 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 137 | +0.025 | +5.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 137 | +0.025 | +5.65€ | 2 | 1 |
| ✅ STREAK_FADE_5M | 2289 | -0.023 | -98.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2289 | -0.023 | -98.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 560 | -0.023 | -23.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 560 | -0.023 | -23.43€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 150 | -0.040 | -13.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 150 | -0.040 | -13.41€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 775 | -0.024 | -34.38€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 775 | -0.024 | -34.38€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 48 | +0.020 | +0.80€ | 1 | 0 |
| ✅ STREAK_FADE_60M#60min | 48 | +0.020 | +0.80€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 29 | -0.048 | -1.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 29 | -0.048 | -1.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 5737 | +0.023 | +84.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 5737 | +0.023 | +84.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1861 | +0.025 | +25.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1861 | +0.025 | +25.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1181 | +0.034 | +36.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1181 | +0.034 | +36.26€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1668 | +0.008 | -5.05€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1668 | +0.008 | -5.05€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1027 | +0.029 | +28.15€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1027 | +0.029 | +28.15€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 5522 | +0.014 | -23.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 5522 | +0.014 | -23.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2166 | +0.022 | +6.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2166 | +0.022 | +6.91€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2196 | +0.016 | -3.28€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2196 | +0.016 | -3.28€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1160 | -0.008 | -26.67€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1160 | -0.008 | -26.67€ | 2 | 0 |
| ✅ UPDOWN_GBM | 21422 | +0.027 | +1112.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 5934 | +0.055 | +904.84€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 810 | +0.003 | +7.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 13329 | +0.020 | +217.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1261 | -0.010 | -21.37€ | 2 | 0 |
| ✅ UPDOWN_GBM#BNB | 1785 | +0.074 | +179.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 266 | +0.131 | +87.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1500 | +0.065 | +92.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 3788 | +0.028 | +240.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 692 | +0.081 | +162.08€ | 1 | 13 |
| ✅ UPDOWN_GBM#BTC#240min | 233 | +0.028 | +7.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2279 | +0.023 | +74.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 551 | -0.004 | -4.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 33 | -0.129 | +1.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 2549 | +0.030 | +79.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 228 | +0.109 | +55.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2305 | +0.022 | +24.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 4354 | +0.015 | +163.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1620 | +0.040 | +160.88€ | 1 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 220 | +0.009 | +8.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2022 | +0.004 | -2.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 463 | -0.014 | -8.66€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 29 | -0.145 | +4.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 5687 | +0.013 | +119.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1595 | +0.020 | +93.69€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 215 | -0.007 | -1.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 3606 | +0.014 | +36.12€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 247 | -0.014 | -8.15€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 24 | -0.154 | -0.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3257 | +0.036 | +331.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1533 | +0.072 | +344.93€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 107 | -0.041 | -5.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1617 | +0.006 | -7.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 86 | -0.148 | +5.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 378 | +0.332 | +98.27€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 378 | +0.332 | +98.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 214 | +0.329 | +49.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 214 | +0.329 | +49.94€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 164 | +0.331 | +48.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 164 | +0.331 | +48.33€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 8182 | -0.052 | +1721.01€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 8182 | -0.052 | +1721.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 396 | -0.048 | +351.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 396 | -0.048 | +351.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1575 | -0.132 | -9.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1575 | -0.132 | -9.01€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 848 | +0.182 | +464.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 848 | +0.182 | +464.86€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2644 | -0.064 | +423.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2644 | -0.064 | +423.05€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2580 | -0.078 | +435.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2580 | -0.078 | +435.97€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 85 | +0.063 | +8.21€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 85 | +0.063 | +8.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 85 | +0.063 | +8.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 85 | +0.063 | +8.21€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 644 | +0.288 | +522.47€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 644 | +0.288 | +522.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 359 | +0.278 | +271.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 359 | +0.278 | +271.79€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 285 | +0.298 | +250.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 285 | +0.298 | +250.68€ | 0 | 14 |
| ✅ UPDOWN_OU_5M | 675 | -0.107 | -78.52€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 675 | -0.107 | -78.52€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 176 | -0.067 | -11.84€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 176 | -0.067 | -11.84€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 65 | -0.172 | -9.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 65 | -0.172 | -9.61€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 56 | -0.190 | -7.52€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 56 | -0.190 | -7.52€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1737 | +0.300 | +866.50€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 573 | +0.237 | +76.19€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 601 | +0.289 | +231.63€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 563 | +0.374 | +558.68€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.059) — sin ventaja clara. oversold(IBS<0.3): IC=+0.041 n=7393 | neutral: IC=+0.026 n=8188 | overbought(IBS>0.7): IC=+0.086 n=7937
  - _Datos_: n=24392 IC=+0.051 PNL=+2812.98€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 405 celda(s) pasan gate riguroso completo de 1956 evaluadas (n>=40) y 2913 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.020 < 0.08 — monitorear
  - _Datos_: n=1594 IC=+0.020 PNL=+93.20€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=601/15 IC=+0.289 PNL=+231.63€ | BTC: n=573/15 IC=+0.237 PNL=+76.19€ | SOL: n=563/15 IC=+0.374 PNL=+558.68€

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
  - _Estado_: 21347 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.067 n=155/60 | contraria IC=+0.141 n=143 | gap=-0.074 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=214, boost estimado=+0.002. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 137 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=463/40 IC=-0.014 PNL=-8.66€ | BTC#60min: n=551/40 IC=-0.004 PNL=-4.56€ | SOL#60min: n=247/40 IC=-0.014 PNL=-8.15€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.055 n=233274 | tras_1loss IC=+0.067 n=182952 | tras_2loss IC=+0.035 n=79105/40 | gap=+0.020 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.004 n=2094 | contrario_BTC IC=+0.012 n=1933/40 | gap=+0.007 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.08 con n=180 PNL=+119.73€
  - _Datos_: n=180 IC=+0.198 PNL=+119.73€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.08 con n=237 PNL=+135.23€
  - _Datos_: n=237 IC=+0.182 PNL=+135.23€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.08 con n=31 PNL=+21.19€
  - _Datos_: n=31 IC=+0.227 PNL=+21.19€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.341 > 0.1 con n=1459 PNL=+861.32€
  - _Datos_: n=1459 IC=+0.341 PNL=+861.32€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=153 IC=+0.055 PNL=+17.52€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=153 IC=+0.055 PNL=+17.52€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=41 IC=+0.198 PNL=+28.61€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=41 IC=+0.198 PNL=+28.61€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=20328 IC=+0.025 PNL=+1018.76€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=20328 IC=+0.025 PNL=+1018.76€

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
  - _Estado_: 1/20 ops en el filtro definido (IC actual=+0.008 PNL=+1.96€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.96€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=936 IC=-0.007 PNL=-18.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=936 IC=-0.007 PNL=-18.19€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=325 IC=-0.017 PNL=-3.18€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=325 IC=-0.017 PNL=-3.18€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=318 IC=+0.034 PNL=+22.09€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=318 IC=+0.034 PNL=+22.09€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.167 > 0.1 con n=1292 PNL=+686.83€
  - _Datos_: n=1292 IC=+0.167 PNL=+686.83€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=787 IC=+0.048 PNL=+62.17€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=787 IC=+0.048 PNL=+62.17€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=692 IC=+0.081 PNL=+162.08€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=692 IC=+0.081 PNL=+162.08€

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
  - _Estado_: n=3413 IC=+0.055 PNL=+597.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3413 IC=+0.055 PNL=+597.37€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=91 IC=-0.210 PNL=-1.92€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=91 IC=-0.210 PNL=-1.92€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=162 IC=-0.018 PNL=+14.75€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=162 IC=-0.018 PNL=+14.75€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=308 IC=+0.032 PNL=+29.08€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=308 IC=+0.032 PNL=+29.08€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=20 IC=-0.045 PNL=-1.64€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=20 IC=-0.045 PNL=-1.64€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2959 IC=-0.008 PNL=-27.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2959 IC=-0.008 PNL=-27.38€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.156 > 0.08 con n=59 PNL=+12.92€
  - _Datos_: n=59 IC=+0.156 PNL=+12.92€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.227 n=53) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=53 IC=+0.227 PNL=+25.89€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=4177 IC=+0.025 PNL=+209.61€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4177 IC=+0.025 PNL=+209.61€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=1408 IC=+0.044 PNL=+131.05€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1408 IC=+0.044 PNL=+131.05€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.107 > 0.08 con n=270 PNL=+75.62€
  - _Datos_: n=270 IC=+0.107 PNL=+75.62€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.152 > 0.08 con n=354 PNL=+73.85€
  - _Datos_: n=354 IC=+0.152 PNL=+73.85€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.08 con n=287 PNL=+149.26€
  - _Datos_: n=287 IC=+0.126 PNL=+149.26€

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
  - _Estado_: n=2925 IC=+0.034 PNL=+185.15€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2925 IC=+0.034 PNL=+185.15€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=512 PNL=+193.54€
  - _Datos_: n=512 IC=+0.124 PNL=+193.54€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=131 IC=-0.049 PNL=+33.33€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=131 IC=-0.049 PNL=+33.33€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.450 > 0.1 con n=892 PNL=+874.78€
  - _Datos_: n=892 IC=+0.450 PNL=+874.78€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=6725 IC=+0.050 PNL=+769.05€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=6725 IC=+0.050 PNL=+769.05€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.190 > 0.1 con n=2019 PNL=+1007.47€
  - _Datos_: n=2019 IC=+0.190 PNL=+1007.47€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.126 < -0.1 con n=129 PNL=+17.86€
  - _Datos_: n=129 IC=-0.126 PNL=+17.86€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1167 IC=+0.045 PNL=+133.76€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1167 IC=+0.045 PNL=+133.76€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=49 IC=-0.108 PNL=+7.40€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=49 IC=-0.108 PNL=+7.40€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.1 con n=221 PNL=+63.89€
  - _Datos_: n=221 IC=+0.119 PNL=+63.89€

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
  - _Estado_: n=12124 IC=-0.142 PNL=+593.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12124 IC=-0.142 PNL=+593.41€

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
  - _Estado_: n=1338 IC=+0.140 PNL=+706.91€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1338 IC=+0.140 PNL=+706.91€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.169 > 0.08 con n=1253 PNL=+674.20€
  - _Datos_: n=1253 IC=+0.169 PNL=+674.20€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=2250 IC=+0.018 PNL=+57.31€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2250 IC=+0.018 PNL=+57.31€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=1431 PNL=+774.42€
  - _Datos_: n=1431 IC=+0.084 PNL=+774.42€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.193 > 0.08 con n=324 PNL=+151.96€
  - _Datos_: n=324 IC=+0.193 PNL=+151.96€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.238 < -0.1 con n=1236 PNL=-169.24€
  - _Datos_: n=1236 IC=-0.238 PNL=-169.24€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=3425 IC=+0.142 PNL=+2008.47€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=3425 IC=+0.142 PNL=+2008.47€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.08 con n=61 PNL=+24.46€
  - _Datos_: n=61 IC=+0.119 PNL=+24.46€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=1388 IC=+0.040 PNL=+279.90€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1388 IC=+0.040 PNL=+279.90€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.185 > 0.08 con n=1246 PNL=+833.64€
  - _Datos_: n=1246 IC=+0.185 PNL=+833.64€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=2059 IC=-0.042 PNL=+477.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2059 IC=-0.042 PNL=+477.32€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.101 > 0.08 con n=436 PNL=-37.43€
  - _Datos_: n=436 IC=+0.101 PNL=-37.43€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.229 > 0.08 con n=2558 PNL=-257.11€
  - _Datos_: n=2558 IC=+0.229 PNL=-257.11€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 25/40 ops en el filtro definido (IC actual=+0.056 PNL=+7.73€)
  - _Datos_: n=25 IC=+0.056 PNL=+7.73€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.093 n=615) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=615 IC=+0.093 PNL=+156.38€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.08 con n=165 PNL=+70.64€
  - _Datos_: n=165 IC=+0.332 PNL=+70.64€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.416 n=355) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=355 IC=+0.416 PNL=+496.74€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=6411 IC=+0.165 PNL=-858.05€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=6411 IC=+0.165 PNL=-858.05€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.1 con n=93 PNL=+59.67€
  - _Datos_: n=93 IC=+0.216 PNL=+59.67€
