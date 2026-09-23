# Hipótesis automáticas — 2026-09-23 17:49 UTC
_Generado por shadow_postmortem.py sobre 576739 resoluciones (PNL=+64388.90€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=466)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.258 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.51 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.8032` → IC=+0.255 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8032 (IC base=+0.139)

- **PATRÓN** `banda_z` > `4.175` → IC=+0.167 (n=541)

  - _Acción_: Kelly boost +0.83€ cuando `banda_z` > 4.175 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=579)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2988.1169` → IC=+0.153 (n=361)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2988.1169 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.131 (n=166)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 96.0 (IC base=+0.045)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.259 (n=413)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=339)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.259 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.148)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.148)

- **PATRÓN** `banda_hit_calibrado` > `0.7976` → IC=+0.266 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7976 (IC base=+0.148)

- **PATRÓN** `banda_z` > `4.348` → IC=+0.173 (n=432)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 4.348 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=490)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `4456.7277` → IC=+0.151 (n=196)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4456.7277 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.148 (n=126)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 96.0 (IC base=+0.047)

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

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.55 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1195.1095` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1195.1095 (IC base=+0.110)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

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
- **FILTRO** `restante_s_al_confirmar` < `146.06` → IC=-0.234 (n=6906)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.06
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=20718)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `139.1` → IC=-0.240 (n=902)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.1
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=2707)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `497.2` → IC=-0.147 (n=358)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 497.2
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1074)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `128.9` → IC=-0.302 (n=855)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.9
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=2565)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.36` → IC=-0.228 (n=1642)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.36
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4928)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `125.17` → IC=-0.357 (n=1373)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.17
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=4121)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.48` → IC=-0.223 (n=380)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=380)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.178 (n=234)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=475)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=559)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.202 (n=13583)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=3410)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5614.1784` → IC=+0.174 (n=2174)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5614.1784 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=11003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=13472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.232 (n=10629)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=5551)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7726.703` → IC=+0.174 (n=2091)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7726.703 (IC base=+0.128)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1651)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.352 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `15862.1611` → IC=+0.233 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15862.1611 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.206 (n=1484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.264 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `14028.8305` → IC=+0.213 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14028.8305 (IC base=+0.201)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.173 (n=319)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.615 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.146 (n=235)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4624.034 (IC base=+0.103)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.109)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.147 (n=805)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.44 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=556)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `5859.5725` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5859.5725 (IC base=+0.109)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2745)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=2347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.334 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.357 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `3737.0999` → IC=+0.233 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3737.0999 (IC base=+0.234)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.153 (n=447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.139 (n=644)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.232 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=524)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1302.4168` → IC=+0.149 (n=639)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1302.4168 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.432 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.167 (n=1064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 7.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.316 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=717)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.163)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.165 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 13.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.743` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.743 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=186)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `1271.2794` → IC=+0.156 (n=222)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1271.2794 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.205 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.113)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=107)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=11160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=10704)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.224 (n=3727)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=2583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.183 (n=1891)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.71 (IC base=+0.168)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.249 (n=788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.353 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.247)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=2528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=2552)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=2199)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=2371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.318 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=2586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=2496)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.198 (n=1905)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.441 (n=489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=459)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `2069.2076` → IC=+0.439 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2069.2076 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.436 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.454 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.438 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `3366.033` → IC=+0.446 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3366.033 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.406 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.406 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.404)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.404)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.406 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.404)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.200 (n=33157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.235 (n=14920)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.176 (n=5734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=4610)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=6177)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=5945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=5946)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=3171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=6055)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.230 (n=2967)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=2255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=5488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.255 (n=2216)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=5546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=5539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.253 (n=2127)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5073)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.15` → IC=+0.128 (n=4669)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.15 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=5004)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=6145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.95` → IC=+0.141 (n=4644)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.95 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=2555)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.123)

- **PATRÓN** `restante_min` < `4.1` → IC=+0.134 (n=2313)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.1 (IC base=+0.123)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2477)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=3422)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.123)

- **PATRÓN** `lag_apertura_s` < `3.44` → IC=+0.145 (n=2309)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.44 (IC base=+0.123)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=2518)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.127 (n=2348)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=2533)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.3` → IC=+0.138 (n=2339)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.3 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `4080.5501` → IC=+0.312 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4080.5501 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.304 (n=334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.345 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `4237.6328` → IC=+0.301 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4237.6328 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.333 (n=364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.294 (n=518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.386 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `1466.3152` → IC=+0.310 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1466.3152 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.349 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.341)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.363 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.341)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.380 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.377 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.341)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.448 (n=494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.445 (n=419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `2547.1781` → IC=+0.440 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2547.1781 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.447 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.449 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `2024.9352` → IC=+0.460 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2024.9352 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.384)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.256)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.267 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.284 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.256)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.256)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.267 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.284 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.256)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4815` → IC=+0.120 (n=7801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.4815 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.9808` → IC=+0.243 (n=2601)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9808 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.839` → IC=+0.249 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.839 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.6335` → IC=+0.249 (n=2174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6335 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.942` → IC=+0.175 (n=2999)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.942 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `1.05` → IC=+0.258 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.05 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.3056` → IC=+0.218 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3056 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.9086` → IC=+0.207 (n=3549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9086 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.57` → IC=+0.133 (n=9426)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.57 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.606` → IC=+0.192 (n=700)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.606 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.1515` → IC=+0.173 (n=2958)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1515 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.181 (n=1445)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6989 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` > `1.0532` → IC=+0.173 (n=1489)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.0532 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.1682` → IC=+0.224 (n=1564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1682 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` > `1.5741` → IC=+0.200 (n=4908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5741 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.211 (n=5284)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=+0.064)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.180 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.175 (n=589)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3482` → IC=+0.165 (n=1766)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3482 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.172 (n=1185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.107` → IC=+0.271 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.107 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.211 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4398` → IC=+0.163 (n=1650)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4398 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.250 (n=1182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0905` → IC=+0.285 (n=440)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0905 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.249 (n=901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0571` → IC=+0.292 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0571 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.427` → IC=+0.248 (n=1372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.427 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0914` → IC=+0.231 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0914 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.264 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.6401` → IC=+0.244 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6401 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1796.78` → IC=+0.238 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1796.78 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.234 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0838` → IC=+0.251 (n=448)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0838 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=1408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.216 (n=1369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9042` → IC=+0.259 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9042 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.2016` → IC=+0.221 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2016 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.7404` → IC=+0.219 (n=1482)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7404 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.863` → IC=+0.257 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.863 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `1.2558` → IC=+0.220 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2558 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.8755` → IC=+0.225 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8755 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.233 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.7485` → IC=+0.219 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7485 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.3766` → IC=+0.223 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3766 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `12345.7637` → IC=+0.218 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12345.7637 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.150 (n=1404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0056 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.160 (n=468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6928` → IC=+0.170 (n=1402)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6928 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.155 (n=1246)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.202` → IC=+0.165 (n=225)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.202 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.243` → IC=+0.140 (n=1277)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.243 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2046` → IC=+0.149 (n=1402)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2046 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.173 (n=506)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4143` → IC=+0.151 (n=1291)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4143 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7671` → IC=+0.144 (n=861)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7671 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.147 (n=1209)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 411.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.216 (n=576)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=1816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.199` → IC=+0.249 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.199 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.2116` → IC=+0.188 (n=1718)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2116 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3629` → IC=+0.199 (n=227)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.3629 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.8719` → IC=+0.206 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8719 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.194 (n=1224)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.225 (n=1477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.5908` → IC=+0.217 (n=1477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5908 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.243 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.609` → IC=+0.243 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.609 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.271 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.7913` → IC=+0.211 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7913 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.221` → IC=+0.220 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.221 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `1875.3584` → IC=+0.229 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1875.3584 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.214 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.215)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=96)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2167)

- **PATRÓN** `ibs_20min` > `0.94` → IC=+0.210 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.94 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.364` → IC=+0.325 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.364 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.7852` → IC=+0.329 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7852 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.666` → IC=+0.154 (n=691)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.666 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.321 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.2004` → IC=+0.341 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2004 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1819` → IC=+0.315 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1819 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.3097` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3097 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4057` → IC=+0.337 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4057 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.329 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.329 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6725` → IC=+0.193 (n=138)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6725 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.163 (n=538)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8504 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2258` → IC=+0.215 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2258 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.5204` → IC=+0.176 (n=673)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5204 (IC base=+0.015)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.172 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=314)

- **FILTRO** `ibs_20min` < `0.2703` → IC=-0.205 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2703
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=280)

- **FILTRO** `ibs_20min` > `0.2571` → IC=-0.125 (n=2126)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2571
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=1053)

- **FILTRO** `sigma_ewma_delta_pct` > `8.653` → IC=-0.204 (n=343)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.653
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2836)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.221 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7913 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `1.6434` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6434 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.7682` → IC=+0.267 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7682 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.6541` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6541 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.7836` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7836 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` < `0.0735` → IC=+0.311 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0735 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.8428` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8428 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.293 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.2571` → IC=+0.126 (n=1053)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.2571 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.6893` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6893 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `1.096` → IC=+0.226 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.096 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` > `0.9031` → IC=+0.212 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9031 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.1045` → IC=+0.231 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1045 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.4396` → IC=+0.263 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4396 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6576` → IC=-0.181 (n=547)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6576
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1643)

- **FILTRO** `ibs_20min` < `0.7098` → IC=-0.157 (n=1445)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7098
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=745)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.198 (n=405)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1785)

- **FILTRO** `ibs_20min` > `0.77` → IC=-0.202 (n=807)

  - _Acción_: SKIP cuando `ibs_20min` > 0.77
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2427)

- **PATRÓN** `dist_vwap_pct` > `0.783` → IC=+0.324 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.783 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.320 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2675 (IC base=-0.068)

- **PATRÓN** `volumen_regimen` < `0.9872` → IC=+0.294 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9872 (IC base=-0.068)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.310 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=-0.068)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.297 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=-0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.311 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.4256` → IC=+0.302 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4256 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.299 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.8718` → IC=+0.269 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8718 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` < `0.7369` → IC=+0.253 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7369 (IC base=-0.025)

