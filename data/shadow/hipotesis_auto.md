# Hipótesis automáticas — 2026-09-28 08:49 UTC
_Generado por shadow_postmortem.py sobre 648342 resoluciones (PNL=+75648.48€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=525)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.234 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.137)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.137)

- **PATRÓN** `banda_hit_calibrado` > `0.8035` → IC=+0.252 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8035 (IC base=+0.137)

- **PATRÓN** `banda_z` > `4.083` → IC=+0.160 (n=565)

  - _Acción_: Kelly boost +0.80€ cuando `banda_z` > 4.083 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.156 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=603)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4804.7376` → IC=+0.165 (n=189)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4804.7376 (IC base=+0.137)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=525)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.057)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=390)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.237 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.146)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.207 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.146)

- **PATRÓN** `banda_hit_calibrado` > `0.7998` → IC=+0.264 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7998 (IC base=+0.146)

- **PATRÓN** `banda_z` > `4.303` → IC=+0.170 (n=455)

  - _Acción_: Kelly boost +0.85€ cuando `banda_z` > 4.303 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=514)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3317.318` → IC=+0.149 (n=303)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3317.318 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.165 (n=153)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 94.0 (IC base=+0.061)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.214 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=101)

- **FILTRO** `banda_hit_calibrado` < `0.6297` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6297
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=90)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=107)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=92)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

- **PATRÓN** `py_entrada` > `0.35` → IC=+0.218 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.35 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1195.1095` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1195.1095 (IC base=+0.110)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=-0.004)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.154)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.154)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.705` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ballenas_wallet_edge_medio` > 0.705 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2518.5859` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2518.5859 (IC base=+0.154)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `146.18` → IC=-0.216 (n=7462)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.18
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=22394)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.36` → IC=-0.245 (n=971)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.36
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=2916)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.83` → IC=-0.308 (n=880)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.83
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2641)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.52` → IC=-0.202 (n=1825)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.52
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=5478)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.48` → IC=-0.335 (n=1465)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.48
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=4395)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.230 (n=357)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=408)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=174)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=539)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=563)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.259 (n=164)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=169)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.218 (n=69)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=234)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.270 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=156)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.175 (n=78)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=161)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.167 (n=70)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=169)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.207 (n=14629)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3646)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5618.809` → IC=+0.177 (n=2335)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5618.809 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=12307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=15166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=11658)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=5923)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7812.228` → IC=+0.173 (n=2251)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7812.228 (IC base=+0.128)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=2217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `15918.3154` → IC=+0.237 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15918.3154 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=1589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=1774)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.262 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=2268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `15830.8412` → IC=+0.212 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15830.8412 (IC base=+0.198)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.175 (n=340)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.62 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.145 (n=240)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.097)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.146 (n=382)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.103)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.143 (n=859)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `5754.4405` → IC=+0.167 (n=226)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5754.4405 (IC base=+0.103)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=2989)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.345 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.365 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.234 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.230)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.133 (n=638)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 15.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.248 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=577)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `1313.4858` → IC=+0.144 (n=705)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1313.4858 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.403 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.157 (n=1137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 7.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.161 (n=617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=752)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.155)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.369 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `1244.5613` → IC=+0.152 (n=231)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1244.5613 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.224 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.76` → IC=-0.289 (n=131)

  - _Acción_: SKIP cuando `py_entrada` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=65)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=12391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=11836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.227 (n=4031)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `5111.8837` → IC=+0.335 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5111.8837 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.172 (n=2824)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=2831)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=1018)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.248 (n=1013)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.342 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.243)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=2928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=2369)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.251 (n=2575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.324 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.241)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2735)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.197 (n=2127)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.193)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.433 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.463 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.427 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `11185.2288` → IC=+0.458 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11185.2288 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.445 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `14073.2838` → IC=+0.446 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14073.2838 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.447 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.461 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.424 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `3299.2146` → IC=+0.444 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3299.2146 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.412 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.410)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.425 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.410)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.410)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=36778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.236 (n=16389)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=7481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=6918)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=6627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=6609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.263 (n=3775)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=6702)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=6715)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.265 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=6096)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=2455)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=7276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=2847)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5614)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.125 (n=5213)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=5261)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=6957)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.62` → IC=+0.140 (n=5196)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.62 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=2826)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.13` → IC=+0.126 (n=2588)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.13 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.144 (n=2585)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.95 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=3433)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `3.3` → IC=+0.144 (n=2591)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.3 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.186 (n=2788)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.128 (n=2622)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.2 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=2917)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.138 (n=2623)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `4107.9466` → IC=+0.304 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4107.9466 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.288 (n=550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.329 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `4255.42` → IC=+0.295 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4255.42 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.325 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=588)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1723.1828` → IC=+0.312 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1723.1828 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.350 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.344)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.344)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.385 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.344)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.344)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.344)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.438 (n=468)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.433 (n=462)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.434 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.435 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.434 (n=254)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.433 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.454 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.444 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.437 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `1978.9685` → IC=+0.464 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.9685 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.394)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.406 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.394)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.394)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.765` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=49)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1366.4094` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1366.4094 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.765` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=49)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1366.4094` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1366.4094 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4859` → IC=+0.126 (n=8748)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.4859 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.9809` → IC=+0.242 (n=2916)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9809 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` < `0.2191` → IC=+0.257 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2191 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.972` → IC=+0.180 (n=3350)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.972 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.251 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` > `1.0466` → IC=+0.262 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0466 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.225 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` > `1.4628` → IC=+0.206 (n=6046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4628 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.5707` → IC=+0.135 (n=10590)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5707 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.6047` → IC=+0.204 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6047 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.186 (n=1659)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6986 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.869` → IC=+0.176 (n=2512)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.869 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.225 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.5692` → IC=+0.201 (n=5712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5692 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.214 (n=6182)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=+0.068)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.196 (n=659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0049 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.177 (n=655)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0081 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.348` → IC=+0.173 (n=1957)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.348 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.172 (n=1320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.178` → IC=+0.269 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.178 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.207 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.169 (n=1839)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.182 (n=1986)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.247 (n=1355)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.198` → IC=+0.262 (n=1011)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.198 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.249 (n=1033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.290 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.49` → IC=+0.242 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.49 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.246 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.266 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4333` → IC=+0.234 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4333 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6054` → IC=+0.247 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6054 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1817.84` → IC=+0.237 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1817.84 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.239 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.243 (n=670)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=1595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.220 (n=1546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.8988` → IC=+0.263 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8988 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.347` → IC=+0.223 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.347 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.483` → IC=+0.267 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.483 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.2572` → IC=+0.222 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2572 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.228 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.244 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7571` → IC=+0.218 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7571 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.3817` → IC=+0.232 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3817 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `11084.2751` → IC=+0.224 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11084.2751 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.176 (n=523)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0745` → IC=+0.167 (n=523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0745 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.3342` → IC=+0.194 (n=1046)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3342 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1289` → IC=+0.153 (n=1414)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1289 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.323` → IC=+0.153 (n=249)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.323 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.327` → IC=+0.144 (n=1439)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.327 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.149 (n=1569)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2089 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.8533` → IC=+0.140 (n=1046)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8533 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.178 (n=417)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4384` → IC=+0.152 (n=1459)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4384 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.147 (n=972)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `14029.1139` → IC=+0.145 (n=1046)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 14029.1139 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.171 (n=611)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 233.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.211 (n=652)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=2052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=1752)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.256 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.0997` → IC=+0.190 (n=1703)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0997 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3557` → IC=+0.201 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3557 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.7734` → IC=+0.195 (n=1666)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7734 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2322)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.223 (n=1497)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.6219` → IC=+0.217 (n=1700)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6219 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.244 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.704` → IC=+0.233 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.704 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.506` → IC=+0.213 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.506 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3508` → IC=+0.265 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3508 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.7536` → IC=+0.206 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7536 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.1776` → IC=+0.219 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1776 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1912.1584` → IC=+0.213 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.1584 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.220 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.213)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.148 (n=106)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=2376)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.138 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0037 (IC base=+0.033)

- **PATRÓN** `ibs_20min` > `0.9456` → IC=+0.216 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9456 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.3549` → IC=+0.328 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3549 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` < `0.1947` → IC=+0.331 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1947 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.811` → IC=+0.168 (n=773)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.811 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.337 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.339 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.350 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.358 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.334 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.334 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 157.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.1047` → IC=+0.152 (n=621)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1047 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6579` → IC=+0.210 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6579 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.155 (n=622)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.852 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.1639` → IC=+0.152 (n=311)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1639 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2304` → IC=+0.214 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2304 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5242` → IC=+0.168 (n=787)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.5242 (IC base=+0.021)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.182 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=356)

- **FILTRO** `ibs_20min` < `0.2941` → IC=-0.201 (n=105)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=315)

- **FILTRO** `ibs_20min` > `0.25` → IC=-0.126 (n=2348)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=1186)

- **FILTRO** `sigma_ewma_delta_pct` > `8.708` → IC=-0.214 (n=376)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.708
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3158)

- **PATRÓN** `ibs_20min` > `0.7834` → IC=+0.224 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7834 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `1.8814` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.8814 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.5572` → IC=+0.277 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5572 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.266` → IC=+0.128 (n=151)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.266 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.5152` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5152 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.291 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.125 (n=1186)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.25 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7328` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7328 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.4655` → IC=+0.233 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4655 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `0.6732` → IC=+0.270 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6732 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.282 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6559` → IC=-0.179 (n=618)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6559
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1855)

