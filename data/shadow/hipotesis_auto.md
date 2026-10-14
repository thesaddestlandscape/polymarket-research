# Hipótesis automáticas — 2026-10-14 12:44 UTC
_Generado por shadow_postmortem.py sobre 894250 resoluciones (PNL=+114217.99€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.258 (n=163)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=602)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.240 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.133)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.197 (n=255)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 68.0 (IC base=+0.133)

- **PATRÓN** `banda_hit_calibrado` > `0.7976` → IC=+0.271 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7976 (IC base=+0.133)

- **PATRÓN** `banda_z` > `9.563` → IC=+0.218 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.563 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=808)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.133)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.237 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.215 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.6176` → IC=+0.263 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6176 (IC base=+0.139)

- **PATRÓN** `banda_z` > `10.085` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.085 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=710)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.139)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.234 (n=107)

- **FILTRO** `banda_hit_calibrado` < `0.8019` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8019
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=96)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=115)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=99)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=102)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=114)

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.125)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `906.0197` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 906.0197 (IC base=+0.125)

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
- **FILTRO** `restante_s_al_confirmar` < `143.87` → IC=-0.206 (n=9379)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.87
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=28138)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.69` → IC=-0.264 (n=1107)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.69
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3323)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.47` → IC=-0.300 (n=1032)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.47
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3098)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.08` → IC=-0.217 (n=2436)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.08
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7309)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.52` → IC=-0.292 (n=1818)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.52
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=5454)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.210 (n=19912)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=4144)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `9345.8788` → IC=+0.178 (n=1858)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9345.8788 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=16769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.132 (n=20367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=15548)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=6879)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7283.3362` → IC=+0.160 (n=2648)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7283.3362 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=1974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1933)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2423)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `16202.3525` → IC=+0.206 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16202.3525 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.194 (n=1739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=1942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=2487)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `16089.4675` → IC=+0.198 (n=641)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 16089.4675 (IC base=+0.188)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=443)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `6891.1913` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6891.1913 (IC base=+0.086)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.137 (n=1046)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.44 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `5854.7033` → IC=+0.126 (n=241)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 5854.7033 (IC base=+0.085)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=3876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.367 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.224 (n=1727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.359 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=2022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.147 (n=830)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.256 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=758)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2157.3615` → IC=+0.152 (n=420)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2157.3615 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.410 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=667)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=835)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.175 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.350 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `3371.7925` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3371.7925 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.253 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=16694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=14224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.232 (n=6966)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=3881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.178 (n=3676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=3756)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=1841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.233 (n=1235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.315 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.225)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=3814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=3658)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3010)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=3323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.246)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.351 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.246)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=3740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=2400)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.195 (n=2758)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.431 (n=653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.427 (n=646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `7390.2621` → IC=+0.442 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7390.2621 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.448 (n=190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `18171.404` → IC=+0.439 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18171.404 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.444 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `4010.7815` → IC=+0.430 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4010.7815 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.403)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.403 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.403)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.403)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=21461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=21883)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=10122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=6910)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=9613)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4422)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3173)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=3673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=6892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=9165)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=4514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=3460)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.276 (n=3101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=8263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=8226)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.263 (n=3246)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=3566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=3629)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=3752)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=7795)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.21` → IC=+0.124 (n=7139)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.21 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=7627)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.43` → IC=+0.138 (n=7139)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.43 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=3857)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=3855)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=4704)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.85` → IC=+0.146 (n=3542)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.85 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=3938)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.132 (n=4172)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.136 (n=3582)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.311 (n=1029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.292 (n=1300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.378 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `4306.2044` → IC=+0.296 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4306.2044 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.288 (n=693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.284 (n=599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.353 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `5377.6935` → IC=+0.293 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5377.6935 (IC base=+0.282)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.384 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1720.692` → IC=+0.300 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1720.692 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.351)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.377 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.351)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.351)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.356 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.351)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.351)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.442 (n=340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.450 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.449 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.445)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.446 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.445)

- **PATRÓN** `libro_liquidez` > `2089.6231` → IC=+0.453 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2089.6231 (IC base=+0.445)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=87)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=73)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.302 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.379 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.272 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `987.2299` → IC=+0.270 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 987.2299 (IC base=+0.255)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=87)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=73)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.302 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.379 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.272 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `987.2299` → IC=+0.270 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 987.2299 (IC base=+0.255)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4757` → IC=+0.134 (n=12035)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.4757 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.9841` → IC=+0.244 (n=4013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9841 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.7682` → IC=+0.257 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7682 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.3692` → IC=+0.255 (n=3256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3692 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.968` → IC=+0.185 (n=4540)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.968 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.254 (n=3431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.259 (n=3433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.3023` → IC=+0.234 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3023 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.344` → IC=+0.225 (n=3857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.344 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=6562)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.5671` → IC=+0.141 (n=14775)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5671 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.5723` → IC=+0.187 (n=1033)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5723 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1501` → IC=+0.185 (n=5197)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1501 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `1.1942` → IC=+0.181 (n=5634)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.1942 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.053` → IC=+0.183 (n=2553)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.053 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2953` → IC=+0.231 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2953 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.6774` → IC=+0.208 (n=3199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6774 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.220 (n=9426)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 110.0 (IC base=+0.074)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.213 (n=886)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.346` → IC=+0.194 (n=2646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.346 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=1280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=1776)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.9738` → IC=+0.273 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9738 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.084` → IC=+0.277 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.084 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.244 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.2724` → IC=+0.207 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2724 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=2776)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2095.424` → IC=+0.211 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2095.424 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.203 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.237 (n=1457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.240 (n=994)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0875` → IC=+0.265 (n=729)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0875 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5099` → IC=+0.254 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5099 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.236 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2861` → IC=+0.247 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2861 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.232 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6474` → IC=+0.246 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6474 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1584.11` → IC=+0.244 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1584.11 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.232 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.235 (n=943)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.259 (n=944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=2250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=2188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.967` → IC=+0.270 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.967 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.228 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.443` → IC=+0.259 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.443 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.244` → IC=+0.226 (n=2142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.244 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.229 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2768` → IC=+0.248 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2768 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.5138` → IC=+0.224 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5138 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4399` → IC=+0.249 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4399 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.185 (n=724)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0026 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0744` → IC=+0.170 (n=722)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0744 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.5867` → IC=+0.182 (n=1905)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.5867 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1275` → IC=+0.155 (n=1977)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1275 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.158` → IC=+0.151 (n=350)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.158 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.229` → IC=+0.143 (n=1983)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.229 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.144 (n=2165)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1913 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0955` → IC=+0.163 (n=790)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0955 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4576` → IC=+0.145 (n=2047)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4576 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4221` → IC=+0.140 (n=2047)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4221 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.171 (n=869)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 221.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.211 (n=909)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=2862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=2444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.342` → IC=+0.263 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.342 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.195 (n=2400)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.351` → IC=+0.216 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.351 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.6973` → IC=+0.208 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6973 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=3221)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `1999.301` → IC=+0.202 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1999.301 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.224 (n=2123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.4613` → IC=+0.222 (n=2123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4613 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.238 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.528` → IC=+0.259 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.528 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3474` → IC=+0.256 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3474 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7249` → IC=+0.219 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7249 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7325` → IC=+0.230 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7325 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2074.8384` → IC=+0.230 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2074.8384 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.219 (n=2227)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.141 (n=140)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=3268)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.159 (n=497)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0036 (IC base=+0.050)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.221 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` < `0.1838` → IC=+0.331 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1838 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.068` → IC=+0.183 (n=1058)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.068 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.333 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `1.2365` → IC=+0.351 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2365 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.1776` → IC=+0.325 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1776 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.339 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4113` → IC=+0.352 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4113 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.334 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.0944` → IC=+0.167 (n=853)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.0944 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.311` → IC=+0.151 (n=419)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.311 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8511` → IC=+0.147 (n=972)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8511 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.201 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.5196` → IC=+0.150 (n=1244)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5196 (IC base=+0.033)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=501)

- **FILTRO** `ibs_20min` < `0.2909` → IC=-0.198 (n=147)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2909
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=443)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.132 (n=3247)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=1624)

- **FILTRO** `sigma_ewma_delta_pct` > `8.659` → IC=-0.232 (n=501)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.659
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4370)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.176 (n=202)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.7857 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.9864` → IC=+0.286 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9864 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.5952` → IC=+0.255 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5952 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.125 (n=206)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.871` → IC=+0.257 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.871 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `1.0006` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0006 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1558` → IC=+0.270 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1558 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.286 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.259 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.150 (n=1624)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2222 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.265` → IC=+0.277 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.265 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.7102` → IC=+0.288 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7102 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.1612` → IC=+0.307 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1612 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.3955` → IC=+0.300 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3955 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6268` → IC=-0.179 (n=864)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6268
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2593)

- **FILTRO** `ibs_20min` < `0.73` → IC=-0.153 (n=2280)

  - _Acción_: SKIP cuando `ibs_20min` < 0.73
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=1177)

- **FILTRO** `ibs_20min` > `0.7585` → IC=-0.204 (n=1273)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7585
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=3820)

- **PATRÓN** `dist_vwap_pct` > `0.7462` → IC=+0.327 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7462 (IC base=-0.071)

- **PATRÓN** `dist_vwap_pct` < `0.2641` → IC=+0.303 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2641 (IC base=-0.071)

- **PATRÓN** `volumen_regimen` < `1.1432` → IC=+0.295 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1432 (IC base=-0.071)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.311 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.071)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.302 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=-0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.4272` → IC=+0.321 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4272 (IC base=-0.071)

- **PATRÓN** `volumen_spike_ratio` > `1.8611` → IC=+0.302 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8611 (IC base=-0.071)

- **PATRÓN** `dist_vwap_pct` > `0.7968` → IC=+0.278 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7968 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `1.0811` → IC=+0.283 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0811 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.1038` → IC=+0.282 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1038 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `2.1737` → IC=+0.258 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1737 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` > `1.4311` → IC=+0.263 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4311 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.204 (n=5296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.8859` → IC=+0.278 (n=7194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8859 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.9405` → IC=+0.292 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9405 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.644` → IC=+0.157 (n=7098)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.644 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.1749` → IC=+0.255 (n=5830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1749 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6888` → IC=+0.261 (n=5207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6888 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.271 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6391` → IC=+0.265 (n=3117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6391 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.286 (n=8911)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.162 (n=5100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.009 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5374` → IC=+0.160 (n=13441)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5374 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1707` → IC=+0.260 (n=4431)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1707 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.8773` → IC=+0.254 (n=3177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8773 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1967` → IC=+0.265 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1967 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.314 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5835` → IC=+0.285 (n=2965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5835 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.272` → IC=+0.279 (n=3054)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.272 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.288 (n=6645)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3697` → IC=-0.163 (n=1445)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3697
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=2942)

- **FILTRO** `ibs_20min` > `0.7516` → IC=-0.200 (n=908)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7516
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=2728)

- **FILTRO** `sigma_ewma_delta_pct` > `4.564` → IC=-0.196 (n=796)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.564
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=2840)

- **PATRÓN** `ibs_20min` > `0.9143` → IC=+0.296 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9143 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.109` → IC=+0.208 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.109 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2287` → IC=+0.294 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2287 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.227 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `2.2395` → IC=+0.261 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2395 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.260 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.034)

- **PATRÓN** `ibs_20min` < `0.1601` → IC=+0.156 (n=911)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1601 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.2216` → IC=+0.406 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2216 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.4825` → IC=+0.403 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4825 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.394 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1124` → IC=+0.205 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1124 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.197` → IC=+0.181 (n=1532)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.197 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6802` → IC=+0.190 (n=1370)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.6802 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.221 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.205 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.4806` → IC=+0.191 (n=503)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4806 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `193.0` → IC=+0.238 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 193.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1067` → IC=+0.232 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1067 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.235 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6206 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0745` → IC=+0.228 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0745 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.294 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.272 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5491` → IC=+0.238 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5491 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1853` → IC=+0.248 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1853 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.299 (n=785)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=2476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=2113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.293 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.272 (n=2036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `1.6152` → IC=+0.265 (n=2265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6152 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.271 (n=2766)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1984.4556` → IC=+0.283 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1984.4556 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.331 (n=908)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.1806` → IC=+0.306 (n=880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1806 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.327 (n=765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.3636` → IC=+0.293 (n=1999)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3636 (IC base=+0.291)

- **PATRÓN** `ibs_20min` > `0.1084` → IC=+0.292 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1084 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.717` → IC=+0.307 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.717 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.1958` → IC=+0.288 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1958 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.3395` → IC=+0.304 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3395 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.7195` → IC=+0.302 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7195 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `2.6446` → IC=+0.298 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6446 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2069.345` → IC=+0.314 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2069.345 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.292 (n=1655)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.291)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7467` → IC=-0.185 (n=941)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7467
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=2827)

- **PATRÓN** `ibs_20min` > `0.8878` → IC=+0.172 (n=882)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8878 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3648` → IC=+0.228 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3648 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0152` → IC=+0.240 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0152 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.1644` → IC=+0.233 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1644 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.244 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.3994` → IC=+0.255 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3994 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.7761` → IC=+0.232 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7761 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.261 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1886` → IC=+0.225 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1886 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.0403` → IC=+0.230 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0403 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.103` → IC=+0.238 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.103 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.291 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.8148` → IC=+0.263 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8148 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.4671` → IC=+0.255 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4671 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.253 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 129.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7636` → IC=-0.200 (n=1680)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7636
  - _Potencial_: sin este filtro IC_bueno=+0.297 (n=1680)

- **FILTRO** `ibs_20min` > `0.6552` → IC=-0.234 (n=832)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6552
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=2504)

- **FILTRO** `sigma_ewma_delta_pct` > `8.58` → IC=-0.235 (n=379)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.58
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2957)

- **PATRÓN** `ibs_20min` > `0.7636` → IC=+0.297 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7636 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.2124` → IC=+0.331 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2124 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.171 (n=526)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.8488` → IC=+0.326 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8488 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.316 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6297 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.313 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.350 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.336 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.340 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.141 (n=2212)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5556 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2801` → IC=+0.243 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2801 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.7096` → IC=+0.260 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7096 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `1.1866` → IC=+0.236 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1866 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.2188` → IC=+0.241 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2188 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.247 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.4243` → IC=+0.252 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4243 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.269 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.030)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.341 (n=1625)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.311 (n=870)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.295)

- **PATRÓN** `ibs_20min` > `0.6512` → IC=+0.327 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6512 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2114` → IC=+0.326 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2114 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.787` → IC=+0.316 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.787 (IC base=+0.295)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.305 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.295)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.343 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.295)

- **PATRÓN** `volumen_spike_ratio` > `1.43` → IC=+0.307 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.43 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `2474.9303` → IC=+0.308 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2474.9303 (IC base=+0.295)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.330 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.329 (n=1278)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.187` → IC=+0.299 (n=844)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.187 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.305 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.297)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.322 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.3067` → IC=+0.298 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3067 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.522` → IC=+0.306 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.522 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.013` → IC=+0.298 (n=2285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.013 (IC base=+0.297)

- **PATRÓN** `volumen_regimen` < `0.7203` → IC=+0.298 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7203 (IC base=+0.297)

- **PATRÓN** `volumen_regimen` > `1.2298` → IC=+0.325 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2298 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.347 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` < `1.4172` → IC=+0.305 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4172 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` > `2.1376` → IC=+0.299 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1376 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `2433.3002` → IC=+0.302 (n=1712)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2433.3002 (IC base=+0.297)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.186 (n=3906)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0048 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.220 (n=3903)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3452` → IC=+0.188 (n=10297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3452 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=12159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.561` → IC=+0.232 (n=11701)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.561 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1663` → IC=+0.207 (n=4889)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1663 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.355` → IC=+0.255 (n=2312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.355 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1966` → IC=+0.169 (n=7765)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1966 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2937` → IC=+0.201 (n=1716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2937 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6037` → IC=+0.188 (n=3776)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6037 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2013.6902` → IC=+0.183 (n=10453)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2013.6902 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.195 (n=10624)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 99.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.186 (n=7484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.225 (n=3741)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=4203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.4954` → IC=+0.235 (n=11218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4954 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` < `0.1715` → IC=+0.174 (n=7868)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1715 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.135` → IC=+0.196 (n=1851)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.135 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1819` → IC=+0.165 (n=8017)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1819 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.226 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6255` → IC=+0.187 (n=3496)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6255 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.195 (n=8977)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 67.0 (IC base=+0.178)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.233 (n=658)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.226 (n=1965)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=1327)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.9231` → IC=+0.289 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9231 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.142` → IC=+0.329 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.142 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.269 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.207 (n=1852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.218 (n=2081)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2096.1051` → IC=+0.218 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2096.1051 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.244 (n=1016)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.242 (n=689)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.295 (n=668)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=1369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0057` → IC=+0.297 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0057 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.244 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.276 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4285` → IC=+0.258 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4285 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.67` → IC=+0.244 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.67 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1563.22` → IC=+0.255 (n=1518)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1563.22 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.243 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.220 (n=588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1622` → IC=+0.185 (n=1175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1622 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=1854)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.3545` → IC=+0.222 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3545 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.213 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.481` → IC=+0.226 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.481 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.169 (n=775)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6892 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.186 (n=278)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4131` → IC=+0.174 (n=575)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4131 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.4971` → IC=+0.162 (n=574)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4971 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `424.0` → IC=+0.161 (n=1684)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 424.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.166 (n=1844)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2319` → IC=+0.175 (n=1621)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2319 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6061` → IC=+0.203 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6061 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.661` → IC=+0.203 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.661 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.163 (n=1842)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2032 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.0703` → IC=+0.146 (n=1472)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0703 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1593` → IC=+0.148 (n=566)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1593 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.150 (n=1723)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4963 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7847` → IC=+0.147 (n=1149)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7847 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.168 (n=730)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 233.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.228 (n=1316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3992` → IC=+0.222 (n=1737)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3992 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=2048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.512` → IC=+0.292 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.512 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.230 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.776` → IC=+0.216 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.776 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7084` → IC=+0.226 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7084 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.218 (n=2328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1989.5584` → IC=+0.221 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1989.5584 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.246 (n=1483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.2518` → IC=+0.257 (n=1123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2518 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.284 (n=647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.3543` → IC=+0.251 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3543 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.616` → IC=+0.275 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.616 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.274 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7245` → IC=+0.243 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7245 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.7347` → IC=+0.242 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7347 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2069.52` → IC=+0.250 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2069.52 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.228 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.233)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.175 (n=1888)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0073 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4027` → IC=+0.166 (n=1888)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4027 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3141` → IC=+0.210 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3141 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1389` → IC=+0.195 (n=1190)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1389 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.202 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8559` → IC=+0.162 (n=1259)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8559 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.176 (n=781)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4237` → IC=+0.156 (n=617)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4237 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5013` → IC=+0.166 (n=617)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5013 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4726.7218` → IC=+0.194 (n=1258)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 4726.7218 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.161 (n=1830)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 144.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.156 (n=1983)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.007 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3873` → IC=+0.146 (n=1981)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3873 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6818` → IC=+0.187 (n=1981)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6818 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.155 (n=1953)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.878` → IC=+0.155 (n=697)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 6.878 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8582` → IC=+0.161 (n=1321)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8582 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.198 (n=299)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.134 (n=1231)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.808 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.130 (n=1846)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `4439.3642` → IC=+0.169 (n=1320)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4439.3642 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.135 (n=1202)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 94.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.130 (n=712)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0059 (IC base=+0.128)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.169 (n=971)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.01 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4377` → IC=+0.130 (n=1881)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4377 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=2179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.216 (n=2136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1958` → IC=+0.190 (n=1274)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1958 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.679` → IC=+0.267 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.679 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.1861` → IC=+0.142 (n=2136)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1861 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.137 (n=2164)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4387` → IC=+0.145 (n=691)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4387 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2851.5493` → IC=+0.211 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2851.5493 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.158 (n=685)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 21.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.142 (n=1916)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0093 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1071` → IC=+0.172 (n=726)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1071 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.220 (n=2181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.1983` → IC=+0.148 (n=2020)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1983 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.524` → IC=+0.130 (n=441)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 7.524 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.130 (n=2177)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1756 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.154 (n=284)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4523` → IC=+0.131 (n=672)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4523 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.132 (n=672)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2699.5616` → IC=+0.190 (n=987)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2699.5616 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.128 (n=2004)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 51.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.242 (n=1770)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.2817` → IC=+0.226 (n=1321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2817 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=2054)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.222 (n=1791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6538` → IC=+0.254 (n=1981)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6538 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1903` → IC=+0.224 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1903 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.594` → IC=+0.247 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.594 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.1814` → IC=+0.220 (n=1981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1814 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.225 (n=1981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6199 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.269 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `2.15` → IC=+0.220 (n=1697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.15 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.8057` → IC=+0.229 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8057 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.219 (n=2575)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2645.437` → IC=+0.228 (n=1321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2645.437 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.237 (n=891)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0123 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.233 (n=916)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.259 (n=673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.4226` → IC=+0.256 (n=2019)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4226 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.2916` → IC=+0.234 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2916 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.349` → IC=+0.249 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.349 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6412` → IC=+0.236 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6412 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.288 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.228 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=2608)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2407.4896` → IC=+0.233 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.4896 (IC base=+0.226)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.206 (n=1326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.177 (n=1004)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0085 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3354` → IC=+0.186 (n=2649)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3354 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.208 (n=1490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.7279` → IC=+0.226 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7279 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.7744` → IC=+0.193 (n=467)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.7744 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.69` → IC=+0.203 (n=1292)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.69 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.0564` → IC=+0.188 (n=2369)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0564 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` > `0.6952` → IC=+0.179 (n=2404)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6952 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.1008` → IC=+0.188 (n=1084)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1008 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.4352` → IC=+0.193 (n=975)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4352 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.5152` → IC=+0.181 (n=975)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.5152 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.179 (n=3413)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2734.3004` → IC=+0.180 (n=2689)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2734.3004 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.189 (n=2792)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 151.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.143 (n=1048)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0036 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.1818` → IC=+0.181 (n=1382)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1818 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4331` → IC=+0.130 (n=1017)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4331 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.133 (n=1331)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 29.0 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.208 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.189 (n=853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.194 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.6492` → IC=+0.221 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6492 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.3049` → IC=+0.190 (n=269)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3049 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.190 (n=363)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.834` → IC=+0.165 (n=905)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.834 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8755` → IC=+0.192 (n=569)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8755 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.174 (n=335)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.2117` → IC=+0.174 (n=734)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.2117 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.4165` → IC=+0.166 (n=834)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4165 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `14847.7814` → IC=+0.179 (n=568)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 14847.7814 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.200 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 155.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.191 (n=335)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0027 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.34` → IC=+0.139 (n=994)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.34 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.137 (n=893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6298` → IC=+0.168 (n=875)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6298 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.715` → IC=+0.137 (n=191)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 8.715 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.14` → IC=+0.128 (n=903)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.14 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.0611` → IC=+0.156 (n=451)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0611 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.0982` → IC=+0.171 (n=347)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0982 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.1165` → IC=+0.137 (n=864)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.1165 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=1289)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.161 (n=644)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 216.0 (IC base=+0.126)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.251 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2022` → IC=+0.227 (n=620)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2022 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.6787` → IC=+0.269 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6787 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.3558` → IC=+0.221 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3558 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.2052` → IC=+0.214 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2052 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.229 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.8392` → IC=+0.214 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8392 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `1.1816` → IC=+0.228 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1816 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.242 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4123` → IC=+0.247 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4123 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.4439` → IC=+0.227 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4439 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0987` → IC=+0.168 (n=308)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0987 (IC base=+0.078)

- **PATRÓN** `libro_liquidez` > `7232.2841` → IC=+0.135 (n=615)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 7232.2841 (IC base=+0.078)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.154 (n=720)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0106 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.159 (n=326)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0094 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.5352` → IC=+0.156 (n=719)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.5352 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.939` → IC=+0.216 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.939 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.219` → IC=+0.218 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.219 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.0509` → IC=+0.177 (n=633)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.0509 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.7163` → IC=+0.162 (n=642)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.7163 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2788` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2788 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4582` → IC=+0.157 (n=231)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4582 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.1893` → IC=+0.168 (n=314)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.1893 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=742)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `3065.6596` → IC=+0.190 (n=240)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3065.6596 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.4872` → IC=+0.148 (n=632)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.4872 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` < `1.5684` → IC=+0.124 (n=304)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.5684 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `2772.1243` → IC=+0.155 (n=326)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2772.1243 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.120 (n=585)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 32.0 (IC base=+0.063)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.170 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0238 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.186 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.007 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.167 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5556 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2393` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2393 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `1.115` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 1.115 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6182 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.2537` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2537 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2503.8283` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2503.8283 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.158 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0119 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.134 (n=214)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.61 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `1.1471` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1471 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.969` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 4.969 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6529` → IC=+0.120 (n=214)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` > 0.6529 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.134 (n=173)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 17.0 (IC base=+0.113)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.182 (n=5079)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0046 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.221 (n=5077)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=15870)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.5584` → IC=+0.239 (n=13588)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5584 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1624` → IC=+0.193 (n=5579)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1624 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.342` → IC=+0.252 (n=3724)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.342 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2255` → IC=+0.169 (n=10187)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2255 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2907` → IC=+0.205 (n=2023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2907 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6084` → IC=+0.196 (n=4922)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6084 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1828.3576` → IC=+0.185 (n=15210)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1828.3576 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.201 (n=13838)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 117.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.194 (n=6053)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0053 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3794` → IC=+0.191 (n=12103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3794 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=5122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5767` → IC=+0.242 (n=13753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5767 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.1739` → IC=+0.171 (n=8243)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1739 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.912` → IC=+0.207 (n=1921)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.912 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.666` → IC=+0.189 (n=13281)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.666 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `1.0602` → IC=+0.159 (n=8182)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0602 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.252 (n=1852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6133` → IC=+0.199 (n=4318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6133 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `1764.7968` → IC=+0.188 (n=13753)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1764.7968 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.214 (n=8553)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.239 (n=834)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3474` → IC=+0.219 (n=2497)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3474 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.230 (n=1206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=1683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.664` → IC=+0.348 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.664 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.280 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.2635` → IC=+0.232 (n=1084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2635 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2017.3302` → IC=+0.232 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2017.3302 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.232 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.267 (n=1404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.2011` → IC=+0.271 (n=1403)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2011 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=1913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.4951` → IC=+0.282 (n=2104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4951 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.394` → IC=+0.262 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.394 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.0954` → IC=+0.259 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0954 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.281 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.638` → IC=+0.273 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.638 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=2325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1583.66` → IC=+0.269 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1583.66 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.261 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.202 (n=820)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1766` → IC=+0.163 (n=1635)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1766 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.2626` → IC=+0.207 (n=2452)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2626 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1244` → IC=+0.193 (n=1333)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1244 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.669` → IC=+0.163 (n=405)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.669 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.156 (n=2244)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.629` → IC=+0.174 (n=818)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.629 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0715` → IC=+0.154 (n=2188)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0715 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.176 (n=350)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1826` → IC=+0.159 (n=2106)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1826 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5323` → IC=+0.155 (n=2138)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5323 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.180 (n=1027)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 268.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=2046)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.2555` → IC=+0.164 (n=1798)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2555 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6969` → IC=+0.198 (n=2044)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6969 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1318` → IC=+0.167 (n=1880)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1318 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.218` → IC=+0.162 (n=453)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.218 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1835` → IC=+0.155 (n=2044)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1835 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1542` → IC=+0.192 (n=547)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1542 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.434` → IC=+0.150 (n=1940)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.434 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.7792` → IC=+0.160 (n=1293)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7792 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `339.0` → IC=+0.147 (n=1232)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 339.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.249 (n=844)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2645)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.376` → IC=+0.315 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.376 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2093` → IC=+0.224 (n=2570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2093 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.6947` → IC=+0.238 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6947 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=2980)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1999.76` → IC=+0.238 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1999.76 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.246 (n=2071)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.244 (n=2106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1798` → IC=+0.255 (n=1036)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1798 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.268 (n=886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0237` → IC=+0.303 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0237 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.074` → IC=+0.291 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.074 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3445` → IC=+0.295 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3445 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7252` → IC=+0.241 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7252 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1358` → IC=+0.248 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1358 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2069.9784` → IC=+0.266 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2069.9784 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.245 (n=1897)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.203 (n=1145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.415` → IC=+0.158 (n=2602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.415 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2558` → IC=+0.194 (n=2602)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2558 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.5533` → IC=+0.176 (n=677)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.5533 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.174` → IC=+0.162 (n=1054)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.174 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.166 (n=1736)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8725 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.184 (n=343)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5228` → IC=+0.171 (n=1117)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5228 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1776` → IC=+0.158 (n=1151)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1776 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6968.46` → IC=+0.238 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6968.46 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.174 (n=1107)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 78.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.190 (n=718)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0032 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4329` → IC=+0.141 (n=2143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4329 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.74` → IC=+0.187 (n=2143)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.74 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1464` → IC=+0.145 (n=1904)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1464 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.206` → IC=+0.172 (n=327)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.206 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8747` → IC=+0.141 (n=1430)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8747 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.232 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.2316` → IC=+0.133 (n=1811)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.2316 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4321` → IC=+0.139 (n=2058)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4321 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `7605.4826` → IC=+0.210 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7605.4826 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.146 (n=1753)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0082 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.198 (n=2626)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4483 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.047` → IC=+0.206 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.047 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.907` → IC=+0.267 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.907 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8868` → IC=+0.149 (n=1751)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8868 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.126 (n=2471)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.136 (n=339)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.4767` → IC=+0.124 (n=2562)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4767 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.4653` → IC=+0.127 (n=2562)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4653 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2682)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2882.2323` → IC=+0.251 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2882.2323 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.137 (n=802)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 25.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.142 (n=2509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0109 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1331` → IC=+0.162 (n=838)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1331 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=2583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.215 (n=2509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2146` → IC=+0.138 (n=2121)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2146 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.36` → IC=+0.134 (n=2416)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.36 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.7116` → IC=+0.140 (n=1104)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7116 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2237` → IC=+0.171 (n=421)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2237 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4358` → IC=+0.150 (n=779)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4358 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2724.0258` → IC=+0.210 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2724.0258 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.140 (n=2048)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 48.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.243 (n=2241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=1675)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6074` → IC=+0.270 (n=2241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6074 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.242 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.725` → IC=+0.268 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.725 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `1.2317` → IC=+0.230 (n=2508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2317 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.228 (n=2508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.236` → IC=+0.251 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.236 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.5107` → IC=+0.247 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5107 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=3251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2654.4856` → IC=+0.237 (n=1672)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2654.4856 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.247 (n=1182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.235 (n=2444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.5094` → IC=+0.265 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5094 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.196` → IC=+0.258 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.196 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.255 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.298 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4346` → IC=+0.229 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4346 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2420.4144` → IC=+0.229 (n=2326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2420.4144 (IC base=+0.226)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=4591)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.239 (n=1553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.5025` → IC=+0.209 (n=4638)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5025 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=1658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=2137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9402` → IC=+0.245 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9402 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.1717` → IC=+0.205 (n=1779)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1717 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.4327` → IC=+0.208 (n=3316)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4327 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.154` → IC=+0.214 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.154 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.648` → IC=+0.201 (n=4142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.648 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.217 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.8864` → IC=+0.205 (n=2260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8864 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.220 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.4541` → IC=+0.208 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4541 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.8433` → IC=+0.203 (n=3046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8433 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=3588)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2598.363` → IC=+0.207 (n=4635)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2598.363 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.231 (n=1152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.4893` → IC=+0.200 (n=3455)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4893 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=1164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=1557)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.18` → IC=+0.200 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.18 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.6713` → IC=+0.195 (n=601)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6713 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.2382` → IC=+0.181 (n=3114)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2382 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.141` → IC=+0.192 (n=3463)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.141 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.0969` → IC=+0.195 (n=2870)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.0969 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.190 (n=3156)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.190 (n=1499)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `1.8123` → IC=+0.191 (n=2271)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.8123 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=4591)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.195 (n=2976)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 162.0 (IC base=+0.184)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.254 (n=567)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.270 (n=215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.241 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.4994` → IC=+0.262 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4994 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` < `0.329` → IC=+0.248 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.329 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.111` → IC=+0.243 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.111 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.598` → IC=+0.239 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.598 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `1.2148` → IC=+0.242 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2148 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.8602` → IC=+0.252 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8602 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.8362` → IC=+0.243 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8362 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `12382.594` → IC=+0.251 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12382.594 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.242 (n=525)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.3687` → IC=+0.176 (n=1186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3687 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.191 (n=451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 5.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.191 (n=522)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1435 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.6071` → IC=+0.170 (n=538)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6071 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.6845` → IC=+0.208 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6845 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.1573` → IC=+0.163 (n=1164)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1573 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.406` → IC=+0.181 (n=1168)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.406 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.883` → IC=+0.197 (n=791)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.883 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2166` → IC=+0.185 (n=246)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2166 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.169 (n=394)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.8045` → IC=+0.177 (n=787)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8045 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `11340.2858` → IC=+0.175 (n=1186)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 11340.2858 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `698.0` → IC=+0.174 (n=1141)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 698.0 (IC base=+0.163)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.201 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.185 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0098 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.5794` → IC=+0.180 (n=696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.5794 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.51` → IC=+0.217 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.51 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` < `0.3521` → IC=+0.172 (n=834)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.3521 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.226 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `3.3854` → IC=+0.184 (n=232)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.3854 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `2525.266` → IC=+0.217 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2525.266 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `2.0` → IC=+0.267 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 2.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.2021` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2021 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.215 (n=1325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4612` → IC=+0.207 (n=1324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4612 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.219 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5155` → IC=+0.216 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5155 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.8779` → IC=+0.204 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8779 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.207 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.8824` → IC=+0.202 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8824 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2383` → IC=+0.211 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2383 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.203 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.1645` → IC=+0.204 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1645 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.4147` → IC=+0.221 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4147 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.246 (n=357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.4923` → IC=+0.206 (n=1068)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4923 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.199 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=759)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.7503` → IC=+0.187 (n=1068)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7503 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.0847` → IC=+0.183 (n=1068)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.0847 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.6564` → IC=+0.194 (n=191)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6564 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.355` → IC=+0.188 (n=965)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 4.355 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2441` → IC=+0.194 (n=1068)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.2441 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.198 (n=451)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `2.1797` → IC=+0.192 (n=919)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.1797 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `7152.1762` → IC=+0.194 (n=1068)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7152.1762 (IC base=+0.181)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.211 (n=607)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.205 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.925` → IC=+0.249 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.925 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7352` → IC=+0.239 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7352 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.204` → IC=+0.219 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.204 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.6985` → IC=+0.239 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6985 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.189 (n=624)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0799` → IC=+0.203 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0799 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.188 (n=296)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.4746` → IC=+0.221 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4746 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.188 (n=800)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `3548.6004` → IC=+0.210 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3548.6004 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.201 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.217 (n=228)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.357` → IC=+0.239 (n=335)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.357 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.233 (n=343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.7181` → IC=+0.220 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7181 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.5172` → IC=+0.215 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5172 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.3104` → IC=+0.209 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3104 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.947` → IC=+0.210 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.947 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.93` → IC=+0.206 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.93 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `0.7551` → IC=+0.208 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7551 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.9335` → IC=+0.206 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9335 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.231 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.588` → IC=+0.239 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.588 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2976.9345` → IC=+0.224 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2976.9345 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.237 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.202)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.161 (n=665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0038 (IC base=+0.073)

- **PATRÓN** `ibs_20min` > `0.4063` → IC=+0.148 (n=1409)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.4063 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.3541` → IC=+0.151 (n=511)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.3541 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.384` → IC=+0.176 (n=310)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.384 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.1875` → IC=+0.262 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1875 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.0946` → IC=+0.138 (n=674)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.0946 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.634` → IC=+0.167 (n=115)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 10.634 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.1476` → IC=+0.196 (n=192)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1476 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `2.6098` → IC=+0.124 (n=637)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.6098 (IC base=+0.064)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.140 (n=506)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0056 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.145 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.5456` → IC=+0.198 (n=425)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5456 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `2.4168` → IC=+0.121 (n=433)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 2.4168 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.5593` → IC=+0.196 (n=281)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5593 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.201` → IC=+0.134 (n=350)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.201 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `2.5595` → IC=+0.121 (n=296)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` < 2.5595 (IC base=+0.080)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7058` → IC=-0.185 (n=71)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7058
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=217)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.154 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0046 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6578` → IC=+0.209 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6578 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.188 (n=245)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.447` → IC=+0.250 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.447 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.8155` → IC=+0.128 (n=307)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8155 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.7849` → IC=+0.123 (n=271)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.7849 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `1768.7923` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 1768.7923 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.0163` → IC=+0.313 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0163 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.031` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.031 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=+0.024)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.219 (n=55)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=166)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.161 (n=322)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.75 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.862` → IC=+0.149 (n=132)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 7.862 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2404` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2404 (IC base=+0.028)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.163 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0094 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.256 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.2139` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2139 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` < `0.3658` → IC=+0.167 (n=181)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3658 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.847` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.847 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` > `1.0763` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0763 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.250 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` < `2.1906` → IC=+0.182 (n=127)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.1906 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` > `1.8571` → IC=+0.194 (n=96)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.8571 (IC base=+0.083)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.202 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.083)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1839` → IC=-0.319 (n=70)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1839
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=212)

- **FILTRO** `dist_vwap_pct` > `0.2344` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2344
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=267)

- **FILTRO** `volumen_regimen` < `0.7708` → IC=-0.336 (n=71)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7708
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=213)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.369 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=180)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.300 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=186)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=217)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=128)

- **FILTRO** `libro_liquidez` < `1285.3712` → IC=-0.303 (n=59)

  - _Acción_: SKIP cuando `libro_liquidez` < 1285.3712
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=180)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.266 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=48)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=63)

- **FILTRO** `volumen_regimen` < `0.8417` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8417
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=70)

- **FILTRO** `volumen_spike_ratio` > `3.5274` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.5274
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=53)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.286 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=78)

- **FILTRO** `sigma_ewma_delta_pct` > `2.402` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.402
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=71)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=79)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.441 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=65)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=68)

- **FILTRO** `ibs_20min` > `0.538` → IC=-0.370 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` > 0.538
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=46)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=39)

- **PATRÓN** `ibs_20min` > `0.9508` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.9508 (IC base=-0.167)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0062` → IC=-0.318 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=63)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=78)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=68)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.170 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0058 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.68` → IC=+0.146 (n=475)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.68 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.5003` → IC=+0.194 (n=106)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.5003 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `0.8589` → IC=+0.136 (n=317)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8589 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` < `0.2329` → IC=+0.135 (n=414)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.2329 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `2.5286` → IC=+0.137 (n=373)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5286 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.165 (n=490)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1558 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.198` → IC=+0.186 (n=135)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.198 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `3185.8393` → IC=+0.146 (n=371)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3185.8393 (IC base=+0.070)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6592` → IC=-0.240 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6592
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=147)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.224 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.171 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 12.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.170 (n=95)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 6.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.203 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1361 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.0916` → IC=+0.165 (n=258)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.0916 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.265` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.265 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.809` → IC=+0.168 (n=200)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 4.809 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.156 (n=254)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6197 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0772` → IC=+0.172 (n=196)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.0772 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.5723` → IC=+0.176 (n=223)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.5723 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.161 (n=222)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5245.5517` → IC=+0.155 (n=169)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 5245.5517 (IC base=+0.147)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.2623` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2623
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=175)

- **FILTRO** `ibs_20min` > `0.2061` → IC=-0.139 (n=95)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2061
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=186)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.128 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0047 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8022` → IC=+0.126 (n=153)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.8022 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `1.0244` → IC=+0.121 (n=151)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.0244 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.129 (n=157)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `1.7926` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.7926 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.2061` → IC=+0.138 (n=186)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.2061 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.044)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `sigma_h` > `0.008` → IC=-0.128 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=93)

- **FILTRO** `dist_vwap_pct` > `0.2724` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2724
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=99)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.306 (n=106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.273 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.244 (n=158)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.258 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.6436` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6436 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.224` → IC=+0.244 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.224 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.333` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.333 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `1.0021` → IC=+0.280 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0021 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.25` → IC=+0.302 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.25 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.328 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.250 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `667.907` → IC=+0.248 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 667.907 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.084)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=58)

- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.294)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.294)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.357 (n=54)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.294)

- **PATRÓN** `ballena_activa_n` < `1115.0` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1115.0 (IC base=+0.294)

- **PATRÓN** `drift_ventana_pct` |x|> `0.356` → IC=+0.236 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.356 (IC base=+0.214)

- **PATRÓN** `elapsed_s` > `185.1` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.1 (IC base=+0.214)

- **PATRÓN** `elapsed_s` < `216.4` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.4 (IC base=+0.214)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.275 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.214)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.214)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=58)

- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.294)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.294)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.357 (n=54)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.294)

- **PATRÓN** `ballena_activa_n` < `1115.0` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1115.0 (IC base=+0.294)

- **PATRÓN** `drift_ventana_pct` |x|> `0.356` → IC=+0.236 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.356 (IC base=+0.214)

- **PATRÓN** `elapsed_s` > `185.1` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.1 (IC base=+0.214)

- **PATRÓN** `elapsed_s` < `216.4` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.4 (IC base=+0.214)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.6365` → IC=+0.275 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6365 (IC base=+0.214)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.214)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2860.2066` → IC=+0.133 (n=535)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2860.2066 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2860.2066` → IC=+0.133 (n=535)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2860.2066 (IC base=+0.103)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=173)

- **FILTRO** `libro_liquidez` < `2715.711` → IC=-0.214 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2715.711
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=142)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=65)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.149 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=3219)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=57)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=89)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.217 (n=58)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=122)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=222)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=+0.031)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=1179)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=1133)

- **FILTRO** `liq_usd_total` < `12056.79` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `liq_usd_total` < 12056.79
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=705)

- **FILTRO** `liq_n` < `11.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `liq_n` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `liq_usd_total` < `13082.51` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `liq_usd_total` < 13082.51
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=398)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=379)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.141 (n=157)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.017)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=813)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=813)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=708)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=708)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=180)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=185)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=209)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=251)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=187)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=221)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=329)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=329)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=241)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=169)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=1074)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=2739)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.55 (IC base=+0.071)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.071)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `restante_min` < `3.89` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.194 (n=119)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.46 (IC base=+0.025)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.196 (n=44)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=195)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.170 (n=110)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=131)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.127 (n=73)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.58 (IC base=+0.045)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.52` → IC=-0.123 (n=263)

  - _Acción_: SKIP cuando `py_entrada` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=89)

- **FILTRO** `profundidad_ratio` < `37.2` → IC=-0.178 (n=88)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.2
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=264)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.242 (n=60)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=261)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.46 (IC base=-0.026)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.133 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=222)