- **PATRÓN** `volumen_regimen` > `1.0829` → IC=+0.281 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0829 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1711` → IC=+0.278 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1711 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.1732` → IC=+0.252 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1732 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4431` → IC=+0.248 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4431 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.246 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.198 (n=3254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.188 (n=8718)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4717 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.7569` → IC=+0.288 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7569 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.577` → IC=+0.155 (n=4615)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.577 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6894` → IC=+0.248 (n=3089)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6894 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2976` → IC=+0.265 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2976 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.4723` → IC=+0.241 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4723 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6833` → IC=+0.238 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6833 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.268 (n=5130)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.151 (n=3263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0091 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5464` → IC=+0.152 (n=8596)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.5464 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2473` → IC=+0.238 (n=2704)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2473 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.7101` → IC=+0.240 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7101 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.2035` → IC=+0.244 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2035 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2459` → IC=+0.299 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2459 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.6089` → IC=+0.256 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6089 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.3282` → IC=+0.256 (n=1706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3282 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.262 (n=3638)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 83.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.497` → IC=-0.165 (n=511)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.497
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1724)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.261 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.77` → IC=+0.203 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.77 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.274 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.178 (n=281)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `2.1594` → IC=+0.189 (n=381)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.1594 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.178 (n=374)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 15.0 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1673` → IC=+0.461 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1673 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.464 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.017)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.463 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.86` → IC=+0.154 (n=652)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.86 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.173 (n=503)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6736` → IC=+0.165 (n=798)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6736 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.217 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4243` → IC=+0.200 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4243 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `248.0` → IC=+0.195 (n=381)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 248.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1622` → IC=+0.219 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1622 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.611` → IC=+0.211 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.611 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2721` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2721 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.4504` → IC=+0.231 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4504 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.230 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `477.0` → IC=+0.214 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 477.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.292 (n=517)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.249 (n=1560)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.741` → IC=+0.280 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.741 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.1379` → IC=+0.258 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1379 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `3.4481` → IC=+0.260 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4481 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.256 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1946.9784` → IC=+0.256 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1946.9784 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.314 (n=557)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.6005` → IC=+0.284 (n=1230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6005 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.329 (n=412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` < `0.2248` → IC=+0.289 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2248 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.841` → IC=+0.298 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.841 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.3423` → IC=+0.307 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3423 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` < `1.6036` → IC=+0.289 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6036 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `2.7724` → IC=+0.285 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7724 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.290 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1930.6632` → IC=+0.301 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.6632 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.283 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.282)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2821` → IC=-0.191 (n=473)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2821
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=1422)

- **FILTRO** `ibs_20min` > `0.7744` → IC=-0.180 (n=579)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7744
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1738)

- **PATRÓN** `ibs_20min` > `0.8153` → IC=+0.158 (n=645)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8153 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.225 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.9978` → IC=+0.231 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9978 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `0.5846` → IC=+0.209 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5846 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.0791` → IC=+0.246 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0791 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.0972` → IC=+0.244 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0972 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.254 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` > `0.1552` → IC=+0.205 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1552 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` < `0.6734` → IC=+0.193 (n=463)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.6734 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1643` → IC=+0.205 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1643 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.1651` → IC=+0.266 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1651 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8288` → IC=+0.254 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8288 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.178` → IC=+0.235 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.178 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.243 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7188` → IC=-0.200 (n=1032)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7188
  - _Potencial_: sin este filtro IC_bueno=+0.280 (n=1035)

- **FILTRO** `ibs_20min` > `0.6875` → IC=-0.231 (n=540)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6875
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1633)

- **FILTRO** `sigma_ewma_delta_pct` > `4.678` → IC=-0.177 (n=475)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.678
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=1698)