- **FILTRO** `ibs_20min` < `0.72` → IC=-0.153 (n=1632)

  - _Acción_: SKIP cuando `ibs_20min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=841)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.197 (n=509)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1964)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.206 (n=903)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=2748)

- **PATRÓN** `dist_vwap_pct` > `0.4581` → IC=+0.314 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4581 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2822` → IC=+0.314 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2822 (IC base=-0.068)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.310 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=-0.068)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.300 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.1123` → IC=+0.297 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1123 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.298 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.5647` → IC=+0.277 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5647 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` < `0.733` → IC=+0.256 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.733 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` > `1.2494` → IC=+0.274 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2494 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.265 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.1399` → IC=+0.264 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1399 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.5236` → IC=+0.247 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5236 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.197 (n=3722)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4733` → IC=+0.185 (n=9956)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4733 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `1.0296` → IC=+0.289 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0296 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.633` → IC=+0.157 (n=5178)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.633 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6911` → IC=+0.253 (n=3563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6911 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.270 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4647` → IC=+0.240 (n=2157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4647 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.663` → IC=+0.249 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.663 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.272 (n=5987)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.163 (n=3655)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0091 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5494` → IC=+0.154 (n=9648)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5494 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7107` → IC=+0.244 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7107 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2492` → IC=+0.246 (n=3133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2492 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7084` → IC=+0.246 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7084 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.205` → IC=+0.248 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.205 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.302 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5966` → IC=+0.266 (n=1932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5966 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2869` → IC=+0.264 (n=1991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2869 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.273 (n=4266)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 83.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2548` → IC=-0.153 (n=770)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2548
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2310)

- **FILTRO** `sigma_ewma_delta_pct` > `4.536` → IC=-0.166 (n=584)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.536
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1943)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.271 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.846` → IC=+0.205 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.846 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2226` → IC=+0.261 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2226 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.186 (n=329)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.1741` → IC=+0.210 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1741 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.204 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.2144` → IC=+0.471 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2144 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.3871` → IC=+0.460 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3871 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.0444` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0444 (IC base=-0.022)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8658` → IC=+0.164 (n=747)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8658 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.2992` → IC=+0.176 (n=396)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2992 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` > `0.6774` → IC=+0.177 (n=923)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6774 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.244 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.191 (n=338)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` > `2.4039` → IC=+0.173 (n=338)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4039 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `237.0` → IC=+0.198 (n=441)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 237.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.222 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.8577` → IC=+0.232 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8577 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2677` → IC=+0.302 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2677 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.4377` → IC=+0.216 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4377 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1623` → IC=+0.235 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1623 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `459.0` → IC=+0.221 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 459.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.288 (n=577)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.248)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.251 (n=1732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.251 (n=660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.248)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.749` → IC=+0.282 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.749 (IC base=+0.248)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.262 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.248)

- **PATRÓN** `volumen_spike_ratio` > `3.3381` → IC=+0.267 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3381 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.248)

- **PATRÓN** `libro_liquidez` > `1913.4832` → IC=+0.260 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.4832 (IC base=+0.248)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.317 (n=641)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.6177` → IC=+0.288 (n=1414)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6177 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.326 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.3459` → IC=+0.293 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3459 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.298 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.7` → IC=+0.284 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.7 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.3387` → IC=+0.299 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3387 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.7371` → IC=+0.289 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7371 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.6935` → IC=+0.293 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6935 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `1904.5592` → IC=+0.298 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.5592 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.293 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.284)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.3037` → IC=-0.160 (n=557)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3037
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=1673)

- **FILTRO** `ibs_20min` > `0.7732` → IC=-0.183 (n=655)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7732
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=1966)

- **PATRÓN** `ibs_20min` > `0.912` → IC=+0.177 (n=558)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.912 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` < `0.1819` → IC=+0.226 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1819 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` < `0.9991` → IC=+0.243 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9991 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` > `0.5902` → IC=+0.223 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5902 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.263 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.3994` → IC=+0.274 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3994 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.7536` → IC=+0.236 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7536 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.253 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 145.0 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` > `0.1481` → IC=+0.217 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1481 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` < `0.1979` → IC=+0.206 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1979 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1663` → IC=+0.218 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1663 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.260 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.808 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1331` → IC=+0.253 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1331 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.264 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7377` → IC=-0.194 (n=1182)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7377
  - _Potencial_: sin este filtro IC_bueno=+0.279 (n=1183)

- **FILTRO** `ibs_20min` > `0.6818` → IC=-0.233 (n=598)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6818
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1797)

- **FILTRO** `sigma_ewma_delta_pct` > `4.743` → IC=-0.190 (n=523)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.743
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=1872)

- **PATRÓN** `ibs_20min` > `0.7377` → IC=+0.279 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7377 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.8477` → IC=+0.324 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8477 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.655` → IC=+0.167 (n=373)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.655 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.304 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.642` → IC=+0.297 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.642 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1016` → IC=+0.297 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1016 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2714` → IC=+0.298 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2714 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4368` → IC=+0.322 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4368 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.319 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.5806` → IC=+0.125 (n=1582)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.5806 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` < `0.22` → IC=+0.231 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.22 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.258 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6989 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.221 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.227 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.46` → IC=+0.237 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.46 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.244 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.017)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.318 (n=944)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.296 (n=671)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.7388` → IC=+0.324 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7388 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2169` → IC=+0.315 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2169 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.672` → IC=+0.304 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.672 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.8619` → IC=+0.308 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8619 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.329 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.289 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1473)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2465.9778` → IC=+0.291 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2465.9778 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.320 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0156` → IC=+0.306 (n=1011)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0156 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.1984` → IC=+0.282 (n=668)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1984 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.289 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.2903` → IC=+0.315 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2903 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.316` → IC=+0.285 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.316 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.2297` → IC=+0.279 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2297 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.07` → IC=+0.299 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.07 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` < `0.6412` → IC=+0.283 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6412 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` > `1.2434` → IC=+0.307 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2434 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.330 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.4234` → IC=+0.288 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4234 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.1415` → IC=+0.275 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1415 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `2608.7306` → IC=+0.280 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2608.7306 (IC base=+0.278)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.178 (n=2838)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.202 (n=2830)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3572` → IC=+0.177 (n=7467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3572 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=8853)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.219 (n=8495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1754` → IC=+0.194 (n=3649)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1754 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.362` → IC=+0.254 (n=1730)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.362 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2076` → IC=+0.162 (n=5632)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2076 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6293` → IC=+0.160 (n=5632)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6293 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2427` → IC=+0.195 (n=1714)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2427 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5596` → IC=+0.168 (n=3590)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5596 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6119` → IC=+0.176 (n=2719)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6119 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `1955.02` → IC=+0.171 (n=7580)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1955.02 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.182 (n=7395)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 110.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.183 (n=5463)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0066 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0815` → IC=+0.213 (n=2731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0815 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=3934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.4838` → IC=+0.226 (n=8191)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4838 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.2357` → IC=+0.162 (n=5957)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2357 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.195 (n=1386)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.156 (n=5900)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1753 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2913` → IC=+0.212 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2913 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5608` → IC=+0.171 (n=3303)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5608 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.621` → IC=+0.172 (n=2501)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.621 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.178 (n=7162)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 111.0 (IC base=+0.170)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.221 (n=485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.187 (n=481)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.3404` → IC=+0.212 (n=1434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3404 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=1512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.19` → IC=+0.329 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.19 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.236 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.4398` → IC=+0.186 (n=1332)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4398 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.242 (n=952)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.248 (n=967)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1824` → IC=+0.288 (n=721)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1824 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.241 (n=997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3485` → IC=+0.259 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3485 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.288` → IC=+0.250 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.288 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.236 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.248 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4211` → IC=+0.269 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4211 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1817.785` → IC=+0.244 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1817.785 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.240 (n=425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.200 (n=421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=1264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.4009` → IC=+0.227 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4009 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2039` → IC=+0.211 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2039 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.479` → IC=+0.236 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.479 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2593` → IC=+0.166 (n=1263)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2593 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.0767` → IC=+0.168 (n=573)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0767 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.201 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5081` → IC=+0.181 (n=540)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5081 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.164 (n=409)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `10581.1275` → IC=+0.170 (n=1263)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10581.1275 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `386.0` → IC=+0.162 (n=1044)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 386.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.157 (n=1361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0057 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.291` → IC=+0.163 (n=1361)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.291 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5785` → IC=+0.188 (n=1361)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5785 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.162 (n=1360)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.204 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2113` → IC=+0.158 (n=1361)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2113 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.154 (n=417)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.148 (n=1249)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.168 (n=392)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 213.0 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.212 (n=644)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.2371` → IC=+0.218 (n=947)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2371 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.441` → IC=+0.277 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.441 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2024` → IC=+0.205 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2024 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.799` → IC=+0.197 (n=596)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.799 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.775` → IC=+0.214 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.775 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.209 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.238 (n=1066)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1015` → IC=+0.256 (n=404)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1015 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.3521` → IC=+0.247 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3521 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.679` → IC=+0.254 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.679 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3553` → IC=+0.256 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3553 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7612` → IC=+0.220 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7612 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.1929` → IC=+0.230 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1929 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.215 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.220)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.218 (n=455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4234` → IC=+0.160 (n=1357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4234 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3688` → IC=+0.196 (n=1356)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3688 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1502` → IC=+0.178 (n=881)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1502 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.969` → IC=+0.229 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.969 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.152 (n=905)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.856 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6208` → IC=+0.146 (n=1356)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6208 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.183 (n=576)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.161 (n=443)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5072` → IC=+0.167 (n=443)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5072 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5814.9525` → IC=+0.188 (n=904)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 5814.9525 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.149 (n=1296)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 160.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.155 (n=1437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.144 (n=1437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6509` → IC=+0.171 (n=1437)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6509 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.1552` → IC=+0.141 (n=1418)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1552 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.964` → IC=+0.163 (n=508)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.964 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8525` → IC=+0.149 (n=958)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8525 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.181 (n=214)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8112` → IC=+0.140 (n=876)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8112 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.5251` → IC=+0.125 (n=438)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.5251 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `9896.1185` → IC=+0.165 (n=652)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 9896.1185 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.122 (n=1251)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 156.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.152 (n=702)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0101 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=1584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.203 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.8396` → IC=+0.208 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8396 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.76` → IC=+0.252 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.76 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2054` → IC=+0.129 (n=1547)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2054 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.122 (n=652)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5436` → IC=+0.136 (n=658)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5436 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1606)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2893.8059` → IC=+0.195 (n=702)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2893.8059 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.134 (n=1203)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 49.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.159 (n=696)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0062 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.105` → IC=+0.169 (n=526)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.105 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.214 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.013` → IC=+0.132 (n=221)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 1.013 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2075` → IC=+0.145 (n=1444)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2075 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.137` → IC=+0.138 (n=255)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 9.137 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6362` → IC=+0.146 (n=526)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6362 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2304` → IC=+0.156 (n=277)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2304 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.141 (n=475)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4234` → IC=+0.135 (n=475)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4234 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2750.8782` → IC=+0.166 (n=714)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2750.8782 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0187` → IC=+0.215 (n=978)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0187 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.208 (n=666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.737` → IC=+0.259 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.737 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.5175` → IC=+0.216 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5175 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.239 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2049` → IC=+0.205 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2049 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.8556` → IC=+0.221 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8556 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.265 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.146` → IC=+0.212 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.146 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4058` → IC=+0.210 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4058 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.206 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2813.5755` → IC=+0.208 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2813.5755 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.225 (n=510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.218 (n=694)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.229 (n=510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.0213` → IC=+0.300 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0213 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.2202` → IC=+0.222 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2202 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2096` → IC=+0.207 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2096 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.392` → IC=+0.245 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.392 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6331` → IC=+0.215 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6331 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.278 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1933` → IC=+0.199 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1933 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4272` → IC=+0.202 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4272 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2575.228` → IC=+0.208 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2575.228 (IC base=+0.207)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.195 (n=717)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.174 (n=715)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0086 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.3424` → IC=+0.164 (n=1887)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3424 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.237 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.8205` → IC=+0.175 (n=346)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.8205 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.1496` → IC=+0.160 (n=1574)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1496 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.759` → IC=+0.187 (n=960)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.759 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.8726` → IC=+0.178 (n=1273)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8726 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.167 (n=638)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.2084 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.180 (n=588)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4437` → IC=+0.169 (n=693)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4437 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.8277` → IC=+0.165 (n=1382)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8277 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.164 (n=2423)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `2654.0473` → IC=+0.162 (n=1915)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2654.0473 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.175 (n=1923)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 150.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.139 (n=1468)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0056 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.130 (n=1937)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=2063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.0598` → IC=+0.189 (n=734)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0598 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2125` → IC=+0.123 (n=1992)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.2125 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2266` → IC=+0.123 (n=1995)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2266 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.134 (n=544)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4487` → IC=+0.152 (n=708)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4487 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2761.0504` → IC=+0.124 (n=1965)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2761.0504 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.134 (n=913)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 28.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.169 (n=179)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0025 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1084` → IC=+0.153 (n=237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1084 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.173 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.6562` → IC=+0.199 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6562 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.2886` → IC=+0.154 (n=183)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.2886 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1215` → IC=+0.133 (n=434)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1215 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.149 (n=243)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6213` → IC=+0.180 (n=179)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6213 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.157` → IC=+0.128 (n=554)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.157 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0914` → IC=+0.149 (n=192)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0914 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.211` → IC=+0.138 (n=459)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.211 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.5157` → IC=+0.136 (n=465)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.5157 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `10682.1975` → IC=+0.145 (n=536)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 10682.1975 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.151 (n=339)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 231.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.206 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3378` → IC=+0.155 (n=680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3378 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6119` → IC=+0.183 (n=598)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6119 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.3088` → IC=+0.151 (n=724)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.3088 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.41` → IC=+0.149 (n=257)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 4.41 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.162` → IC=+0.138 (n=619)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.162 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2266` → IC=+0.144 (n=680)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2266 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.0619` → IC=+0.159 (n=309)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.0619 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.197 (n=183)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1165` → IC=+0.161 (n=590)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1165 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4187` → IC=+0.143 (n=670)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4187 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `12264.8322` → IC=+0.138 (n=608)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 12264.8322 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `318.0` → IC=+0.151 (n=571)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 318.0 (IC base=+0.137)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.272 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2023` → IC=+0.221 (n=449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2023 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.9667` → IC=+0.270 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9667 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1455` → IC=+0.211 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1455 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2163` → IC=+0.207 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2163 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.02` → IC=+0.234 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.02 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.8358` → IC=+0.212 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8358 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.1614` → IC=+0.230 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1614 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.1546` → IC=+0.263 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1546 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4064` → IC=+0.223 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4064 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.1032` → IC=+0.239 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1032 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `12367.1146` → IC=+0.208 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12367.1146 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.084` → IC=+0.153 (n=211)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.084 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6887` → IC=+0.136 (n=278)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6887 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2266` → IC=+0.130 (n=98)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2266 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.009` → IC=+0.163 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.009 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.173 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.947` → IC=+0.226 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.947 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.557` → IC=+0.200 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.557 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.0671` → IC=+0.157 (n=461)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0671 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.7217` → IC=+0.145 (n=468)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.7217 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1794` → IC=+0.160 (n=145)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1794 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.482` → IC=+0.147 (n=168)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.482 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.2151` → IC=+0.170 (n=228)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2151 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=549)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3106.8106` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3106.8106 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.127 (n=464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.4286` → IC=+0.167 (n=425)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.4286 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.2218` → IC=+0.125 (n=483)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.2218 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.5803` → IC=+0.180 (n=201)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5803 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2575.5064` → IC=+0.139 (n=322)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2575.5064 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.146 (n=433)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 40.0 (IC base=+0.100)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.183 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0068 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.191 (n=179)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.2434` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2434 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `1.0655` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0655 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.0007` → IC=+0.148 (n=157)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0007 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.6087` → IC=+0.167 (n=178)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6087 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.2548` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2548 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2497.2192` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2497.2192 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.152 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0091 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.6 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.1734` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1734 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.53` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.53 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.0734` → IC=+0.122 (n=178)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0734 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.132 (n=202)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6515 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1181` → IC=+0.126 (n=180)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1181 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5435` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5435 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.8185` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.8185 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.142 (n=163)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 17.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.175 (n=3664)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0047 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.209 (n=3654)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=11433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=3666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.9394` → IC=+0.201 (n=1538)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9394 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.875` → IC=+0.237 (n=4011)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.875 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.8801` → IC=+0.168 (n=4892)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8801 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.200 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5936` → IC=+0.191 (n=3522)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5936 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `1794.2115` → IC=+0.176 (n=10962)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1794.2115 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.199 (n=8443)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 83.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6634)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1495` → IC=+0.190 (n=4377)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1495 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=3748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=4655)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4497` → IC=+0.247 (n=8749)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4497 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2505` → IC=+0.163 (n=6214)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2505 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.055` → IC=+0.202 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.055 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.184 (n=9615)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.164 (n=2990)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7049 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.240 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6126` → IC=+0.191 (n=3061)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6126 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.199 (n=5880)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 46.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.218 (n=615)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.218 (n=616)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.3528` → IC=+0.196 (n=1839)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3528 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.211 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.199 (n=1248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.603` → IC=+0.347 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.603 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.250 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.8455` → IC=+0.196 (n=1161)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8455 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.261 (n=983)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.264 (n=1474)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.286 (n=648)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=1342)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.3547` → IC=+0.283 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3547 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.489` → IC=+0.264 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.489 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.283 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.5484` → IC=+0.259 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5484 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.6218` → IC=+0.276 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6218 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1814.4372` → IC=+0.264 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1814.4372 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.205 (n=587)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.164 (n=772)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3058` → IC=+0.204 (n=1753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3058 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1256` → IC=+0.186 (n=979)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1256 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.699` → IC=+0.174 (n=397)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 9.699 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.167` → IC=+0.155 (n=1585)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.167 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6273` → IC=+0.183 (n=585)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6273 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2669` → IC=+0.193 (n=255)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2669 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1166` → IC=+0.162 (n=1494)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1166 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.7577` → IC=+0.160 (n=1132)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7577 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `11225.311` → IC=+0.160 (n=1566)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11225.311 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `471.0` → IC=+0.163 (n=1631)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 471.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=1515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.32` → IC=+0.161 (n=1513)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.32 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=690)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.2852` → IC=+0.236 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2852 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6688` → IC=+0.157 (n=240)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6688 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1325` → IC=+0.163 (n=1382)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1325 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.52` → IC=+0.164 (n=254)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.52 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.31` → IC=+0.153 (n=1376)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.31 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.163 (n=1513)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1917 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1509` → IC=+0.197 (n=404)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1509 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4071` → IC=+0.159 (n=1415)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4071 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.757` → IC=+0.161 (n=943)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.757 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `416.0` → IC=+0.153 (n=1161)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 416.0 (IC base=+0.150)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.254 (n=596)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=1871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=1811)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.343` → IC=+0.302 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.343 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1346` → IC=+0.219 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1346 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.6215` → IC=+0.227 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6215 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1918.06` → IC=+0.222 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1918.06 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.240 (n=1675)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1764` → IC=+0.241 (n=737)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1764 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0146` → IC=+0.306 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0146 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.756` → IC=+0.274 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.756 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3431` → IC=+0.299 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3431 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7422` → IC=+0.230 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7422 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1664` → IC=+0.239 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1664 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1909.088` → IC=+0.241 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1909.088 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.258 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.188 (n=824)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.004 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4307` → IC=+0.150 (n=1869)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4307 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=1947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.8741` → IC=+0.262 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8741 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.3615` → IC=+0.163 (n=714)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3615 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.174` → IC=+0.162 (n=774)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.174 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.156 (n=1246)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8725 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2798` → IC=+0.210 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2798 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5181` → IC=+0.154 (n=798)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5181 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4694` → IC=+0.156 (n=605)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4694 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7930.353` → IC=+0.237 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7930.353 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.173 (n=586)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 75.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.168 (n=1018)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0052 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4377` → IC=+0.146 (n=1524)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4377 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=705)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.1493` → IC=+0.261 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1493 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1587` → IC=+0.136 (n=1333)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1587 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.297` → IC=+0.161 (n=228)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.297 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.151 (n=671)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6973 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.2015` → IC=+0.137 (n=508)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.2015 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.234 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.145 (n=1451)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `7067.2817` → IC=+0.191 (n=691)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7067.2817 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `172.0` → IC=+0.137 (n=1446)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 172.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.139 (n=1243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0081 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1915)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.193 (n=1865)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4667 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0841` → IC=+0.203 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0841 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.54` → IC=+0.238 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.54 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8928` → IC=+0.140 (n=1244)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8928 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=1877)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2549.0292` → IC=+0.237 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2549.0292 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.135 (n=1453)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 53.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.176 (n=600)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0058 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1336` → IC=+0.157 (n=598)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1336 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.6389` → IC=+0.206 (n=1793)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6389 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.2221` → IC=+0.135 (n=1466)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2221 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.446` → IC=+0.127 (n=1730)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.446 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.7141` → IC=+0.157 (n=789)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7141 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2207` → IC=+0.170 (n=280)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2207 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4382` → IC=+0.143 (n=544)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4382 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2793.9248` → IC=+0.173 (n=598)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2793.9248 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.126 (n=1423)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 51.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.231 (n=1655)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=1935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.214 (n=1658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.262 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.2137` → IC=+0.233 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2137 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.264` → IC=+0.269 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.264 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2478` → IC=+0.215 (n=1852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2478 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.223 (n=1852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.252 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.505` → IC=+0.238 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.505 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2446.4744` → IC=+0.218 (n=1655)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2446.4744 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.219 (n=657)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.227 (n=657)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.216 (n=1380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.266 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `1.2288` → IC=+0.207 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2288 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2151` → IC=+0.211 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2151 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.848` → IC=+0.266 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.848 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.2355` → IC=+0.234 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2355 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.269 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.1803` → IC=+0.203 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1803 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.4285` → IC=+0.202 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4285 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=3380)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.184 (n=2957)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0092 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.5136` → IC=+0.181 (n=3357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.5136 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=1303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.177 (n=1518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.232 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.184` → IC=+0.182 (n=1217)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.184 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.4712` → IC=+0.168 (n=2117)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.4712 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.187` → IC=+0.198 (n=564)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.187 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.166 (n=982)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7053 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.8924` → IC=+0.175 (n=1487)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8924 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1706` → IC=+0.204 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1706 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.4558` → IC=+0.180 (n=1106)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4558 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6322` → IC=+0.183 (n=1105)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6322 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=2390)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `2846.5669` → IC=+0.174 (n=2999)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2846.5669 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.204 (n=850)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.4893` → IC=+0.171 (n=2547)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.4893 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.174 (n=1142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.1782` → IC=+0.181 (n=1121)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1782 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.6804` → IC=+0.176 (n=471)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.6804 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.208` → IC=+0.164 (n=2544)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.208 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2459` → IC=+0.158 (n=2395)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2459 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.159 (n=2318)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5399` → IC=+0.166 (n=1107)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5399 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.8256` → IC=+0.161 (n=1677)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8256 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=3380)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `5354.3412` → IC=+0.158 (n=2275)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 5354.3412 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.160 (n=1659)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 87.0 (IC base=+0.154)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.200 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.181 (n=374)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0033 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0869` → IC=+0.232 (n=140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0869 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.193 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 8.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5463` → IC=+0.205 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5463 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1455` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1455 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.3659` → IC=+0.189 (n=406)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.3659 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.174` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.174 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.187 (n=442)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.8402` → IC=+0.211 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8402 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.3007` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3007 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.211 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6311` → IC=+0.209 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6311 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `12550.0528` → IC=+0.220 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12550.0528 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.217 (n=425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.177 (n=320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.175 (n=367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1386` → IC=+0.179 (n=422)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1386 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6103` → IC=+0.148 (n=435)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6103 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6926` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6926 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.162 (n=939)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8795` → IC=+0.186 (n=641)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8795 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0682` → IC=+0.167 (n=448)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0682 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4209` → IC=+0.145 (n=319)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4209 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.151 (n=637)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `14911.0423` → IC=+0.161 (n=435)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 14911.0423 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `705.0` → IC=+0.145 (n=913)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 705.0 (IC base=+0.139)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.187 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.01 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.5756` → IC=+0.175 (n=625)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.5756 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` < `0.3498` → IC=+0.169 (n=751)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.3498 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2085` → IC=+0.201 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2085 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `3.3854` → IC=+0.166 (n=623)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3854 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.8279` → IC=+0.169 (n=557)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8279 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2427.507` → IC=+0.195 (n=283)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2427.507 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.318 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.250 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `0.4634` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4634 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` > `0.1043` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1043 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` < `2.564` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.564 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `4.0788` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 4.0788 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `2362.8582` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.8582 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.246)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.182 (n=926)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0072 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3764` → IC=+0.181 (n=926)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3764 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.183 (n=361)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 4.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.190 (n=702)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5305 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.8827` → IC=+0.183 (n=351)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8827 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.2121` → IC=+0.183 (n=874)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2121 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.178` → IC=+0.185 (n=940)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 4.178 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.176 (n=927)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0845 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6393` → IC=+0.177 (n=1053)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6393 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.194 (n=318)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.4736` → IC=+0.179 (n=1034)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.4736 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.176 (n=924)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=1049)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.202 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.4837` → IC=+0.184 (n=859)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4837 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.161 (n=605)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.7429` → IC=+0.162 (n=859)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.7429 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.0945` → IC=+0.164 (n=859)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.0945 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.6041` → IC=+0.172 (n=187)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6041 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.639` → IC=+0.163 (n=884)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.639 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.647` → IC=+0.196 (n=287)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.647 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.7253` → IC=+0.157 (n=768)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7253 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.176 (n=365)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.1996` → IC=+0.171 (n=742)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.1996 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `7861.9245` → IC=+0.177 (n=768)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7861.9245 (IC base=+0.157)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.161 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0109 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.165 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 7.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.139 (n=314)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 14.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.257 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.2209` → IC=+0.193 (n=216)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2209 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `1.3488` → IC=+0.138 (n=332)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 1.3488 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.097` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.097 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8864` → IC=+0.168 (n=209)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8864 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1626` → IC=+0.226 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1626 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5377` → IC=+0.144 (n=133)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5377 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.424` → IC=+0.156 (n=303)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.424 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=369)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3146.1978` → IC=+0.159 (n=312)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3146.1978 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.154 (n=258)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 54.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.180 (n=264)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0069 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.392` → IC=+0.193 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.392 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.179 (n=182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 10.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.1224` → IC=+0.247 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1224 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.6252` → IC=+0.235 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6252 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.281` → IC=+0.167 (n=256)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 5.281 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6777` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6777 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.221 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.6095` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.6095 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.1932` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.1932 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `3251.3358` → IC=+0.188 (n=264)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3251.3358 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.200 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.152)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.196 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=411)

