# Hipótesis automáticas — 2026-10-01 20:56 UTC
_Generado por shadow_postmortem.py sobre 703256 resoluciones (PNL=+83942.84€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=568)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.232 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.135)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.218 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.135)

- **PATRÓN** `banda_hit_calibrado` > `0.8033` → IC=+0.254 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8033 (IC base=+0.135)

- **PATRÓN** `banda_z` > `4.006` → IC=+0.152 (n=596)

  - _Acción_: Kelly boost +0.76€ cuando `banda_z` > 4.006 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=629)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `3010.8456` → IC=+0.152 (n=397)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3010.8456 (IC base=+0.135)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=433)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.240 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.145)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.211 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.145)

- **PATRÓN** `banda_hit_calibrado` > `0.8017` → IC=+0.263 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8017 (IC base=+0.145)

- **PATRÓN** `banda_z` > `10.168` → IC=+0.214 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.168 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=538)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `6529.0114` → IC=+0.146 (n=159)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 6529.0114 (IC base=+0.145)

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

- **PATRÓN** `py_entrada` > `0.35` → IC=+0.218 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.35 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.124 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 4.0 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `891.6461` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 891.6461 (IC base=+0.110)

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
- **FILTRO** `restante_s_al_confirmar` < `145.28` → IC=-0.218 (n=7881)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.28
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=23648)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `135.36` → IC=-0.258 (n=1033)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 135.36
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3102)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.44` → IC=-0.309 (n=932)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.44
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=2797)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.69` → IC=-0.208 (n=1947)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.69
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5841)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.34` → IC=-0.329 (n=1520)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.34
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=4560)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.48` → IC=-0.224 (n=385)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=385)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=174)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=542)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=566)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.210 (n=15415)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=3751)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5513.2609` → IC=+0.172 (n=2423)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5513.2609 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=13323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=16177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=12472)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=6150)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7716.0988` → IC=+0.169 (n=2346)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7716.0988 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.208 (n=1758)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=1804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=2270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `16028.7692` → IC=+0.230 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16028.7692 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.200 (n=1626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=1816)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2324)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `15940.9457` → IC=+0.209 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15940.9457 (IC base=+0.195)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.169 (n=361)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.615 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4624.034 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.099)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.143 (n=892)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.154 (n=229)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.099)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.355 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.363 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.224)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.137 (n=759)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.248 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=862)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `1322.2406` → IC=+0.147 (n=754)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1322.2406 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.407 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.155 (n=595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.160 (n=639)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=789)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.151)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.370 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `1218.3909` → IC=+0.152 (n=234)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1218.3909 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.226 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=13364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=12762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.231 (n=4236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.175 (n=2994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3005)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=3037)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=1205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.242 (n=1200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.341 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.238)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=2955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=2979)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=2513)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.253 (n=2756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.329 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.243)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=3048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.191 (n=2931)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.194 (n=2307)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.194 (n=1112)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=613)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `11551.3768` → IC=+0.460 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11551.3768 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.446 (n=239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.446 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.454 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `17527.5783` → IC=+0.454 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 17527.5783 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.464 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3371.5411` → IC=+0.448 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3371.5411 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.416 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.413)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.414 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.413)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.427 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.413)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.413 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.413)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=39860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=17476)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=6856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.183 (n=5492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=7487)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=3553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.265 (n=4058)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=7254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=7250)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=3591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2434)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=2603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=6668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=3040)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=6056)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=5796)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.52` → IC=+0.135 (n=5636)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.52 (IC base=+0.115)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=3049)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=2870)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.130 (n=4154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 8.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `3.23` → IC=+0.138 (n=2801)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.23 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.182 (n=3007)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.38 (IC base=+0.111)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.128 (n=3195)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` > 4.96 (IC base=+0.111)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=2852)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.111)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.315 (n=885)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.288 (n=1241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `4184.0589` → IC=+0.307 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4184.0589 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.293 (n=582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.330 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `5187.3569` → IC=+0.307 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5187.3569 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=625)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1447.4658` → IC=+0.302 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1447.4658 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.354 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.346)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.364 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.346)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.388 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.346)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.346)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.375 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.346)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.436 (n=486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.437 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.441 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.437 (n=268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.456 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.925` → IC=+0.455 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `1966.3827` → IC=+0.457 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.3827 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.385 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.396)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.409 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.396)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.396)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=66)

- **FILTRO** `py_entrada` > `0.745` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `py_entrada` > 0.745
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=57)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=66)

- **FILTRO** `py_entrada` > `0.745` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `py_entrada` > 0.745
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=57)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4945` → IC=+0.129 (n=9484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4945 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.244 (n=3165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2196` → IC=+0.258 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2196 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.36` → IC=+0.190 (n=2489)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 8.36 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.253 (n=2634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6157` → IC=+0.254 (n=2633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6157 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.232 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.3215` → IC=+0.221 (n=2990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3215 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5671` → IC=+0.136 (n=11512)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5671 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.5976` → IC=+0.202 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5976 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.1561` → IC=+0.176 (n=3824)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1561 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.183 (n=1828)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6973 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.869` → IC=+0.177 (n=2769)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.869 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.1663` → IC=+0.224 (n=1989)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1663 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.5594` → IC=+0.200 (n=6341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5594 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.213 (n=6896)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 122.0 (IC base=+0.068)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.205 (n=713)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.186 (n=709)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0081 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3555` → IC=+0.179 (n=2114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3555 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=1022)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.180 (n=1418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 11.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.704` → IC=+0.293 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.704 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.215 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `1.4331` → IC=+0.177 (n=1992)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4331 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.191 (n=2152)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.234 (n=1116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.240 (n=1497)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1259` → IC=+0.267 (n=737)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1259 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=1520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0583` → IC=+0.286 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0583 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.479` → IC=+0.241 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.479 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.416` → IC=+0.239 (n=1747)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.416 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.229 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.265 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.5649` → IC=+0.242 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5649 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1575.869` → IC=+0.243 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1575.869 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.237 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3574` → IC=+0.229 (n=1675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3574 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.236 (n=1679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.221 (n=1709)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8956` → IC=+0.264 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8956 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3463` → IC=+0.223 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3463 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.619` → IC=+0.256 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.619 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2524` → IC=+0.223 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2524 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.223 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.244 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.4005` → IC=+0.222 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4005 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3766` → IC=+0.242 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3766 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11104.1249` → IC=+0.224 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11104.1249 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.170 (n=1132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.151 (n=1493)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7172` → IC=+0.171 (n=1696)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7172 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1308` → IC=+0.154 (n=1532)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1308 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.146 (n=269)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.284` → IC=+0.144 (n=1566)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.284 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.148 (n=1696)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2089 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8575` → IC=+0.140 (n=1131)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8575 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.181 (n=450)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4384` → IC=+0.149 (n=1586)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4384 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.77` → IC=+0.148 (n=1057)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.77 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `14128.8098` → IC=+0.141 (n=1131)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 14128.8098 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.173 (n=661)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 230.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.211 (n=708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=2124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=1909)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.298` → IC=+0.261 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.298 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.195 (n=1859)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3499` → IC=+0.207 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3499 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `1.7676` → IC=+0.201 (n=1817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7676 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=2527)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2002.2484` → IC=+0.197 (n=708)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2002.2484 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.220 (n=1642)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6292` → IC=+0.215 (n=1864)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6292 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=870)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.234 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.67` → IC=+0.234 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.67 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3469` → IC=+0.248 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3469 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.724` → IC=+0.214 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.724 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.743` → IC=+0.219 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.743 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.218 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1992.72` → IC=+0.215 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1992.72 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.211 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.170 (n=116)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=2548)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.148 (n=410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0037 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9526` → IC=+0.225 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9526 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.5438` → IC=+0.331 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5438 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.854` → IC=+0.170 (n=841)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 4.854 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.342 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.325 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.357 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.1917` → IC=+0.333 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1917 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.330 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.1024` → IC=+0.153 (n=667)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1024 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.6576` → IC=+0.205 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6576 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.148 (n=682)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8504 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2286` → IC=+0.201 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2286 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.5175` → IC=+0.164 (n=865)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.5175 (IC base=+0.020)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=388)

- **FILTRO** `ibs_20min` < `0.3056` → IC=-0.198 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3056
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=344)

- **FILTRO** `ibs_20min` > `0.24` → IC=-0.126 (n=2563)

  - _Acción_: SKIP cuando `ibs_20min` > 0.24
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=1265)

- **FILTRO** `sigma_ewma_delta_pct` > `8.719` → IC=-0.208 (n=402)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.719
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3426)

- **PATRÓN** `ibs_20min` > `0.625` → IC=+0.171 (n=229)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.625 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.332` → IC=+0.128 (n=162)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.332 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `1.0824` → IC=+0.316 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0824 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `2.5152` → IC=+0.290 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5152 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` > `1.4704` → IC=+0.276 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4704 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.300 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.24` → IC=+0.131 (n=1265)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.24 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7098` → IC=+0.253 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7098 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.4479` → IC=+0.243 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4479 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.6806` → IC=+0.277 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6806 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.159` → IC=+0.298 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.159 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.4034` → IC=+0.290 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4034 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.181 (n=665)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2008)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.211 (n=627)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=2046)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.210 (n=975)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=2999)

- **PATRÓN** `dist_vwap_pct` > `0.4705` → IC=+0.326 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4705 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.21` → IC=+0.320 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.21 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` < `0.9814` → IC=+0.298 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9814 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6251` → IC=+0.312 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6251 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.304 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.302 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.4513` → IC=+0.306 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4513 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8125` → IC=+0.307 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8125 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5629` → IC=+0.281 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5629 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` < `0.2254` → IC=+0.246 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2254 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` < `0.728` → IC=+0.258 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.728 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` > `1.0786` → IC=+0.270 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0786 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.264 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.167 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.1331` → IC=+0.263 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1331 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.5236` → IC=+0.255 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5236 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.200 (n=4097)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.4732` → IC=+0.189 (n=10947)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4732 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.7142` → IC=+0.285 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7142 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.64` → IC=+0.158 (n=5614)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.64 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `1.1795` → IC=+0.246 (n=4444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1795 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.254 (n=3970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.277 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `1.4633` → IC=+0.241 (n=2389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4633 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `2.2645` → IC=+0.255 (n=3248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2645 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.276 (n=6692)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.101)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.168 (n=3968)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0092 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5459` → IC=+0.157 (n=10475)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5459 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7082` → IC=+0.247 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7082 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2501` → IC=+0.249 (n=3447)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2501 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.708` → IC=+0.249 (n=1581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.708 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1988` → IC=+0.260 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1988 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2394` → IC=+0.303 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2394 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5869` → IC=+0.275 (n=2157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5869 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.278 (n=4781)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.255` → IC=-0.158 (n=848)

  - _Acción_: SKIP cuando `ibs_20min` < 0.255
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2544)

- **FILTRO** `ibs_20min` > `0.7572` → IC=-0.161 (n=692)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7572
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2077)

- **FILTRO** `sigma_ewma_delta_pct` > `4.536` → IC=-0.173 (n=629)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.536
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2140)

- **PATRÓN** `ibs_20min` > `0.8991` → IC=+0.278 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8991 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.851` → IC=+0.211 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.851 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.275 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.202 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.185` → IC=+0.232 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.185 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.217 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.2221` → IC=+0.442 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2221 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1442` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1442 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4701` → IC=+0.450 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4701 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.474 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8652` → IC=+0.169 (n=820)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.8652 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.2999` → IC=+0.192 (n=439)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2999 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6762` → IC=+0.176 (n=1021)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6762 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2714` → IC=+0.236 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2714 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.200 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4012` → IC=+0.178 (n=374)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.4012 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.217 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 233.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.228 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.6867` → IC=+0.230 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6867 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2665` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2665 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5529` → IC=+0.225 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5529 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1554` → IC=+0.243 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1554 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `456.0` → IC=+0.222 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 456.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.287 (n=1254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.260 (n=1688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.253 (n=1896)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.691` → IC=+0.284 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.691 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.267 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.1873` → IC=+0.267 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1873 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.265 (n=2212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `1993.7784` → IC=+0.272 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1993.7784 (IC base=+0.254)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.317 (n=703)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.1865` → IC=+0.295 (n=682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1865 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.323 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.3558` → IC=+0.292 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3558 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.684` → IC=+0.292 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.684 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.1912` → IC=+0.280 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1912 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.1194` → IC=+0.291 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1194 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `1.5716` → IC=+0.301 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5716 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.6496` → IC=+0.288 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6496 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `1913.1432` → IC=+0.304 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.1432 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.289 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.285)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7732` → IC=-0.190 (n=707)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7732
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=2125)

- **PATRÓN** `ibs_20min` > `0.905` → IC=+0.186 (n=628)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.905 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1857` → IC=+0.235 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1857 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0041` → IC=+0.254 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0041 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.0813` → IC=+0.266 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0813 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4024` → IC=+0.275 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4024 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.262 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1468` → IC=+0.220 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1468 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1801` → IC=+0.213 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1801 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` < `0.1022` → IC=+0.231 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1022 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.261 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8106 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.4508` → IC=+0.232 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4508 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.256 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7561` → IC=-0.186 (n=1299)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7561
  - _Potencial_: sin este filtro IC_bueno=+0.282 (n=1299)

- **FILTRO** `ibs_20min` > `0.675` → IC=-0.238 (n=650)

  - _Acción_: SKIP cuando `ibs_20min` > 0.675
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=1951)

- **FILTRO** `sigma_ewma_delta_pct` > `4.714` → IC=-0.192 (n=559)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.714
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=2042)

- **PATRÓN** `ibs_20min` > `0.7561` → IC=+0.282 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7561 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.2161` → IC=+0.317 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2161 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.69` → IC=+0.166 (n=411)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.69 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8622` → IC=+0.306 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8622 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6396` → IC=+0.302 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6396 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.300 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2733` → IC=+0.295 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2733 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.319 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `2.3618` → IC=+0.294 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3618 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.325 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.132 (n=1719)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5714 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.4805` → IC=+0.233 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4805 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.268 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.227 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.241 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4318` → IC=+0.246 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4318 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.255 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.021)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.326 (n=1379)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.281)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.300 (n=723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` > `0.7411` → IC=+0.322 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7411 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2145` → IC=+0.315 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2145 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.739` → IC=+0.305 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.739 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.295 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.331 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.292 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.285 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `2468.9246` → IC=+0.291 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2468.9246 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.320 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.312 (n=1092)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.1967` → IC=+0.288 (n=721)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1967 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.290 (n=823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` < `0.1341` → IC=+0.329 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1341 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.3209` → IC=+0.291 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3209 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.513` → IC=+0.298 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.513 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` < `0.642` → IC=+0.285 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.642 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.314 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.337 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `1.4219` → IC=+0.289 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4219 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `2419.9926` → IC=+0.286 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2419.9926 (IC base=+0.281)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.176 (n=3095)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0049 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.207 (n=3090)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.3644` → IC=+0.179 (n=8148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3644 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=9686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.224 (n=9264)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1747` → IC=+0.195 (n=3975)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1747 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.37` → IC=+0.254 (n=1867)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.37 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.2078` → IC=+0.165 (n=6166)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2078 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6298` → IC=+0.160 (n=6165)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6298 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.202 (n=1372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.5581` → IC=+0.170 (n=3920)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5581 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5982` → IC=+0.179 (n=2970)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.5982 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `1962.12` → IC=+0.175 (n=8271)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1962.12 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.186 (n=8177)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 108.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.186 (n=5935)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0819` → IC=+0.214 (n=2966)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0819 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=3410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4853` → IC=+0.227 (n=8889)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4853 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.1755` → IC=+0.165 (n=6232)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1755 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.319` → IC=+0.197 (n=1493)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.319 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1783` → IC=+0.158 (n=6385)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1783 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2906` → IC=+0.215 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2906 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5543` → IC=+0.171 (n=3607)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5543 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.5933` → IC=+0.172 (n=2732)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5933 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.179 (n=7851)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 108.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.228 (n=524)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.205 (n=521)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.3432` → IC=+0.216 (n=1549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3432 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=1638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=1042)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.9071` → IC=+0.284 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9071 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.238` → IC=+0.330 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.238 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.246 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.4293` → IC=+0.193 (n=1445)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4293 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.209 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.246 (n=1041)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.249 (n=1058)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.184` → IC=+0.285 (n=788)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.184 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.246 (n=1201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3503` → IC=+0.260 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3503 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.39` → IC=+0.238 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.39 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.224` → IC=+0.247 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.224 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.262 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4169` → IC=+0.262 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4169 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=1297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1567.4033` → IC=+0.253 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1567.4033 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.234 (n=465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.192 (n=465)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=1399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.3933` → IC=+0.224 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3933 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.2016` → IC=+0.207 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2016 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.225 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.176 (n=613)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6892 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.202 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.5013` → IC=+0.179 (n=596)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.5013 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.4598` → IC=+0.156 (n=452)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4598 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `11929.0923` → IC=+0.162 (n=1244)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11929.0923 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.163 (n=580)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 235.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.160 (n=1475)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2938` → IC=+0.165 (n=1474)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2938 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.5841` → IC=+0.191 (n=1474)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5841 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.912` → IC=+0.205 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.912 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.158 (n=1474)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2145 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.157` → IC=+0.150 (n=446)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.157 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4507` → IC=+0.145 (n=1363)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4507 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.7504` → IC=+0.140 (n=908)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.7504 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.173 (n=429)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 208.0 (IC base=+0.139)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.226 (n=702)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2514` → IC=+0.221 (n=1031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2514 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.435` → IC=+0.277 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.435 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2005` → IC=+0.215 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2005 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.7866` → IC=+0.203 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7866 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.216 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `1994.9584` → IC=+0.216 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1994.9584 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.234 (n=1166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1435` → IC=+0.253 (n=582)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1435 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.275 (n=455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.246 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.624` → IC=+0.253 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.624 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.250 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7377` → IC=+0.232 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7377 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1709` → IC=+0.224 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1709 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1985.3184` → IC=+0.227 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1985.3184 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.215 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.219)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.180 (n=1314)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0065 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.429` → IC=+0.161 (n=1491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.429 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.3502` → IC=+0.202 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3502 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1478` → IC=+0.182 (n=966)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1478 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.224 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.161 (n=995)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.856 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2914` → IC=+0.196 (n=228)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2914 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4303` → IC=+0.161 (n=487)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4303 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.164 (n=486)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5280.4621` → IC=+0.192 (n=994)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 5280.4621 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.151 (n=1428)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 155.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=1563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3891` → IC=+0.146 (n=1563)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3891 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.66` → IC=+0.175 (n=1563)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.66 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.158` → IC=+0.140 (n=1533)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.158 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.896` → IC=+0.163 (n=544)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.896 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8578` → IC=+0.150 (n=1042)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8578 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.179 (n=232)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.8021` → IC=+0.138 (n=959)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8021 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.5127` → IC=+0.130 (n=479)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5127 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `9330.5523` → IC=+0.164 (n=709)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 9330.5523 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.125 (n=1216)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 128.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.165 (n=768)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0101 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.5066` → IC=+0.211 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5066 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0815` → IC=+0.216 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0815 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.818` → IC=+0.254 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.818 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.2058` → IC=+0.133 (n=1690)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2058 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6454` → IC=+0.127 (n=1689)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6454 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.128 (n=1699)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.126 (n=702)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.5387` → IC=+0.139 (n=718)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5387 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=1767)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2892.276` → IC=+0.204 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2892.276 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.142 (n=1326)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 47.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.162 (n=753)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.170 (n=570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.216 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.146 (n=1583)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.604` → IC=+0.138 (n=354)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 7.604 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6382` → IC=+0.150 (n=570)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6382 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.226` → IC=+0.161 (n=299)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.226 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4463` → IC=+0.147 (n=519)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4463 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4187` → IC=+0.130 (n=519)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4187 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2750.8782` → IC=+0.179 (n=774)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2750.8782 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.126 (n=1504)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 52.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.229 (n=1425)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.2938` → IC=+0.208 (n=1063)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2938 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1667)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=717)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.245 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.5232` → IC=+0.214 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5232 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.9501` → IC=+0.203 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9501 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.602` → IC=+0.244 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.602 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.1935` → IC=+0.209 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1935 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6293` → IC=+0.215 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6293 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.271 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.4642` → IC=+0.211 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4642 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.7991` → IC=+0.213 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7991 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.209 (n=1578)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2837.1742` → IC=+0.208 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2837.1742 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.223 (n=724)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0174` → IC=+0.213 (n=1095)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0174 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.233 (n=549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.243 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `1.2202` → IC=+0.223 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2202 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.42` → IC=+0.249 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.42 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `0.7033` → IC=+0.219 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7033 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.284 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `2.1901` → IC=+0.202 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1901 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.206 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2391.9744` → IC=+0.215 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2391.9744 (IC base=+0.209)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.190 (n=807)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0037 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.175 (n=807)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0085 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3473` → IC=+0.174 (n=2128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3473 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.208 (n=1211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.51` → IC=+0.202 (n=2160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.51 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.7982` → IC=+0.186 (n=390)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.7982 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.713` → IC=+0.192 (n=1062)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.713 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8735` → IC=+0.189 (n=1433)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8735 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.2081` → IC=+0.175 (n=716)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2081 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.163` → IC=+0.182 (n=652)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.163 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.4355` → IC=+0.176 (n=781)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4355 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8202` → IC=+0.174 (n=1561)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8202 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=2737)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2672.5659` → IC=+0.171 (n=2160)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2672.5659 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.182 (n=2197)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 143.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.142 (n=1657)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0056 (IC base=+0.110)

- **PATRÓN** `drift_60min` |x|≤ `0.3426` → IC=+0.125 (n=2186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.3426 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=2335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.0649` → IC=+0.192 (n=828)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0649 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6996` → IC=+0.128 (n=987)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.6996 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.1642` → IC=+0.133 (n=609)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1642 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.147 (n=802)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2761.3271` → IC=+0.124 (n=2219)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2761.3271 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.130 (n=1026)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 27.0 (IC base=+0.110)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.175 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0029 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.143 (n=211)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0055 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3325` → IC=+0.161 (n=632)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3325 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=588)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.6492` → IC=+0.207 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6492 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.2886` → IC=+0.167 (n=220)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2886 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1221` → IC=+0.143 (n=514)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1221 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.164 (n=281)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.835` → IC=+0.144 (n=661)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.835 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.9019` → IC=+0.179 (n=422)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.9019 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.1555` → IC=+0.145 (n=657)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1555 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.0922` → IC=+0.158 (n=223)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0922 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.2024` → IC=+0.154 (n=542)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.2024 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.5048` → IC=+0.149 (n=550)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5048 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=817)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `10810.9505` → IC=+0.156 (n=632)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 10810.9505 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.183 (n=266)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 156.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.214 (n=260)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.160 (n=778)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6155` → IC=+0.180 (n=685)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6155 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.183` → IC=+0.154 (n=770)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.183 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.72` → IC=+0.142 (n=146)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 8.72 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.057` → IC=+0.144 (n=712)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.057 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2213` → IC=+0.146 (n=778)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2213 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.7044` → IC=+0.153 (n=695)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.7044 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.208 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1023` → IC=+0.156 (n=676)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1023 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4106` → IC=+0.148 (n=768)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4106 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11958.1784` → IC=+0.140 (n=695)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 11958.1784 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `357.0` → IC=+0.151 (n=746)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 357.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.263 (n=335)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4096` → IC=+0.221 (n=761)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4096 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.6792` → IC=+0.256 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6792 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1485` → IC=+0.219 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1485 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2204` → IC=+0.212 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2204 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.949` → IC=+0.233 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.949 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `0.836` → IC=+0.222 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.836 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `1.168` → IC=+0.234 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.168 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.1551` → IC=+0.256 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1551 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4105` → IC=+0.235 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4105 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.4384` → IC=+0.246 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4384 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.142 (n=238)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.087 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.6874` → IC=+0.148 (n=313)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6874 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `8174.0114` → IC=+0.128 (n=474)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 8174.0114 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.160 (n=515)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0059 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.182 (n=532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.9943` → IC=+0.236 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9943 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.527` → IC=+0.190 (n=301)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.527 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.069` → IC=+0.160 (n=507)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.069 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.646` → IC=+0.149 (n=576)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.646 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1735` → IC=+0.169 (n=161)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1735 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.2017` → IC=+0.165 (n=252)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.2017 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=609)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3103.1049` → IC=+0.186 (n=192)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3103.1049 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.4524` → IC=+0.159 (n=482)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.4524 (IC base=+0.081)

- **PATRÓN** `volumen_spike_ratio` < `1.5787` → IC=+0.164 (n=230)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5787 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `2505.4496` → IC=+0.132 (n=365)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2505.4496 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.128 (n=492)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 40.0 (IC base=+0.081)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.167 (n=181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0232 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.187 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0068 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2345` → IC=+0.175 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2345 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.194 (n=181)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.4 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `1.0655` → IC=+0.165 (n=204)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 1.0655 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.181 (n=155)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.6087` → IC=+0.170 (n=180)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6087 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2547` → IC=+0.180 (n=176)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.2547 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4437` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4437 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.181 (n=183)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2499.5335` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2499.5335 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.149 (n=206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0091 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.141 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 10.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.6 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.576` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.576 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6508` → IC=+0.130 (n=206)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6508 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.139 (n=167)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 17.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.210 (n=3993)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=12541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.9949` → IC=+0.310 (n=3991)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9949 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.916` → IC=+0.200 (n=1669)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.916 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.36` → IC=+0.248 (n=2962)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.36 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.172 (n=5356)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8812 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2879` → IC=+0.204 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2879 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.5741` → IC=+0.196 (n=3854)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5741 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `1796.8784` → IC=+0.178 (n=11971)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1796.8784 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.201 (n=9333)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 81.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.197 (n=4764)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0054 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1513` → IC=+0.191 (n=4750)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1513 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5703` → IC=+0.236 (n=10791)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5703 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2517` → IC=+0.162 (n=6749)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2517 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.039` → IC=+0.202 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.039 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.183 (n=10420)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7063` → IC=+0.162 (n=3230)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7063 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.242 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.5946` → IC=+0.192 (n=3342)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5946 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.201 (n=6488)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.229 (n=665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.231 (n=664)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.3618` → IC=+0.205 (n=1987)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3618 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.222 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.206 (n=1342)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.333 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.666` → IC=+0.356 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.666 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2724` → IC=+0.261 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2724 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.2361` → IC=+0.210 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2361 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.219 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.260 (n=1082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.260 (n=1624)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.126` → IC=+0.280 (n=713)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.126 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.3587` → IC=+0.282 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3587 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.511` → IC=+0.258 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.511 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.466` → IC=+0.257 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.466 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.291 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.5428` → IC=+0.256 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5428 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6054` → IC=+0.276 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6054 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1571.94` → IC=+0.266 (n=1620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1571.94 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.204 (n=644)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0832` → IC=+0.157 (n=643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0832 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.2913` → IC=+0.205 (n=1926)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2913 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.185 (n=1082)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.709` → IC=+0.175 (n=420)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.709 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.169` → IC=+0.154 (n=1759)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.169 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6277` → IC=+0.181 (n=643)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6277 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0731` → IC=+0.155 (n=1703)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0731 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2673` → IC=+0.192 (n=277)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2673 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1148` → IC=+0.161 (n=1646)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1148 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.7588` → IC=+0.155 (n=1247)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7588 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `11366.8951` → IC=+0.157 (n=1721)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 11366.8951 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.174 (n=799)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 278.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=1624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2608` → IC=+0.167 (n=1428)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2608 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=735)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.29` → IC=+0.237 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.29 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6493` → IC=+0.150 (n=258)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6493 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.164 (n=1482)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.534` → IC=+0.164 (n=272)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.534 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.508` → IC=+0.149 (n=1649)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.508 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2003` → IC=+0.162 (n=1623)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2003 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.204 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4071` → IC=+0.155 (n=1525)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4071 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7569` → IC=+0.163 (n=1016)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.7569 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `259.0` → IC=+0.158 (n=477)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 259.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.258 (n=651)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=2053)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=1981)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.343` → IC=+0.305 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.343 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.1323` → IC=+0.223 (n=1790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1323 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.232 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2003.6763` → IC=+0.237 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2003.6763 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.240 (n=1612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.232 (n=1640)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.6121` → IC=+0.236 (n=1831)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6121 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.232 (n=861)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.303 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.824` → IC=+0.278 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.824 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3404` → IC=+0.292 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3404 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7283` → IC=+0.232 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7283 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.1488` → IC=+0.237 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1488 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1987.1062` → IC=+0.249 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1987.1062 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.249 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.193 (n=685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4369` → IC=+0.150 (n=2052)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4369 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=2145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.2748` → IC=+0.189 (n=2052)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2748 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.5674` → IC=+0.166 (n=579)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.5674 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.555` → IC=+0.165 (n=329)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.555 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.162 (n=1369)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8725 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.210 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.153 (n=877)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.157 (n=904)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7631.7113` → IC=+0.237 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7631.7113 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.171 (n=642)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 72.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.170 (n=1101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0052 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3605` → IC=+0.140 (n=1452)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3605 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.132 (n=754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.5885` → IC=+0.197 (n=1452)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5885 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1587` → IC=+0.131 (n=1446)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1587 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.285` → IC=+0.164 (n=248)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.285 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6994` → IC=+0.140 (n=726)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6994 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.225 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.141 (n=1575)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `9568.5341` → IC=+0.203 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9568.5341 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.129 (n=1383)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 145.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.148 (n=1360)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0082 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.5784` → IC=+0.126 (n=2041)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.5784 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=2103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4634` → IC=+0.198 (n=2040)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4634 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0684` → IC=+0.208 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0684 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.54` → IC=+0.239 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.54 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8928` → IC=+0.144 (n=1361)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8928 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.126 (n=2099)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.456` → IC=+0.126 (n=1985)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.456 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=2075)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2890.5622` → IC=+0.254 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2890.5622 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.143 (n=1622)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 52.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.183 (n=651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1372` → IC=+0.158 (n=650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1372 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6343` → IC=+0.209 (n=1948)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6343 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2238` → IC=+0.137 (n=1622)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2238 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.463` → IC=+0.128 (n=1872)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.463 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6475` → IC=+0.164 (n=650)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6475 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2207` → IC=+0.183 (n=307)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2207 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4358` → IC=+0.146 (n=594)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4358 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2799.6738` → IC=+0.187 (n=649)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2799.6738 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.131 (n=1577)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 51.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.229 (n=2016)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.215 (n=889)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.262 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.2153` → IC=+0.233 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2153 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.59` → IC=+0.256 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.59 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.0602` → IC=+0.217 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0602 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6422` → IC=+0.221 (n=2016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6422 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2849` → IC=+0.247 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2849 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.1495` → IC=+0.233 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1495 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1968)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2622.2916` → IC=+0.220 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2622.2916 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.217 (n=711)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.230 (n=708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.223 (n=1501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.262 (n=1870)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `1.2245` → IC=+0.213 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2245 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.214 (n=1885)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2197 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.258 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.237 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.278 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `2.1736` → IC=+0.203 (n=1701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1736 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.205 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2399.8931` → IC=+0.211 (n=1896)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.8931 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.199 (n=1853)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 37.0 (IC base=+0.208)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=3664)

- **PATRÓN** `sigma_h` < `0.009` → IC=+0.196 (n=3192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.009 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.5113` → IC=+0.190 (n=3628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.5113 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=1360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1656)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.237 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1738` → IC=+0.187 (n=1328)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1738 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.4549` → IC=+0.178 (n=2376)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.4549 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.2` → IC=+0.208 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.2 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.7086` → IC=+0.183 (n=1091)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.7086 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.8941` → IC=+0.182 (n=1653)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.8941 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.1683` → IC=+0.208 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1683 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.4541` → IC=+0.188 (n=1195)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4541 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.8617` → IC=+0.186 (n=2387)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8617 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=2689)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2514.7508` → IC=+0.185 (n=3627)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2514.7508 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.218 (n=921)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.182 (n=2429)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.187 (n=1215)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1827 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.6674` → IC=+0.184 (n=514)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6674 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.214` → IC=+0.171 (n=2755)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.214 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2566` → IC=+0.166 (n=2596)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2566 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.168 (n=2521)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5347` → IC=+0.169 (n=1199)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5347 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8236` → IC=+0.172 (n=1817)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8236 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=3664)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `5320.6072` → IC=+0.167 (n=2465)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5320.6072 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.167 (n=1791)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 85.0 (IC base=+0.162)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.229 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.263 (n=167)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=221)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.5153` → IC=+0.229 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5153 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.7609` → IC=+0.207 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7609 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.1363` → IC=+0.209 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1363 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.96` → IC=+0.223 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.96 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.529` → IC=+0.206 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.529 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.2183` → IC=+0.209 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2183 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.5892` → IC=+0.213 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5892 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.222 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `12591.1219` → IC=+0.235 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12591.1219 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.225 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3662` → IC=+0.163 (n=1042)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3662 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.182 (n=401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.185 (n=459)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1485 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.154 (n=472)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.6091 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6687` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6687 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.377` → IC=+0.170 (n=1024)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.377 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8817` → IC=+0.193 (n=695)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8817 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0692` → IC=+0.172 (n=477)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0692 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4149` → IC=+0.152 (n=346)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4149 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8156` → IC=+0.166 (n=692)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8156 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `12143.1795` → IC=+0.161 (n=930)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12143.1795 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `698.0` → IC=+0.158 (n=996)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 698.0 (IC base=+0.150)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.188 (n=213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.180 (n=289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.01 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.173 (n=637)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.242 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.56` → IC=+0.231 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.56 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2079` → IC=+0.204 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2079 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.6711` → IC=+0.173 (n=212)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.6711 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8234` → IC=+0.171 (n=567)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8234 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2429.8516` → IC=+0.204 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2429.8516 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.241 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.295 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.288 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1988` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1988 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.237)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.196 (n=1018)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0071 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1538` → IC=+0.199 (n=507)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1538 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.187 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5342` → IC=+0.198 (n=769)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5342 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.886` → IC=+0.189 (n=384)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.886 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.207` → IC=+0.197 (n=971)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.207 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.194 (n=1038)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.0854` → IC=+0.190 (n=1014)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.0854 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `1.2477` → IC=+0.189 (n=384)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.2477 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.200 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `2.4754` → IC=+0.192 (n=1130)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.4754 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=1156)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.224 (n=313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3844` → IC=+0.197 (n=824)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3844 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.177 (n=626)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 10.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.7588` → IC=+0.171 (n=937)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7588 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.0908` → IC=+0.172 (n=936)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.0908 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.6081` → IC=+0.191 (n=202)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6081 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.74` → IC=+0.172 (n=960)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.74 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6434` → IC=+0.205 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6434 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `0.7257` → IC=+0.166 (n=837)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7257 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.182 (n=398)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.181 (n=808)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.5255` → IC=+0.169 (n=306)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5255 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `7781.8228` → IC=+0.182 (n=837)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 7781.8228 (IC base=+0.166)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.167 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0108 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.171 (n=357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 3.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.145 (n=367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 14.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.246 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.2235` → IC=+0.196 (n=241)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2235 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.097` → IC=+0.224 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.097 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.7088` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.7088 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.4144` → IC=+0.198 (n=117)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.4144 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.152 (n=429)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2997.549` → IC=+0.166 (n=363)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2997.549 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.167 (n=304)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 51.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.190 (n=298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0068 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.6689` → IC=+0.177 (n=298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.6689 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.160 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 16.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.6782` → IC=+0.191 (n=263)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6782 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.6343` → IC=+0.225 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6343 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.639` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.639 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.281` → IC=+0.163 (n=289)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 5.281 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.3839` → IC=+0.167 (n=298)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.3839 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.218 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.6095` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.6095 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3191.6314` → IC=+0.197 (n=298)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3191.6314 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.214 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.159)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.167 (n=497)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.6464` → IC=+0.180 (n=928)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6464 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1469` → IC=+0.145 (n=556)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1469 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.422` → IC=+0.190 (n=243)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.422 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.185 (n=141)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.080)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.123 (n=414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0056 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.0406` → IC=+0.294 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0406 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.1922` → IC=+0.136 (n=438)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1922 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.074` → IC=+0.151 (n=328)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.074 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.138` → IC=+0.206 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.138 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.146 (n=334)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `1.4422` → IC=+0.147 (n=298)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4422 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `3267.7768` → IC=+0.148 (n=160)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3267.7768 (IC base=+0.045)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.199 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.129 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 16.0 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.426` → IC=+0.160 (n=357)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.426 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.160 (n=186)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `2.4916` → IC=+0.126 (n=316)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.4916 (IC base=+0.089)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.135 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0052 (IC base=+0.089)

- **PATRÓN** `drift_60min` |x|≤ `0.0576` → IC=+0.205 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0576 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.287` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.287 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.0689` → IC=+0.146 (n=190)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0689 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.069` → IC=+0.194 (n=178)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 7.069 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `1.151` → IC=+0.136 (n=185)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.151 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.8238` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.8238 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `2.3732` → IC=+0.167 (n=163)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.3732 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `1.437` → IC=+0.146 (n=145)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.437 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `3311.1631` → IC=+0.146 (n=156)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3311.1631 (IC base=+0.089)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6967` → IC=-0.128 (n=151)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6967
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=308)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=152)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.134 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0049 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.134 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6967` → IC=+0.219 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6967 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.3353` → IC=+0.199 (n=134)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3353 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.289 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.8` → IC=+0.134 (n=230)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.7617` → IC=+0.150 (n=195)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.7617 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `1135.8896` → IC=+0.150 (n=304)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1135.8896 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.1674` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1674 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` < `0.1753` → IC=+0.129 (n=130)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1753 (IC base=+0.008)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.558` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.558 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `2.637` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.637 (IC base=+0.008)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=106)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.008)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0094` → IC=-0.232 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=107)

- **FILTRO** `ibs_20min` > `0.1786` → IC=-0.286 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1786
  - _Potencial_: sin este filtro IC_bueno=+0.268 (n=80)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.122 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0063 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.7805` → IC=+0.178 (n=225)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7805 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.064` → IC=+0.160 (n=95)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.064 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.053)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.133 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0094 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1786` → IC=+0.268 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1786 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.815` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.815 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `1.4436` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4436 (IC base=+0.009)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=175)

- **FILTRO** `dist_vwap_pct` > `0.1613` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1613
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=208)

- **FILTRO** `volumen_regimen` < `0.7296` → IC=-0.350 (n=58)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7296
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=175)

- **FILTRO** `volumen_spike_ratio` > `3.0912` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.0912
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=120)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.368 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=129)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=174)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=165)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=90)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.250 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=45)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=40)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

- **FILTRO** `sigma_ewma_delta_pct` > `2.55` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.55
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=52)

- **FILTRO** `volumen_regimen` > `0.8664` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8664
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=62)

- **FILTRO** `libro_liquidez` < `3685.6992` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 3685.6992
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.395 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=53)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=50)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=47)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=-0.220)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=65)

- **FILTRO** `ibs_20min` < `0.125` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.125
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.178 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0059 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.146 (n=323)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6667 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.5013` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5013 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.4188` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4188 (IC base=+0.088)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.128 (n=329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.006 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.188 (n=290)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1558 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.769` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.769 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `2.627` → IC=+0.148 (n=254)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.627 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` > `1.5868` → IC=+0.124 (n=227)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.5868 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=347)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `3936.7645` → IC=+0.209 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3936.7645 (IC base=+0.093)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6247` → IC=-0.265 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6247
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=99)

- **PATRÓN** `sigma_h` > `0.0022` → IC=+0.171 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0022 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.232 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.179 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.227 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1622 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.1046` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1046 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.668` → IC=+0.176 (n=134)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 6.668 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.180 (n=148)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.1737 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.229 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `2.5856` → IC=+0.229 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5856 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.4576` → IC=+0.195 (n=116)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4576 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `4542.5709` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 4542.5709 (IC base=+0.162)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.2505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2505
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=88)

- **FILTRO** `libro_liquidez` < `1419.7314` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 1419.7314
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=103)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.183 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0027 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.123 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 8.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.156 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.818` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.818 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` < `1.008` → IC=+0.125 (n=102)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.008 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `1570.5288` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1570.5288 (IC base=+0.083)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=67)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.283 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.275 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.242 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.9583` → IC=+0.262 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9583 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.264 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.309 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.1671` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1671 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.423 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `591.0149` → IC=+0.239 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 591.0149 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=-0.044)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.274)

- **PATRÓN** `elapsed_s` > `210.3` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.3 (IC base=+0.274)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.8301` → IC=+0.357 (n=40)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8301 (IC base=+0.274)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.274)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3583` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3583 (IC base=+0.212)

- **PATRÓN** `elapsed_s` > `194.4` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 194.4 (IC base=+0.212)

- **PATRÓN** `elapsed_s` < `194.4` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 194.4 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.306 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `1457.0` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1457.0 (IC base=+0.212)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.274)

- **PATRÓN** `elapsed_s` > `210.3` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.3 (IC base=+0.274)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.8301` → IC=+0.357 (n=40)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8301 (IC base=+0.274)

- **PATRÓN** `ballena_activa_n` < `1158.0` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1158.0 (IC base=+0.274)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3583` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3583 (IC base=+0.212)

- **PATRÓN** `elapsed_s` > `194.4` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 194.4 (IC base=+0.212)

- **PATRÓN** `elapsed_s` < `194.4` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 194.4 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.306 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `1457.0` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1457.0 (IC base=+0.212)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.123 (n=1054)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.495 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2925.1106` → IC=+0.162 (n=300)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2925.1106 (IC base=+0.111)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.123 (n=1054)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.495 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2925.1106` → IC=+0.162 (n=300)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2925.1106 (IC base=+0.111)

### LIQUIDACIONES_15M
- **FILTRO** `py_entrada` < `0.445` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=116)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=147)

- **FILTRO** `libro_liquidez` < `9493.103` → IC=-0.179 (n=107)

  - _Acción_: SKIP cuando `libro_liquidez` < 9493.103
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=229)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=215)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=46)

- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=50)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.133 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=16)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=95)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=2303)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=94)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=51)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=83)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=94)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=92)

### LIQUIDACIONES_5M#BTC#5min
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

- **PATRÓN** `liq_usd_total` > `138064.32` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `liq_usd_total` > 138064.32 (IC base=+0.048)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.164 (n=138)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.495 (IC base=+0.048)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=945)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=899)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9855` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `ballena_activa_n` > `142.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 142.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=542)

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
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=241)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.495 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `4094.1814` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4094.1814 (IC base=+0.033)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=720)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=720)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=454)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=454)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=194)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=194)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.127 (n=81)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=128)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=113)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=135)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=235)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=108)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=121)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=276)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=276)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=161)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.133 (n=538)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1350)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=92)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=152)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.52 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.148 (n=126)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.56 (IC base=+0.050)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` < `9.6` → IC=-0.143 (n=40)

  - _Acción_: SKIP cuando `restante_min` < 9.6
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=83)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.192 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **FILTRO** `lag_apertura_s` > `311.35` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `lag_apertura_s` > 311.35
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=82)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.150 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 9.0 (IC base=+0.086)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.121 (n=114)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=42)

- **FILTRO** `profundidad_ratio` < `55.0` → IC=-0.217 (n=51)

  - _Acción_: SKIP cuando `profundidad_ratio` < 55.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=105)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=141)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.53 (IC base=-0.038)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=169)

- **FILTRO** `restante_min` < `3.4` → IC=-0.254 (n=67)

  - _Acción_: SKIP cuando `restante_min` < 3.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=141)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.167 (n=61)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=147)

- **FILTRO** `lag_apertura_s` > `92.29` → IC=-0.250 (n=70)

  - _Acción_: SKIP cuando `lag_apertura_s` > 92.29
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=138)

- **FILTRO** `profundidad_ratio` < `123.7` → IC=-0.147 (n=137)

  - _Acción_: SKIP cuando `profundidad_ratio` < 123.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=71)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **PATRÓN** `lag_apertura_s` < `98.43` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 98.43 (IC base=-0.023)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.48` → IC=+0.125 (n=62)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.48 (IC base=+0.008)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.160 (n=139)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=76)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.5 (IC base=-0.044)

- **PATRÓN** `profundidad_ratio` > `14.4` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `profundidad_ratio` > 14.4 (IC base=+0.023)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.222 (n=70)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=190)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.165 (n=4216)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=12770)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.165 (n=4262)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=13307)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.197 (n=738)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2248)

- **PATRÓN** `libro_liquidez` > `1796.98` → IC=+0.125 (n=1016)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1796.98 (IC base=+0.032)

- **PATRÓN** `libro_liquidez` > `1564.8769` → IC=+0.141 (n=1069)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1564.8769 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.180 (n=739)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=2306)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=751)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2429)

- **PATRÓN** `libro_liquidez` > `1792.5347` → IC=+0.126 (n=1036)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1792.5347 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.167 (n=727)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2255)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2381)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3121)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

- **FILTRO** `libro_liquidez` < `17081.1281` → IC=-0.143 (n=233)

  - _Acción_: SKIP cuando `libro_liquidez` < 17081.1281
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=699)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ballena_activa_n` > `89.0` → IC=-0.220 (n=116)

  - _Acción_: SKIP cuando `ballena_activa_n` > 89.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=231)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1922.3295` → IC=-0.176 (n=322)

  - _Acción_: SKIP cuando `libro_liquidez` < 1922.3295
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=654)

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

- **FILTRO** `drift_7min_pct` |x|> `0.0331` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0331
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.136 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.032)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=11837)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=26549)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=8918)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=29468)

- **FILTRO** `ibs_7min` < `0.2667` → IC=-0.234 (n=9593)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=28793)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=12698)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=25688)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=11873)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=36724)

- **FILTRO** `ibs_7min` > `0.291` → IC=-0.181 (n=12149)

  - _Acción_: SKIP cuando `ibs_7min` > 0.291
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=36448)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.140 (n=1926)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4544)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=1555)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=4915)

- **FILTRO** `ibs_7min` < `0.7077` → IC=-0.252 (n=2134)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7077
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=4336)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.181 (n=1510)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=4960)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.262 (n=2064)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=6319)

- **FILTRO** `ibs_7min` > `0.7917` → IC=-0.210 (n=2094)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7917
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6289)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1553)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=5027)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=1607)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4973)

- **FILTRO** `ibs_7min` < `0.7439` → IC=-0.196 (n=1645)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7439
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4935)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.179 (n=1642)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4938)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1562)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5129)

- **FILTRO** `ibs_7min` > `0.262` → IC=-0.185 (n=1672)

  - _Acción_: SKIP cuando `ibs_7min` > 0.262
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5019)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.187 (n=1664)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5027)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.161 (n=1513)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=4650)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=1449)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4714)

- **FILTRO** `ibs_7min` < `0.7046` → IC=-0.243 (n=2032)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7046
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=4131)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.211 (n=1464)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4699)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.245 (n=2056)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=6907)

- **FILTRO** `ibs_7min` > `0.7442` → IC=-0.176 (n=2239)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7442
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=6724)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.234 (n=1863)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=4457)

- **FILTRO** `ibs_7min` < `0.7407` → IC=-0.182 (n=1579)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4741)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.173 (n=1561)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4759)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1609)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=4878)

- **FILTRO** `ibs_7min` > `0.2747` → IC=-0.180 (n=1621)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4866)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.182 (n=1563)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4924)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.262 (n=1601)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4957)

- **FILTRO** `ibs_7min` < `0.2593` → IC=-0.230 (n=1638)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2593
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=4920)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.173 (n=2322)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=6969)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.272 (n=1465)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=4830)

- **FILTRO** `ibs_7min` < `0.2727` → IC=-0.221 (n=1573)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4722)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.212 (n=1465)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=4830)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.206 (n=2062)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=6720)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1178)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=584)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7888.4442` → IC=-0.133 (n=344)

  - _Acción_: SKIP cuando `libro_liquidez` < 7888.4442
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=701)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=333)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.150 (n=158)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=476)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.130 (n=855)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `447.889` → IC=+0.152 (n=285)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 447.889 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=281)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 16.0 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.162 (n=66)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.195 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 11.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.138 (n=175)

  - _Acción_: Kelly boost +0.69€ cuando `total_vol_5m` < 422.506 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2576.9482` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2576.9482 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.178 (n=88)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 13.0 (IC base=+0.139)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 11.0 (IC base=+0.109)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4137` → IC=+0.183 (n=118)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.4137 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.189 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 16.0 (IC base=+0.103)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.171 (n=77)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 73.0 (IC base=+0.103)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.158 (n=150)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.176 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 11.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.151 (n=150)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 8043.774 (IC base=+0.127)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4006` → IC=+0.138 (n=150)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.4006 (IC base=+0.096)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.125 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `3593.0166` → IC=+0.141 (n=76)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3593.0166 (IC base=+0.096)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=113)

- **FILTRO** `sigma_h` > `0.0055` → IC=-0.275 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=239)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.222 (n=106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.263 (n=36)

- **FILTRO** `T_h` > `95.0392` → IC=-0.419 (n=35)

  - _Acción_: SKIP cuando `T_h` > 95.0392
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.097)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0087` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0087
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=34)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.210 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=57)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.181 (n=333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=112)