- **PATRÓN** `ibs_20min` > `0.7188` → IC=+0.280 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7188 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.8477` → IC=+0.335 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8477 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.159 (n=329)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.302 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `0.6434` → IC=+0.290 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6434 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1042` → IC=+0.293 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1042 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.294 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.443` → IC=+0.323 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.443 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.312 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.212 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.2135` → IC=+0.218 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2135 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.253 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7031 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.208 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.199 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.4945` → IC=+0.218 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4945 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.236 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.015)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.321 (n=847)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.301 (n=595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.6316` → IC=+0.314 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6316 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2035` → IC=+0.319 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2035 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.509` → IC=+0.305 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.509 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.8631` → IC=+0.304 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8631 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.324 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.294 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.286 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2622.2574` → IC=+0.299 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2622.2574 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.295 (n=920)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.278 (n=695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.273 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.3953` → IC=+0.305 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3953 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.2981` → IC=+0.279 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2981 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` < `0.9619` → IC=+0.272 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9619 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.991` → IC=+0.296 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.991 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` < `0.6391` → IC=+0.273 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6391 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `1.2432` → IC=+0.307 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2432 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.337 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `1.4342` → IC=+0.269 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4342 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `2.1624` → IC=+0.275 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1624 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2613.6582` → IC=+0.277 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2613.6582 (IC base=+0.271)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.171 (n=2552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.202 (n=2545)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0899` → IC=+0.185 (n=2545)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0899 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=7948)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.5775` → IC=+0.217 (n=7626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5775 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1759` → IC=+0.196 (n=3358)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1759 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.291` → IC=+0.258 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.291 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2155` → IC=+0.159 (n=5044)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2155 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6287` → IC=+0.160 (n=5044)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6287 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2458` → IC=+0.194 (n=1538)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2458 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.563` → IC=+0.170 (n=3215)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.563 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6282` → IC=+0.175 (n=2436)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6282 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2399.5624` → IC=+0.168 (n=5083)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2399.5624 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.180 (n=6532)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 116.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.182 (n=4870)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0808` → IC=+0.209 (n=2434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0808 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=2789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.226 (n=7299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.1704` → IC=+0.161 (n=5107)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1704 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.316` → IC=+0.195 (n=1246)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.316 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.1748` → IC=+0.153 (n=5298)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1748 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.223 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5653` → IC=+0.168 (n=2913)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5653 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.2631` → IC=+0.171 (n=3001)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.2631 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.174 (n=6266)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 118.0 (IC base=+0.168)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.221 (n=435)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.186 (n=870)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0065 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.3418` → IC=+0.205 (n=1303)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3418 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=871)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.8947` → IC=+0.276 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8947 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.105` → IC=+0.312 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.105 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.236 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.180 (n=1203)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.253 (n=844)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1882` → IC=+0.296 (n=629)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1882 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.264 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.25` → IC=+0.253 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.25 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0959` → IC=+0.235 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0959 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.263 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4205` → IC=+0.260 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4205 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1799.7248` → IC=+0.251 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1799.7248 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.234 (n=382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.0742` → IC=+0.201 (n=379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0742 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=1194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.4081` → IC=+0.224 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4081 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.211` → IC=+0.214 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.211 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.506` → IC=+0.236 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.506 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `1.268` → IC=+0.162 (n=1135)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.268 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `1.0769` → IC=+0.167 (n=515)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0769 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.2324` → IC=+0.200 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2324 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.191 (n=367)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `15862.1611` → IC=+0.162 (n=515)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 15862.1611 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.157 (n=1248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0057 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.204 (n=417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.175 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.5649` → IC=+0.184 (n=1246)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5649 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1345` → IC=+0.160 (n=1229)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1345 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.806` → IC=+0.204 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.806 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.155 (n=1246)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2116 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1573` → IC=+0.153 (n=379)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1573 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4266` → IC=+0.144 (n=1134)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4266 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.171 (n=351)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 215.0 (IC base=+0.135)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.219 (n=581)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.2248` → IC=+0.215 (n=853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2248 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.876` → IC=+0.275 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.876 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.1335` → IC=+0.199 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1335 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.6452` → IC=+0.198 (n=405)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.6452 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.8719` → IC=+0.206 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8719 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.208 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `1952.4384` → IC=+0.199 (n=426)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1952.4384 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.234 (n=1058)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.256 (n=354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.281 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.2417` → IC=+0.258 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2417 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.735` → IC=+0.270 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.735 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3579` → IC=+0.271 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3579 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7913` → IC=+0.218 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7913 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.2259` → IC=+0.226 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2259 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1880.0598` → IC=+0.226 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1880.0598 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.220 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.221)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.172 (n=1072)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0067 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.4324` → IC=+0.157 (n=1217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4324 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=1278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.194 (n=1217)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.375 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1612` → IC=+0.180 (n=817)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1612 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.868` → IC=+0.223 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.868 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.0445` → IC=+0.142 (n=1071)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0445 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.147 (n=1217)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6297 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2462` → IC=+0.198 (n=256)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2462 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.5369` → IC=+0.147 (n=525)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5369 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.5308` → IC=+0.169 (n=397)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.5308 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `6913.8034` → IC=+0.184 (n=811)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 6913.8034 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.141 (n=1159)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 166.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.155 (n=1291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3836` → IC=+0.144 (n=1289)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3836 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.635` → IC=+0.170 (n=1289)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.635 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.5799` → IC=+0.133 (n=1492)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.5799 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.896` → IC=+0.170 (n=453)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 6.896 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.147 (n=860)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8509 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.197 (n=186)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.7931` → IC=+0.133 (n=780)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.7931 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.4935` → IC=+0.135 (n=390)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4935 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `9988.1936` → IC=+0.163 (n=585)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 9988.1936 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.157 (n=625)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=1412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5167` → IC=+0.204 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5167 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.0956` → IC=+0.223 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0956 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.71` → IC=+0.256 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.71 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.130 (n=1380)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2233 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.7251` → IC=+0.122 (n=1231)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.7251 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.165` → IC=+0.131 (n=1387)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.165 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.144 (n=445)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1444)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2897.5388` → IC=+0.195 (n=625)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2897.5388 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.136 (n=1055)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.150 (n=616)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0061 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1031` → IC=+0.155 (n=467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1031 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.209 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.9902` → IC=+0.140 (n=187)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.9902 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.197` → IC=+0.139 (n=1285)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.197 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.973` → IC=+0.145 (n=226)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 8.973 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.1785` → IC=+0.123 (n=1400)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.1785 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2777` → IC=+0.174 (n=170)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2777 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4589` → IC=+0.133 (n=418)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4589 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.4306` → IC=+0.130 (n=417)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4306 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3086.3351` → IC=+0.161 (n=467)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3086.3351 (IC base=+0.114)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0189` → IC=+0.216 (n=877)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0189 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.209 (n=599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.7386` → IC=+0.262 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7386 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.5014` → IC=+0.221 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5014 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.543` → IC=+0.245 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.543 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.209` → IC=+0.206 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.209 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.8594` → IC=+0.224 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8594 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.272 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.1554` → IC=+0.216 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1554 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4098` → IC=+0.208 (n=1270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4098 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2613.0554` → IC=+0.208 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2613.0554 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.233 (n=455)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.207 (n=619)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.224 (n=455)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4385` → IC=+0.246 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4385 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `1.1799` → IC=+0.228 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1799 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.8921` → IC=+0.204 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8921 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.244 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6289` → IC=+0.215 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6289 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.286 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.2213` → IC=+0.195 (n=1077)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2213 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.4425` → IC=+0.199 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4425 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2584.4484` → IC=+0.207 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2584.4484 (IC base=+0.205)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.165 (n=600)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.180 (n=599)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0089 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0996` → IC=+0.153 (n=598)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0996 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.55` → IC=+0.186 (n=1602)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.55 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.3935` → IC=+0.183 (n=547)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.3935 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.719` → IC=+0.175 (n=823)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.719 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8755` → IC=+0.162 (n=1046)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8755 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.2111` → IC=+0.155 (n=523)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.2111 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.173 (n=497)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4385` → IC=+0.164 (n=576)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4385 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5493` → IC=+0.157 (n=575)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5493 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=2031)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `12307.7364` → IC=+0.152 (n=598)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 12307.7364 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.165 (n=1570)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 163.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.134 (n=1259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0057 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.120 (n=1911)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 5.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.188 (n=630)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0588 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.227` → IC=+0.123 (n=1598)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.227 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3863.6748` → IC=+0.124 (n=1259)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3863.6748 (IC base=+0.105)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3377` → IC=+0.123 (n=449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.3377 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.146 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 9.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.2513` → IC=+0.143 (n=449)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.2513 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.3081` → IC=+0.165 (n=159)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3081 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.264` → IC=+0.126 (n=201)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 3.264 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.9156` → IC=+0.136 (n=300)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.9156 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `12687.2059` → IC=+0.133 (n=401)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 12687.2059 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.207 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3387` → IC=+0.151 (n=602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3387 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6039` → IC=+0.179 (n=530)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6039 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.3066` → IC=+0.152 (n=636)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.3066 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.384` → IC=+0.155 (n=233)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 4.384 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.2138` → IC=+0.136 (n=602)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2138 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `0.7175` → IC=+0.148 (n=538)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7175 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.203 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.1013` → IC=+0.154 (n=521)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1013 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.4203` → IC=+0.141 (n=592)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4203 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `332.0` → IC=+0.145 (n=503)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 332.0 (IC base=+0.132)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.259 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.194 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0071 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.0977` → IC=+0.210 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0977 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.226 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.7033` → IC=+0.240 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7033 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.9336` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9336 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.93` → IC=+0.219 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.93 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.8399` → IC=+0.195 (n=368)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8399 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.215 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2607` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2607 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.3924` → IC=+0.234 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3924 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.405` → IC=+0.227 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.405 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=613)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `12351.8233` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 12351.8233 (IC base=+0.190)

- **PATRÓN** `ibs_20min` < `0.0816` → IC=+0.151 (n=173)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0816 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.6847` → IC=+0.123 (n=229)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.6847 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2242` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.2242 (IC base=+0.086)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.525` → IC=-0.159 (n=124)

  - _Acción_: SKIP cuando `ibs_20min` > 0.525
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=376)

- **FILTRO** `dist_vwap_pct` > `0.3414` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3414
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=466)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.192 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0089 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.164 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.7333` → IC=+0.203 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7333 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.6296` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6296 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.208 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.0712` → IC=+0.145 (n=345)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0712 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.7373` → IC=+0.156 (n=350)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7373 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.2252` → IC=+0.167 (n=169)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.2252 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=428)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3062.644` → IC=+0.199 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3062.644 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.525` → IC=+0.140 (n=376)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.525 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.604` → IC=+0.162 (n=155)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.604 (IC base=+0.066)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.182 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0068 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.189 (n=178)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6778` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6778 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.2547` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2547 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.155 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0091 (IC base=+0.122)

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
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.208 (n=3247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=10166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.215 (n=9745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9631` → IC=+0.207 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9631 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.227 (n=4717)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8828` → IC=+0.164 (n=4338)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8828 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2401` → IC=+0.201 (n=1819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2401 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6067` → IC=+0.188 (n=3116)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6067 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2342.4972` → IC=+0.172 (n=6490)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2342.4972 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.195 (n=7361)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 87.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.190 (n=5904)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.007 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1472` → IC=+0.189 (n=3896)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1472 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.237 (n=8849)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2471` → IC=+0.161 (n=5478)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2471 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.975` → IC=+0.202 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.975 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.719` → IC=+0.181 (n=8571)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.719 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7048` → IC=+0.162 (n=2683)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7048 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.243 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6334` → IC=+0.193 (n=2700)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6334 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.192 (n=5169)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 48.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.208 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.224 (n=552)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.200 (n=1120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.321 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.524` → IC=+0.344 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.524 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2734` → IC=+0.249 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2734 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.552` → IC=+0.181 (n=688)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.552 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.2444` → IC=+0.201 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2444 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=983)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.258 (n=1288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.263 (n=1150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1279` → IC=+0.287 (n=566)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1279 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=1180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3469` → IC=+0.290 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3469 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.466` → IC=+0.263 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.466 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.291 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `1.8649` → IC=+0.274 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8649 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1796.4338` → IC=+0.265 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1796.4338 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.193 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.084` → IC=+0.160 (n=519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.084 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3123` → IC=+0.202 (n=1557)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3123 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.3427` → IC=+0.196 (n=640)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3427 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.74` → IC=+0.174 (n=357)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 9.74 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.23` → IC=+0.152 (n=1399)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.23 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.63` → IC=+0.177 (n=519)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.63 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2681` → IC=+0.204 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2681 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1149` → IC=+0.162 (n=1322)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1149 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7577` → IC=+0.155 (n=1001)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7577 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `15643.6309` → IC=+0.151 (n=706)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 15643.6309 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `478.0` → IC=+0.158 (n=1432)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 478.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.165 (n=1355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3225` → IC=+0.161 (n=1353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3225 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.175 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.653` → IC=+0.192 (n=1353)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.653 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.135` → IC=+0.165 (n=1217)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.135 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.177` → IC=+0.157 (n=645)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.177 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.162 (n=1353)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1894 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1533` → IC=+0.200 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1533 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.3998` → IC=+0.160 (n=1255)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.3998 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.0862` → IC=+0.161 (n=570)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.0862 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `424.0` → IC=+0.157 (n=1018)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 424.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.246 (n=526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=1650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=1606)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6711` → IC=+0.256 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6711 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.811` → IC=+0.292 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.811 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2126` → IC=+0.221 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2126 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.8468` → IC=+0.243 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8468 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.229 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1955.5029` → IC=+0.221 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1955.5029 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.231 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.241 (n=1465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1656` → IC=+0.240 (n=645)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1656 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.266 (n=548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3594` → IC=+0.271 (n=1289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3594 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.751` → IC=+0.279 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.751 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3451` → IC=+0.298 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3451 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7614` → IC=+0.238 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7614 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1969` → IC=+0.236 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1969 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.245 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1876.5391` → IC=+0.250 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.5391 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.231 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.183 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0035 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4376` → IC=+0.142 (n=1658)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4376 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=1735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.8762` → IC=+0.259 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8762 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.3708` → IC=+0.165 (n=663)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3708 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.171` → IC=+0.158 (n=688)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.171 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.877` → IC=+0.153 (n=1106)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.877 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2367` → IC=+0.215 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2367 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.5214` → IC=+0.147 (n=706)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.5214 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.7649` → IC=+0.145 (n=1069)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7649 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `8147.128` → IC=+0.228 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8147.128 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.152 (n=518)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 80.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.155 (n=1360)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4464` → IC=+0.153 (n=1360)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4464 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6991` → IC=+0.181 (n=1360)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6991 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.5983` → IC=+0.141 (n=1501)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.5983 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.137` → IC=+0.178 (n=200)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.137 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.146 (n=907)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8616 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1921` → IC=+0.138 (n=454)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.1921 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.245 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4439` → IC=+0.150 (n=1288)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4439 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `10917.9028` → IC=+0.208 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10917.9028 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.143 (n=1282)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 179.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.137 (n=1097)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0081 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=1690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.191 (n=1644)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4717 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0762` → IC=+0.203 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0762 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.453` → IC=+0.234 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.453 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.8926` → IC=+0.133 (n=1097)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8926 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1658)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2911.4143` → IC=+0.249 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.4143 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.130 (n=1261)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 54.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.173 (n=539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.1305` → IC=+0.162 (n=539)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1305 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=1669)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.203 (n=1619)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.2182` → IC=+0.129 (n=1311)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.2182 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.446` → IC=+0.124 (n=1564)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.446 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.72` → IC=+0.153 (n=712)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.72 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.172 (n=251)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.139 (n=485)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.5228` → IC=+0.130 (n=485)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5228 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2848.7898` → IC=+0.164 (n=539)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2848.7898 (IC base=+0.112)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0193` → IC=+0.221 (n=1099)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0193 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.213 (n=1476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.5146` → IC=+0.251 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5146 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.2017` → IC=+0.234 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2017 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.171` → IC=+0.271 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.171 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.6381` → IC=+0.218 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6381 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.253 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.239 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2618.726` → IC=+0.224 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2618.726 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.225 (n=591)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.218 (n=591)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.208 (n=1249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5185` → IC=+0.255 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5185 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `1.2198` → IC=+0.201 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2198 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.9088` → IC=+0.204 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9088 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.764` → IC=+0.264 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.764 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2333` → IC=+0.233 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2333 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.262 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2045` → IC=+0.195 (n=1396)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2045 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.197 (n=1587)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=2942)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.159 (n=2476)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0093 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.151 (n=2510)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0056 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.5232` → IC=+0.159 (n=2809)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5232 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=1121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.166 (n=1260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.213 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1896` → IC=+0.156 (n=1029)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1896 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.4942` → IC=+0.144 (n=1677)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4942 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.136` → IC=+0.180 (n=458)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.136 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.9028` → IC=+0.164 (n=1199)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.9028 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1725` → IC=+0.182 (n=768)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1725 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4563` → IC=+0.157 (n=925)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4563 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8861` → IC=+0.162 (n=1850)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8861 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3701.6132` → IC=+0.152 (n=1873)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3701.6132 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=740)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.156 (n=2219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.164 (n=754)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1841` → IC=+0.167 (n=976)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1841 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6896` → IC=+0.149 (n=428)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.6896 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.4314` → IC=+0.130 (n=2189)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4314 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.22` → IC=+0.145 (n=2209)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.22 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2456` → IC=+0.142 (n=2116)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2456 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.145 (n=1029)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5357` → IC=+0.146 (n=964)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.5357 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.8147` → IC=+0.142 (n=1460)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8147 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=2942)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `6937.818` → IC=+0.150 (n=1982)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6937.818 (IC base=+0.137)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.168 (n=329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0056 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.177 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0065 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0895` → IC=+0.185 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0895 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.5452` → IC=+0.186 (n=250)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.5452 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.212` → IC=+0.150 (n=178)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.212 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.3825` → IC=+0.155 (n=363)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.3825 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.399` → IC=+0.163 (n=398)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 2.399 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.849` → IC=+0.189 (n=249)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.849 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.3101` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3101 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.185 (n=125)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.6734` → IC=+0.209 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6734 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `12451.0907` → IC=+0.191 (n=334)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 12451.0907 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.212 (n=408)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1116` → IC=+0.172 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1116 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.172 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.175 (n=407)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1382 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.142 (n=420)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6084 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.6984` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6984 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2186` → IC=+0.138 (n=947)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2186 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.159 (n=904)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.183 (n=617)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8812 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.165 (n=434)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.422` → IC=+0.145 (n=308)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.422 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.147 (n=615)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `11389.4654` → IC=+0.148 (n=925)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 11389.4654 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `707.0` → IC=+0.144 (n=880)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 707.0 (IC base=+0.136)

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

- **PATRÓN** `volumen_pendiente_norm` < `0.3499` → IC=+0.170 (n=749)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.3499 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `3.3904` → IC=+0.167 (n=622)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3904 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2425.929` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2425.929 (IC base=+0.165)

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
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.153 (n=759)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0075 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.162 (n=862)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.154 (n=287)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.168 (n=302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 4.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5618` → IC=+0.156 (n=574)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5618 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.8892` → IC=+0.171 (n=287)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8892 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.9756` → IC=+0.163 (n=200)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.9756 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.4256` → IC=+0.165 (n=792)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.4256 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.161 (n=863)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.7212` → IC=+0.155 (n=769)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7212 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.1119` → IC=+0.156 (n=792)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1119 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1724` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1724 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.211` → IC=+0.157 (n=742)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.211 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.154 (n=753)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=839)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.155 (n=726)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0084 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3946` → IC=+0.172 (n=639)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3946 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.148 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.141 (n=726)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.7466 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.103` → IC=+0.152 (n=726)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.103 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.6243` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6243 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.3867` → IC=+0.142 (n=730)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3867 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.738` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.738 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.141 (n=658)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6452` → IC=+0.168 (n=242)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6452 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.7288` → IC=+0.143 (n=648)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.7288 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.167 (n=307)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.153 (n=626)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7829` → IC=+0.151 (n=474)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.7829 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7600.4466` → IC=+0.164 (n=726)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 7600.4466 (IC base=+0.140)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.2712` → IC=+0.130 (n=133)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.2712 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.218` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.218 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `1.3888` → IC=+0.121 (n=204)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.3888 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `3421.4081` → IC=+0.147 (n=188)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3421.4081 (IC base=+0.092)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.146 (n=207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0069 (IC base=+0.110)

- **PATRÓN** `drift_60min` |x|≤ `0.3981` → IC=+0.157 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3981 (IC base=+0.110)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.155 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 10.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1429 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `0.6189` → IC=+0.180 (n=98)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6189 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.711` → IC=+0.136 (n=116)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 2.711 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` < `0.089` → IC=+0.165 (n=159)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.089 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.8703` → IC=+0.125 (n=134)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.8703 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `3258.9665` → IC=+0.146 (n=207)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3258.9665 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.155 (n=201)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 62.0 (IC base=+0.110)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.214 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=355)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.187 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=359)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.195 (n=388)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.004 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.127 (n=815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6778` → IC=+0.204 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6778 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.153` → IC=+0.161 (n=437)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.153 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.428` → IC=+0.220 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.428 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.199 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `2.0918` → IC=+0.137 (n=593)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.0918 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=632)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2424.4386` → IC=+0.145 (n=345)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2424.4386 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.057` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.057 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.122 (n=305)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `2.5523` → IC=+0.135 (n=220)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5523 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.136 (n=196)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4444 (IC base=+0.002)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.165 (n=299)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.006 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.5273` → IC=+0.189 (n=268)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5273 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.1343` → IC=+0.183 (n=143)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1343 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.581` → IC=+0.132 (n=161)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 3.581 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` < `0.0677` → IC=+0.137 (n=202)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.0677 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.176 (n=202)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=276)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `4049.9563` → IC=+0.144 (n=116)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4049.9563 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.279` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.279 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.6023` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6023 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.3433` → IC=+0.170 (n=98)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.3433 (IC base=+0.051)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.237 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=111)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=112)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.179 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0039 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.6816` → IC=+0.227 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6816 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.3362` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.3362 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.807` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.807 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `1.0654` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0654 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `1.7369` → IC=+0.160 (n=145)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.7369 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=178)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `1767.0561` → IC=+0.189 (n=88)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1767.0561 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.1419` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1419 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` < `0.1269` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1269 (IC base=-0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.838` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.838 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `2.3094` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.3094 (IC base=-0.017)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=-0.017)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.0714` → IC=-0.245 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0714
  - _Potencial_: sin este filtro IC_bueno=+0.276 (n=47)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.124 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0061 (IC base=+0.075)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.133 (n=197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 13.0 (IC base=+0.075)

- **PATRÓN** `ibs_20min` > `0.6744` → IC=+0.176 (n=223)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6744 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.158 (n=144)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.351` → IC=+0.183 (n=99)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.351 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0643` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0643 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2448` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2448 (IC base=+0.075)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.123 (n=67)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0075 (IC base=-0.048)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=-0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.202` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.202 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.1002` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1002 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5975 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` > `1.3803` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.3803 (IC base=-0.048)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `9.0` → IC=-0.396 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=148)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=179)

- **FILTRO** `volumen_regimen` < `0.7468` → IC=-0.348 (n=64)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=130)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.379 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=112)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=147)

- **FILTRO** `sigma_ewma_delta_pct` > `8.488` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.488
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=139)

- **FILTRO** `volumen_pendiente_norm` > `0.0895` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0895
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=67)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=53)

- **FILTRO** `ibs_20min` < `0.0329` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0329
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

- **FILTRO** `volumen_regimen` < `0.8127` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8127
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=51)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.292 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=47)

- **FILTRO** `dist_vwap_pct` < `0.0689` → IC=-0.309 (n=40)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0689
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **FILTRO** `sigma_ewma_delta_pct` > `5.128` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.128
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=49)

- **FILTRO** `volumen_regimen` > `0.9309` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9309
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=52)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.441 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33)

- **FILTRO** `volumen_regimen` > `0.8808` → IC=-0.235 (n=32)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8808
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=33)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=38)

- **FILTRO** `ibs_20min` > `0.6404` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6404
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **FILTRO** `dist_vwap_pct` < `0.2294` → IC=-0.276 (n=47)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2294
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2109` → IC=-0.409 (n=20)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2109
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=40)

- **FILTRO** `volumen_spike_ratio` > `2.138` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.138
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `dist_vwap_pct` > `0.6355` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6355
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=322)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.140 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0057 (IC base=+0.087)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.133 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.157 (n=246)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.6522 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.4919` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.4919 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.122 (n=231)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.2 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `3787.1326` → IC=+0.150 (n=118)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3787.1326 (IC base=+0.042)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.576` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.576
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=82)

- **FILTRO** `volumen_regimen` < `0.7924` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7924
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=82)

- **PATRÓN** `drift_60min` |x|≤ `0.2285` → IC=+0.141 (n=101)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2285 (IC base=+0.106)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.1218` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1218 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` < `0.1813` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1813 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `2.9499` → IC=+0.144 (n=88)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.9499 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.106)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_liquidez` < `1549.4073` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 1549.4073
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=55)

- **FILTRO** `ibs_20min` > `0.2038` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2038
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=73)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.009)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=42)

- **FILTRO** `volumen_regimen` < `1.0341` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0341
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=40)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.194 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0069 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.214 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.189 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.6875` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6875 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.7975` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7975 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.06 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.043)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.8446` → IC=+0.361 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8446 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `1559.0` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1559.0 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `193.3` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.3 (IC base=+0.202)

- **PATRÓN** `drift_15min` |x|≤ `2.414` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.414 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.300 (n=23)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.202)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.8446` → IC=+0.361 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8446 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `1559.0` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1559.0 (IC base=+0.288)

- **PATRÓN** `elapsed_s` > `193.3` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.3 (IC base=+0.202)

- **PATRÓN** `drift_15min` |x|≤ `2.414` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.414 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.300 (n=23)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.202)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=673)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2908.9915` → IC=+0.171 (n=226)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2908.9915 (IC base=+0.106)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=673)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2908.9915` → IC=+0.171 (n=226)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2908.9915 (IC base=+0.106)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=78)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=131)

- **FILTRO** `libro_liquidez` < `2415.4574` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `libro_liquidez` < 2415.4574
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=111)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=206)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=192)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1714)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9583` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9583
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=76)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=60)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.127 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 14.0 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 25.0 (IC base=+0.045)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `29085.84` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `liq_usd_total` < 29085.84
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=130)

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