- **FILTRO** `dist_vwap_pct` > `0.1778` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1778
  - _Potencial_: sin este filtro IC_bueno=+0.137 (n=378)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.169 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.079)

- **PATRÓN** `ibs_20min` > `0.6481` → IC=+0.185 (n=836)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.6481 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.1469` → IC=+0.143 (n=494)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1469 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.186 (n=218)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.191 (n=124)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.079)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.126 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0045 (IC base=+0.030)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.305 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.1778` → IC=+0.137 (n=378)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1778 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.187` → IC=+0.136 (n=127)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.187 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.236` → IC=+0.131 (n=280)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.236 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1368` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1368 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.5184` → IC=+0.145 (n=274)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.5184 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.437` → IC=+0.140 (n=245)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.437 (IC base=+0.030)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=284)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.030)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.143 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0058 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4669` → IC=+0.177 (n=323)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4669 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.0813` → IC=+0.145 (n=249)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.0813 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.137 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0044 (IC base=+0.076)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.160 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.297 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.0673` → IC=+0.148 (n=163)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.0673 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.585` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 4.585 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `1.1168` → IC=+0.136 (n=152)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1168 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.0669` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0669 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.174 (n=130)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.076)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=133)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.135 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0049 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.6606` → IC=+0.215 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6606 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.3347` → IC=+0.178 (n=119)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.3347 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.74` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.74 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` < `1.7387` → IC=+0.144 (n=175)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.7387 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `1125.4271` → IC=+0.146 (n=278)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1125.4271 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1283` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1283 (IC base=+0.012)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.258` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.258 (IC base=+0.012)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.558` → IC=+0.143 (n=82)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.558 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.3281` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.3281 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.1925` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.1925 (IC base=+0.012)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=92)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.012)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.265 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=96)

- **FILTRO** `ibs_20min` > `0.2051` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2051
  - _Potencial_: sin este filtro IC_bueno=+0.232 (n=69)

- **PATRÓN** `ibs_20min` > `0.6383` → IC=+0.142 (n=266)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6383 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.263` → IC=+0.123 (n=83)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 8.263 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2436` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2436 (IC base=+0.051)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.200 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.024)

- **PATRÓN** `ibs_20min` < `0.2051` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2051 (IC base=-0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5975 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.4883` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4883 (IC base=-0.024)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.297 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=151)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.365 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=173)