- **FILTRO** `T_h` > `71.8388` → IC=-0.145 (n=333)

  - _Acción_: SKIP cuando `T_h` > 71.8388
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=112)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.327 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=292)

- **FILTRO** `sigma_h` < `0.0046` → IC=-0.318 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=291)

- **FILTRO** `T_h` > `60.9549` → IC=-0.312 (n=290)

  - _Acción_: SKIP cuando `T_h` > 60.9549
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=98)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `68.7654` → IC=-0.150 (n=115)

  - _Acción_: SKIP cuando `T_h` > 68.7654
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.375 (n=38)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=116)

- **FILTRO** `T_h` > `143.9199` → IC=-0.296 (n=47)

  - _Acción_: SKIP cuando `T_h` > 143.9199
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=94)

- **FILTRO** `pct_vs_K` |x|> `2.9616` → IC=-0.439 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9616
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=94)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.403 (n=29)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=95)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.339 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=90)

- **FILTRO** `sigma_h` < `0.0048` → IC=-0.339 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=90)

- **FILTRO** `T_h` > `57.801` → IC=-0.340 (n=79)

  - _Acción_: SKIP cuando `T_h` > 57.801
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=40)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.190 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=83)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.155 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=83)

- **FILTRO** `T_h` > `135.1308` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `T_h` > 135.1308
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=83)