- **PATRÓN** `liq_n` > `18.0` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.026)

- **PATRÓN** `liq_usd_total` > `80598.37` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `liq_usd_total` > 80598.37 (IC base=+0.026)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.026)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=758)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=427)

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
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=146)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=87)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=620)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=620)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=492)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=339)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=339)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.148 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=268)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.122 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=99)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=198)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=78)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=81)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=235)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=235)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=122)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.183 (n=102)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=243)

- **FILTRO** `restante_min` < `3.32` → IC=-0.148 (n=86)

  - _Acción_: SKIP cuando `restante_min` < 3.32
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=259)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.126 (n=97)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=278)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.47 (IC base=+0.030)

- **PATRÓN** `profundidad_ratio` > `99.1` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `profundidad_ratio` > 99.1 (IC base=+0.030)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.56 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.096)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.59` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.59 (IC base=+0.119)

- **PATRÓN** `restante_min` < `3.1` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` < 3.1 (IC base=+0.119)

- **PATRÓN** `restante_min` > `3.99` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `restante_min` > 3.99 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `60.77` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 60.77 (IC base=+0.119)

- **PATRÓN** `profundidad_ratio` > `79.6` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `profundidad_ratio` > 79.6 (IC base=+0.119)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=23)

- **FILTRO** `profundidad_ratio` < `60.7` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `profundidad_ratio` < 60.7
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.58` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `restante_min` < `3.82` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `restante_min` < 3.82
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `lag_apertura_s` > `60.81` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.81
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` > `0.54` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=16)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.257 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `restante_min` < `2.9` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `restante_min` < 2.9
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=38)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=40)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=7421)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.172 (n=3224)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=10437)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.168 (n=3536)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=10626)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.212 (n=588)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1778)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.156 (n=628)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=1910)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.202 (n=585)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=1826)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=619)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1911)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.168 (n=585)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1764)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.182 (n=620)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1910)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2724)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2895)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2901)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=615)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` > `0.1705` → IC=-0.142 (n=121)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1705
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=366)

- **FILTRO** `libro_liquidez` < `17151.9847` → IC=-0.130 (n=160)

  - _Acción_: SKIP cuando `libro_liquidez` < 17151.9847
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=327)

- **FILTRO** `libro_liquidez` < `16943.7323` → IC=-0.135 (n=220)

  - _Acción_: SKIP cuando `libro_liquidez` < 16943.7323
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=662)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=239)

- **FILTRO** `ibs_20min` < `0.1064` → IC=-0.244 (n=76)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1064
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=231)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.279 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=232)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.227 (n=192)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=583)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=9688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=21716)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=7658)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=23746)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.236 (n=7835)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=23569)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=10672)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=20732)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9677)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=29633)

- **FILTRO** `ibs_7min` > `0.2936` → IC=-0.179 (n=9827)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2936
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=29483)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=1234)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3945)

- **FILTRO** `ibs_7min` < `0.7099` → IC=-0.250 (n=1709)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7099
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3470)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.185 (n=1195)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3984)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.260 (n=1672)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=5088)

- **FILTRO** `drift_7min_pct` |x|> `0.112` → IC=-0.124 (n=2298)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.112
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4462)

- **FILTRO** `ibs_7min` > `0.7911` → IC=-0.206 (n=1689)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7911
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=5071)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4166)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1305)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4126)

- **FILTRO** `ibs_7min` < `0.7484` → IC=-0.192 (n=1357)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7484
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4074)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.170 (n=1357)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4074)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.254 (n=1364)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4134)

- **FILTRO** `ibs_7min` > `0.2607` → IC=-0.176 (n=1373)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2607
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4125)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.184 (n=1372)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4126)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.166 (n=1394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=3513)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.307 (n=1205)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3702)

- **FILTRO** `ibs_7min` < `0.1935` → IC=-0.259 (n=1225)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1935
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3682)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.219 (n=1153)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3754)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.237 (n=1659)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=5561)

- **FILTRO** `ibs_7min` > `0.75` → IC=-0.177 (n=1800)

  - _Acción_: SKIP cuando `ibs_7min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=5420)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.233 (n=1531)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=3652)