- **FILTRO** `dist_vwap_pct` > `0.166` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.166
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=200)

- **FILTRO** `volumen_regimen` < `0.7209` → IC=-0.342 (n=55)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7209
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=168)

- **FILTRO** `volumen_spike_ratio` > `3.0912` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.0912
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=112)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.357 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=121)

- **FILTRO** `hora_utc` < `4.0` → IC=-0.305 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=143)

- **FILTRO** `dist_vwap_pct` > `0.338` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.338
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=150)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=152)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=80)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.275 (n=38)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=39)

- **FILTRO** `sigma_h` < `0.0018` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **FILTRO** `dist_vwap_pct` < `0.0689` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0689
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=30)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7335` → IC=-0.446 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7335
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `volumen_regimen` > `1.108` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.108
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=53)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.389 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=49)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.375 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=60)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1679` → IC=-0.136 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1679
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=254)

- **FILTRO** `dist_vwap_pct` > `0.6344` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6344
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=358)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.148 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0058 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.641` → IC=+0.145 (n=277)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.641 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.4941` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4941 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.1679` → IC=+0.184 (n=254)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1679 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.105` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.105 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `3761.0521` → IC=+0.177 (n=131)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3761.0521 (IC base=+0.075)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=91)

- **FILTRO** `volumen_regimen` < `0.7924` → IC=-0.188 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7924
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=91)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.167 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0034 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2299` → IC=+0.152 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.2299 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.206 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.101` → IC=+0.214 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.101 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1936` → IC=+0.145 (n=153)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1936 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.611` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.611 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1443` → IC=+0.152 (n=133)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1443 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.196 (n=100)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.2899` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.2899 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.135)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6191` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6191
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=84)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.194 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0022 (IC base=+0.015)

- **PATRÓN** `ibs_20min` > `0.8782` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.8782 (IC base=+0.015)

- **PATRÓN** `libro_liquidez` > `1624.9844` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1624.9844 (IC base=+0.015)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.122 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0053 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.1644` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1644 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` < `0.8247` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.8247 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.0753` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0753 (IC base=+0.062)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=62)

- **FILTRO** `dist_vwap_pct` > `0.1415` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1415
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=57)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.218 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.231 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.236 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.212 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.6875` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6875 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.289 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.0812` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0812 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.216 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.036)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.282)

- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.397 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.282)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.7846` → IC=+0.338 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7846 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `1695.0` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1695.0 (IC base=+0.282)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.222)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.222)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.328 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.222)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.282)

- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.397 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.282)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.7846` → IC=+0.338 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7846 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `1695.0` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1695.0 (IC base=+0.282)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.222)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.222)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.328 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.222)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=790)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2904.8757` → IC=+0.165 (n=270)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2904.8757 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2444.7516` → IC=+0.123 (n=744)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2444.7516 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=790)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2904.8757` → IC=+0.165 (n=270)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2904.8757 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2444.7516` → IC=+0.123 (n=744)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2444.7516 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=139)