- **FILTRO** `sigma_h` > `0.011` → IC=-0.346 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=-0.329 (n=39)

- **FILTRO** `T_h` > `52.8235` → IC=-0.379 (n=56)

  - _Acción_: SKIP cuando `T_h` > 52.8235
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

- **PATRÓN** `pct_vs_K` |x|≤ `1.0286` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.0286 (IC base=-0.062)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.468 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.354)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.389 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.387 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.354)

- **PATRÓN** `T_h` < `0.6188` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6188 (IC base=+0.354)

- **PATRÓN** `T_h` > `1.2259` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2259 (IC base=+0.354)

- **PATRÓN** `dist_50` > `0.4067` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4067 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.379 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.354)

- **PATRÓN** `edge` > `0.097` → IC=+0.453 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.097 (IC base=+0.420)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.433 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.420)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.448 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.420)

- **PATRÓN** `T_h` < `0.608` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.420)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.449 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.420)

- **PATRÓN** `dist_50` > `0.4077` → IC=+0.482 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4077 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.474 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.420)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1072` → IC=+0.450 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.419)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.406 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.419)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.455 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.419)

- **PATRÓN** `T_h` < `0.8618` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8618 (IC base=+0.419)

- **PATRÓN** `dist_50` > `0.4166` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4166 (IC base=+0.419)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.431 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.419)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.434)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.469 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.434)

- **PATRÓN** `T_h` > `0.8294` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8294 (IC base=+0.434)

- **PATRÓN** `dist_50` > `0.3691` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3691 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

- **PATRÓN** `edge` > `0.1155` → IC=+0.471 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.487 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.463)

- **PATRÓN** `T_h` > `0.8021` → IC=+0.465 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8021 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.491 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.468 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=223)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=321)

- **PATRÓN** `streak_estiramiento` < `0.5782` → IC=+0.150 (n=141)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.5782 (IC base=+0.035)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4382` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4382
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=39)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_racha` < 990711.2 (IC base=-0.007)

- **PATRÓN** `streak_estiramiento` < `0.4382` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `streak_estiramiento` < 0.4382 (IC base=-0.007)

- **PATRÓN** `streak_estiramiento` < `0.3856` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.3856 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.129 (n=95)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 49.0 (IC base=+0.060)

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
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=806)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=812)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=485)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `3.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `libro_liquidez` < `2775.6672` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 2775.6672
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

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
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=721)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1306)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=864)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=849)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3228)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1647)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.232 (n=905)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.1592` → IC=+0.203 (n=1757)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1592 (IC base=+0.197)

- **PATRÓN** `delta_ratio_macro` |x|> `0.218` → IC=+0.205 (n=665)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.218 (IC base=+0.197)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.238 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.206 (n=1864)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=2068)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_15` > `0.6174` → IC=+0.276 (n=1995)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6174 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.192 (n=989)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.758` → IC=+0.287 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.758 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `2958.1829` → IC=+0.203 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2958.1829 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.217 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.197)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=847)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.234 (n=288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.281 (n=144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `0.3831` → IC=+0.219 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3831 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2014` → IC=+0.242 (n=196)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2014 (IC base=+0.212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4004` → IC=+0.245 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4004 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.244 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.7141` → IC=+0.277 (n=432)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7141 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.280 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.395` → IC=+0.259 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.395 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.247 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.212)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.297` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.297
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=513)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.173 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0035 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.146 (n=306)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.005 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.067` → IC=+0.157 (n=202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.067 (IC base=+0.138)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.171 (n=153)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.138)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.171 (n=171)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.159 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.144 (n=481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_15` > `0.6603` → IC=+0.263 (n=411)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6603 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1186` → IC=+0.154 (n=330)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1186 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.257` → IC=+0.229 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.257 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `3382.103` → IC=+0.146 (n=411)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3382.103 (IC base=+0.138)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.293 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.1498` → IC=+0.220 (n=212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1498 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0716` → IC=+0.201 (n=215)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0716 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3249` → IC=+0.233 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3249 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=214)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.278 (n=241)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.1256` → IC=+0.197 (n=130)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1256 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.33` → IC=+0.188 (n=238)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.33 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.981` → IC=+0.402 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.981 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=262)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `3089.3424` → IC=+0.284 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3089.3424 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.217 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.186)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=-0.009)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.285 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.221 (n=224)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0847` → IC=+0.264 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0847 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.228 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.5758` → IC=+0.289 (n=509)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5758 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3587` → IC=+0.216 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3587 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.5623` → IC=+0.201 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5623 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.241` → IC=+0.248 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.241 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2923.757` → IC=+0.291 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2923.757 (IC base=+0.202)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.356 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.382 (n=159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.356 (n=318)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1476` → IC=+0.378 (n=317)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1476 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1316` → IC=+0.391 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1316 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.373 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.7872` → IC=+0.391 (n=476)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7872 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.389 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.085` → IC=+0.365 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.085 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.354 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.354)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.358 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `3836.614` → IC=+0.371 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3836.614 (IC base=+0.354)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.366 (n=230)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.376 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.376 (n=87)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.360)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.372 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.371 (n=261)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1241` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1241 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.383 (n=263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.390 (n=261)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.399 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.072` → IC=+0.360 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.072 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.362 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `15942.0974` → IC=+0.388 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15942.0974 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `504.0` → IC=+0.410 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 504.0 (IC base=+0.360)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.381 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.344)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.356 (n=144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.344)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.361 (n=193)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.344)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.374 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.344)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.406 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.344)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.395 (n=216)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.344)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.381 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.344)