- **FILTRO** `ibs_7min` < `0.742` → IC=-0.182 (n=1295)

  - _Acción_: SKIP cuando `ibs_7min` < 0.742
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3888)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.171 (n=1276)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3907)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.267 (n=1167)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=4105)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.175 (n=1317)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3955)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.188 (n=1309)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3963)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.262 (n=1323)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=4167)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.241 (n=1367)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4123)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.178 (n=1787)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=5690)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=1241)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3973)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.228 (n=1290)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3924)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1262)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3952)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.203 (n=1707)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=5376)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1059)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=527)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=984)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=550)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.145 (n=482)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.134 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 14.0 (IC base=+0.114)

- **PATRÓN** `total_vol_5m` < `469.512` → IC=+0.147 (n=242)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 469.512 (IC base=+0.114)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.144 (n=57)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.138 (n=150)

  - _Acción_: Kelly boost +0.69€ cuando `total_vol_5m` < 451.687 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 13.0 (IC base=+0.132)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.121 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 13.0 (IC base=+0.093)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.180 (n=98)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.094)

- **PATRÓN** `total_vol_5m` < `394.71` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.71 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 69.0 (IC base=+0.094)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.180 (n=126)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 6300.756 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 37.0 (IC base=+0.141)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.148 (n=126)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.139 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 13.0 (IC base=+0.105)

- **PATRÓN** `total_vol_5m` < `262739.3` → IC=+0.149 (n=95)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 262739.3 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3566.692` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3566.692 (IC base=+0.105)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.327 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=245)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `51.365` → IC=-0.347 (n=57)

  - _Acción_: SKIP cuando `T_h` > 51.365
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=58)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.175 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0053 (IC base=-0.133)

- **PATRÓN** `T_h` < `39.9942` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `T_h` < 39.9942 (IC base=-0.133)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.208 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=44)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.237 (n=184)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=189)

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.317 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=240)

- **FILTRO** `T_h` > `63.8116` → IC=-0.326 (n=239)

  - _Acción_: SKIP cuando `T_h` > 63.8116
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=81)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.008` → IC=-0.136 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

- **FILTRO** `T_h` > `72.5264` → IC=-0.163 (n=87)

  - _Acción_: SKIP cuando `T_h` > 72.5264
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=44)

- **FILTRO** `pct_vs_K` |x|> `2.9087` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9087
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=99)

- **FILTRO** `T_h` < `96.6729` → IC=-0.375 (n=38)

  - _Acción_: SKIP cuando `T_h` < 96.6729
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=79)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9558` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `T_h` > 135.9558
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=79)

- **FILTRO** `pct_vs_K` |x|> `2.4229` → IC=-0.352 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4229
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.315 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=78)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.352 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=78)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0082` → IC=-0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=59)

- **FILTRO** `T_h` > `133.4167` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `T_h` > 133.4167
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=59)

- **FILTRO** `pct_vs_K` |x|> `5.0091` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.0091
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **FILTRO** `sigma_h` < `0.0156` → IC=-0.360 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0156
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `T_h` > `63.3218` → IC=-0.378 (n=47)

  - _Acción_: SKIP cuando `T_h` > 63.3218
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=17)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.381)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.447 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.381)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.381)

- **PATRÓN** `dist_50` > `0.4444` → IC=+0.474 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.381)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.381)

- **PATRÓN** `edge` > `0.096` → IC=+0.456 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.456 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.417)

- **PATRÓN** `T_h` < `0.639` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.639 (IC base=+0.417)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.438 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.3938` → IC=+0.485 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3938 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.467 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1078` → IC=+0.443 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1078 (IC base=+0.407)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.389 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.407)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.407)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.441 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.407)

- **PATRÓN** `T_h` > `0.5243` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5243 (IC base=+0.407)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.407)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.407)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.481)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.471 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.481)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.471 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.481)

- **PATRÓN** `T_h` > `0.8566` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8566 (IC base=+0.481)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.463 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.481)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.481)

- **PATRÓN** `edge` > `0.096` → IC=+0.478 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.469)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.478 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.469)

- **PATRÓN** `T_h` > `1.2464` → IC=+0.467 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2464 (IC base=+0.469)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.488 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.469)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.476 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.469)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=167)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=284)

- **PATRÓN** `streak_estiramiento` < `0.4117` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.4117 (IC base=+0.038)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.161 (n=122)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.034)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.206 (n=15)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `990711.2` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_racha` > 990711.2
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=27)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=78)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=88)

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
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=747)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=753)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=387)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=582)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1108)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=728)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=702)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2843)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1444)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1452)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.221 (n=693)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0744` → IC=+0.201 (n=673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0744 (IC base=+0.185)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2127` → IC=+0.193 (n=510)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.2127 (IC base=+0.185)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1263` → IC=+0.228 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1263 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=1429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.185)

- **PATRÓN** `ibs_15` > `0.6047` → IC=+0.262 (n=1530)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6047 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.3008` → IC=+0.191 (n=542)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.3008 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.899` → IC=+0.276 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.899 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2979.0729` → IC=+0.192 (n=1019)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2979.0729 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.203 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.185)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=567)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.209 (n=352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.292 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.199)

- **PATRÓN** `drift_15min` |x|≤ `0.3838` → IC=+0.208 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3838 (IC base=+0.199)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.248 (n=117)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.199)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.266 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.218 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.199)

- **PATRÓN** `ibs_15` > `0.7036` → IC=+0.266 (n=352)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7036 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.3946` → IC=+0.255 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3946 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.55` → IC=+0.268 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.55 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `15953.0262` → IC=+0.233 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15953.0262 (IC base=+0.199)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `24.537` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 24.537
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=352)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.139 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0036 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.158 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0051 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.069` → IC=+0.152 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.069 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.178 (n=119)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2558` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2558 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.6642` → IC=+0.241 (n=319)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6642 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.5648` → IC=+0.142 (n=79)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.5648 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1658` → IC=+0.154 (n=278)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1658 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.386` → IC=+0.201 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.386 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3459.7073` → IC=+0.148 (n=319)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3459.7073 (IC base=+0.136)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2175` → IC=-0.233 (n=28)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2175
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=86)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.297 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1498` → IC=+0.207 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1498 (IC base=+0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.207 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2704` → IC=+0.224 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2704 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.213 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.258 (n=184)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.2696` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2696 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.532` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.532 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `3056.7878` → IC=+0.279 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3056.7878 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.226 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.172)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.7105` → IC=-0.146 (n=97)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.7105
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=870)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.662` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.662 (IC base=+0.021)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0178` → IC=+0.237 (n=272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0178 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0864` → IC=+0.210 (n=181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0864 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0389` → IC=+0.193 (n=408)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0389 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.245 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.239 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.285 (n=408)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1318` → IC=+0.210 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1318 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.928` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.928 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.396` → IC=+0.189 (n=365)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 7.396 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2911.0954` → IC=+0.283 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.0954 (IC base=+0.188)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.159 (n=458)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1176 (IC base=+0.046)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.336 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.335)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.374 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `0.1082` → IC=+0.343 (n=266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1082 (IC base=+0.335)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.361 (n=265)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.335)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.372 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.382 (n=185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.335)

- **PATRÓN** `ibs_15` > `0.7853` → IC=+0.380 (n=399)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7853 (IC base=+0.335)

- **PATRÓN** `dist_vwap_pct` > `0.4316` → IC=+0.387 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4316 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.143` → IC=+0.340 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.143 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.729` → IC=+0.335 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.729 (IC base=+0.335)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.342 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `3532.3524` → IC=+0.350 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3532.3524 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `472.0` → IC=+0.357 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 472.0 (IC base=+0.335)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.349 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.340)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.370 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.340)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.370 (n=75)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.340)

- **PATRÓN** `drift_15min` |x|≤ `0.4326` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4326 (IC base=+0.340)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.360 (n=148)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.340)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.382 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.340)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.366 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.340)

- **PATRÓN** `ibs_15` > `0.8154` → IC=+0.376 (n=223)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8154 (IC base=+0.340)