- **FILTRO** `restante_min` < `3.33` → IC=-0.171 (n=141)

  - _Acción_: SKIP cuando `restante_min` < 3.33
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=289)

- **FILTRO** `lag_apertura_s` > `98.43` → IC=-0.182 (n=146)

  - _Acción_: SKIP cuando `lag_apertura_s` > 98.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=284)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.185 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=277)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` > `0.48` → IC=+0.130 (n=136)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.48 (IC base=-0.013)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.121 (n=286)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=99)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.180 (n=101)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=370)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7798)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=5278)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=16841)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.169 (n=5676)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=17138)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.191 (n=969)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=3011)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.162 (n=947)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3140)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.137 (n=1052)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1420.26` → IC=+0.132 (n=1990)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1420.26 (IC base=+0.037)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.123 (n=1892)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.5 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `1545.66` → IC=+0.147 (n=1390)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1545.66 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=794)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2470)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.174 (n=981)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=3042)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.186 (n=1035)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=3121)

- **PATRÓN** `ibs_20min` > `0.9632` → IC=+0.124 (n=1369)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.9632 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1854.5984` → IC=+0.127 (n=1368)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1854.5984 (IC base=+0.037)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2281)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2691)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3431)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=418)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.254 (n=132)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=411)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `libro_liquidez` < `2574.706` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2574.706
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.191 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=296)

- **FILTRO** `libro_liquidez` < `3721.8218` → IC=-0.167 (n=208)

  - _Acción_: SKIP cuando `libro_liquidez` < 3721.8218
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=209)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=846)

- **FILTRO** `libro_liquidez` < `2053.5963` → IC=-0.164 (n=343)

  - _Acción_: SKIP cuando `libro_liquidez` < 2053.5963
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=699)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=232)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=43)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.037)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=15290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=34127)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=11972)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=37445)

- **FILTRO** `ibs_7min` < `0.2455` → IC=-0.231 (n=12353)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2455
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=37064)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=16221)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33196)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.237 (n=15185)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=47376)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.180 (n=15534)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=47027)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=2463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6056)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=4233)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=4286)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.248 (n=2809)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=5710)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.175 (n=1948)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6571)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.271 (n=2683)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=8181)

- **FILTRO** `ibs_7min` > `0.7759` → IC=-0.210 (n=2715)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7759
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=8149)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.126 (n=2019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=6370)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=1916)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=6473)

- **FILTRO** `ibs_7min` < `0.7315` → IC=-0.196 (n=2096)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7315
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6293)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.190 (n=2097)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6292)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2062)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6459)

- **FILTRO** `ibs_7min` > `0.2677` → IC=-0.194 (n=2130)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2677
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6391)

- **FILTRO** `ballena_activa_n` > `148.0` → IC=-0.184 (n=2126)

  - _Acción_: SKIP cuando `ballena_activa_n` > 148.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6395)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.156 (n=1996)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=6117)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=1965)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=6148)

- **FILTRO** `ibs_7min` < `0.7012` → IC=-0.246 (n=2677)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7012
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=5436)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.224 (n=1688)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6425)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.249 (n=2639)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=8915)

- **FILTRO** `ibs_7min` > `0.734` → IC=-0.175 (n=2888)

  - _Acción_: SKIP cuando `ibs_7min` > 0.734
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=8666)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=1872)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=6217)

- **FILTRO** `ibs_7min` < `0.7335` → IC=-0.186 (n=2022)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7335
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6067)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.191 (n=2004)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=6085)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=2088)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6274)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.180 (n=2089)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=6273)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.178 (n=2041)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6321)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=2041)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=6162)

- **FILTRO** `ibs_7min` < `0.2273` → IC=-0.234 (n=2046)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2273
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=6157)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=2824)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=9132)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=2003)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=6101)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.220 (n=2025)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6079)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1869)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6235)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.209 (n=2748)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=8556)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=980)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1264)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.160 (n=51)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=633)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=821)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=374)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.138 (n=158)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=318)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=611)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.146 (n=1056)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `442.3859` → IC=+0.159 (n=353)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 442.3859 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3687.403` → IC=+0.138 (n=479)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3687.403 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.158 (n=349)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 13.0 (IC base=+0.130)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4367` → IC=+0.171 (n=83)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.4367 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.225 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2602.0106` → IC=+0.229 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2602.0106 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 9.0 (IC base=+0.148)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` < `3.0` → IC=+0.149 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 3.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.128 (n=253)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.04 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2365.7446` → IC=+0.141 (n=143)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2365.7446 (IC base=+0.117)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4156` → IC=+0.181 (n=142)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.4156 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.156 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 4.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `391.8444` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 391.8444 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 72.0 (IC base=+0.132)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4335` → IC=+0.247 (n=85)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4335 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.169 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.151)