- **FILTRO** `libro_liquidez` < `11811.9773` → IC=-0.161 (n=116)

  - _Acción_: SKIP cuando `libro_liquidez` < 11811.9773
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=218)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=204)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=43)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=88)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1951)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=50)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=82)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=61)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=86)

- **PATRÓN** `libro_liquidez` > `2413.9166` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2413.9166 (IC base=+0.036)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35750.18` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `liq_usd_total` < 35750.18
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=144)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

- **FILTRO** `libro_liquidez` < `15247.5472` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 15247.5472
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `liq_n` > `18.0` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.014)

- **PATRÓN** `liq_usd_total` > `68754.71` → IC=+0.161 (n=107)

  - _Acción_: Kelly boost +0.80€ cuando `liq_usd_total` > 68754.71 (IC base=+0.014)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=146)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=849)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=803)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=441)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=205)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.495 (IC base=+0.016)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=664)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=664)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.145 (n=212)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=532)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=402)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=402)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=177)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=177)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=112)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=97)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=220)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=99)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=102)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=252)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=252)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.152 (n=67)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=215)

- **FILTRO** `libro_liquidez` < `516.7992` → IC=-0.121 (n=93)

  - _Acción_: SKIP cuando `libro_liquidez` < 516.7992
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=189)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=142)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.143 (n=340)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=846)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=123)

- **PATRÓN** `py_entrada` > `0.49` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.49 (IC base=+0.023)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.57` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.57 (IC base=+0.069)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.069)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=69)

- **FILTRO** `restante_min` > `13.27` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `restante_min` > 13.27
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=56)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.239 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=63)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=66)

- **FILTRO** `profundidad_ratio` < `22.1` → IC=-0.233 (n=28)

  - _Acción_: SKIP cuando `profundidad_ratio` < 22.1
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **FILTRO** `profundidad_ratio` < `79.8` → IC=-0.194 (n=47)

  - _Acción_: SKIP cuando `profundidad_ratio` < 79.8
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=48)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.53 (IC base=-0.036)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.46 (IC base=-0.009)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=102)

- **FILTRO** `restante_min` < `3.25` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `restante_min` < 3.25
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=96)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.250 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=89)

- **FILTRO** `lag_apertura_s` > `88.83` → IC=-0.300 (n=43)

  - _Acción_: SKIP cuando `lag_apertura_s` > 88.83
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=84)

- **FILTRO** `profundidad_ratio` < `76.0` → IC=-0.238 (n=63)

  - _Acción_: SKIP cuando `profundidad_ratio` < 76.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=64)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.44 (IC base=+0.064)

- **PATRÓN** `profundidad_ratio` > `24.5` → IC=+0.127 (n=73)

  - _Acción_: Kelly boost +0.63€ cuando `profundidad_ratio` > 24.5 (IC base=+0.064)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `restante_min` < `13.49` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `restante_min` < 13.49
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=26)

- **FILTRO** `lag_apertura_s` > `91.34` → IC=-0.152 (n=67)

  - _Acción_: SKIP cuando `lag_apertura_s` > 91.34
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=34)

- **PATRÓN** `restante_min` > `13.49` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 13.49 (IC base=-0.024)

- **PATRÓN** `lag_apertura_s` < `91.34` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 91.34 (IC base=-0.024)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 13.48 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `restante_min` < `3.75` → IC=-0.148 (n=52)

  - _Acción_: SKIP cuando `restante_min` < 3.75
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

- **FILTRO** `lag_apertura_s` > `74.79` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `lag_apertura_s` > 74.79
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=54)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.46 (IC base=+0.028)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.135 (n=94)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=54)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.5 (IC base=-0.027)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.255 (n=51)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=121)

- **FILTRO** `restante_min` < `2.81` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `restante_min` < 2.81
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=129)

- **FILTRO** `profundidad_ratio` < `6.1` → IC=-0.182 (n=42)

  - _Acción_: SKIP cuando `profundidad_ratio` < 6.1
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=130)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7798)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.168 (n=3809)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=11728)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.160 (n=3961)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=12169)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.465` → IC=-0.202 (n=679)

  - _Acción_: SKIP cuando `py_entrada` < 0.465
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=2037)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.187 (n=681)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2085)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=695)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2207)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.172 (n=668)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=2042)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.171 (n=719)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=2184)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2222)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2318)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3058)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=409)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=400)

- **FILTRO** `libro_liquidez` < `17011.7455` → IC=-0.143 (n=228)

  - _Acción_: SKIP cuando `libro_liquidez` < 17011.7455
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=685)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `hora_utc` > `18.0` → IC=-0.146 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.126 (n=263)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.214 (n=82)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=261)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=230)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.134 (n=10972)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=24361)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=8750)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=26583)

- **FILTRO** `ibs_7min` < `0.2742` → IC=-0.235 (n=8832)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2742
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=26501)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=11847)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=23486)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.231 (n=10913)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=33705)

- **FILTRO** `ibs_7min` > `0.2913` → IC=-0.178 (n=11154)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2913
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=33464)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=1790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4104)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=1401)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4493)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.253 (n=1944)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3950)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.175 (n=1451)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4443)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.260 (n=1900)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=5767)

- **FILTRO** `ibs_7min` > `0.7889` → IC=-0.206 (n=1916)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7889
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=5751)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=4648)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1482)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4603)

- **FILTRO** `ibs_7min` < `0.7462` → IC=-0.195 (n=1521)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7462
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=4564)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.178 (n=1521)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4564)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=1424)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4760)

- **FILTRO** `ibs_7min` > `0.2609` → IC=-0.184 (n=1542)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4642)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.180 (n=1539)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4645)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.169 (n=1586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=4025)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=1309)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4302)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.243 (n=1851)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3760)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.210 (n=1391)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4220)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=1898)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=6328)

- **FILTRO** `ibs_7min` > `0.7465` → IC=-0.175 (n=2056)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7465
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=6170)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.198 (n=2776)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=3045)

- **FILTRO** `ibs_7min` < `0.7412` → IC=-0.183 (n=1455)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7412
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4366)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.174 (n=1415)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=4406)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.256 (n=1491)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=4484)

- **FILTRO** `ibs_7min` > `0.2753` → IC=-0.178 (n=1493)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2753
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4482)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.183 (n=1480)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4495)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.263 (n=1424)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4671)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.234 (n=1523)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=4572)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.168 (n=2123)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=6387)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=1432)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4395)

- **FILTRO** `ibs_7min` < `0.2903` → IC=-0.224 (n=1456)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2903
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4371)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1388)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4439)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.207 (n=1886)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=6170)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1145)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=568)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=331)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=572)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.130 (n=803)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `471.727` → IC=+0.141 (n=268)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 471.727 (IC base=+0.115)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.135 (n=61)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.197 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.136 (n=160)

  - _Acción_: Kelly boost +0.68€ cuando `total_vol_5m` < 445.688 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `2333.2912` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2333.2912 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 14.0 (IC base=+0.131)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 11.0 (IC base=+0.104)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.175 (n=112)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.124 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 4.0 (IC base=+0.098)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 75.0 (IC base=+0.098)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.181 (n=139)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.235 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `6163.256` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 6163.256 (IC base=+0.136)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.133 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 13.0 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.104)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.295 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=209)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `54.581` → IC=-0.315 (n=63)

  - _Acción_: SKIP cuando `T_h` > 54.581
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=65)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.115)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.013` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=58)

- **FILTRO** `T_h` < `39.9918` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `T_h` < 39.9918
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=58)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.166 (n=309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=104)

- **FILTRO** `sigma_h` > `0.0095` → IC=-0.322 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=267)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.322 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=267)

- **FILTRO** `T_h` > `61.3303` → IC=-0.321 (n=266)

  - _Acción_: SKIP cuando `T_h` > 61.3303
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=89)

- **PATRÓN** `pct_vs_K` |x|≤ `1.0667` → IC=+0.189 (n=104)

  - _Acción_: Kelly boost +0.94€ cuando `pct_vs_K` |x|≤ 1.0667 (IC base=-0.117)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.004` → IC=-0.158 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=109)

- **FILTRO** `T_h` > `79.6334` → IC=-0.146 (n=97)

  - _Acción_: SKIP cuando `T_h` > 79.6334
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

- **FILTRO** `pct_vs_K` |x|> `2.84` → IC=-0.368 (n=36)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.84
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=109)

- **FILTRO** `pct_vs_K` |x|> `2.9509` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9509
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=88)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.4229` → IC=-0.357 (n=54)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4229
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.328 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=84)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=84)

- **FILTRO** `T_h` > `60.9515` → IC=-0.329 (n=74)

  - _Acción_: SKIP cuando `T_h` > 60.9515
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3415` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3415 (IC base=-0.203)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0073` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=75)

- **FILTRO** `T_h` > `132.7892` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `T_h` > 132.7892
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=67)

- **FILTRO** `pct_vs_K` |x|> `4.8556` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.8556
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=76)

- **FILTRO** `sigma_h` < `0.0146` → IC=-0.375 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0146
  - _Potencial_: sin este filtro IC_bueno=-0.315 (n=25)

- **FILTRO** `T_h` > `58.2361` → IC=-0.373 (n=53)

  - _Acción_: SKIP cuando `T_h` > 58.2361
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=18)

- **PATRÓN** `pct_vs_K` |x|≤ `1.14` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.14 (IC base=-0.039)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1186` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1186 (IC base=+0.378)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.407 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.378)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.427 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.378)

- **PATRÓN** `T_h` > `0.4704` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4704 (IC base=+0.378)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.378)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.378)

- **PATRÓN** `edge` > `0.1135` → IC=+0.458 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1135 (IC base=+0.419)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.419)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.443 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.419)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.419)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.463 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.419)

- **PATRÓN** `dist_50` > `0.4092` → IC=+0.481 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4092 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.473 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.419)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1078` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1078 (IC base=+0.414)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.400 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.414)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.414)

- **PATRÓN** `T_h` < `0.9168` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9168 (IC base=+0.414)

- **PATRÓN** `dist_50` > `0.4178` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4178 (IC base=+0.414)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.429 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.414)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.472 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.464)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.446 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.464)

- **PATRÓN** `T_h` > `0.8497` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8497 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.464 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.464 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

- **PATRÓN** `edge` > `0.1155` → IC=+0.469 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.486 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.462)