- **PATRÓN** `dist_vwap_pct` > `0.4016` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4016 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.343 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `15670.1365` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15670.1365 (IC base=+0.340)

- **PATRÓN** `ballena_activa_n` < `581.0` → IC=+0.387 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 581.0 (IC base=+0.340)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.380 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.326)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.342 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.326)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.350 (n=158)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.326)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.357 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.326)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.393 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.326)

- **PATRÓN** `ibs_15` > `0.7359` → IC=+0.388 (n=176)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7359 (IC base=+0.326)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.379 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.326)

- **PATRÓN** `dist_vwap_pct` < `0.1256` → IC=+0.332 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1256 (IC base=+0.326)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.639` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.639 (IC base=+0.326)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.587` → IC=+0.329 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.587 (IC base=+0.326)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.341 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `3546.8859` → IC=+0.357 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3546.8859 (IC base=+0.326)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.338 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.326)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0131` → IC=-0.220 (n=640)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0131
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1924)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.191 (n=864)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1700)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1365` → IC=+0.249 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1365 (IC base=-0.064)

- **PATRÓN** `ibs_15` > `0.6349` → IC=+0.268 (n=615)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6349 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` > `0.581` → IC=+0.178 (n=116)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.581 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` < `0.2759` → IC=+0.178 (n=482)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2759 (IC base=-0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1184` → IC=+0.241 (n=1109)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1184 (IC base=-0.035)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1771` → IC=+0.235 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1771 (IC base=-0.035)

- **PATRÓN** `ibs_15` < `0.3488` → IC=+0.276 (n=1664)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3488 (IC base=-0.035)

- **PATRÓN** `dist_vwap_pct` > `0.6882` → IC=+0.287 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6882 (IC base=-0.035)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.217 (n=390)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1173)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.230 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1173)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.207 (n=990)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=573)

- **FILTRO** `sigma_ewma_delta_pct` > `19.563` → IC=-0.247 (n=279)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.563
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1284)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.169 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0028 (IC base=+0.074)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.282 (n=76)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.074)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=+0.074)

- **PATRÓN** `ibs_15` > `0.7413` → IC=+0.316 (n=166)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7413 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.281 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.5415` → IC=+0.272 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5415 (IC base=+0.074)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6647` → IC=-0.197 (n=97)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6647
  - _Potencial_: sin este filtro IC_bueno=+0.263 (n=293)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=373)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.147 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0068 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.190 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0051 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.218 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.148)

- **PATRÓN** `drift_15min` |x|≤ `0.4223` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `drift_15min` |x|≤ 0.4223 (IC base=+0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1329` → IC=+0.160 (n=195)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1329 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.238 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.6647` → IC=+0.263 (n=293)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6647 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.4713` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.4713 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.164` → IC=+0.176 (n=223)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.164 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.009` → IC=+0.157 (n=249)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 9.009 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=373)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.196 (n=133)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.261 (n=220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.4431` → IC=+0.225 (n=660)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4431 (IC base=+0.224)

- **PATRÓN** `drift_15min` |x|≤ `0.7872` → IC=+0.231 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7872 (IC base=+0.224)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.251 (n=299)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.240 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.224)

- **PATRÓN** `ibs_15` < `0.2693` → IC=+0.277 (n=581)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2693 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.7711` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7711 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.823` → IC=+0.248 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.823 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.182` → IC=+0.231 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.182 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `3551.8492` → IC=+0.225 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3551.8492 (IC base=+0.224)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.237 (n=150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=453)

- **FILTRO** `drift_60min` |x|> `0.1657` → IC=-0.220 (n=205)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1657
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=398)

- **FILTRO** `drift_15min` |x|> `0.8922` → IC=-0.263 (n=150)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8922
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=453)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.166)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0758` → IC=+0.223 (n=269)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0758 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.262 (n=301)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.4921` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4921 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.218 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.199 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.261 (n=379)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=380)

- **FILTRO** `drift_15min` |x|> `1.2406` → IC=-0.259 (n=189)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2406
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=570)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=185)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=574)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1563` → IC=+0.281 (n=149)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1563 (IC base=-0.046)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.348 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.3457` → IC=+0.307 (n=448)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3457 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` > `0.8999` → IC=+0.343 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8999 (IC base=-0.046)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.200 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.054)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.200 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1687` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1687 (IC base=+0.054)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.293 (n=428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.288 (n=291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.319 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.306 (n=214)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.344 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.324 (n=641)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.1578` → IC=+0.320 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1578 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.329 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `14446.4188` → IC=+0.301 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14446.4188 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.310 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.287 (n=162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.343 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.302 (n=119)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3729` → IC=+0.302 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3729 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.313 (n=356)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.4357` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4357 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.355 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `16045.3097` → IC=+0.326 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16045.3097 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.306 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.298 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1882` → IC=+0.312 (n=131)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1882 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2866` → IC=+0.334 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2866 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.330 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8486` → IC=+0.336 (n=285)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8486 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` < `0.456` → IC=+0.294 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.456 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.315 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.308 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.186 (n=68)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=206)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1131` → IC=-0.171 (n=68)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1131
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=206)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1209` → IC=-0.164 (n=108)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1209
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=327)

- **FILTRO** `drift_15min` |x|> `0.5291` → IC=-0.136 (n=108)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5291
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=327)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1445` → IC=-0.148 (n=52)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1445
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=107)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.262 (n=19)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

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
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.103` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.103
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `drift_15min` |x|> `0.2655` → IC=-0.220 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `71.4766` → IC=+0.211 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 71.4766 (IC base=+0.198)

- **PATRÓN** `ratio` < `0.9779` → IC=+0.462 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9779 (IC base=+0.198)

- **PATRÓN** `T_h` > `145.7851` → IC=+0.394 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7851 (IC base=+0.332)

- **PATRÓN** `ratio` > `1.0088` → IC=+0.273 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0088 (IC base=+0.332)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `73.0783` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `T_h` > 73.0783 (IC base=+0.172)

- **PATRÓN** `ratio` < `0.973` → IC=+0.442 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.172)

- **PATRÓN** `T_h` > `99.1458` → IC=+0.291 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 99.1458 (IC base=+0.281)