- **PATRÓN** `total_vol_5m` < `4950.202` → IC=+0.188 (n=126)

  - _Acción_: Kelly boost +0.94€ cuando `total_vol_5m` < 4950.202 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `3267.081` → IC=+0.165 (n=168)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3267.081 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 27.0 (IC base=+0.151)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.135 (n=176)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.095)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.121 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 13.0 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=122)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `3635.4092` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3635.4092 (IC base=+0.095)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.4547` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.4547
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=130)

- **FILTRO** `sigma_h` > `0.0051` → IC=-0.265 (n=300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=302)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.167 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0034 (IC base=-0.084)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.351 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=136)

- **FILTRO** `T_h` > `87.9981` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=136)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.292 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.046)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `87.9936` → IC=-0.148 (n=52)

  - _Acción_: SKIP cuando `T_h` < 87.9936
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=52)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.066)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.224 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=140)

- **FILTRO** `pct_vs_K` |x|> `2.2191` → IC=-0.386 (n=234)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.2191
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=235)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=142)

- **FILTRO** `T_h` > `79.3043` → IC=-0.185 (n=125)

  - _Acción_: SKIP cuando `T_h` > 79.3043
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

- **FILTRO** `pct_vs_K` |x|> `1.9565` → IC=-0.397 (n=85)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.9565
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=86)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.302 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=54)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=108)

- **FILTRO** `pct_vs_K` |x|> `3.2846` → IC=-0.439 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2846
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=97)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.300 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=100)

- **FILTRO** `T_h` > `113.7599` → IC=-0.220 (n=73)

  - _Acción_: SKIP cuando `T_h` > 113.7599
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=75)

- **FILTRO** `sigma_h` < `0.0105` → IC=-0.304 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=49)

- **FILTRO** `pct_vs_K` |x|> `3.8261` → IC=-0.414 (n=33)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8261
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=65)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1224` → IC=+0.475 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1224 (IC base=+0.337)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.357 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.337)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.378 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.337)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.385 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.337)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.337)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.354 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.337)