- **PATRÓN** `dist_vwap_pct` < `0.1186` → IC=+0.350 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1186 (IC base=+0.344)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.717` → IC=+0.360 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.717 (IC base=+0.344)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.587` → IC=+0.346 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.587 (IC base=+0.344)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.351 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.344)

- **PATRÓN** `libro_liquidez` > `4314.8149` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4314.8149 (IC base=+0.344)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.227 (n=766)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2300)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.207 (n=1084)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1982)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1363` → IC=+0.244 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1363 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6429` → IC=+0.274 (n=742)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6429 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.192 (n=606)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1231` → IC=+0.249 (n=1516)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1231 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1785` → IC=+0.250 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1785 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.277 (n=2272)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.6717` → IC=+0.295 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6717 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.242 (n=1966)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=-0.024)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.215 (n=465)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1397)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.214 (n=614)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1248)

- **FILTRO** `sigma_ewma_delta_pct` > `23.623` → IC=-0.259 (n=264)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.623
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1598)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.163 (n=179)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0028 (IC base=+0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.284 (n=100)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.084)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.084)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.121 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 12.0 (IC base=+0.084)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.333 (n=219)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.293 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.2297` → IC=+0.278 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2297 (IC base=+0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0802` → IC=+0.157 (n=33)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.0802 (IC base=-0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1833` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1833 (IC base=-0.193)

- **PATRÓN** `ibs_15` < `0.5472` → IC=+0.294 (n=32)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.5472 (IC base=-0.193)

- **PATRÓN** `dist_vwap_pct` < `0.0553` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0553 (IC base=-0.193)

- **PATRÓN** `ballena_activa_n` < `305.0` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 305.0 (IC base=-0.193)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=459)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.153 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0065 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.170 (n=319)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0039 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.212 (n=158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.151)