- **PATRÓN** `ratio` > `1.0455` → IC=+0.327 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0455 (IC base=+0.281)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.9957` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9957 (IC base=+0.242)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.413 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.242)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.326 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.308)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.306 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.308)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1359` → IC=+0.457 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1359 (IC base=+0.403)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6047 sube el IC de +0.185 a +0.262 en UPDOWN_GBM#15min (n=1530). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.199 a +0.266 en UPDOWN_GBM#BTC#15min (n=352). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6642 sube el IC de +0.136 a +0.241 en UPDOWN_GBM#ETH#15min (n=319). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.172 a +0.258 en UPDOWN_GBM#SOL#15min (n=184). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.188 a +0.285 en UPDOWN_GBM#XRP#15min (n=408). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.046 a +0.159 en UPDOWN_GBM#XRP#15min (n=458). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6349 sube el IC de -0.064 a +0.268 en UPDOWN_GBM_15M_TARDIO (n=615). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3488 sube el IC de -0.035 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1664). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7413 sube el IC de +0.074 a +0.316 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=166). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.148 a +0.263 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=293). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2693 sube el IC de +0.224 a +0.277 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=581). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.166 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.042 a +0.262 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=301). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3457 sube el IC de -0.046 a +0.307 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=448). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.289 a +0.324 en UPDOWN_GBM_IBS_ALTO (n=641). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.281 a +0.313 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=356). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8486 sube el IC de +0.296 a +0.336 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=285). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7853 sube el IC de +0.335 a +0.380 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=399). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8154 sube el IC de +0.340 a +0.376 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=223). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7359 sube el IC de +0.326 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=176). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1299 | +0.097 | +188.34€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1299 | +0.097 | +188.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 966 | +0.107 | +163.28€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 966 | +0.107 | +163.28€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 247 | +0.050 | +6.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 247 | +0.050 | +6.40€ | 6 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 24578 | -0.091 | -3160.29€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1432 | -0.047 | -222.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 23146 | -0.094 | -2937.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3609 | -0.087 | -590.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3609 | -0.087 | -590.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1432 | -0.047 | -222.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1432 | -0.047 | -222.59€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7099 | -0.024 | -659.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7099 | -0.024 | -659.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6570 | -0.098 | -454.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6570 | -0.098 | -454.35€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5494 | -0.183 | -1072.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5494 | -0.183 | -1072.71€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 17381 | -0.029 | +4078.94€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4548 | +0.000 | +1826.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 12833 | -0.039 | +2251.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 17381 | -0.029 | +4078.94€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4548 | +0.000 | +1826.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 12833 | -0.039 | +2251.98€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1469 | -0.102 | -185.83€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1301 | -0.108 | -164.47€ | 0 | 0 |
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
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 90335 | +0.112 | -4651.86€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13710 | +0.184 | -442.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 361 | -0.089 | -50.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 70353 | +0.100 | -3947.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5911 | +0.108 | -211.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11703 | +0.097 | -1018.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 44 | -0.174 | -3.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11644 | +0.099 | -1003.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 18271 | +0.131 | -384.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4304 | +0.202 | -148.29€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11661 | +0.111 | -186.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2264 | +0.105 | -27.82€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11742 | +0.089 | -1105.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 51 | -0.085 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11676 | +0.090 | -1088.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 19232 | +0.123 | -406.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5298 | +0.175 | -80.89€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11785 | +0.105 | -263.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2137 | +0.098 | -53.32€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 17669 | +0.114 | -1035.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3968 | +0.188 | -212.18€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 264 | -0.049 | +3.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11927 | +0.091 | -697.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1510 | +0.127 | -130.09€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11718 | +0.101 | -700.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 45 | -0.032 | +7.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11660 | +0.101 | -708.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 14325 | +0.192 | -935.25€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 14325 | +0.192 | -935.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3423 | +0.168 | -360.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3423 | +0.168 | -360.41€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1144 | +0.195 | -8.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1144 | +0.195 | -8.99€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3367 | +0.181 | -285.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3367 | +0.181 | -285.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3007 | +0.238 | -99.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3007 | +0.238 | -99.49€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3305 | +0.194 | -194.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3305 | +0.194 | -194.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 675 | +0.431 | -17.86€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 675 | +0.431 | -17.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 259 | +0.435 | -4.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 259 | +0.435 | -4.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 254 | +0.438 | -2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 254 | +0.438 | -2.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 154 | +0.404 | -10.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 154 | +0.404 | -10.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 49294 | +0.197 | -3922.30€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 49294 | +0.197 | -3922.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8542 | +0.175 | -1009.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8542 | +0.175 | -1009.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7871 | +0.223 | -297.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7871 | +0.223 | -297.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8507 | +0.172 | -1027.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8507 | +0.172 | -1027.81€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7964 | +0.218 | -322.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7964 | +0.218 | -322.89€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8139 | +0.203 | -543.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8139 | +0.203 | -543.67€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8271 | +0.194 | -721.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8271 | +0.194 | -721.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 18570 | +0.118 | +164.29€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 18570 | +0.118 | +164.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9218 | +0.123 | +149.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9218 | +0.123 | +149.11€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9352 | +0.113 | +15.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9352 | +0.113 | +15.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1434 | +0.292 | -6.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1434 | +0.292 | -6.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 640 | +0.279 | -14.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 640 | +0.279 | -14.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 689 | +0.294 | +5.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 689 | +0.294 | +5.70€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 105 | +0.341 | +2.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 105 | +0.341 | +2.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 624 | +0.439 | +1.73€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 624 | +0.439 | +1.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 294 | +0.439 | +0.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 294 | +0.439 | +0.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 289 | +0.442 | +1.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 289 | +0.442 | +1.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 41 | +0.384 | +0.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 41 | +0.384 | +0.01€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1079 | +0.074 | -43.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 375 | +0.062 | -28.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 704 | +0.081 | -14.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 850 | +0.081 | -18.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 146 | +0.081 | -3.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 704 | +0.081 | -14.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 168 | +0.024 | -28.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 168 | +0.024 | -28.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 34233 | +0.097 | -1075.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2834 | +0.090 | +22.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 31399 | +0.098 | -1097.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 19262 | +0.101 | -324.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2834 | +0.090 | +22.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 16428 | +0.103 | -346.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6381 | +0.107 | -35.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6381 | +0.107 | -35.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8590 | +0.080 | -715.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8590 | +0.080 | -715.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 788 | +0.213 | -99.59€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 788 | +0.213 | -99.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 788 | +0.213 | -99.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 788 | +0.213 | -99.59€ | 2 | 4 |
| ✅ GBM_LATE_15M | 24671 | +0.081 | +11625.17€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 24671 | +0.081 | +11625.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4113 | +0.193 | +2978.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4113 | +0.193 | +2978.80€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 3656 | +0.176 | +2523.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3656 | +0.176 | +2523.73€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 4266 | +0.200 | +3204.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4266 | +0.200 | +3204.17€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 3660 | +0.017 | +745.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3660 | +0.017 | +745.59€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3552 | -0.033 | +813.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3552 | -0.033 | +813.87€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 5424 | -0.042 | +1359.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5424 | -0.042 | +1359.01€ | 4 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 26035 | +0.085 | +13584.52€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 26035 | +0.085 | +13584.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4929 | +0.017 | +2628.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4929 | +0.017 | +2628.62€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5426 | +0.014 | +1109.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5426 | +0.014 | +1109.20€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3695 | +0.262 | +3716.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3695 | +0.262 | +3716.37€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4212 | +0.000 | +768.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4212 | +0.000 | +768.59€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4240 | +0.027 | +1596.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4240 | +0.027 | +1596.12€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3533 | +0.275 | +3765.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3533 | +0.275 | +3765.62€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 19895 | +0.168 | +14809.33€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 19895 | +0.168 | +14809.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2993 | +0.206 | +2367.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2993 | +0.206 | +2367.03€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3172 | +0.147 | +2296.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3172 | +0.147 | +2296.25€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3114 | +0.208 | +2481.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3114 | +0.208 | +2481.30€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3340 | +0.132 | +2310.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3340 | +0.132 | +2310.86€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3703 | +0.116 | +2525.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3703 | +0.116 | +2525.03€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3573 | +0.204 | +2828.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3573 | +0.204 | +2828.86€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4907 | +0.125 | +2006.92€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4907 | +0.125 | +2006.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1400 | +0.120 | +616.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1400 | +0.120 | +616.88€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 372 | +0.144 | +178.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 372 | +0.144 | +178.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1425 | +0.140 | +609.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1425 | +0.140 | +609.28€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1022 | +0.099 | +309.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1022 | +0.099 | +309.14€ | 2 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 24776 | +0.174 | +18337.78€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 24776 | +0.174 | +18337.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3922 | +0.220 | +3293.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3922 | +0.220 | +3293.00€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3878 | +0.149 | +2542.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3878 | +0.149 | +2542.15€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4051 | +0.226 | +3496.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4051 | +0.226 | +3496.22€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4023 | +0.135 | +2702.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4023 | +0.135 | +2702.17€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4345 | +0.112 | +2716.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4345 | +0.112 | +2716.73€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4557 | +0.205 | +3587.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4557 | +0.205 | +3587.51€ | 0 | 23 |
| ✅ GBM_LATE_5M | 6702 | +0.144 | +3744.86€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 6702 | +0.144 | +3744.86€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1731 | +0.141 | +1102.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1731 | +0.141 | +1102.14€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2114 | +0.147 | +1156.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2114 | +0.147 | +1156.24€ | 0 | 32 |
| ✅ GBM_LATE_5M#SOL | 555 | +0.101 | +189.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 555 | +0.101 | +189.09€ | 0 | 16 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1640 | +0.069 | +706.66€ | 2 | 14 |
| ✅ GBM_LATE_60M#60min | 1640 | +0.069 | +706.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 590 | +0.089 | +250.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 590 | +0.089 | +250.06€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 545 | +0.070 | +267.32€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 545 | +0.070 | +267.32€ | 2 | 16 |
| ✅ GBM_LATE_60M#SOL | 505 | +0.042 | +189.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 505 | +0.042 | +189.28€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 362 | -0.258 | -27.08€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 362 | -0.258 | -27.08€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 137 | -0.227 | -11.84€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 137 | -0.227 | -11.84€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 121 | -0.256 | -8.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 121 | -0.256 | -8.96€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 104 | -0.292 | -6.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 104 | -0.292 | -6.28€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 674 | +0.064 | +126.20€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 674 | +0.064 | +126.20€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 267 | +0.054 | +44.84€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 267 | +0.054 | +44.84€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 192 | +0.031 | -4.08€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 192 | +0.031 | -4.08€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 215 | +0.104 | +85.44€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 215 | +0.104 | +85.44€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 95 | +0.253 | +75.39€ | 0 | 9 |
| ✅ LATE_WINDOW_5MIN#5min | 95 | +0.253 | +75.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 95 | +0.253 | +75.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 95 | +0.253 | +75.39€ | 0 | 9 |
| ✅ LEADLAG_BTC_XRP_15M | 1858 | +0.097 | +497.98€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1858 | +0.097 | +497.98€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1858 | +0.097 | +497.98€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1858 | +0.097 | +497.98€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 374 | -0.082 | -35.05€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 374 | -0.082 | -35.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 94 | -0.062 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 94 | -0.062 | -5.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 132 | -0.030 | -5.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 132 | -0.030 | -5.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1912 | +0.004 | +11.46€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1912 | +0.004 | +11.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 103 | +0.024 | +0.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 103 | +0.024 | +0.01€ | 0 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 207 | -0.007 | +11.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 207 | -0.007 | +11.30€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 155 | -0.041 | -8.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 155 | -0.041 | -8.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 805 | +0.025 | +21.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 805 | +0.025 | +21.87€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 467 | -0.001 | -5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 467 | -0.001 | -5.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 175 | -0.042 | -8.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 175 | -0.042 | -8.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 1054 | -0.048 | -31.68€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1054 | -0.048 | -31.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 301 | -0.045 | -13.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 301 | -0.045 | -13.58€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 351 | -0.035 | -4.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 351 | -0.035 | -4.55€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 402 | -0.062 | -13.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 402 | -0.062 | -13.56€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 720 | -0.026 | +3.35€ | 3 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 324 | -0.015 | +8.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 396 | -0.035 | -5.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 23 | -0.020 | +1.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 13 | +0.065 | +3.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 10 | -0.083 | -2.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 179 | +0.064 | +39.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 79 | +0.068 | +16.76€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 100 | +0.059 | +22.39€ | 0 | 6 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 119 | -0.062 | -9.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 54 | -0.054 | -3.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 65 | -0.067 | -5.58€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 117 | -0.080 | -12.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 52 | -0.074 | -5.43€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 65 | -0.082 | -7.01€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 112 | -0.018 | -0.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 56 | -0.017 | +2.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 56 | -0.017 | -2.36€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 170 | -0.064 | -14.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 70 | -0.056 | -4.65€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 100 | -0.069 | -10.10€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 14285 | -0.011 | -203.70€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14285 | -0.011 | -203.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3002 | -0.020 | -56.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3002 | -0.020 | -56.89€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 27823 | -0.007 | +1227.65€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 27823 | -0.007 | +1227.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4904 | +0.016 | +596.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4904 | +0.016 | +596.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4331 | -0.028 | -52.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4331 | -0.028 | -52.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4941 | +0.014 | +440.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4941 | +0.014 | +440.43€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4112 | -0.052 | -143.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4112 | -0.052 | -143.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4656 | -0.011 | +181.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4656 | -0.011 | +181.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4879 | +0.007 | +205.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4879 | +0.007 | +205.85€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5720 | -0.056 | -127.83€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5720 | -0.056 | -127.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1369 | -0.077 | -33.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1369 | -0.077 | -33.07€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 605 | -0.116 | -19.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 605 | -0.116 | -19.96€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1653 | -0.075 | -28.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1653 | -0.075 | -28.12€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 70714 | -0.072 | +1710.92€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 70714 | -0.072 | +1710.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 11939 | -0.079 | +691.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 11939 | -0.079 | +691.78€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10929 | -0.092 | -467.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10929 | -0.092 | -467.20€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 12127 | -0.067 | +678.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 12127 | -0.067 | +678.65€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 10455 | -0.093 | -148.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 10455 | -0.093 | -148.46€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 12967 | -0.048 | +369.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 12967 | -0.048 | +369.12€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 12297 | -0.062 | +587.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 12297 | -0.062 | +587.04€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7380 | -0.023 | -111.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7380 | -0.023 | -111.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1647 | -0.025 | +1.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1647 | -0.025 | +1.31€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1966 | -0.020 | -21.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1966 | -0.020 | -21.33€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1030 | -0.040 | -16.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1030 | -0.040 | -16.40€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1100 | +0.107 | +368.34€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 964 | +0.114 | +355.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 226 | +0.132 | +107.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 226 | +0.132 | +107.88€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 187 | +0.093 | +43.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 187 | +0.093 | +43.26€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 195 | +0.094 | +64.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 195 | +0.094 | +64.08€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 168 | +0.141 | +82.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 168 | +0.141 | +82.71€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 188 | +0.105 | +57.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 188 | +0.105 | +57.82€ | 0 | 5 |
| ✅ ORDER_FLOW_5M_REACTIVO | 439 | -0.058 | -49.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 439 | -0.058 | -49.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 95 | -0.015 | +1.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 95 | -0.015 | +1.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 54 | -0.125 | -15.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 127 | -0.081 | -25.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 127 | -0.081 | -25.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 89 | +0.017 | +4.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 89 | +0.017 | +4.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 74 | -0.105 | -14.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 74 | -0.105 | -14.81€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 555 | -0.103 | -40.18€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 256 | -0.155 | -57.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 208 | -0.200 | -60.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 193 | -0.080 | -0.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 149 | -0.089 | -8.28€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 106 | -0.018 | +17.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 84 | -0.035 | +11.21€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 441 | -0.132 | -57.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 693 | -0.208 | -32.85€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 285 | -0.200 | -27.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 248 | -0.196 | -26.82€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 240 | -0.223 | -22.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 208 | -0.233 | -27.06€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 168 | -0.194 | +16.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 152 | -0.195 | +12.09€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 608 | -0.210 | -41.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 284 | +0.409 | +213.96€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 76 | +0.372 | +56.60€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 76 | +0.372 | +56.60€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 179 | +0.478 | +161.59€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 179 | +0.478 | +161.59€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 284 | +0.409 | +213.96€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 489 | +0.036 | +16.17€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 489 | +0.036 | +16.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 227 | +0.042 | +7.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 227 | +0.042 | +7.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 33 | +0.071 | +0.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 33 | +0.071 | +0.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 53 | -0.009 | -2.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 53 | -0.009 | -2.28€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 176 | +0.034 | +10.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 176 | +0.034 | +10.02€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 2719 | -0.023 | -114.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2719 | -0.023 | -114.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 566 | -0.023 | -23.32€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 566 | -0.023 | -23.32€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1194 | -0.023 | -49.60€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1194 | -0.023 | -49.60€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 73 | -0.060 | -7.39€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 73 | -0.060 | -7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7602 | +0.023 | +110.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7602 | +0.023 | +110.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2129 | +0.021 | +20.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2129 | +0.021 | +20.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1694 | +0.035 | +50.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1694 | +0.035 | +50.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2307 | +0.011 | +1.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2307 | +0.011 | +1.20€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1472 | +0.030 | +38.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1472 | +0.030 | +38.00€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7123 | +0.011 | -48.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7123 | +0.011 | -48.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2862 | +0.015 | -11.29€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2862 | +0.015 | -11.29€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2785 | +0.011 | -18.85€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2785 | +0.011 | -18.85€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1476 | +0.003 | -18.52€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1476 | +0.003 | -18.52€ | 2 | 0 |
| ✅ UPDOWN_GBM | 35498 | +0.030 | +2076.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 9586 | +0.065 | +1690.82€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 1317 | +0.004 | +5.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 22302 | +0.020 | +360.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2154 | +0.006 | +19.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3559 | +0.066 | +375.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 605 | +0.146 | +230.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 29 | -0.016 | -0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2925 | +0.051 | +144.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6572 | +0.035 | +435.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1213 | +0.082 | +261.44€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 358 | +0.019 | +7.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3981 | +0.031 | +149.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 967 | +0.004 | +16.48€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 53 | -0.100 | +0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4136 | +0.039 | +242.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 559 | +0.140 | +200.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 27 | -0.017 | -2.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3550 | +0.024 | +44.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7554 | +0.017 | +276.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2480 | +0.045 | +266.13€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 346 | +0.006 | +6.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3949 | +0.005 | +3.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 734 | +0.003 | -4.24€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 45 | -0.138 | +3.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8531 | +0.015 | +214.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2364 | +0.026 | +162.38€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 340 | -0.006 | -3.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5335 | +0.013 | +50.68€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 453 | +0.019 | +7.43€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 39 | -0.159 | -2.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5144 | +0.035 | +533.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2365 | +0.079 | +569.89€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 217 | -0.002 | -3.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2562 | -0.003 | -33.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 137 | -0.133 | +2.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 531 | +0.335 | +151.87€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 531 | +0.335 | +151.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 297 | +0.340 | +82.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 297 | +0.340 | +82.27€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 234 | +0.326 | +69.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 234 | +0.326 | +69.60€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 11502 | -0.042 | +2350.76€ | 2 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 11502 | -0.042 | +2350.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 709 | -0.042 | +332.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 709 | -0.042 | +332.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2143 | -0.124 | +15.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2143 | -0.124 | +15.84€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 345 | +0.177 | +226.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 345 | +0.177 | +226.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1269 | +0.201 | +728.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1269 | +0.201 | +728.14€ | 2 | 24 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3511 | -0.064 | +536.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3511 | -0.064 | +536.11€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3525 | -0.079 | +511.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3525 | -0.079 | +511.65€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 137 | +0.040 | +8.30€ | 2 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 137 | +0.040 | +8.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 137 | +0.040 | +8.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 137 | +0.040 | +8.30€ | 2 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 854 | +0.289 | +684.51€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 854 | +0.289 | +684.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 474 | +0.281 | +353.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 474 | +0.281 | +353.77€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 380 | +0.296 | +330.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 380 | +0.296 | +330.74€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 709 | -0.108 | -80.32€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 709 | -0.108 | -80.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 199 | -0.067 | -12.28€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 199 | -0.067 | -12.28€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 69 | -0.162 | -8.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 69 | -0.162 | -8.81€ | 3 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 63 | -0.208 | -9.68€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 63 | -0.208 | -9.68€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2332 | +0.299 | +1160.88€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 803 | +0.248 | +108.30€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 869 | +0.288 | +362.56€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 660 | +0.376 | +690.02€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.017 n=464 — no justifica filtro, seguir monitorizando
  - _Datos_: n=464 IC=+0.017 PNL=+21.72€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 519 celda(s) pasan gate riguroso completo de 2200 evaluadas (n>=40) y 3195 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.026 < 0.08 — monitorear
  - _Datos_: n=2362 IC=+0.026 PNL=+162.38€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=869/15 IC=+0.288 PNL=+362.56€ | BTC: n=803/15 IC=+0.248 PNL=+108.30€ | SOL: n=660/15 IC=+0.376 PNL=+690.02€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 30 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: alineada_con_outcome_prev IC=+0.094 n=284/60 | contraria IC=+0.149 n=277 | gap=-0.054 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=276, boost estimado=+0.004. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=733/40 IC=+0.003 PNL=-3.73€ | BTC#60min: n=965/40 IC=+0.004 PNL=+16.10€ | SOL#60min: n=452/40 IC=+0.020 PNL=+7.94€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.051 n=323785 | tras_1loss IC=+0.077 n=252244 | tras_2loss IC=+0.046 n=106666/40 | gap=+0.005 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.174 > 0.08 con n=311 PNL=+193.62€
  - _Datos_: n=311 IC=+0.174 PNL=+193.62€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.219 > 0.08 con n=368 PNL=+267.11€
  - _Datos_: n=368 IC=+0.219 PNL=+267.11€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.275 > 0.08 con n=38 PNL=+33.67€
  - _Datos_: n=38 IC=+0.275 PNL=+33.67€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.327 > 0.1 con n=1919 PNL=+1069.33€
  - _Datos_: n=1919 IC=+0.327 PNL=+1069.33€