- **PATRÓN** `edge` > `0.096` → IC=+0.447 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.419)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.419)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.442 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.419)

- **PATRÓN** `T_h` < `0.5922` → IC=+0.429 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5922 (IC base=+0.419)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.444 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.419)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.466 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.419)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.430)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.417 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.430)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.460 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.430)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.430)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.423 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.430)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.478 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.430)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.430)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1975` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1975 (IC base=+0.434)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.465 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.434)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.434)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

- **PATRÓN** `edge` > `0.1961` → IC=+0.478 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.478 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.1968` → IC=+0.478 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1968 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4421` → IC=+0.485 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4421 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=284)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=363)

- **FILTRO** `streak_estiramiento` > `0.8581` → IC=-0.171 (n=80)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8581
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=242)

- **PATRÓN** `streak_estiramiento` < `0.4095` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4095 (IC base=+0.036)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `volumen_racha` < `945898.4` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_racha` < 945898.4 (IC base=+0.014)

- **PATRÓN** `streak_estiramiento` < `0.2918` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `streak_estiramiento` < 0.2918 (IC base=+0.014)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.155 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 10.0 (IC base=+0.079)

- **PATRÓN** `streak_estiramiento` < `0.3243` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.3243 (IC base=+0.079)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 44.0 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `2312.8768` → IC=+0.150 (n=118)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2312.8768 (IC base=+0.079)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=43)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=708)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `volumen_racha` > `3677.1957` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_racha` > 3677.1957
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `libro_liquidez` < `3338.6704` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 3338.6704
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_FADE_60M#SOL#60min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.050)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=922)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1327)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1060)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=1076)

### STRUCT_NO_15M
- **FILTRO** `libro_liquidez` < `6797.2178` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 6797.2178
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3771)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `libro_liquidez` < `6797.2178` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 6797.2178
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2037)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.203 (n=1057)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.222 (n=1057)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1669` → IC=+0.198 (n=2791)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1669 (IC base=+0.189)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3519` → IC=+0.199 (n=2837)

  - _Acción_: Kelly boost +0.99€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3519 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.193 (n=2950)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=2911)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_15` > `0.5814` → IC=+0.267 (n=3171)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5814 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.1224` → IC=+0.182 (n=1531)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1224 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.4715` → IC=+0.177 (n=2727)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.4715 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.67` → IC=+0.263 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.67 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `5195.5881` → IC=+0.203 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5195.5881 (IC base=+0.189)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=1254)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.243 (n=371)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.261 (n=186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.218)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.254 (n=185)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.218)

- **PATRÓN** `ibs_15` > `0.7231` → IC=+0.281 (n=555)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7231 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.245 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.196` → IC=+0.300 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.196 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.220 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `16272.4583` → IC=+0.254 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16272.4583 (IC base=+0.218)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.391` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.391
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=708)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.189 (n=210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0033 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0667` → IC=+0.152 (n=277)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0667 (IC base=+0.146)