- **PATRÓN** `drift_15min` |x|≤ `0.4157` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `drift_15min` |x|≤ 0.4157 (IC base=+0.151)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.225 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.178 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 11.0 (IC base=+0.151)

- **PATRÓN** `ibs_15` > `0.6603` → IC=+0.260 (n=357)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6603 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1135` → IC=+0.178 (n=256)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1135 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.838` → IC=+0.152 (n=386)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 18.838 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=459)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.183 (n=162)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.246 (n=868)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4443` → IC=+0.239 (n=868)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4443 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.7799` → IC=+0.247 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7799 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2071` → IC=+0.258 (n=394)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2071 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.2751` → IC=+0.281 (n=764)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2751 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.7494` → IC=+0.308 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7494 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.226` → IC=+0.268 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.226 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.472` → IC=+0.240 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.472 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1704` → IC=-0.233 (n=245)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1704
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=477)

- **FILTRO** `drift_15min` |x|> `0.9044` → IC=-0.269 (n=180)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9044
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=542)

- **FILTRO** `sigma_ewma_delta_pct` > `18.215` → IC=-0.136 (n=383)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.215
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3093)

- **PATRÓN** `ibs_15` > `0.6071` → IC=+0.198 (n=51)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.99€ cuando `ibs_15` > 0.6071 (IC base=-0.174)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0777` → IC=+0.229 (n=338)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0777 (IC base=-0.041)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.183` → IC=+0.229 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.183 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.271 (n=378)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7153` → IC=+0.253 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7153 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.1747` → IC=+0.234 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1747 (IC base=-0.041)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1986` → IC=-0.217 (n=295)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1986
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=574)

- **FILTRO** `sigma_ewma_delta_pct` > `7.063` → IC=-0.214 (n=267)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.063
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=602)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.271 (n=251)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=618)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1442` → IC=+0.274 (n=263)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1442 (IC base=-0.036)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1668` → IC=+0.311 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1668 (IC base=-0.036)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.296 (n=582)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` > `0.8845` → IC=+0.345 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8845 (IC base=-0.036)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=8)