- **PATRÓN** `T_h` > `0.8977` → IC=+0.469 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8977 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.4948` → IC=+0.486 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4948 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.467 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=202)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=308)

- **FILTRO** `streak_estiramiento` > `0.8566` → IC=-0.162 (n=66)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8566
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=201)

- **PATRÓN** `streak_estiramiento` < `0.4787` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.4787 (IC base=+0.034)

- **PATRÓN** `streak_estiramiento` < `0.7314` → IC=+0.120 (n=177)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.7314 (IC base=+0.035)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=19)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `2331737.7` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 2331737.7
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=46)

- **FILTRO** `streak_estiramiento` > `0.479` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.479
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=37)

- **PATRÓN** `streak_estiramiento` < `0.479` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.479 (IC base=-0.008)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.121 (n=93)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 49.0 (IC base=+0.053)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=88)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=32)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=797)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=803)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=430)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `libro_liquidez` < `2775.6672` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 2775.6672
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `streak_estiramiento` > `0.9124` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.9124
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=660)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1214)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=815)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=789)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3074)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1560)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1568)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.193 (n=598)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0043 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.226 (n=599)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.202 (n=598)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.187)

- **PATRÓN** `delta_ratio_macro` |x|> `0.217` → IC=+0.191 (n=597)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.217 (IC base=+0.187)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.234 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=1680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=1863)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_15` > `0.6099` → IC=+0.267 (n=1792)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6099 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.183 (n=898)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.6065` → IC=+0.179 (n=1701)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.6065 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.822` → IC=+0.275 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.822 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `8758.4418` → IC=+0.195 (n=598)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 8758.4418 (IC base=+0.187)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=733)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.221 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.285 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.207)

- **PATRÓN** `drift_15min` |x|≤ `0.3839` → IC=+0.211 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3839 (IC base=+0.207)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.246 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.207)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.280 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_15` > `0.7077` → IC=+0.274 (n=396)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7077 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.265 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.537` → IC=+0.272 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.537 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `16060.5409` → IC=+0.231 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16060.5409 (IC base=+0.207)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.849` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.849
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=449)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6586` → IC=-0.122 (n=183)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6586
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=374)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.169 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0035 (IC base=+0.130)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.135 (n=280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.005 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.161 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.176 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.130)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.165 (n=153)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.130 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 16.0 (IC base=+0.130)

- **PATRÓN** `ibs_15` > `0.6586` → IC=+0.253 (n=374)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6586 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1135` → IC=+0.147 (n=301)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1135 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.257` → IC=+0.221 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.257 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `4165.118` → IC=+0.141 (n=279)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 4165.118 (IC base=+0.130)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.281 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.1481` → IC=+0.195 (n=188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1481 (IC base=+0.171)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0606` → IC=+0.188 (n=213)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.0606 (IC base=+0.171)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.216 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.255 (n=214)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.177 (n=122)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.175 (n=207)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.286` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.286 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=154)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3071.8702` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3071.8702 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.213 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.171)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.688` → IC=-0.157 (n=103)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.688
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=1109)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=-0.003)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.271 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.225 (n=205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.196)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0403` → IC=+0.200 (n=465)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0403 (IC base=+0.196)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.260 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `ibs_15` > `0.5695` → IC=+0.286 (n=465)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5695 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.3546` → IC=+0.209 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3546 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` < `0.8342` → IC=+0.199 (n=539)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.8342 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.251` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.251 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.374` → IC=+0.199 (n=423)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 7.374 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2911.0954` → IC=+0.283 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.0954 (IC base=+0.196)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.150 (n=524)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1176 (IC base=+0.053)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.356 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.350)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.373 (n=148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.350)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.353 (n=297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.350)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.363 (n=443)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.350)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.388 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.350)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.369 (n=449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.350)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.390 (n=444)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.350)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.388 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.350)

- **PATRÓN** `dist_vwap_pct` < `0.1081` → IC=+0.351 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1081 (IC base=+0.350)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.247` → IC=+0.356 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.247 (IC base=+0.350)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.350 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.350)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.354 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.350)

- **PATRÓN** `libro_liquidez` > `3397.72` → IC=+0.361 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3397.72 (IC base=+0.350)

- **PATRÓN** `ballena_activa_n` < `459.0` → IC=+0.371 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 459.0 (IC base=+0.350)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.362 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.381 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.369 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.354)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.364 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0763` → IC=+0.362 (n=245)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0763 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1241` → IC=+0.394 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1241 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.380 (n=247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.387 (n=246)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.405 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.360 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.357 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `11121.9309` → IC=+0.373 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11121.9309 (IC base=+0.354)

- **PATRÓN** `ballena_activa_n` < `571.0` → IC=+0.400 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 571.0 (IC base=+0.354)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.341 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.342)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.380 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.342)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.352 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.367 (n=178)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.342)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.368 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.342)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.405 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.342)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.395 (n=198)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.375 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` < `0.1175` → IC=+0.355 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1175 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.345 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.342)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.349 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.342)

- **PATRÓN** `libro_liquidez` > `3456.6166` → IC=+0.351 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3456.6166 (IC base=+0.342)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.353 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.342)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.224 (n=708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2127)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=983)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1852)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.251 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.068)

- **PATRÓN** `ibs_15` > `0.6409` → IC=+0.271 (n=675)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6409 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.189 (n=545)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2675 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0771` → IC=+0.246 (n=1792)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0771 (IC base=-0.028)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1797` → IC=+0.242 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1797 (IC base=-0.028)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.274 (n=2006)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.6798` → IC=+0.300 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6798 (IC base=-0.028)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.214 (n=428)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=1285)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.223 (n=565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1148)

- **FILTRO** `sigma_ewma_delta_pct` > `19.563` → IC=-0.256 (n=305)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.563
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1408)

- **FILTRO** `libro_liquidez` < `16352.3518` → IC=-0.201 (n=1130)

  - _Acción_: SKIP cuando `libro_liquidez` < 16352.3518
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=583)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.159 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0028 (IC base=+0.079)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2051` → IC=+0.267 (n=88)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2051 (IC base=+0.079)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1066` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1066 (IC base=+0.079)

- **PATRÓN** `ibs_15` > `0.7497` → IC=+0.330 (n=192)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7497 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.099` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.099 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.3585` → IC=+0.272 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3585 (IC base=+0.079)

- **PATRÓN** `ibs_15` < `0.213` → IC=+0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.213 (IC base=-0.198)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=409)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.149 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0068 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.170 (n=286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.004 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.220 (n=141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.147)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.233 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.6647` → IC=+0.258 (n=320)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6647 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.178 (n=231)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.042` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 14.042 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.009` → IC=+0.149 (n=274)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 9.009 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=409)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `11052.2058` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 11052.2058 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.248 (n=772)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.3569` → IC=+0.242 (n=679)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3569 (IC base=+0.235)

- **PATRÓN** `drift_15min` |x|≤ `0.4747` → IC=+0.260 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4747 (IC base=+0.235)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2071` → IC=+0.261 (n=350)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2071 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.247 (n=299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.235)

- **PATRÓN** `ibs_15` < `0.2722` → IC=+0.281 (n=679)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2722 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.7494` → IC=+0.329 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7494 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.827` → IC=+0.250 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.827 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.283` → IC=+0.243 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.283 (IC base=+0.235)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.257 (n=167)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=504)

- **FILTRO** `drift_15min` |x|> `0.8925` → IC=-0.269 (n=167)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8925
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=504)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=270)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=401)

- **FILTRO** `sigma_ewma_delta_pct` > `18.215` → IC=-0.139 (n=358)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.215
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2881)