- **PATRÓN** `drift_15min` |x|≤ `0.3985` → IC=+0.146 (n=210)

  - _Acción_: Kelly boost +0.73€ cuando `drift_15min` |x|≤ 0.3985 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.160 (n=419)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1283` → IC=+0.163 (n=244)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1283 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.149 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5656` → IC=+0.244 (n=628)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5656 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1175` → IC=+0.159 (n=400)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1175 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.5915` → IC=+0.147 (n=707)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.5915 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.028` → IC=+0.293 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.028 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3537.6258` → IC=+0.157 (n=561)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3537.6258 (IC base=+0.146)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `18.722` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.722
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=267)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.149 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0057 (IC base=+0.113)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.162 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0103 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.156 (n=417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.130 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.113)

- **PATRÓN** `ibs_15` > `0.9091` → IC=+0.283 (n=210)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9091 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2025` → IC=+0.128 (n=543)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.2025 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.536` → IC=+0.142 (n=121)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 17.536 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=344)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.113)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.191` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 8.191 (IC base=+0.022)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.284 (n=243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0793` → IC=+0.228 (n=321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0793 (IC base=+0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3349` → IC=+0.244 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3349 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.233 (n=643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.216)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.296 (n=729)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.1823` → IC=+0.218 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1823 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.866` → IC=+0.248 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.866 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2993.2618` → IC=+0.288 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2993.2618 (IC base=+0.216)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.162 (n=735)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.81€ cuando `ibs_15` < 0.1111 (IC base=+0.065)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.368 (n=391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.369 (n=586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.385 (n=390)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2309` → IC=+0.384 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2309 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.375 (n=592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.7881` → IC=+0.398 (n=586)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7881 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.4165` → IC=+0.391 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4165 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.722` → IC=+0.388 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.722 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.367 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.371 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.361 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.376 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.362)

- **PATRÓN** `drift_15min` |x|≤ `0.5078` → IC=+0.361 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5078 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.394 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.394 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.382 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.388 (n=309)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2504` → IC=+0.394 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2504 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.859` → IC=+0.382 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.859 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.763` → IC=+0.361 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.763 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `15285.027` → IC=+0.388 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15285.027 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.409 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.363 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.383 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.361 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0901` → IC=+0.376 (n=248)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0901 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.382 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.390 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.360)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.366 (n=125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.7557` → IC=+0.407 (n=277)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7557 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.1542` → IC=+0.365 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1542 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.363 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.973` → IC=+0.397 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.973 (IC base=+0.360)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `3911.5181` → IC=+0.391 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3911.5181 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.363 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.360)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.221 (n=1008)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3028)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1567)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2469)

- **FILTRO** `libro_liquidez` < `4145.3507` → IC=-0.147 (n=2663)

  - _Acción_: SKIP cuando `libro_liquidez` < 4145.3507
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=1373)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.189 (n=647)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.283 (n=972)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1102` → IC=+0.208 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1102 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.4198` → IC=+0.203 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4198 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2273` → IC=+0.266 (n=1099)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2273 (IC base=-0.013)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3299` → IC=+0.254 (n=3228)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3299 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.281 (n=3293)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6455` → IC=+0.275 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6455 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.204 (n=570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1712)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.229 (n=570)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1712)

- **FILTRO** `sigma_ewma_delta_pct` > `23.623` → IC=-0.265 (n=330)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.623
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1952)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2218)