- **PATRÓN** `dist_vwap_pct` > `0.1688` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1688 (IC base=+0.051)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=8)

- **PATRÓN** `dist_vwap_pct` > `0.1688` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1688 (IC base=+0.051)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.301 (n=517)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.328 (n=259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2389` → IC=+0.300 (n=258)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2389 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2213` → IC=+0.322 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2213 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8411` → IC=+0.328 (n=775)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8411 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.4372` → IC=+0.337 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4372 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.343 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `13022.3239` → IC=+0.299 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13022.3239 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.301 (n=284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0549` → IC=+0.333 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0549 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.312 (n=142)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3977` → IC=+0.307 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3977 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.317 (n=425)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.4131` → IC=+0.359 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4131 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.319 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.304 (n=309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.315 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.149` → IC=+0.297 (n=234)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.149 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.328 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8743` → IC=+0.348 (n=313)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8743 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.4611` → IC=+0.305 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4611 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.221` → IC=+0.330 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.221 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2521` → IC=-0.153 (n=73)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2521
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=220)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.138 (n=194)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=67)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.197 (n=64)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=126)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0687` → IC=-0.139 (n=59)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0687
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=115)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1259` → IC=-0.167 (n=43)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1259
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=131)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1819` → IC=-0.260 (n=23)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1819
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

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

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0928` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0928
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `79.5964` → IC=+0.226 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.5964 (IC base=+0.212)