- **PATRÓN** `ibs_15` > `0.9` → IC=+0.309 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9 (IC base=-0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0776` → IC=+0.229 (n=308)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0776 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.258 (n=345)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7501` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7501 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1863` → IC=+0.224 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1863 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.259 (n=409)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=411)

- **FILTRO** `sigma_ewma_delta_pct` > `7.05` → IC=-0.207 (n=254)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.05
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=566)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.260 (n=215)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=605)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1379` → IC=+0.300 (n=238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1379 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1078` → IC=+0.334 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1078 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3391` → IC=+0.305 (n=525)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3391 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.8999` → IC=+0.340 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8999 (IC base=-0.039)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.048)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.048)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.302 (n=478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.330 (n=239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.306 (n=240)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.337 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8405` → IC=+0.327 (n=716)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8405 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.337 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.348 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.291 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `14493.8191` → IC=+0.297 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14493.8191 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.293 (n=346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.287 (n=350)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.342 (n=131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2605` → IC=+0.304 (n=131)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2605 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3917` → IC=+0.312 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3917 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.317 (n=392)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.367 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.327 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.314 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.304 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.303 (n=216)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3017` → IC=+0.324 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3017 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.341 (n=324)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.4471` → IC=+0.302 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4471 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` < `0.1631` → IC=+0.294 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1631 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.334 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.299 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.162 (n=72)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=217)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.134 (n=192)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=65)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.121` → IC=-0.173 (n=111)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.121
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=336)

- **FILTRO** `ballena_activa_n` > `56.0` → IC=-0.208 (n=46)

  - _Acción_: SKIP cuando `ballena_activa_n` > 56.0
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=140)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1232` → IC=-0.159 (n=42)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1232
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=129)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1681` → IC=-0.250 (n=22)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1681
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0943` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0943
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.2131` → IC=-0.231 (n=24)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2131
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1195` → IC=-0.206 (n=15)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1195
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.3593` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3593
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3119` → IC=-0.184 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3119
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `79.068` → IC=+0.219 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.068 (IC base=+0.205)

- **PATRÓN** `ratio` < `0.9779` → IC=+0.467 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9779 (IC base=+0.205)

- **PATRÓN** `T_h` > `145.7688` → IC=+0.395 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7688 (IC base=+0.330)

- **PATRÓN** `ratio` > `1.0559` → IC=+0.420 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0559 (IC base=+0.330)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `121.3227` → IC=+0.220 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 121.3227 (IC base=+0.185)

- **PATRÓN** `ratio` < `0.973` → IC=+0.448 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.185)

- **PATRÓN** `T_h` > `102.8316` → IC=+0.289 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 102.8316 (IC base=+0.279)

- **PATRÓN** `ratio` > `1.0467` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0467 (IC base=+0.279)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `93.6267` → IC=+0.278 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 93.6267 (IC base=+0.241)

- **PATRÓN** `ratio` < `0.9949` → IC=+0.382 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9949 (IC base=+0.241)

- **PATRÓN** `T_h` > `105.6124` → IC=+0.325 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 105.6124 (IC base=+0.309)

- **PATRÓN** `ratio` > `1.012` → IC=+0.321 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.309)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1332` → IC=+0.459 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1332 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6099 sube el IC de +0.187 a +0.267 en UPDOWN_GBM#15min (n=1792). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7077 sube el IC de +0.207 a +0.274 en UPDOWN_GBM#BTC#15min (n=396). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6586 sube el IC de +0.130 a +0.253 en UPDOWN_GBM#ETH#15min (n=374). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.171 a +0.255 en UPDOWN_GBM#SOL#15min (n=214). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5695 sube el IC de +0.196 a +0.286 en UPDOWN_GBM#XRP#15min (n=465). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.053 a +0.150 en UPDOWN_GBM#XRP#15min (n=524). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6409 sube el IC de -0.068 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=675). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.028 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=2006). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7497 sube el IC de +0.079 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=192). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.213 sube el IC de -0.198 a +0.382 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.147 a +0.258 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=320). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2722 sube el IC de +0.235 a +0.281 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=679). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9 sube el IC de -0.175 a +0.309 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.042 a +0.258 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=345). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3391 sube el IC de -0.039 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8405 sube el IC de +0.291 a +0.327 en UPDOWN_GBM_IBS_ALTO (n=716). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.286 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=392). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.295 a +0.341 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=324). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.350 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=444). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.354 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.342 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=198). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1390 | +0.101 | +198.78€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1390 | +0.101 | +198.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 27 | +0.017 | -3.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 27 | +0.017 | -3.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1048 | +0.111 | +172.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1048 | +0.111 | +172.76€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 29856 | -0.083 | -3987.18€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1572 | -0.029 | -215.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 28284 | -0.086 | -3771.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3887 | -0.097 | -648.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3887 | -0.097 | -648.98€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1572 | -0.029 | -215.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1572 | -0.029 | -215.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3521 | -0.098 | -805.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3521 | -0.098 | -805.40€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7713 | -0.014 | -730.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7713 | -0.014 | -730.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7303 | -0.088 | -471.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7303 | -0.088 | -471.06€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5860 | -0.162 | -1115.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5860 | -0.162 | -1115.56€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 20509 | -0.025 | +3878.49€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5313 | +0.001 | +1795.68€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 15196 | -0.034 | +2082.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 20509 | -0.025 | +3878.49€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5313 | +0.001 | +1795.68€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 15196 | -0.034 | +2082.81€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1478 | -0.103 | -191.97€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 780 | -0.091 | -97.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 144 | -0.048 | -16.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 100062 | +0.113 | -4827.52€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14772 | +0.185 | -445.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 409 | -0.069 | -51.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 78485 | +0.101 | -4112.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6396 | +0.107 | -218.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 13046 | +0.099 | -1047.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 48 | -0.160 | +1.58€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 12983 | +0.101 | -1037.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 20155 | +0.132 | -348.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4628 | +0.202 | -134.75€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 13014 | +0.114 | -160.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2471 | +0.100 | -30.71€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13084 | +0.091 | -1160.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 54 | -0.107 | -8.00€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 13015 | +0.092 | -1140.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 21253 | +0.124 | -382.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5766 | +0.176 | -73.65€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13158 | +0.106 | -237.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2317 | +0.099 | -62.98€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 19467 | +0.114 | -1118.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4227 | +0.188 | -239.76€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 312 | -0.029 | +2.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13320 | +0.092 | -756.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1608 | +0.130 | -124.99€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13057 | +0.100 | -771.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 49 | -0.029 | +9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 12995 | +0.101 | -780.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 15882 | +0.193 | -1022.47€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 15882 | +0.193 | -1022.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3757 | +0.167 | -394.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3757 | +0.167 | -394.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1458 | +0.203 | -7.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1458 | +0.203 | -7.92€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3697 | +0.180 | -314.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3697 | +0.180 | -314.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3262 | +0.241 | -103.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3262 | +0.241 | -103.62€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3629 | +0.193 | -215.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3629 | +0.193 | -215.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 748 | +0.428 | -23.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 748 | +0.428 | -23.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 291 | +0.439 | -2.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 291 | +0.439 | -2.35€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 283 | +0.426 | -9.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 283 | +0.426 | -9.29€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 164 | +0.410 | -9.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 164 | +0.410 | -9.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 54899 | +0.198 | -4268.29€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 54899 | +0.198 | -4268.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9472 | +0.178 | -1076.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9472 | +0.178 | -1076.56€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8783 | +0.223 | -321.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8783 | +0.223 | -321.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9476 | +0.174 | -1107.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9476 | +0.174 | -1107.67€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8880 | +0.217 | -364.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8880 | +0.217 | -364.92€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9079 | +0.203 | -596.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9079 | +0.203 | -596.57€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9209 | +0.193 | -801.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9209 | +0.193 | -801.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 20779 | +0.117 | +175.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 20779 | +0.117 | +175.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10318 | +0.121 | +135.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10318 | +0.121 | +135.42€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10461 | +0.114 | +39.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10461 | +0.114 | +39.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1560 | +0.287 | -26.54€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1560 | +0.287 | -26.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 698 | +0.277 | -19.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 698 | +0.277 | -19.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 749 | +0.287 | -9.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 749 | +0.287 | -9.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 113 | +0.344 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 113 | +0.344 | +2.86€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 692 | +0.434 | -6.87€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 692 | +0.434 | -6.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 331 | +0.431 | -5.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 331 | +0.431 | -5.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 316 | +0.437 | -1.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 316 | +0.437 | -1.54€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1189 | +0.064 | -68.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 419 | +0.044 | -45.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 770 | +0.075 | -23.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 62 | +0.109 | +2.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 62 | +0.109 | +2.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 938 | +0.072 | -33.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 168 | +0.059 | -10.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 770 | +0.075 | -23.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 189 | +0.008 | -36.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 189 | +0.008 | -36.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 38984 | +0.098 | -1104.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3201 | +0.089 | +24.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 35783 | +0.099 | -1129.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 21788 | +0.103 | -310.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3201 | +0.089 | +24.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 18587 | +0.105 | -335.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7467 | +0.110 | -10.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7467 | +0.110 | -10.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9729 | +0.080 | -783.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9729 | +0.080 | -783.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 846 | +0.216 | -101.25€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 846 | +0.216 | -101.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 846 | +0.216 | -101.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 846 | +0.216 | -101.25€ | 1 | 4 |
| ✅ GBM_LATE_15M | 27705 | +0.085 | +13486.69€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 27705 | +0.085 | +13486.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4629 | +0.197 | +3449.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4629 | +0.197 | +3449.09€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 4119 | +0.178 | +2940.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4119 | +0.178 | +2940.99€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 4869 | +0.198 | +3637.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4869 | +0.198 | +3637.96€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4010 | +0.026 | +938.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4010 | +0.026 | +938.63€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 3954 | -0.032 | +919.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3954 | -0.032 | +919.45€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6124 | -0.039 | +1600.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6124 | -0.039 | +1600.57€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 29475 | +0.086 | +15546.43€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 29475 | +0.086 | +15546.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5607 | +0.012 | +2949.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5607 | +0.012 | +2949.61€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6156 | +0.015 | +1306.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6156 | +0.015 | +1306.31€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4192 | +0.264 | +4257.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4192 | +0.264 | +4257.10€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4851 | +0.005 | +957.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4851 | +0.005 | +957.40€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4760 | +0.030 | +1855.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4760 | +0.030 | +1855.71€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3909 | +0.279 | +4220.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3909 | +0.279 | +4220.31€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 22234 | +0.170 | +16866.53€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 22234 | +0.170 | +16866.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3352 | +0.209 | +2699.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3352 | +0.209 | +2699.88€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3497 | +0.150 | +2592.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3497 | +0.150 | +2592.18€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3507 | +0.209 | +2804.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3507 | +0.209 | +2804.35€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3723 | +0.134 | +2646.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3723 | +0.134 | +2646.47€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4162 | +0.118 | +2950.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4162 | +0.118 | +2950.13€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3993 | +0.205 | +3173.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3993 | +0.205 | +3173.51€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5790 | +0.136 | +2630.62€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5790 | +0.136 | +2630.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1620 | +0.134 | +799.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1620 | +0.134 | +799.30€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1737 | +0.151 | +827.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1737 | +0.151 | +827.16€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1341 | +0.119 | +524.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1341 | +0.119 | +524.82€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 27870 | +0.177 | +21123.45€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 27870 | +0.177 | +21123.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4413 | +0.224 | +3790.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4413 | +0.224 | +3790.28€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4354 | +0.152 | +2922.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4354 | +0.152 | +2922.45€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4614 | +0.226 | +3977.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4614 | +0.226 | +3977.40€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4522 | +0.136 | +3120.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4522 | +0.136 | +3120.19€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4876 | +0.116 | +3223.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4876 | +0.116 | +3223.48€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5091 | +0.209 | +4089.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5091 | +0.209 | +4089.65€ | 0 | 24 |
| ✅ GBM_LATE_5M | 7870 | +0.164 | +4967.04€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 7870 | +0.164 | +4967.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 810 | +0.223 | +688.00€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 810 | +0.223 | +688.00€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1834 | +0.152 | +1234.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1834 | +0.152 | +1234.95€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 893 | +0.170 | +564.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 893 | +0.170 | +564.35€ | 0 | 21 |
| ✅ GBM_LATE_5M#ETH | 2548 | +0.166 | +1586.91€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2548 | +0.166 | +1586.91€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 768 | +0.144 | +396.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 768 | +0.144 | +396.42€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1017 | +0.140 | +496.41€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1017 | +0.140 | +496.41€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1916 | +0.065 | +717.52€ | 2 | 14 |
| ✅ GBM_LATE_60M#60min | 1916 | +0.065 | +717.52€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 705 | +0.088 | +256.96€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 705 | +0.088 | +256.96€ | 0 | 12 |
| ✅ GBM_LATE_60M#ETH | 629 | +0.069 | +286.69€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 629 | +0.069 | +286.69€ | 1 | 16 |
| ✅ GBM_LATE_60M#SOL | 582 | +0.033 | +173.86€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 582 | +0.033 | +173.86€ | 2 | 9 |
| 🚫 GBM_LATE_60M_FADE | 405 | -0.259 | -24.88€ | 10 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 405 | -0.259 | -24.88€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 151 | -0.226 | -8.14€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 151 | -0.226 | -8.14€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 135 | -0.259 | -8.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 135 | -0.259 | -8.36€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 119 | -0.293 | -8.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 119 | -0.293 | -8.38€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 753 | +0.077 | +174.73€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 753 | +0.077 | +174.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 297 | +0.069 | +60.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 297 | +0.069 | +60.86€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 227 | +0.042 | +13.76€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 227 | +0.042 | +13.76€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 229 | +0.123 | +100.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 229 | +0.123 | +100.11€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 105 | +0.257 | +87.77€ | 0 | 10 |
| ✅ LATE_WINDOW_5MIN#5min | 105 | +0.257 | +87.77€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 105 | +0.257 | +87.77€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 105 | +0.257 | +87.77€ | 0 | 10 |
| ✅ LEADLAG_BTC_XRP_15M | 2188 | +0.105 | +602.11€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2188 | +0.105 | +602.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2188 | +0.105 | +602.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2188 | +0.105 | +602.11€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 394 | -0.076 | -33.23€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 394 | -0.076 | -33.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 101 | -0.053 | -4.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 101 | -0.053 | -4.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 144 | -0.021 | -4.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 144 | -0.021 | -4.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2150 | +0.008 | +20.47€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2150 | +0.008 | +20.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 116 | +0.017 | -2.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 116 | +0.017 | -2.94€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 249 | -0.014 | +9.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 249 | -0.014 | +9.33€ | 5 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 174 | -0.028 | -6.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 174 | -0.028 | -6.39€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 896 | +0.022 | +21.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 896 | +0.022 | +21.06€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 481 | +0.005 | -2.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 481 | +0.005 | -2.37€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 234 | +0.004 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 234 | +0.004 | +1.79€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M | 1161 | -0.043 | -27.28€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1161 | -0.043 | -27.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 328 | -0.045 | -14.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 328 | -0.045 | -14.40€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 394 | -0.025 | -0.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 394 | -0.025 | -0.33€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 439 | -0.058 | -12.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 439 | -0.058 | -12.55€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 2289 | -0.018 | +49.54€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1098 | -0.014 | +33.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1191 | -0.022 | +16.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 68 | +0.014 | +6.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 38 | +0.075 | +9.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 30 | -0.062 | -3.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 536 | +0.011 | +44.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 253 | +0.014 | +17.93€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 283 | +0.009 | +26.98€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 298 | -0.040 | -4.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 147 | -0.064 | -8.74€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 151 | -0.016 | +4.16€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 434 | -0.034 | -14.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 199 | -0.022 | -1.46€ | 3 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 235 | -0.044 | -13.09€ | 5 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 422 | -0.009 | +20.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 211 | -0.012 | +12.04€ | 2 | 3 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 211 | -0.007 | +8.26€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 531 | -0.033 | -2.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 250 | -0.020 | +3.80€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 281 | -0.044 | -6.76€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 31667 | -0.006 | +1413.45€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 31667 | -0.006 | +1413.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5597 | +0.019 | +690.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5597 | +0.019 | +690.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4843 | -0.030 | -63.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4843 | -0.030 | -63.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5668 | +0.015 | +497.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5668 | +0.015 | +497.40€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4627 | -0.053 | -147.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4627 | -0.053 | -147.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5319 | -0.009 | +209.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5319 | -0.009 | +209.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5613 | +0.009 | +227.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5613 | +0.009 | +227.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5998 | -0.060 | -147.06€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5998 | -0.060 | -147.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1445 | -0.084 | -40.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1445 | -0.084 | -40.56€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 677 | -0.121 | -28.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 677 | -0.121 | -28.69€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1761 | -0.078 | -33.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1761 | -0.078 | -33.59€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 79951 | -0.073 | +1741.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 79951 | -0.073 | +1741.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 13561 | -0.077 | +814.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 13561 | -0.077 | +814.91€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12269 | -0.095 | -617.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12269 | -0.095 | -617.64€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 13837 | -0.067 | +739.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 13837 | -0.067 | +739.17€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 11796 | -0.093 | -222.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 11796 | -0.093 | -222.82€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 14605 | -0.048 | +398.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 14605 | -0.048 | +398.06€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 13883 | -0.063 | +629.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 13883 | -0.063 | +629.87€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7781 | -0.027 | -134.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7781 | -0.027 | -134.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1774 | -0.035 | -14.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1774 | -0.035 | -14.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2197 | -0.022 | -25.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2197 | -0.022 | -25.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1060 | -0.045 | -20.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1060 | -0.045 | -20.58€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 751 | -0.019 | -22.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 751 | -0.019 | -22.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1205 | +0.109 | +411.14€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1069 | +0.115 | +398.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 242 | +0.131 | +114.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 242 | +0.131 | +114.58€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 205 | +0.104 | +54.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 205 | +0.104 | +54.58€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 222 | +0.098 | +75.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 222 | +0.098 | +75.75€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 185 | +0.136 | +88.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 185 | +0.136 | +88.57€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 215 | +0.104 | +65.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 215 | +0.104 | +65.07€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 601 | -0.049 | -56.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 601 | -0.049 | -56.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 122 | -0.016 | +0.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 122 | -0.016 | +0.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 80 | -0.098 | -16.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 80 | -0.098 | -16.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 176 | -0.056 | -23.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 176 | -0.056 | -23.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 121 | -0.029 | -5.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 121 | -0.029 | -5.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 102 | -0.058 | -10.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 102 | -0.058 | -10.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 611 | -0.112 | -55.61€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 280 | -0.163 | -67.41€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 227 | -0.203 | -68.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 53 | +0.009 | +0.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 212 | -0.075 | -0.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 162 | -0.079 | -6.75€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 50 | -0.058 | +6.23€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 119 | -0.054 | +12.32€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 95 | -0.077 | +6.09€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 24 | +0.038 | +6.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 484 | -0.138 | -68.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 127 | -0.012 | +13.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 768 | -0.200 | -32.29€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 319 | -0.198 | -28.83€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 278 | -0.196 | -29.04€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 41 | -0.198 | +0.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 262 | -0.216 | -23.30€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 227 | -0.225 | -28.39€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 35 | -0.149 | +5.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 187 | -0.177 | +19.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 171 | -0.176 | +15.17€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 676 | -0.202 | -42.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 92 | -0.181 | +9.98€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 320 | +0.410 | +239.73€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 32 | +0.088 | -2.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 32 | +0.088 | -2.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 81 | +0.380 | +59.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 81 | +0.380 | +59.35€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 207 | +0.467 | +182.96€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 207 | +0.467 | +182.96€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 320 | +0.410 | +239.73€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 548 | +0.035 | +19.57€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 548 | +0.035 | +19.57€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 263 | +0.036 | +7.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 263 | +0.036 | +7.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 57 | -0.009 | -1.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 57 | -0.009 | -1.59€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 191 | +0.034 | +10.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 191 | +0.034 | +10.66€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2843 | -0.021 | -113.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2843 | -0.021 | -113.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 828 | -0.017 | -25.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 828 | -0.017 | -25.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 572 | -0.023 | -23.22€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 572 | -0.023 | -23.22€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1287 | -0.021 | -49.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1287 | -0.021 | -49.62€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 76 | -0.051 | -6.76€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 76 | -0.051 | -6.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 38 | +0.000 | -2.32€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 38 | +0.000 | -2.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8415 | +0.023 | +125.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8415 | +0.023 | +125.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2300 | +0.024 | +30.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2300 | +0.024 | +30.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1905 | +0.032 | +51.50€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1905 | +0.032 | +51.50€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2564 | +0.013 | +6.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2564 | +0.013 | +6.04€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1646 | +0.027 | +37.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1646 | +0.027 | +37.29€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7727 | +0.014 | -31.06€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7727 | +0.014 | -31.06€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3093 | +0.017 | -6.95€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3093 | +0.017 | -6.95€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3042 | +0.014 | -12.77€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3042 | +0.014 | -12.77€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1592 | +0.008 | -11.35€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1592 | +0.008 | -11.35€ | 2 | 0 |
| ✅ UPDOWN_GBM | 42624 | +0.034 | +2715.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11208 | +0.071 | +2101.28€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1528 | +0.004 | +5.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 27149 | +0.025 | +590.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2581 | +0.001 | +20.30€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4374 | +0.074 | +529.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 789 | +0.160 | +340.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3552 | +0.056 | +190.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 8081 | +0.041 | +592.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1430 | +0.087 | +326.10€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 408 | +0.015 | +6.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5019 | +0.041 | +231.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1164 | +0.003 | +28.23€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 60 | -0.097 | +0.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4953 | +0.041 | +313.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 746 | +0.138 | +260.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4179 | +0.024 | +54.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 9257 | +0.023 | +370.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2835 | +0.049 | +308.20€ | 1 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 401 | +0.006 | +7.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5101 | +0.016 | +62.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 868 | -0.003 | -9.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 52 | -0.130 | +3.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 9736 | +0.015 | +251.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2703 | +0.027 | +187.36€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 393 | -0.004 | -2.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6047 | +0.014 | +68.48€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 549 | +0.004 | +1.81€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 44 | -0.174 | -3.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6221 | +0.040 | +658.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2705 | +0.086 | +678.72€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 265 | -0.002 | -3.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3251 | +0.004 | -16.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 156 | -0.133 | +0.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 591 | +0.350 | +194.49€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 591 | +0.350 | +194.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 327 | +0.354 | +104.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 327 | +0.354 | +104.54€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 264 | +0.342 | +89.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 264 | +0.342 | +89.95€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 13006 | -0.036 | +2849.11€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 13006 | -0.036 | +2849.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2369 | -0.121 | +38.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2369 | -0.121 | +38.16€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1454 | +0.209 | +885.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1454 | +0.209 | +885.48€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3910 | -0.064 | +578.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3910 | -0.064 | +578.67€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3915 | -0.073 | +638.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3915 | -0.073 | +638.56€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 152 | +0.039 | +8.44€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 152 | +0.039 | +8.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 152 | +0.039 | +8.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 152 | +0.039 | +8.44€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 954 | +0.291 | +760.69€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 954 | +0.291 | +760.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 522 | +0.286 | +396.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 522 | +0.286 | +396.48€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 432 | +0.295 | +364.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 432 | +0.295 | +364.21€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 736 | -0.113 | -84.24€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 736 | -0.113 | -84.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 216 | -0.083 | -16.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 216 | -0.083 | -16.24€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 71 | -0.199 | -8.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 71 | -0.199 | -8.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2553 | +0.299 | +1253.77€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 892 | +0.249 | +121.79€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 965 | +0.288 | +406.63€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 696 | +0.377 | +725.36€ | 0 | 1 |