- **FILTRO** `libro_liquidez` < `16220.5636` → IC=-0.205 (n=1506)

  - _Acción_: SKIP cuando `libro_liquidez` < 16220.5636
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=776)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.171 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0026 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2118` → IC=+0.291 (n=137)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2118 (IC base=+0.095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.282 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.332 (n=302)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.302 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.3651` → IC=+0.296 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3651 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.678` → IC=+0.144 (n=158)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 24.678 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.222 (n=52)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1833` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1833 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.6128` → IC=+0.296 (n=52)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6128 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=632)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.168 (n=435)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0037 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.0709` → IC=+0.196 (n=215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0709 (IC base=+0.156)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1402` → IC=+0.161 (n=325)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1402 (IC base=+0.156)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.201 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.177 (n=348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 11.0 (IC base=+0.156)

- **PATRÓN** `ibs_15` > `0.6285` → IC=+0.259 (n=487)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6285 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.454` → IC=+0.162 (n=134)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.454 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.2713` → IC=+0.159 (n=453)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2713 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.263 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=632)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.173 (n=163)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.254 (n=506)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.3518` → IC=+0.245 (n=1012)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3518 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7609` → IC=+0.254 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7609 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1543` → IC=+0.257 (n=766)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1543 (IC base=+0.243)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3313` → IC=+0.244 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3313 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.243 (n=1022)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3682` → IC=+0.273 (n=1149)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3682 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.7772` → IC=+0.291 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7772 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.522` → IC=+0.254 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.522 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.673` → IC=+0.247 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.673 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0101` → IC=-0.222 (n=232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=700)

- **FILTRO** `drift_60min` |x|> `0.1723` → IC=-0.252 (n=316)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1723
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=616)

- **FILTRO** `drift_15min` |x|> `0.8825` → IC=-0.274 (n=232)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8825
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=700)

- **FILTRO** `sigma_ewma_delta_pct` > `6.57` → IC=-0.196 (n=222)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.57
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=710)

- **FILTRO** `sigma_ewma_delta_pct` > `18.158` → IC=-0.144 (n=479)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.158
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3865)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.182)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.182)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.182)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.182)

- **PATRÓN** `delta_ratio_macro` |x|> `0.082` → IC=+0.240 (n=463)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.082 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.283 (n=520)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4441` → IC=+0.246 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4441 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.249 (n=559)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=560)

- **FILTRO** `drift_15min` |x|> `1.2346` → IC=-0.265 (n=279)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2346
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=840)

- **FILTRO** `sigma_ewma_delta_pct` > `7.442` → IC=-0.204 (n=350)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.442
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=769)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1100)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.203)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.268 (n=709)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.027)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1124` → IC=+0.303 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1124 (IC base=-0.027)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=797)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` > `0.7702` → IC=+0.349 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7702 (IC base=-0.027)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.296 (n=985)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0537` → IC=+0.322 (n=329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0537 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2446` → IC=+0.297 (n=328)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2446 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2245` → IC=+0.306 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2245 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=1033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8379` → IC=+0.323 (n=984)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8379 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2684` → IC=+0.321 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2684 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.865` → IC=+0.370 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.865 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `12693.279` → IC=+0.313 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12693.279 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.309 (n=234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.311 (n=178)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.304 (n=177)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.306 (n=534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.827` → IC=+0.312 (n=531)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.827 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.324 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.276` → IC=+0.377 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.276 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.285 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16334.7136` → IC=+0.327 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16334.7136 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.307 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.298 (n=453)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.325 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1516` → IC=+0.306 (n=302)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1516 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3023` → IC=+0.313 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3023 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8743` → IC=+0.338 (n=405)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8743 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.328 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.354 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1078` → IC=-0.145 (n=212)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1078
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=72)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.136 (n=218)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=75)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.167 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=354)

- **FILTRO** `ballena_activa_n` > `50.0` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `ballena_activa_n` > 50.0
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=159)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1319` → IC=-0.173 (n=47)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1319
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=144)

- **FILTRO** `drift_60min` |x|> `0.2244` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2244
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=33)

- **FILTRO** `drift_15min` |x|> `0.3481` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3481
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1941` → IC=-0.231 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1254` → IC=-0.200 (n=18)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1254
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2968` → IC=-0.375 (n=22)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2968
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0775` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0775
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `83.3501` → IC=+0.201 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.194)

- **PATRÓN** `ratio` < `0.973` → IC=+0.419 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.194)

- **PATRÓN** `T_h` > `111.996` → IC=+0.351 (n=2003)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0235` → IC=+0.369 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0235 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.181 (n=183)

  - _Acción_: Kelly boost +0.91€ cuando `T_h` > 103.3918 (IC base=+0.168)

- **PATRÓN** `ratio` < `0.9839` → IC=+0.333 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9839 (IC base=+0.168)

- **PATRÓN** `T_h` > `109.696` → IC=+0.303 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.696 (IC base=+0.291)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.393 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.291)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.241 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.232)