**🟡 H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=265 PNL=+34.78€
  - _Datos_: n=265 IC=+0.084 PNL=+34.78€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=50 IC=+0.192 PNL=+34.21€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=50 IC=+0.192 PNL=+34.21€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=1532 IC=+0.012 PNL=+8.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1532 IC=+0.012 PNL=+8.51€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=618 IC=-0.006 PNL=+11.80€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=618 IC=-0.006 PNL=+11.80€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=464 IC=+0.017 PNL=+21.72€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=464 IC=+0.017 PNL=+21.72€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.185 > 0.1 con n=2037 PNL=+1263.28€
  - _Datos_: n=2037 IC=+0.185 PNL=+1263.28€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1213 IC=+0.082 PNL=+261.44€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1213 IC=+0.082 PNL=+261.44€

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
  - _Estado_: n=513 IC=+0.003 PNL=+28.80€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=513 IC=+0.003 PNL=+28.80€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=49 IC=+0.049 PNL=+2.29€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=49 IC=+0.049 PNL=+2.29€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.253 n=95) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=95 IC=+0.253 PNL=+75.39€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.02 con n=630 PNL=+245.08€
  - _Datos_: n=630 IC=+0.123 PNL=+245.08€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=147 IC=-0.044 PNL=+35.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=147 IC=-0.044 PNL=+35.89€

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
  - _Estado_: n=12264 IC=+0.054 PNL=+1491.02€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=12264 IC=+0.054 PNL=+1491.02€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.158 < -0.1 con n=223 PNL=+19.25€
  - _Datos_: n=223 IC=-0.158 PNL=+19.25€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1819 IC=+0.046 PNL=+188.63€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1819 IC=+0.046 PNL=+188.63€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=74 IC=-0.105 PNL=+5.08€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=74 IC=-0.105 PNL=+5.08€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.1 con n=384 PNL=+105.48€
  - _Datos_: n=384 IC=+0.127 PNL=+105.48€

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
  - _Estado_: n=17239 IC=-0.137 PNL=+1182.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=17239 IC=-0.137 PNL=+1182.99€

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
  - _Estado_: n=1867 IC=+0.138 PNL=+1001.70€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1867 IC=+0.138 PNL=+1001.70€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=3730 IC=+0.021 PNL=+125.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3730 IC=+0.021 PNL=+125.99€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=2001 PNL=+1052.79€
  - _Datos_: n=2001 IC=+0.087 PNL=+1052.79€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.239 < -0.1 con n=1687 PNL=-185.47€
  - _Datos_: n=1687 IC=-0.239 PNL=-185.47€

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

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 35/40 ops en el filtro definido (IC actual=-0.041 PNL=+2.93€)
  - _Datos_: n=35 IC=-0.041 PNL=+2.93€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.087 n=952) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=952 IC=+0.087 PNL=+211.43€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=438) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=438 IC=+0.411 PNL=+617.55€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=8537 IC=+0.175 PNL=-1008.30€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8537 IC=+0.175 PNL=-1008.30€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.1 con n=132 PNL=+75.67€
  - _Datos_: n=132 IC=+0.194 PNL=+75.67€