- **PATRÓN** `ratio` < `0.9763` → IC=+0.470 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9763 (IC base=+0.212)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0112` → IC=+0.314 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0112 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `126.1277` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 126.1277 (IC base=+0.193)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.467 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.193)

- **PATRÓN** `T_h` > `103.8914` → IC=+0.295 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.8914 (IC base=+0.286)

- **PATRÓN** `ratio` > `1.0474` → IC=+0.373 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0474 (IC base=+0.286)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `80.0063` → IC=+0.269 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 80.0063 (IC base=+0.247)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.428 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.247)

- **PATRÓN** `T_h` > `106.9024` → IC=+0.333 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 106.9024 (IC base=+0.318)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.349 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.318)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6174 sube el IC de +0.197 a +0.276 en UPDOWN_GBM#15min (n=1995). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7141 sube el IC de +0.212 a +0.277 en UPDOWN_GBM#BTC#15min (n=432). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6603 sube el IC de +0.138 a +0.263 en UPDOWN_GBM#ETH#15min (n=411). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.186 a +0.278 en UPDOWN_GBM#SOL#15min (n=241). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5758 sube el IC de +0.202 a +0.289 en UPDOWN_GBM#XRP#15min (n=509). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6429 sube el IC de -0.066 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=742). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.024 a +0.277 en UPDOWN_GBM_15M_TARDIO (n=2272). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.084 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=219). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.5472 sube el IC de -0.193 a +0.294 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6603 sube el IC de +0.151 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2751 sube el IC de +0.234 a +0.281 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=764). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.6071 sube el IC de -0.174 a +0.198 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=51). Ya aplicado como kelly_boost=+0.99€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.041 a +0.271 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=378). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.036 a +0.296 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=582). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8411 sube el IC de +0.290 a +0.328 en UPDOWN_GBM_IBS_ALTO (n=775). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.285 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=425). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8743 sube el IC de +0.295 a +0.348 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=313). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7872 sube el IC de +0.354 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=476). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.360 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=261). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.344 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=216). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1473 | +0.097 | +193.49€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1473 | +0.097 | +193.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1120 | +0.106 | +166.99€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1120 | +0.106 | +166.99€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 5 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 67 | +0.123 | +17.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 67 | +0.123 | +17.79€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 33 | +0.014 | -5.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 33 | +0.014 | -5.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 27 | +0.017 | -5.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 27 | +0.017 | -5.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 6 | +0.000 | +0.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 6 | +0.000 | +0.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 31529 | -0.087 | -4089.53€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1628 | -0.021 | -212.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 29901 | -0.091 | -3876.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4135 | -0.109 | -670.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4135 | -0.109 | -670.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1628 | -0.021 | -212.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1628 | -0.021 | -212.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3729 | -0.108 | -858.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3729 | -0.108 | -858.51€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8169 | -0.015 | -769.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8169 | -0.015 | -769.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7788 | -0.097 | -450.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7788 | -0.097 | -450.03€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6080 | -0.162 | -1127.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6080 | -0.162 | -1127.65€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 22887 | -0.022 | +3766.31€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5927 | +0.001 | +1757.71€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 16960 | -0.030 | +2008.61€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 22887 | -0.022 | +3766.31€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5927 | +0.001 | +1757.71€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 16960 | -0.030 | +2008.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1486 | -0.102 | -190.28€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 176 | -0.045 | -19.67€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 788 | -0.089 | -95.94€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 152 | -0.039 | -14.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 107318 | +0.113 | -5167.47€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15469 | +0.184 | -467.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 448 | -0.060 | -56.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 84638 | +0.101 | -4397.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6763 | +0.106 | -245.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14061 | +0.100 | -1074.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 49 | -0.147 | +8.51€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 13997 | +0.102 | -1071.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 21451 | +0.130 | -389.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4741 | +0.199 | -141.53€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14037 | +0.115 | -171.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2631 | +0.095 | -53.49€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14107 | +0.091 | -1229.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 57 | -0.110 | -7.74€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14035 | +0.092 | -1210.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 22789 | +0.124 | -435.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6138 | +0.177 | -83.93€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 14188 | +0.105 | -287.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2451 | +0.101 | -54.83€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 20830 | +0.114 | -1177.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4432 | +0.188 | -252.98€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 351 | -0.021 | -2.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 14366 | +0.093 | -784.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1681 | +0.131 | -137.35€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14080 | +0.098 | -861.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 52 | -0.037 | +9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14015 | +0.099 | -871.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 17077 | +0.195 | -1044.94€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 17077 | +0.195 | -1044.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3995 | +0.173 | -382.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3995 | +0.173 | -382.86€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1697 | +0.204 | -12.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1697 | +0.204 | -12.61€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3939 | +0.183 | -315.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3939 | +0.183 | -315.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3484 | +0.243 | -107.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3484 | +0.243 | -107.88€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3883 | +0.191 | -240.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3883 | +0.191 | -240.34€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 799 | +0.433 | -17.67€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 799 | +0.433 | -17.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 313 | +0.443 | +0.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 313 | +0.443 | +0.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 304 | +0.431 | -6.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 304 | +0.431 | -6.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 170 | +0.413 | -8.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 170 | +0.413 | -8.58€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 59236 | +0.198 | -4576.02€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 59236 | +0.198 | -4576.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10196 | +0.179 | -1140.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10196 | +0.179 | -1140.19€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9492 | +0.222 | -351.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9492 | +0.222 | -351.33€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10212 | +0.175 | -1174.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10212 | +0.175 | -1174.85€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9576 | +0.218 | -381.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9576 | +0.218 | -381.83€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9813 | +0.202 | -655.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9813 | +0.202 | -655.02€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9947 | +0.192 | -872.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9947 | +0.192 | -872.80€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 22504 | +0.115 | +105.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 22504 | +0.115 | +105.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11172 | +0.118 | +107.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11172 | +0.118 | +107.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11332 | +0.111 | -2.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11332 | +0.111 | -2.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1649 | +0.289 | -24.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1649 | +0.289 | -24.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 738 | +0.280 | -16.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 738 | +0.280 | -16.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 796 | +0.287 | -11.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 796 | +0.287 | -11.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 115 | +0.346 | +3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 115 | +0.346 | +3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 729 | +0.437 | -2.35€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 729 | +0.437 | -2.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 349 | +0.434 | -3.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 349 | +0.434 | -3.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 334 | +0.441 | +0.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 334 | +0.441 | +0.67€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1257 | +0.066 | -67.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 442 | +0.052 | -40.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 815 | +0.073 | -27.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 65 | +0.112 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 65 | +0.112 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 992 | +0.071 | -36.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 177 | +0.064 | -9.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 815 | +0.073 | -27.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 200 | +0.020 | -34.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 200 | +0.020 | -34.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 42667 | +0.098 | -1226.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3486 | +0.089 | +26.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 39181 | +0.099 | -1253.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 23749 | +0.102 | -340.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3486 | +0.089 | +26.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 20263 | +0.104 | -366.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8319 | +0.107 | -40.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8319 | +0.107 | -40.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10599 | +0.080 | -846.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10599 | +0.080 | -846.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 858 | +0.209 | -102.37€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 858 | +0.209 | -102.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 858 | +0.209 | -102.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 858 | +0.209 | -102.37€ | 2 | 4 |
| ✅ GBM_LATE_15M | 30086 | +0.087 | +14766.71€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 30086 | +0.087 | +14766.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5048 | +0.200 | +3835.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5048 | +0.200 | +3835.70€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4493 | +0.178 | +3211.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4493 | +0.178 | +3211.20€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 5314 | +0.200 | +4002.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5314 | +0.200 | +4002.00€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4298 | +0.028 | +1047.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4298 | +0.028 | +1047.95€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4286 | -0.032 | +941.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4286 | -0.032 | +941.29€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6647 | -0.039 | +1728.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6647 | -0.039 | +1728.57€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 32209 | +0.088 | +17172.24€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 32209 | +0.088 | +17172.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6161 | +0.013 | +3221.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6161 | +0.013 | +3221.44€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6699 | +0.016 | +1418.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6699 | +0.016 | +1418.13€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4567 | +0.268 | +4703.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4567 | +0.268 | +4703.84€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5342 | +0.009 | +1147.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5342 | +0.009 | +1147.18€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5199 | +0.035 | +2070.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5199 | +0.035 | +2070.09€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4241 | +0.281 | +4611.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4241 | +0.281 | +4611.56€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 24195 | +0.171 | +18532.26€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 24195 | +0.171 | +18532.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3640 | +0.214 | +3004.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3640 | +0.214 | +3004.39€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3821 | +0.148 | +2769.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3821 | +0.148 | +2769.20€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3822 | +0.212 | +3096.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3822 | +0.212 | +3096.10€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4070 | +0.135 | +2955.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4070 | +0.135 | +2955.21€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4528 | +0.121 | +3252.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4528 | +0.121 | +3252.37€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4314 | +0.206 | +3454.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4314 | +0.206 | +3454.98€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6534 | +0.138 | +3073.72€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6534 | +0.138 | +3073.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 308 | +0.132 | +158.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 308 | +0.132 | +158.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1879 | +0.142 | +993.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1879 | +0.142 | +993.85€ | 0 | 31 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1962 | +0.154 | +966.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1962 | +0.154 | +966.03€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1497 | +0.113 | +559.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1497 | +0.113 | +559.00€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 514 | +0.134 | +218.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 514 | +0.134 | +218.86€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO | 30348 | +0.178 | +23178.27€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 30348 | +0.178 | +23178.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4808 | +0.227 | +4201.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4808 | +0.227 | +4201.77€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4731 | +0.150 | +3107.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4731 | +0.150 | +3107.51€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5043 | +0.227 | +4365.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5043 | +0.227 | +4365.99€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4934 | +0.135 | +3465.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4934 | +0.135 | +3465.73€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5316 | +0.120 | +3581.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5316 | +0.120 | +3581.85€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5516 | +0.211 | +4455.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5516 | +0.211 | +4455.41€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8515 | +0.172 | +5632.64€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 8515 | +0.172 | +5632.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2054 | +0.167 | +1488.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2054 | +0.167 | +1488.35€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2784 | +0.177 | +1829.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2784 | +0.177 | +1829.03€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 880 | +0.151 | +503.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 880 | +0.151 | +503.30€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2132 | +0.069 | +772.26€ | 0 | 13 |
| ✅ GBM_LATE_60M#60min | 2132 | +0.069 | +772.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 794 | +0.089 | +270.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 794 | +0.089 | +270.88€ | 0 | 17 |
| ✅ GBM_LATE_60M#ETH | 687 | +0.072 | +315.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 687 | +0.072 | +315.38€ | 2 | 15 |
| ✅ GBM_LATE_60M#SOL | 651 | +0.042 | +186.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 651 | +0.042 | +186.00€ | 2 | 9 |
| 🚫 GBM_LATE_60M_FADE | 428 | -0.246 | -16.22€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 428 | -0.246 | -16.22€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 161 | -0.218 | -5.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 161 | -0.218 | -5.44€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 143 | -0.245 | -5.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 143 | -0.245 | -5.01€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 124 | -0.278 | -5.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 124 | -0.278 | -5.77€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 868 | +0.091 | +224.33€ | 0 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 868 | +0.091 | +224.33€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 327 | +0.081 | +73.57€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 327 | +0.081 | +73.57€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 291 | +0.060 | +36.76€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 291 | +0.060 | +36.76€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 250 | +0.139 | +114.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 250 | +0.139 | +114.00€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 117 | +0.248 | +95.63€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 117 | +0.248 | +95.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 117 | +0.248 | +95.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 117 | +0.248 | +95.63€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2450 | +0.106 | +678.06€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2450 | +0.106 | +678.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2450 | +0.106 | +678.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2450 | +0.106 | +678.06€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 413 | -0.073 | -33.24€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 413 | -0.073 | -33.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 110 | -0.045 | -3.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 110 | -0.045 | -3.37€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 154 | -0.026 | -5.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 154 | -0.026 | -5.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2503 | +0.020 | +63.72€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2503 | +0.020 | +63.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 128 | +0.023 | -2.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 128 | +0.023 | -2.10€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 347 | +0.024 | +28.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 347 | +0.024 | +28.46€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 183 | -0.013 | -3.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 183 | -0.013 | -3.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 993 | +0.033 | +33.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 993 | +0.033 | +33.39€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 582 | +0.005 | -2.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 582 | +0.005 | -2.98€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 270 | +0.022 | +10.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 270 | +0.022 | +10.88€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1269 | -0.042 | -25.01€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1269 | -0.042 | -25.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 359 | -0.040 | -12.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 359 | -0.040 | -12.76€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 428 | -0.030 | -2.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 428 | -0.030 | -2.39€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 482 | -0.054 | -9.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 482 | -0.054 | -9.86€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 3608 | -0.016 | +84.59€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1689 | -0.024 | +6.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1919 | -0.010 | +78.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 100 | +0.020 | +9.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 51 | +0.066 | +10.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 49 | -0.029 | -1.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 864 | +0.002 | +48.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 402 | -0.005 | +12.39€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 462 | +0.009 | +36.12€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 420 | -0.014 | +16.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 202 | -0.039 | -2.35€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 218 | +0.009 | +19.28€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 726 | -0.040 | -28.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 329 | -0.053 | -24.11€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 397 | -0.029 | -3.98€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 712 | -0.022 | +10.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 341 | -0.031 | +1.56€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 371 | -0.015 | +9.10€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 786 | -0.015 | +26.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 364 | -0.016 | +8.35€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 422 | -0.014 | +18.64€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 34555 | -0.005 | +1562.46€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 34555 | -0.005 | +1562.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6129 | +0.022 | +786.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6129 | +0.022 | +786.79€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5222 | -0.031 | -78.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5222 | -0.031 | -78.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6225 | +0.017 | +565.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6225 | +0.017 | +565.76€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5002 | -0.054 | -170.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5002 | -0.054 | -170.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5824 | -0.009 | +194.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5824 | -0.009 | +194.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6153 | +0.012 | +264.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6153 | +0.012 | +264.35€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6064 | -0.061 | -153.85€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6064 | -0.061 | -153.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1467 | -0.084 | -41.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1467 | -0.084 | -41.73€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 689 | -0.127 | -33.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 689 | -0.127 | -33.66€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1793 | -0.078 | -34.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1793 | -0.078 | -34.24€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3347 | +0.004 | -3.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3347 | +0.004 | -3.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1317 | +0.006 | +6.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1317 | +0.006 | +6.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 86983 | -0.073 | +1811.75€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 86983 | -0.073 | +1811.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 14853 | -0.076 | +886.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 14853 | -0.076 | +886.73€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 13271 | -0.096 | -699.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 13271 | -0.096 | -699.82€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 15126 | -0.067 | +788.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 15126 | -0.067 | +788.28€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 12807 | -0.093 | -259.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 12807 | -0.093 | -259.70€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 15849 | -0.050 | +374.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 15849 | -0.050 | +374.05€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 15077 | -0.063 | +722.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 15077 | -0.063 | +722.21€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7892 | -0.028 | -134.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7892 | -0.028 | -134.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1823 | -0.037 | -12.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1823 | -0.037 | -12.71€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2234 | -0.024 | -28.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2234 | -0.024 | -28.55€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1070 | -0.044 | -16.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1070 | -0.044 | -16.85€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 766 | -0.022 | -24.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 766 | -0.022 | -24.97€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1275 | +0.110 | +443.08€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1139 | +0.116 | +430.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 264 | +0.139 | +133.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 264 | +0.139 | +133.98€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 218 | +0.109 | +62.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 218 | +0.109 | +62.88€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 235 | +0.103 | +84.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 235 | +0.103 | +84.60€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 199 | +0.127 | +88.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 199 | +0.127 | +88.13€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 223 | +0.096 | +60.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 223 | +0.096 | +60.90€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 736 | -0.035 | -43.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 736 | -0.035 | -43.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 147 | +0.003 | +6.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 147 | +0.003 | +6.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 104 | -0.057 | -10.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 104 | -0.057 | -10.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 208 | -0.052 | -23.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 208 | -0.052 | -23.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 157 | -0.022 | -7.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 157 | -0.022 | -7.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 120 | -0.049 | -9.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 120 | -0.049 | -9.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 694 | -0.095 | -64.60€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 317 | -0.146 | -74.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 246 | -0.190 | -70.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 71 | +0.007 | -4.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 245 | -0.059 | -3.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 176 | -0.067 | -6.25€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 69 | -0.035 | +3.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 132 | -0.037 | +13.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 104 | -0.057 | +7.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 28 | +0.033 | +5.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 526 | -0.123 | -68.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 168 | -0.006 | +4.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 833 | -0.201 | -40.70€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 345 | -0.195 | -30.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 295 | -0.197 | -30.77€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 50 | -0.173 | +0.17€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 284 | -0.217 | -26.27€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 243 | -0.227 | -32.11€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 204 | -0.184 | +16.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 186 | -0.181 | +12.51€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 18 | -0.180 | +3.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 724 | -0.204 | -50.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 109 | -0.176 | +9.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 349 | +0.403 | +268.41€ | 0 | 14 |
| ✅ RESOLUTION_SNIPER#BTC | 39 | +0.134 | +0.80€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 39 | +0.134 | +0.80€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 89 | +0.368 | +73.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 89 | +0.368 | +73.91€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 221 | +0.460 | +193.70€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 221 | +0.460 | +193.70€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 349 | +0.403 | +268.41€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 582 | +0.034 | +19.45€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 582 | +0.034 | +19.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 283 | +0.033 | +5.63€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 283 | +0.033 | +5.63€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 40 | +0.071 | +1.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 40 | +0.071 | +1.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 62 | +0.000 | -1.18€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 62 | +0.000 | -1.18€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 197 | +0.038 | +13.11€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 197 | +0.038 | +13.11€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 2980 | -0.022 | -120.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2980 | -0.022 | -120.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 897 | -0.021 | -31.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 897 | -0.021 | -31.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 576 | -0.024 | -24.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 576 | -0.024 | -24.20€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1351 | -0.020 | -50.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1351 | -0.020 | -50.64€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 79 | -0.043 | -6.02€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 79 | -0.043 | -6.02€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 41 | +0.012 | -1.58€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 41 | +0.012 | -1.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9149 | +0.021 | +120.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9149 | +0.021 | +120.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2529 | +0.022 | +28.61€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2529 | +0.022 | +28.61€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2091 | +0.031 | +52.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2091 | +0.031 | +52.90€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2774 | +0.013 | +8.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2774 | +0.013 | +8.56€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1755 | +0.022 | +30.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1755 | +0.022 | +30.69€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8181 | +0.013 | -43.99€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8181 | +0.013 | -43.99€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3247 | +0.017 | -7.36€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3247 | +0.017 | -7.36€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3253 | +0.011 | -22.46€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3253 | +0.011 | -22.46€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1681 | +0.007 | -14.16€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1681 | +0.007 | -14.16€ | 1 | 0 |
| ✅ UPDOWN_GBM | 48238 | +0.038 | +3326.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 12476 | +0.073 | +2471.34€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1678 | +0.004 | +7.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 31015 | +0.030 | +821.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2887 | +0.003 | +27.90€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4893 | +0.076 | +621.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 917 | +0.159 | +406.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3943 | +0.057 | +216.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 9271 | +0.046 | +721.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1622 | +0.087 | +370.50€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 449 | +0.012 | +5.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5825 | +0.049 | +311.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1307 | +0.005 | +33.20€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 68 | -0.086 | +1.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5581 | +0.045 | +400.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 877 | +0.144 | +328.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4676 | +0.026 | +72.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 10601 | +0.028 | +517.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3117 | +0.051 | +394.59€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 442 | +0.007 | +8.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6009 | +0.023 | +116.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 973 | -0.002 | -6.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 60 | -0.113 | +3.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 10839 | +0.018 | +329.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2980 | +0.028 | +227.30€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 433 | -0.003 | -1.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6767 | +0.018 | +106.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 607 | +0.004 | +1.43€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 52 | -0.148 | -3.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7051 | +0.041 | +737.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2963 | +0.087 | +743.71€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 293 | -0.002 | -3.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3795 | +0.008 | -2.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 180 | -0.115 | +0.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 634 | +0.354 | +219.18€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 634 | +0.354 | +219.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 347 | +0.360 | +118.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 347 | +0.360 | +118.58€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 287 | +0.344 | +100.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 287 | +0.344 | +100.61€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 14144 | -0.033 | +3130.04€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 14144 | -0.033 | +3130.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1011 | -0.052 | +381.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1011 | -0.052 | +381.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2574 | -0.117 | +58.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2574 | -0.117 | +58.09€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 546 | +0.199 | +408.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 546 | +0.199 | +408.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1633 | +0.210 | +1028.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1633 | +0.210 | +1028.29€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4198 | -0.064 | +581.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4198 | -0.064 | +581.13€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4182 | -0.072 | +672.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4182 | -0.072 | +672.82€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 163 | +0.039 | +8.29€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 163 | +0.039 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 163 | +0.039 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 163 | +0.039 | +8.29€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1033 | +0.290 | +854.69€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1033 | +0.290 | +854.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 566 | +0.285 | +434.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 566 | +0.285 | +434.66€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 467 | +0.295 | +420.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 467 | +0.295 | +420.03€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 744 | -0.111 | -82.52€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 744 | -0.111 | -82.52€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 220 | -0.081 | -16.26€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 220 | -0.081 | -16.26€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 75 | -0.188 | -6.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 75 | -0.188 | -6.89€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2733 | +0.305 | +1353.40€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 958 | +0.257 | +142.14€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1043 | +0.296 | +460.38€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 732 | +0.377 | +750.88€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.052) — sin ventaja clara. oversold(IBS<0.3): IC=+0.049 n=16990 | neutral: IC=+0.038 n=17973 | overbought(IBS>0.7): IC=+0.091 n=17186
  - _Datos_: n=54015 IC=+0.060 PNL=+7064.60€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 595 celda(s) pasan gate riguroso completo de 2358 evaluadas (n>=40) y 3348 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.028 < 0.08 — monitorear
  - _Datos_: n=2980 IC=+0.028 PNL=+227.30€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1043/15 IC=+0.296 PNL=+460.38€ | BTC: n=958/15 IC=+0.257 PNL=+142.14€ | SOL: n=732/15 IC=+0.377 PNL=+750.88€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 30 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: 48176 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.122 n=442/60 | contraria IC=+0.171 n=433 | gap=-0.050 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=341, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 199 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=973/40 IC=-0.002 PNL=-6.73€ | BTC#60min: n=1307/40 IC=+0.005 PNL=+33.20€ | SOL#60min: n=607/40 IC=+0.004 PNL=+1.43€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=396758 | tras_1loss IC=+0.085 n=306198 | tras_2loss IC=+0.054 n=127163/40 | gap=-0.005 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.021 n=5953 | contrario_BTC IC=+0.035 n=5259/40 | gap=+0.013 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.209 > 0.08 con n=410 PNL=+320.12€
  - _Datos_: n=410 IC=+0.209 PNL=+320.12€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.221 > 0.08 con n=474 PNL=+367.25€
  - _Datos_: n=474 IC=+0.221 PNL=+367.25€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.235 > 0.08 con n=47 PNL=+34.80€
  - _Datos_: n=47 IC=+0.235 PNL=+34.80€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.331 > 0.1 con n=2231 PNL=+1224.30€
  - _Datos_: n=2231 IC=+0.331 PNL=+1224.30€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=386 IC=+0.064 PNL=+39.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=386 IC=+0.064 PNL=+39.51€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=58 IC=+0.167 PNL=+33.93€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=58 IC=+0.167 PNL=+33.93€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=46188 IC=+0.037 PNL=+3187.79€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=46188 IC=+0.037 PNL=+3187.79€

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
  - _Estado_: n=1986 IC=+0.004 PNL=-4.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1986 IC=+0.004 PNL=-4.35€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=901 IC=-0.002 PNL=+32.25€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=901 IC=-0.002 PNL=+32.25€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=619 IC=+0.018 PNL=+27.70€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=619 IC=+0.018 PNL=+27.70€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.197 > 0.1 con n=2659 PNL=+1827.29€
  - _Datos_: n=2659 IC=+0.197 PNL=+1827.29€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1480 IC=+0.055 PNL=+106.88€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1480 IC=+0.055 PNL=+106.88€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1622 IC=+0.087 PNL=+370.50€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1622 IC=+0.087 PNL=+370.50€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.091 > 0.08 con n=7129 PNL=+1857.11€
  - _Datos_: n=7129 IC=+0.091 PNL=+1857.11€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=191 IC=-0.257 PNL=-9.19€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=191 IC=-0.257 PNL=-9.19€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=312 IC=-0.038 PNL=-4.80€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=312 IC=-0.038 PNL=-4.80€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=652 IC=+0.015 PNL=+44.82€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=652 IC=+0.015 PNL=+44.82€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=70 IC=+0.069 PNL=+5.34€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=70 IC=+0.069 PNL=+5.34€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6351 IC=+0.001 PNL=+10.04€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6351 IC=+0.001 PNL=+10.04€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=74 PNL=+21.75€
  - _Datos_: n=74 IC=+0.184 PNL=+21.75€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.248 n=117) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=117 IC=+0.248 PNL=+95.63€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=8817 IC=+0.039 PNL=+567.42€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=8817 IC=+0.039 PNL=+567.42€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2947 IC=+0.056 PNL=+371.06€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2947 IC=+0.056 PNL=+371.06€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.08 con n=406 PNL=+119.99€
  - _Datos_: n=406 IC=+0.108 PNL=+119.99€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.147 > 0.08 con n=740 PNL=+195.00€
  - _Datos_: n=740 IC=+0.147 PNL=+195.00€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.107 > 0.08 con n=571 PNL=+302.83€
  - _Datos_: n=571 IC=+0.107 PNL=+302.83€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64171 IC=+0.118 PNL=+23873.79€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64171 IC=+0.118 PNL=+23873.79€

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
  - _Estado_: n=7121 IC=+0.043 PNL=+593.27€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7121 IC=+0.043 PNL=+593.27€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=731 PNL=+274.76€
  - _Datos_: n=731 IC=+0.118 PNL=+274.76€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=179 IC=-0.064 PNL=+28.99€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=179 IC=-0.064 PNL=+28.99€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.450 > 0.1 con n=1277 PNL=+1254.23€
  - _Datos_: n=1277 IC=+0.450 PNL=+1254.23€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=17596 IC=+0.060 PNL=+2281.46€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=17596 IC=+0.060 PNL=+2281.46€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.1 con n=4316 PNL=+2471.36€
  - _Datos_: n=4316 IC=+0.204 PNL=+2471.36€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.157 < -0.1 con n=292 PNL=+24.96€
  - _Datos_: n=292 IC=-0.157 PNL=+24.96€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2285 IC=+0.054 PNL=+230.36€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2285 IC=+0.054 PNL=+230.36€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=98 IC=-0.110 PNL=+3.48€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=98 IC=-0.110 PNL=+3.48€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.1 con n=536 PNL=+143.29€
  - _Datos_: n=536 IC=+0.121 PNL=+143.29€

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
  - _Estado_: n=21728 IC=-0.136 PNL=+1553.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=21728 IC=-0.136 PNL=+1553.99€

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
  - _Estado_: n=2261 IC=+0.138 PNL=+1274.64€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2261 IC=+0.138 PNL=+1274.64€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.08 con n=2620 PNL=+1814.65€
  - _Datos_: n=2620 IC=+0.198 PNL=+1814.65€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=5032 IC=+0.030 PNL=+252.25€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5032 IC=+0.030 PNL=+252.25€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.089 > 0.08 con n=2442 PNL=+1315.61€
  - _Datos_: n=2442 IC=+0.089 PNL=+1315.61€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.212 > 0.08 con n=574 PNL=+307.06€
  - _Datos_: n=574 IC=+0.212 PNL=+307.06€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.229 < -0.1 con n=2159 PNL=-181.60€
  - _Datos_: n=2159 IC=-0.229 PNL=-181.60€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6359 IC=+0.183 PNL=+4485.72€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6359 IC=+0.183 PNL=+4485.72€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=86 PNL=+31.10€
  - _Datos_: n=86 IC=+0.102 PNL=+31.10€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2291 IC=+0.069 PNL=+705.27€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2291 IC=+0.069 PNL=+705.27€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=2092 PNL=+1469.57€
  - _Datos_: n=2092 IC=+0.179 PNL=+1469.57€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3494 IC=-0.032 PNL=+898.91€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3494 IC=-0.032 PNL=+898.91€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=593 PNL=-49.25€
  - _Datos_: n=593 IC=+0.087 PNL=-49.25€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.238 > 0.08 con n=3718 PNL=-322.50€
  - _Datos_: n=3718 IC=+0.238 PNL=-322.50€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=45 IC=+0.011 PNL=+6.42€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=45 IC=+0.011 PNL=+6.42€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1253) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1253 IC=+0.102 PNL=+293.42€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.322 > 0.08 con n=318 PNL=+106.11€
  - _Datos_: n=318 IC=+0.322 PNL=+106.11€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.409 n=470) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=470 IC=+0.409 PNL=+661.82€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=10196 IC=+0.179 PNL=-1140.19€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=10196 IC=+0.179 PNL=-1140.19€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.1 con n=160 PNL=+100.23€
  - _Datos_: n=160 IC=+0.210 PNL=+100.23€