- **PATRÓN** `ratio` < `0.9849` → IC=+0.429 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.232)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.350 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.343 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1038` → IC=+0.448 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1038 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5814 sube el IC de +0.189 a +0.267 en UPDOWN_GBM#15min (n=3171). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7231 sube el IC de +0.218 a +0.281 en UPDOWN_GBM#BTC#15min (n=555). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5656 sube el IC de +0.146 a +0.244 en UPDOWN_GBM#ETH#15min (n=628). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9091 sube el IC de +0.113 a +0.283 en UPDOWN_GBM#SOL#15min (n=210). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.216 a +0.296 en UPDOWN_GBM#XRP#15min (n=729). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.065 a +0.162 en UPDOWN_GBM#XRP#15min (n=735). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.065 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=972). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.013 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=3293). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.095 a +0.332 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=302). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6128 sube el IC de -0.195 a +0.296 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6285 sube el IC de +0.156 a +0.259 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=487). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3682 sube el IC de +0.243 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1149). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.182 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.283 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=520). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.203 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.027 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=797). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8379 sube el IC de +0.291 a +0.323 en UPDOWN_GBM_IBS_ALTO (n=984). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.827 sube el IC de +0.286 a +0.312 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=531). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8743 sube el IC de +0.295 a +0.338 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=405). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7881 sube el IC de +0.362 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=586). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.362 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=309). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7557 sube el IC de +0.360 a +0.407 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=277). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1765 | +0.090 | +198.00€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1765 | +0.090 | +198.00€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1389 | +0.095 | +172.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1389 | +0.095 | +172.18€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 273 | +0.064 | +10.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 273 | +0.064 | +10.10€ | 6 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 443 | -0.003 | +64.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 443 | -0.003 | +64.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 318 | -0.013 | +40.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 318 | -0.013 | +40.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 99 | +0.035 | +18.98€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 99 | +0.035 | +18.98€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 37517 | -0.083 | -4682.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2020 | +0.019 | -237.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 35497 | -0.089 | -4445.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4430 | -0.116 | -761.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4430 | -0.116 | -761.64€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2020 | +0.019 | -237.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2020 | +0.019 | -237.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4130 | -0.113 | -845.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4130 | -0.113 | -845.58€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9920 | -0.008 | -832.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9920 | -0.008 | -832.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9745 | -0.108 | -728.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9745 | -0.108 | -728.58€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7272 | -0.143 | -1277.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7272 | -0.143 | -1277.01€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 31210 | -0.017 | +3558.39€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8077 | +0.004 | +1736.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 23133 | -0.025 | +1821.73€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 31210 | -0.017 | +3558.39€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8077 | +0.004 | +1736.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 23133 | -0.025 | +1821.73€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 133155 | +0.114 | -5584.01€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17680 | +0.182 | -535.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 579 | -0.028 | -65.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 106813 | +0.105 | -4703.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8083 | +0.103 | -279.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 17723 | +0.107 | -1111.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 59 | -0.156 | +9.83€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 17649 | +0.108 | -1109.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 26016 | +0.128 | -416.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5075 | +0.191 | -155.72€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 17706 | +0.118 | -152.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3193 | +0.086 | -86.20€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 17772 | +0.097 | -1302.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 69 | -0.106 | -3.93€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 17688 | +0.098 | -1287.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 28310 | +0.124 | -514.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7417 | +0.176 | -132.07€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 17931 | +0.106 | -319.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2950 | +0.100 | -53.74€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 25591 | +0.114 | -1344.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4997 | +0.193 | -260.84€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 482 | +0.006 | -11.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 18172 | +0.093 | -932.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1940 | +0.134 | -139.15€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 17743 | +0.104 | -895.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 63 | -0.069 | +6.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 17667 | +0.105 | -901.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 21374 | +0.195 | -1323.71€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 21374 | +0.195 | -1323.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4898 | +0.176 | -438.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4898 | +0.176 | -438.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2560 | +0.203 | -51.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2560 | +0.203 | -51.86€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4839 | +0.180 | -395.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4839 | +0.180 | -395.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4224 | +0.246 | -139.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4224 | +0.246 | -139.33€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4774 | +0.188 | -312.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4774 | +0.188 | -312.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 952 | +0.428 | -31.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 952 | +0.428 | -31.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 375 | +0.436 | -5.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 375 | +0.436 | -5.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 371 | +0.430 | -9.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 371 | +0.430 | -9.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 193 | +0.403 | -14.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 193 | +0.403 | -14.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 74441 | +0.201 | -5393.62€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 74441 | +0.201 | -5393.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 12791 | +0.185 | -1320.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 12791 | +0.185 | -1320.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 12005 | +0.224 | -416.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 12005 | +0.224 | -416.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 12759 | +0.180 | -1373.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 12759 | +0.180 | -1373.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 12089 | +0.220 | -459.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 12089 | +0.220 | -459.66€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 12341 | +0.202 | -814.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 12341 | +0.202 | -814.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 12456 | +0.196 | -1010.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 12456 | +0.196 | -1010.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 28463 | +0.117 | +195.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 28463 | +0.117 | +195.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 14149 | +0.120 | +173.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 14149 | +0.120 | +173.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 14314 | +0.114 | +22.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 14314 | +0.114 | +22.64€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1933 | +0.291 | -10.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1933 | +0.291 | -10.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 880 | +0.282 | -14.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 880 | +0.282 | -14.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 934 | +0.291 | -1.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 934 | +0.291 | -1.24€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 892 | +0.441 | +3.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 892 | +0.441 | +3.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 433 | +0.438 | -1.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 433 | +0.438 | -1.80€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 413 | +0.445 | +4.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 413 | +0.445 | +4.25€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1503 | +0.070 | -63.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 570 | +0.058 | -42.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 933 | +0.077 | -21.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 70 | +0.111 | +3.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 70 | +0.111 | +3.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1160 | +0.077 | -29.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 227 | +0.072 | -7.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 933 | +0.077 | -21.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 273 | +0.031 | -37.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 273 | +0.031 | -37.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 55573 | +0.100 | -1398.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4496 | +0.092 | +57.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 51077 | +0.101 | -1456.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 30665 | +0.105 | -334.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4496 | +0.092 | +57.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 26169 | +0.107 | -391.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 11283 | +0.109 | -54.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 11283 | +0.109 | -54.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 13625 | +0.082 | -1010.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 13625 | +0.082 | -1010.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 889 | +0.194 | -113.12€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 889 | +0.194 | -113.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 889 | +0.194 | -113.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 889 | +0.194 | -113.12€ | 2 | 4 |
| ✅ GBM_LATE_15M | 38429 | +0.092 | +19625.39€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 38429 | +0.092 | +19625.39€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6436 | +0.209 | +5126.56€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6436 | +0.209 | +5126.56€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 5741 | +0.179 | +4271.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5741 | +0.179 | +4271.05€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 6849 | +0.203 | +5282.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6849 | +0.203 | +5282.21€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5392 | +0.039 | +1445.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5392 | +0.039 | +1445.51€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 5461 | -0.030 | +1187.65€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5461 | -0.030 | +1187.65€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 8550 | -0.034 | +2312.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 8550 | -0.034 | +2312.41€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 41522 | +0.086 | +22440.10€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 41522 | +0.086 | +22440.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8023 | +0.006 | +4145.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8023 | +0.006 | +4145.02€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8733 | +0.013 | +1963.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8733 | +0.013 | +1963.89€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5800 | +0.274 | +6134.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5800 | +0.274 | +6134.41€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7295 | +0.013 | +1743.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7295 | +0.013 | +1743.66€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6696 | +0.039 | +2752.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6696 | +0.039 | +2752.20€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4975 | +0.296 | +5700.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4975 | +0.296 | +5700.91€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 30558 | +0.178 | +24390.30€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 30558 | +0.178 | +24390.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4642 | +0.222 | +3982.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4642 | +0.222 | +3982.59€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4803 | +0.150 | +3530.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4803 | +0.150 | +3530.64€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4876 | +0.221 | +4155.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4876 | +0.221 | +4155.83€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5156 | +0.139 | +3897.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5156 | +0.139 | +3897.69€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5749 | +0.124 | +4225.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5749 | +0.124 | +4225.47€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5332 | +0.222 | +4598.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5332 | +0.222 | +4598.07€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8197 | +0.136 | +3954.48€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8197 | +0.136 | +3954.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 396 | +0.153 | +247.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 396 | +0.153 | +247.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2461 | +0.143 | +1362.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2461 | +0.143 | +1362.97€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 417 | +0.149 | +209.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 417 | +0.149 | +209.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2468 | +0.144 | +1176.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2468 | +0.144 | +1176.11€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1915 | +0.108 | +720.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1915 | +0.108 | +720.39€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 540 | +0.133 | +238.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 540 | +0.133 | +238.31€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 38617 | +0.183 | +30450.16€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 38617 | +0.183 | +30450.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6133 | +0.236 | +5571.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6133 | +0.236 | +5571.53€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5993 | +0.148 | +4023.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5993 | +0.148 | +4023.52€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6506 | +0.231 | +5763.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6506 | +0.231 | +5763.34€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6326 | +0.139 | +4504.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6326 | +0.139 | +4504.02€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6845 | +0.122 | +4686.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6845 | +0.122 | +4686.69€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6814 | +0.225 | +5901.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6814 | +0.225 | +5901.06€ | 0 | 20 |
| ✅ GBM_LATE_5M | 10786 | +0.194 | +8022.89€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 10786 | +0.194 | +8022.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2440 | +0.188 | +1918.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2440 | +0.188 | +1918.94€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1002 | +0.176 | +657.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1002 | +0.176 | +657.98€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 3187 | +0.191 | +2232.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3187 | +0.191 | +2232.99€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 1588 | +0.191 | +1203.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1588 | +0.191 | +1203.92€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1650 | +0.196 | +1195.07€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1650 | +0.196 | +1195.07€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3036 | +0.070 | +1039.87€ | 0 | 9 |
| ✅ GBM_LATE_60M#60min | 3036 | +0.070 | +1039.87€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1131 | +0.089 | +415.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1131 | +0.089 | +415.71€ | 0 | 9 |
| ✅ GBM_LATE_60M#ETH | 971 | +0.072 | +382.64€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 971 | +0.072 | +382.64€ | 1 | 11 |
| ✅ GBM_LATE_60M#SOL | 934 | +0.044 | +241.53€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 934 | +0.044 | +241.53€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 523 | -0.243 | -18.90€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 523 | -0.243 | -18.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 197 | -0.234 | -8.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 197 | -0.234 | -8.90€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 187 | -0.225 | -2.53€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 187 | -0.225 | -2.53€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 139 | -0.273 | -7.47€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 139 | -0.273 | -7.47€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1375 | +0.087 | +353.39€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1375 | +0.087 | +353.39€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 533 | +0.085 | +112.99€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 533 | +0.085 | +112.99€ | 1 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 509 | +0.064 | +89.40€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 509 | +0.064 | +89.40€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 333 | +0.124 | +151.01€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 333 | +0.124 | +151.01€ | 3 | 14 |
| ✅ LATE_WINDOW_5MIN | 146 | +0.257 | +128.85€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 146 | +0.257 | +128.85€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 146 | +0.257 | +128.85€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 146 | +0.257 | +128.85€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3193 | +0.100 | +793.88€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3193 | +0.100 | +793.88€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3193 | +0.100 | +793.88€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3193 | +0.100 | +793.88€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 456 | -0.063 | -29.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 456 | -0.063 | -29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 134 | -0.015 | +1.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 134 | -0.015 | +1.43€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 73 | -0.087 | -8.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 73 | -0.087 | -8.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 168 | -0.029 | -5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 168 | -0.029 | -5.75€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3425 | +0.017 | +79.11€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3425 | +0.017 | +79.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 168 | +0.018 | -3.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 168 | +0.018 | -3.27€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 651 | +0.019 | +36.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 651 | +0.019 | +36.69€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1229 | +0.027 | +30.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1229 | +0.027 | +30.98€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 746 | +0.011 | +0.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 746 | +0.011 | +0.72€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 428 | +0.009 | +19.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 428 | +0.009 | +19.07€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1616 | -0.042 | -28.58€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1616 | -0.042 | -28.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 457 | -0.036 | -12.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 457 | -0.036 | -12.84€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 544 | -0.020 | +2.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 544 | -0.020 | +2.88€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 615 | -0.066 | -18.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 615 | -0.066 | -18.62€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 6896 | -0.023 | +58.67€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3285 | -0.032 | -39.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3611 | -0.015 | +97.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 195 | -0.003 | +11.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 96 | +0.041 | +14.05€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 99 | -0.045 | -2.61€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1733 | -0.013 | +34.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 828 | -0.019 | +3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 905 | -0.008 | +30.27€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 754 | -0.026 | +4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 381 | -0.043 | -10.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 373 | -0.009 | +14.29€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1444 | -0.035 | -32.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 673 | -0.048 | -38.05€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 771 | -0.024 | +5.99€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1366 | -0.017 | +31.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 658 | -0.029 | +0.16€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 708 | -0.006 | +31.18€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1404 | -0.028 | +9.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 649 | -0.039 | -8.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 755 | -0.019 | +18.57€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 44933 | -0.001 | +2184.98€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 44933 | -0.001 | +2184.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8067 | +0.025 | +1022.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8067 | +0.025 | +1022.09€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6558 | -0.034 | -105.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6558 | -0.034 | -105.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 8179 | +0.023 | +808.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 8179 | +0.023 | +808.30€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6392 | -0.047 | -144.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6392 | -0.047 | -144.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7577 | -0.004 | +243.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7577 | -0.004 | +243.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 8160 | +0.015 | +360.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 8160 | +0.015 | +360.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6430 | -0.060 | -159.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6430 | -0.060 | -159.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1224 | +0.000 | -14.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1224 | +0.000 | -14.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1639 | -0.080 | -42.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1639 | -0.080 | -42.35€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 751 | -0.120 | -32.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 751 | -0.120 | -32.23€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1907 | -0.078 | -42.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1907 | -0.078 | -42.20€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3365 | +0.005 | -0.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3365 | +0.005 | -0.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 138 | +0.000 | -1.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 138 | +0.000 | -1.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1390 | +0.007 | +0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1390 | +0.007 | +0.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 111978 | -0.074 | +1803.19€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 111978 | -0.074 | +1803.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 19383 | -0.075 | +1015.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 19383 | -0.075 | +1015.95€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 16910 | -0.099 | -915.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 16910 | -0.099 | -915.00€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 19667 | -0.066 | +1129.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 19667 | -0.066 | +1129.43€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 16451 | -0.095 | -487.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 16451 | -0.095 | -487.43€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 20159 | -0.054 | +367.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 20159 | -0.054 | +367.70€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 19408 | -0.065 | +692.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 19408 | -0.065 | +692.55€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8648 | -0.033 | -178.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8648 | -0.033 | -178.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 999 | -0.017 | -19.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 999 | -0.017 | -19.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1963 | -0.045 | -22.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1963 | -0.045 | -22.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2572 | -0.026 | -41.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2572 | -0.026 | -41.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1156 | -0.052 | -26.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1156 | -0.052 | -26.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 950 | -0.033 | -36.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 950 | -0.033 | -36.85€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1544 | +0.123 | +629.00€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1408 | +0.130 | +616.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 330 | +0.148 | +179.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 330 | +0.148 | +179.32€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 285 | +0.117 | +96.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 285 | +0.117 | +96.31€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 283 | +0.132 | +131.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 283 | +0.132 | +131.45€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 250 | +0.151 | +136.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 250 | +0.151 | +136.45€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 260 | +0.095 | +72.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 260 | +0.095 | +72.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1237 | -0.021 | -29.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1237 | -0.021 | -29.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 235 | -0.006 | +5.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 235 | -0.006 | +5.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 214 | -0.014 | +0.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 214 | -0.014 | +0.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 322 | -0.049 | -30.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 322 | -0.049 | -30.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 262 | -0.004 | -1.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 262 | -0.004 | -1.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 204 | -0.024 | -4.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 204 | -0.024 | -4.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 842 | -0.071 | -42.25€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 389 | -0.119 | -77.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 300 | -0.152 | -67.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 301 | -0.035 | +22.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 215 | -0.030 | +22.89€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 152 | -0.019 | +13.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 122 | -0.024 | +8.23€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 637 | -0.087 | -36.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1027 | -0.207 | -57.18€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 414 | -0.207 | -37.94€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 358 | -0.211 | -38.22€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 348 | -0.217 | -30.63€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 302 | -0.227 | -36.32€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 265 | -0.193 | +11.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 246 | -0.190 | +8.24€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 906 | -0.211 | -66.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 421 | +0.396 | +401.59€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 105 | +0.369 | +91.40€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 105 | +0.369 | +91.40€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 263 | +0.459 | +264.06€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 263 | +0.459 | +264.06€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 421 | +0.396 | +401.59€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 685 | +0.027 | +25.98€ | 3 | 1 |
| ✅ STREAK_FADE_15M#15min | 685 | +0.027 | +25.98€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 297 | +0.022 | +2.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 297 | +0.022 | +2.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 55 | -0.026 | -5.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 55 | -0.026 | -5.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 71 | -0.007 | -0.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 71 | -0.007 | -0.09€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 262 | +0.053 | +28.49€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 262 | +0.053 | +28.49€ | 0 | 6 |
| ✅ STREAK_FADE_5M | 3387 | -0.022 | -132.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3387 | -0.022 | -132.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 586 | -0.025 | -25.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 586 | -0.025 | -25.10€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 162 | -0.043 | -14.36€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 162 | -0.043 | -14.36€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1588 | -0.018 | -55.84€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1588 | -0.018 | -55.84€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 95 | -0.046 | -8.93€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 95 | -0.046 | -8.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 40 | -0.071 | -3.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 40 | -0.071 | -3.54€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 55 | -0.026 | -5.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 55 | -0.026 | -5.39€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10364 | +0.018 | +97.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10364 | +0.018 | +97.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2652 | +0.020 | +26.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2652 | +0.020 | +26.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2650 | +0.021 | +39.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2650 | +0.021 | +39.24€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2884 | +0.009 | -2.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2884 | +0.009 | -2.06€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2178 | +0.022 | +33.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2178 | +0.022 | +33.69€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9465 | +0.013 | -50.62€ | 1 | 0 |
| ✅ STRUCT_NO_15M#15min | 9465 | +0.013 | -50.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3790 | +0.017 | -8.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3790 | +0.017 | -8.93€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3604 | +0.011 | -27.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3604 | +0.011 | -27.64€ | 1 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2071 | +0.008 | -14.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2071 | +0.008 | -14.05€ | 1 | 0 |
| ✅ UPDOWN_GBM | 69825 | +0.052 | +6107.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 17399 | +0.085 | +3938.42€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2294 | +0.006 | +20.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 45868 | +0.046 | +2066.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4027 | +0.010 | +82.31€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6818 | +0.089 | +1072.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1543 | +0.158 | +694.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 14285 | +0.054 | +1210.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2185 | +0.091 | +533.93€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 595 | +0.013 | +10.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 9626 | +0.059 | +605.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1793 | +0.007 | +56.59€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 86 | -0.068 | +4.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8060 | +0.066 | +843.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1529 | +0.149 | +607.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6453 | +0.047 | +237.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 15565 | +0.042 | +978.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4038 | +0.063 | +582.46€ | 0 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 586 | +0.009 | +12.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 9482 | +0.041 | +366.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1380 | +0.012 | +15.89€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 79 | -0.105 | +2.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 15375 | +0.030 | +694.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4223 | +0.036 | +371.38€ | 0 | 8 |
| ✅ UPDOWN_GBM#SOL#240min | 570 | -0.004 | +0.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9658 | +0.032 | +317.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 854 | +0.012 | +9.83€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 70 | -0.139 | -4.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9720 | +0.062 | +1309.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3881 | +0.103 | +1148.61€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5451 | +0.036 | +160.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 235 | -0.103 | +1.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 781 | +0.362 | +279.04€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 781 | +0.362 | +279.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 412 | +0.362 | +141.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 412 | +0.362 | +141.99€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 369 | +0.360 | +137.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 369 | +0.360 | +137.05€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 18516 | -0.024 | +4457.70€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 18516 | -0.024 | +4457.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3197 | -0.112 | +130.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3197 | -0.112 | +130.68€ | 5 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2180 | +0.217 | +1425.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2180 | +0.217 | +1425.45€ | 1 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5276 | -0.064 | +694.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5276 | -0.064 | +694.02€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5263 | -0.064 | +939.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5263 | -0.064 | +939.08€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 208 | +0.038 | +6.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 208 | +0.038 | +6.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 208 | +0.038 | +6.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 208 | +0.038 | +6.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1312 | +0.291 | +1105.12€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1312 | +0.291 | +1105.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 708 | +0.286 | +557.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 708 | +0.286 | +557.81€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 604 | +0.295 | +547.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 604 | +0.295 | +547.31€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 797 | -0.111 | -81.74€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 797 | -0.111 | -81.74€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 240 | -0.083 | -17.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 240 | -0.083 | -17.98€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 85 | -0.155 | -8.13€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 85 | -0.155 | -8.13€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 89 | -0.181 | -6.27€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 89 | -0.181 | -6.27€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3328 | +0.304 | +1606.07€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1210 | +0.257 | +164.75€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1278 | +0.298 | +569.42€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 840 | +0.379 | +871.90€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.013 n=863 — no justifica filtro, seguir monitorizando
  - _Datos_: n=863 IC=+0.013 PNL=+30.56€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 684 celda(s) pasan gate riguroso completo de 2610 evaluadas (n>=40) y 3622 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.036 < 0.08 — monitorear
  - _Datos_: n=4219 IC=+0.036 PNL=+371.51€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1278/15 IC=+0.298 PNL=+569.42€ | BTC: n=1210/15 IC=+0.257 PNL=+164.75€ | SOL: n=840/15 IC=+0.379 PNL=+871.90€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 31 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: 40
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Solo 0 ops con ibs_15 (feature añadida 2026-06-27). Esperar n≥40.

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: 20
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: Solo 0 ops GBM con hora_utc en features. Esperar n≥20 para patrones.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.139 n=729/60 | contraria IC=+0.201 n=758 | gap=-0.062 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=425, boost estimado=+0.011. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1378/40 IC=+0.012 PNL=+15.88€ | BTC#60min: n=1791/40 IC=+0.007 PNL=+56.58€ | SOL#60min: n=854/40 IC=+0.012 PNL=+9.83€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=506918 | tras_1loss IC=+0.093 n=386431 | tras_2loss IC=+0.062 n=157166/40 | gap=-0.015 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.000 n=0 | contrario_BTC IC=+0.000 n=0/40 | gap=+0.000 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.08 con n=656 PNL=+513.34€
  - _Datos_: n=656 IC=+0.210 PNL=+513.34€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.183 > 0.08 con n=736 PNL=+458.14€
  - _Datos_: n=736 IC=+0.183 PNL=+458.14€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=59 PNL=+35.04€
  - _Datos_: n=59 IC=+0.189 PNL=+35.04€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=2714 PNL=+1513.88€
  - _Datos_: n=2714 IC=+0.333 PNL=+1513.88€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=583 IC=+0.078 PNL=+68.68€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=583 IC=+0.078 PNL=+68.68€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=76 IC=+0.179 PNL=+49.33€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=76 IC=+0.179 PNL=+49.33€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 5/15 ops en el filtro definido (IC actual=+0.054 PNL=+5.10€)
  - _Datos_: n=5 IC=+0.054 PNL=+5.10€

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
  - _Estado_: n=2717 IC=+0.010 PNL=+10.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2717 IC=+0.010 PNL=+10.49€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1306 IC=+0.010 PNL=+71.80€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1306 IC=+0.010 PNL=+71.80€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=863 IC=+0.013 PNL=+30.56€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=863 IC=+0.013 PNL=+30.56€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.188 > 0.1 con n=4220 PNL=+2817.22€
  - _Datos_: n=4220 IC=+0.188 PNL=+2817.22€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2181 IC=+0.091 PNL=+534.45€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2181 IC=+0.091 PNL=+534.45€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**⏳ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: 40
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: 20
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=901 IC=+0.040 PNL=+92.11€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=901 IC=+0.040 PNL=+92.11€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=105 IC=+0.033 PNL=+3.54€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=105 IC=+0.033 PNL=+3.54€

**⏳ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: 40
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: 30
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.257 n=146) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=146 IC=+0.257 PNL=+128.85€

**⏳ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: 40
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: 40
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: 40
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: 200
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: 100
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: 40
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=891 PNL=+381.52€
  - _Datos_: n=891 IC=+0.128 PNL=+381.52€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=202 IC=-0.083 PNL=+23.24€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=202 IC=-0.083 PNL=+23.24€

**⏳ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=26941 IC=+0.074 PNL=+3974.97€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=26941 IC=+0.074 PNL=+3974.97€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=417 PNL=+54.00€
  - _Datos_: n=417 IC=-0.137 PNL=+54.00€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2909 IC=+0.065 PNL=+357.56€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2909 IC=+0.065 PNL=+357.56€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=126 IC=-0.109 PNL=+3.80€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=126 IC=-0.109 PNL=+3.80€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.1 con n=706 PNL=+190.50€
  - _Datos_: n=706 IC=+0.117 PNL=+190.50€

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
  - _Estado_: n=28663 IC=-0.134 PNL=+2244.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=28663 IC=-0.134 PNL=+2244.32€

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
  - _Estado_: n=2883 IC=+0.136 PNL=+1727.34€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2883 IC=+0.136 PNL=+1727.34€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=7186 IC=+0.048 PNL=+561.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7186 IC=+0.048 PNL=+561.60€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=3148 PNL=+1674.00€
  - _Datos_: n=3148 IC=+0.090 PNL=+1674.00€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=2943 PNL=-229.43€
  - _Datos_: n=2943 IC=-0.224 PNL=-229.43€

**⏳ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: 100
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: 40
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: 40
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=62 IC=-0.016 PNL=+3.71€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=62 IC=-0.016 PNL=+3.71€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.098 n=1622) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1622 IC=+0.098 PNL=+348.04€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.413 n=538) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=538 IC=+0.413 PNL=+773.91€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=12783 IC=+0.185 PNL=-1318.58€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=12783 IC=+0.185 PNL=-1318.58€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.1 con n=211 PNL=+134.64€
  - _Datos_: n=211 IC=+0.214 PNL=+134.64€
