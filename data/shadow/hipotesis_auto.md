# Hipótesis automáticas — 2026-09-24 10:54 UTC
_Generado por shadow_postmortem.py sobre 587906 resoluciones (PNL=+65820.39€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=473)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.237 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.8028` → IC=+0.256 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8028 (IC base=+0.140)

- **PATRÓN** `banda_z` > `4.109` → IC=+0.165 (n=545)

  - _Acción_: Kelly boost +0.83€ cuando `banda_z` > 4.109 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=584)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3000.2192` → IC=+0.152 (n=363)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3000.2192 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.121 (n=473)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.136 (n=171)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 96.0 (IC base=+0.047)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.260 (n=418)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=345)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.260 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.149)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.149)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.265 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.149)

- **PATRÓN** `banda_z` > `4.305` → IC=+0.175 (n=435)

  - _Acción_: Kelly boost +0.88€ cuando `banda_z` > 4.305 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=495)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `4494.3377` → IC=+0.150 (n=198)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4494.3377 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.151 (n=130)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 96.0 (IC base=+0.049)

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
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=88)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=87)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=98)

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
- **FILTRO** `restante_s_al_confirmar` < `145.96` → IC=-0.234 (n=7007)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.96
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=21033)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.17` → IC=-0.248 (n=920)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.17
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=2763)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `497.2` → IC=-0.147 (n=361)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 497.2
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1083)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `127.05` → IC=-0.304 (n=865)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.05
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2595)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.85` → IC=-0.227 (n=1676)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.85
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=5031)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `125.68` → IC=-0.357 (n=1382)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.68
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=4149)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.230 (n=353)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=408)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.197 (n=176)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=534)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=560)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.203 (n=13725)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=3454)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `5620.2261` → IC=+0.176 (n=2200)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5620.2261 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=11252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=13787)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=10773)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=5619)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7792.686` → IC=+0.174 (n=2118)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7792.686 (IC base=+0.128)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=1670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.350 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2099)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15944.5355` → IC=+0.235 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15944.5355 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.205 (n=1503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.206 (n=1671)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.264 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `15863.0179` → IC=+0.215 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15863.0179 (IC base=+0.201)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.168 (n=323)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.615 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.146 (n=235)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4624.034 (IC base=+0.103)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.140 (n=517)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 11.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=816)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=556)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `5859.5725` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5859.5725 (IC base=+0.107)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.154 (n=2784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=2379)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.336 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.357 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.237 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `3729.7102` → IC=+0.233 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3729.7102 (IC base=+0.233)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.156 (n=452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.140 (n=653)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.238 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=532)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1302.4168` → IC=+0.150 (n=649)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1302.4168 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.433 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.167 (n=1073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 7.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.316 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=721)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.162)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.171 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.346 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=188)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `1261.7454` → IC=+0.152 (n=225)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1261.7454 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.195 (n=382)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.355 (IC base=+0.113)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=11328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=10874)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.225 (n=3769)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=2751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.173 (n=2619)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.181 (n=1923)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.71 (IC base=+0.167)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.257 (n=389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.243 (n=820)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.244)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.350 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.244)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=2707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=2590)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=2229)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.319 (n=850)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.196 (n=1939)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.429 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `2073.3909` → IC=+0.438 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2073.3909 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.434 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.436 (n=202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.449 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.435 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `3366.033` → IC=+0.447 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3366.033 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.406 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.405)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.406 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.405)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.405)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.408 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.405)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.199 (n=33612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.235 (n=15106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=6849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=4696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=6284)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=6033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=6037)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=2149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=3231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=6122)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.171)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3023)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.219 (n=2311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=2088)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=5565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.255 (n=2250)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=2420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=5629)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2150)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=5141)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.15` → IC=+0.128 (n=4747)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.15 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=5122)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=6306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.85` → IC=+0.142 (n=4731)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.85 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.198 (n=2591)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.123)

- **PATRÓN** `restante_min` < `4.1` → IC=+0.134 (n=2350)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.1 (IC base=+0.123)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2539)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.94 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=3112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.123)

- **PATRÓN** `lag_apertura_s` < `3.41` → IC=+0.144 (n=2349)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.41 (IC base=+0.123)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=2550)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.128 (n=2388)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.19 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=2589)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.3` → IC=+0.139 (n=2390)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.3 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.324 (n=770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `4093.3151` → IC=+0.314 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4093.3151 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.305 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.343 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `4254.7258` → IC=+0.304 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4254.7258 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.335 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.385 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `1462.5909` → IC=+0.311 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1462.5909 (IC base=+0.295)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.444 (n=426)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.450 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.455 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `1988.111` → IC=+0.461 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1988.111 (IC base=+0.443)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.256)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.384 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.287 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.256)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.256)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.384 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.287 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.256)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4836` → IC=+0.121 (n=7951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.4836 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.244 (n=2650)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.8442` → IC=+0.248 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8442 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.634` → IC=+0.248 (n=2234)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.634 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.968` → IC=+0.176 (n=3050)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.968 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.2119` → IC=+0.246 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2119 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `1.0496` → IC=+0.256 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0496 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.3045` → IC=+0.217 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3045 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.9075` → IC=+0.204 (n=3622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9075 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.5687` → IC=+0.134 (n=9603)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5687 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.6138` → IC=+0.193 (n=701)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6138 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.1523` → IC=+0.174 (n=3048)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1523 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` < `0.6995` → IC=+0.181 (n=1478)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6995 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.0553` → IC=+0.176 (n=1522)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.0553 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.1675` → IC=+0.222 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1675 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.5706` → IC=+0.201 (n=5041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5706 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.211 (n=5427)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=+0.066)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.179 (n=602)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.005 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.173 (n=601)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0082 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.165 (n=1800)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=866)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.167 (n=1215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 11.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.138` → IC=+0.268 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.138 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.209 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.162 (n=1681)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.250 (n=1211)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0915` → IC=+0.282 (n=452)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0915 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=1223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0517` → IC=+0.293 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0517 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.424` → IC=+0.247 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.424 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.231 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.258 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `1.8381` → IC=+0.237 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8381 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1801.22` → IC=+0.236 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1801.22 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.228 (n=913)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0838` → IC=+0.253 (n=456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0838 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=1430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.9902` → IC=+0.269 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9902 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.2006` → IC=+0.220 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2006 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.5869` → IC=+0.218 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5869 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.83` → IC=+0.254 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.83 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.2554` → IC=+0.218 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2554 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.8746` → IC=+0.224 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8746 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.238 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.7478` → IC=+0.217 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7478 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.368` → IC=+0.226 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.368 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `12395.6781` → IC=+0.218 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12395.6781 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.153 (n=1429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0056 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.163 (n=476)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=644)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.3234` → IC=+0.196 (n=952)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.3234 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.158 (n=1277)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1327 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.254` → IC=+0.168 (n=227)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.254 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.274` → IC=+0.141 (n=1302)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.274 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2049` → IC=+0.151 (n=1428)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2049 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.096` → IC=+0.174 (n=514)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.096 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4238` → IC=+0.154 (n=1318)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4238 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4188` → IC=+0.147 (n=1317)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4188 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `14064.3418` → IC=+0.146 (n=952)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 14064.3418 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.148 (n=1237)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 411.0 (IC base=+0.140)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.210 (n=587)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=1848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1580)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.224` → IC=+0.251 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.224 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.2115` → IC=+0.188 (n=1757)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2115 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.3605` → IC=+0.197 (n=232)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.3605 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.8411` → IC=+0.203 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8411 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=1271)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.219 (n=1518)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.5953` → IC=+0.214 (n=1516)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5953 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.215 (n=714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.249 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.615` → IC=+0.244 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.615 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3556` → IC=+0.265 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3556 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7743` → IC=+0.207 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7743 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.2108` → IC=+0.220 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2108 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.218 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1882.9554` → IC=+0.226 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.9554 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.215 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.212)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.153 (n=99)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2198)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.217 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.1556` → IC=+0.319 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1556 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.7929` → IC=+0.330 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7929 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.724` → IC=+0.156 (n=702)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 4.724 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.324 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.2014` → IC=+0.335 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2014 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1818` → IC=+0.315 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1818 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.343 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4057` → IC=+0.340 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4057 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.332 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.330 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.68` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.68 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.163 (n=550)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8504 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.2258` → IC=+0.222 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2258 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.5138` → IC=+0.176 (n=689)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5138 (IC base=+0.017)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.172 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=318)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.208 (n=94)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=283)

- **FILTRO** `ibs_20min` > `0.2553` → IC=-0.124 (n=2163)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2553
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=1066)

- **FILTRO** `sigma_ewma_delta_pct` > `8.654` → IC=-0.211 (n=347)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.654
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2882)

- **PATRÓN** `ibs_20min` > `0.7846` → IC=+0.218 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7846 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` < `0.5947` → IC=+0.271 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5947 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.6541` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6541 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7836` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7836 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.312 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.2264` → IC=+0.290 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2264 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.293 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.2553` → IC=+0.128 (n=1066)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.2553 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.6893` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6893 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `1.0952` → IC=+0.227 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0952 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` > `0.9027` → IC=+0.220 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9027 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.1022` → IC=+0.233 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1022 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1501` → IC=+0.253 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1501 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.267 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6599` → IC=-0.181 (n=559)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6599
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1679)

- **FILTRO** `ibs_20min` < `0.71` → IC=-0.157 (n=1475)

  - _Acción_: SKIP cuando `ibs_20min` < 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=763)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.199 (n=407)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1831)

- **FILTRO** `ibs_20min` > `0.77` → IC=-0.200 (n=818)

  - _Acción_: SKIP cuando `ibs_20min` > 0.77
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=2475)

- **PATRÓN** `dist_vwap_pct` > `0.7824` → IC=+0.324 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7824 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2662` → IC=+0.319 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2662 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` < `0.9865` → IC=+0.291 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9865 (IC base=-0.067)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.305 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.295 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.294 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.3932` → IC=+0.309 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3932 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.7985` → IC=+0.297 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7985 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.8778` → IC=+0.265 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8778 (IC base=-0.023)

- **PATRÓN** `volumen_regimen` < `0.7389` → IC=+0.252 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7389 (IC base=-0.023)

- **PATRÓN** `volumen_regimen` > `1.0909` → IC=+0.278 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0909 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.272 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.1643` → IC=+0.255 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1643 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.434` → IC=+0.244 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.434 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.195 (n=3323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0097 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4749` → IC=+0.187 (n=8897)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4749 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.7667` → IC=+0.289 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7667 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.593` → IC=+0.155 (n=4703)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.593 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.245 (n=3158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.263 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4663` → IC=+0.240 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4663 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6694` → IC=+0.237 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6694 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.266 (n=5250)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 97.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.154 (n=3322)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0091 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5462` → IC=+0.154 (n=8764)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5462 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2474` → IC=+0.239 (n=2784)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2474 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7101` → IC=+0.239 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7101 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.205` → IC=+0.247 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.205 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.302 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.6044` → IC=+0.257 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6044 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.3196` → IC=+0.255 (n=1749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3196 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `84.0` → IC=+0.262 (n=3743)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 84.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.536` → IC=-0.155 (n=526)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.536
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1766)

- **PATRÓN** `ibs_20min` > `0.8933` → IC=+0.266 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8933 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.783` → IC=+0.206 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.783 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.266 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.4344` → IC=+0.177 (n=289)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4344 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.1445` → IC=+0.191 (n=393)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.1445 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.173 (n=374)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 14.0 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` < `0.1673` → IC=+0.442 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1673 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` < `2.7434` → IC=+0.432 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7434 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.3568` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3568 (IC base=-0.016)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.859` → IC=+0.157 (n=666)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.859 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.171 (n=506)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6736` → IC=+0.163 (n=817)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6736 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.218 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.197 (n=298)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `245.0` → IC=+0.190 (n=388)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 245.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1603` → IC=+0.220 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1603 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `0.613` → IC=+0.214 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.613 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2715` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2715 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.4389` → IC=+0.221 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4389 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.238 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `473.0` → IC=+0.214 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 473.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.286 (n=526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=1654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.247 (n=1404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.742` → IC=+0.279 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.742 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.1373` → IC=+0.256 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1373 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `3.4315` → IC=+0.259 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4315 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.253 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1956.62` → IC=+0.253 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1956.62 (IC base=+0.244)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.315 (n=572)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.6052` → IC=+0.284 (n=1260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6052 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.329 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.289 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2222 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.812` → IC=+0.298 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.812 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.306 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `1.597` → IC=+0.287 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.597 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `2.7489` → IC=+0.284 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7489 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `1875.32` → IC=+0.298 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1875.32 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.286 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.281)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2842` → IC=-0.186 (n=486)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2842
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=1460)

- **FILTRO** `ibs_20min` > `0.7744` → IC=-0.182 (n=590)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7744
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1772)

- **PATRÓN** `ibs_20min` > `0.9105` → IC=+0.179 (n=487)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9105 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.4516` → IC=+0.222 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4516 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `0.9869` → IC=+0.232 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9869 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.5875` → IC=+0.208 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5875 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.0807` → IC=+0.253 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0807 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.5078` → IC=+0.259 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5078 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.238 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.1552` → IC=+0.207 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1552 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` < `0.6853` → IC=+0.201 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6853 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1615` → IC=+0.209 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1615 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.1645` → IC=+0.276 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1645 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.8269` → IC=+0.260 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8269 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1518` → IC=+0.240 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1518 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.249 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7188` → IC=-0.202 (n=1056)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7188
  - _Potencial_: sin este filtro IC_bueno=+0.280 (n=1058)

- **FILTRO** `ibs_20min` > `0.6857` → IC=-0.227 (n=551)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6857
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1655)

- **FILTRO** `sigma_ewma_delta_pct` > `4.689` → IC=-0.178 (n=482)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.689
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=1724)

- **PATRÓN** `ibs_20min` > `0.7188` → IC=+0.280 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7188 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.8477` → IC=+0.335 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8477 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.606` → IC=+0.162 (n=335)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.606 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.87` → IC=+0.301 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.87 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `0.7299` → IC=+0.291 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7299 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.1016` → IC=+0.291 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1016 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2243` → IC=+0.299 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2243 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.326 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4267 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.311 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.121 (n=1457)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.5789 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.2135` → IC=+0.220 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2135 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.250 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7031 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.209 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.205 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.481` → IC=+0.220 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.481 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.237 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.015)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.317 (n=861)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.293 (n=611)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` > `0.6316` → IC=+0.311 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6316 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2035` → IC=+0.317 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2035 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.566` → IC=+0.299 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.566 (IC base=+0.277)

- **PATRÓN** `volumen_regimen` > `0.8621` → IC=+0.302 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8621 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.321 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.292 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.282 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `2626.1883` → IC=+0.291 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2626.1883 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.296 (n=935)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.280 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.273 (n=698)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.3939` → IC=+0.304 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3939 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.3011` → IC=+0.278 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3011 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.9709` → IC=+0.271 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9709 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.011` → IC=+0.293 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.011 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.273 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `1.2435` → IC=+0.306 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2435 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.338 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `1.823` → IC=+0.268 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.823 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.1531` → IC=+0.274 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1531 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2620.4458` → IC=+0.273 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2620.4458 (IC base=+0.270)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.170 (n=2595)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.199 (n=2589)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0112 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.0899` → IC=+0.186 (n=2587)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0899 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=8065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.5775` → IC=+0.216 (n=7759)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5775 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.1754` → IC=+0.195 (n=3386)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1754 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.352` → IC=+0.253 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.352 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `1.2128` → IC=+0.159 (n=5134)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2128 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.159 (n=5133)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6297 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.1058` → IC=+0.187 (n=3050)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1058 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.5597` → IC=+0.169 (n=3273)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5597 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.621` → IC=+0.174 (n=2480)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.621 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2400.6014` → IC=+0.167 (n=5173)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2400.6014 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.179 (n=6676)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 116.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.183 (n=4980)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0811` → IC=+0.208 (n=2486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0811 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=2855)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.227 (n=7459)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.2323` → IC=+0.160 (n=5429)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2323 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.345` → IC=+0.197 (n=1264)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.345 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.152 (n=5404)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1756 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.222 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5616` → IC=+0.168 (n=2982)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5616 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.2548` → IC=+0.171 (n=3072)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2548 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.173 (n=6418)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 116.0 (IC base=+0.168)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.216 (n=442)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.184 (n=600)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0076 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.3429` → IC=+0.205 (n=1324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3429 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=889)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.15` → IC=+0.310 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.15 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.233 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.178 (n=1223)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.239 (n=855)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.251 (n=865)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1882` → IC=+0.292 (n=646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1882 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.264 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.25` → IC=+0.251 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.25 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.234 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.254 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4215` → IC=+0.263 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4215 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1804.6172` → IC=+0.245 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1804.6172 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.233 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0742` → IC=+0.200 (n=385)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0742 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=1216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.4061` → IC=+0.226 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4061 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.211` → IC=+0.213 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.211 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.506` → IC=+0.236 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.506 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.163 (n=1155)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2653 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.0767` → IC=+0.167 (n=524)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0767 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2316` → IC=+0.199 (n=257)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2316 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.5005` → IC=+0.183 (n=493)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5005 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `15928.6386` → IC=+0.162 (n=524)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 15928.6386 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.159 (n=1270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.2922` → IC=+0.160 (n=1267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.2922 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5636` → IC=+0.186 (n=1267)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.5636 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1339` → IC=+0.162 (n=1257)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1339 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.882` → IC=+0.205 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.882 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.157 (n=1267)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2145 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.154 (n=388)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4292` → IC=+0.147 (n=1156)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4292 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4221` → IC=+0.136 (n=1155)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4221 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.170 (n=359)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 215.0 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.214 (n=435)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.2279` → IC=+0.214 (n=869)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2279 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.868` → IC=+0.276 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.868 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.1322` → IC=+0.196 (n=508)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1322 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `1.6387` → IC=+0.199 (n=413)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.6387 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.8468` → IC=+0.209 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8468 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.206 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `1956.8086` → IC=+0.200 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1956.8086 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.229 (n=1087)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.248 (n=363)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.276 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.2407` → IC=+0.256 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2407 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.735` → IC=+0.267 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.735 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3558` → IC=+0.264 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3558 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7913` → IC=+0.212 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7913 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `3.4055` → IC=+0.233 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4055 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1886.9572` → IC=+0.221 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1886.9572 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.214 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.218)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.206 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.158 (n=1242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=1300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.195 (n=1242)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.375 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1604` → IC=+0.180 (n=825)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1604 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.995` → IC=+0.228 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.995 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.0418` → IC=+0.142 (n=1093)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0418 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.6274` → IC=+0.147 (n=1242)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6274 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2464` → IC=+0.193 (n=262)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2464 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.4237` → IC=+0.149 (n=406)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4237 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.529` → IC=+0.167 (n=406)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.529 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `6237.095` → IC=+0.181 (n=828)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 6237.095 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.144 (n=1179)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 164.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=1317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3848` → IC=+0.144 (n=1317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3848 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.4585` → IC=+0.188 (n=1159)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.4585 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.5823` → IC=+0.133 (n=1531)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.5823 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.963` → IC=+0.170 (n=462)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 6.963 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.849` → IC=+0.147 (n=878)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.849 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.291` → IC=+0.200 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.291 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.7906` → IC=+0.134 (n=798)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7906 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.489` → IC=+0.133 (n=399)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.489 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `10015.5876` → IC=+0.158 (n=597)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 10015.5876 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.154 (n=637)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0101 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=1428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5169` → IC=+0.202 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5169 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0956` → IC=+0.223 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0956 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.731` → IC=+0.249 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.731 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.2208` → IC=+0.129 (n=1400)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2208 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1637` → IC=+0.128 (n=1405)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1637 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.5459` → IC=+0.141 (n=595)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5459 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1465)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2891.3724` → IC=+0.197 (n=635)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2891.3724 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.135 (n=1076)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 50.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.152 (n=631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0061 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.155 (n=477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=1446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.5625` → IC=+0.211 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5625 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.0029` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 1.0029 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.2001` → IC=+0.141 (n=1322)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2001 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.006` → IC=+0.144 (n=231)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 9.006 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.174` → IC=+0.122 (n=1429)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.174 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.167 (n=175)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4527` → IC=+0.132 (n=427)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4527 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.4248` → IC=+0.134 (n=427)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4248 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `1464.4397` → IC=+0.136 (n=1277)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1464.4397 (IC base=+0.115)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0188` → IC=+0.214 (n=892)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0188 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=1386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.205 (n=615)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.260 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7391 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.5039` → IC=+0.222 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5039 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.576` → IC=+0.240 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.576 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.204 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2075 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.8587` → IC=+0.220 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8587 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2322` → IC=+0.270 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2322 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.1508` → IC=+0.212 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1508 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.7991` → IC=+0.209 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7991 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.204 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2615.829` → IC=+0.208 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.829 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.227 (n=614)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0114 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0172` → IC=+0.204 (n=928)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0172 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.221 (n=464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.221 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.438` → IC=+0.246 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.438 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.2401` → IC=+0.226 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2401 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.9121` → IC=+0.203 (n=1628)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9121 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.437` → IC=+0.243 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.437 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6295` → IC=+0.215 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6295 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.291 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.2138` → IC=+0.193 (n=1100)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2138 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.198 (n=1250)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2591.5202` → IC=+0.205 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2591.5202 (IC base=+0.203)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.159 (n=617)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0039 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.179 (n=614)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0088 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0996` → IC=+0.151 (n=614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0996 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.388` → IC=+0.178 (n=1842)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.388 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.8737` → IC=+0.191 (n=286)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.8737 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.726` → IC=+0.175 (n=847)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.726 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.8749` → IC=+0.161 (n=1077)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8749 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.2081` → IC=+0.151 (n=539)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.2081 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.176 (n=513)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4385` → IC=+0.167 (n=592)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4385 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5431` → IC=+0.154 (n=591)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.5431 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=2088)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `12367.2302` → IC=+0.153 (n=614)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 12367.2302 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.164 (n=1619)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 162.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.137 (n=1300)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0057 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=1961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.3143` → IC=+0.166 (n=1296)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.3143 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.2104` → IC=+0.121 (n=1730)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2104 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `2.2258` → IC=+0.125 (n=1645)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.2258 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3894.1106` → IC=+0.128 (n=1295)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3894.1106 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3382` → IC=+0.121 (n=462)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.3382 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.150 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 8.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.2515` → IC=+0.142 (n=462)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.2515 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.3081` → IC=+0.165 (n=159)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3081 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6136` → IC=+0.154 (n=154)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6136 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `12851.8973` → IC=+0.129 (n=413)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 12851.8973 (IC base=+0.103)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.211 (n=206)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3378` → IC=+0.153 (n=617)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3378 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5957` → IC=+0.181 (n=543)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.5957 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.3066` → IC=+0.157 (n=656)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.3066 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.388` → IC=+0.160 (n=239)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.388 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2138` → IC=+0.140 (n=617)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2138 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0609` → IC=+0.167 (n=280)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0609 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.198 (n=167)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1013` → IC=+0.157 (n=534)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1013 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4187` → IC=+0.147 (n=607)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4187 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `386.0` → IC=+0.149 (n=585)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 386.0 (IC base=+0.136)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.256 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.191 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.007 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.0958` → IC=+0.205 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0958 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.7004` → IC=+0.241 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7004 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.9443` → IC=+0.226 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9443 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.948` → IC=+0.220 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.948 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.8392` → IC=+0.195 (n=381)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8392 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `1.1573` → IC=+0.205 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1573 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2651` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2651 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.3975` → IC=+0.237 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3975 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.405` → IC=+0.221 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.405 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=634)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `12377.2518` → IC=+0.205 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12377.2518 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.121 (n=476)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1536` → IC=+0.154 (n=238)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1536 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.128 (n=127)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.091)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.5152` → IC=-0.157 (n=129)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5152
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=390)

- **FILTRO** `dist_vwap_pct` > `0.5944` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5944
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=503)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.177 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0089 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.5281` → IC=+0.130 (n=406)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.5281 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.182 (n=294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 11.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.7317` → IC=+0.201 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7317 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.6296` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6296 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.1` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.1 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.0699` → IC=+0.144 (n=358)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.0699 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.2151` → IC=+0.169 (n=176)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.2151 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=442)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3065.6596` → IC=+0.181 (n=136)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3065.6596 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.5152` → IC=+0.150 (n=390)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5152 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7097` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.7097 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.847` → IC=+0.149 (n=243)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.847 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `2931.8404` → IC=+0.131 (n=177)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2931.8404 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.125 (n=222)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 24.0 (IC base=+0.074)

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
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.206 (n=3309)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=10330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.215 (n=9926)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.9723` → IC=+0.206 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9723 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.626` → IC=+0.225 (n=4805)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.626 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8815` → IC=+0.164 (n=4421)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8815 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.198 (n=1854)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.601` → IC=+0.185 (n=3178)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.601 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2342.7057` → IC=+0.171 (n=6614)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2342.7057 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.193 (n=7541)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 87.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6016)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1482` → IC=+0.189 (n=3972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1482 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=3403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.238 (n=9026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5652 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2477` → IC=+0.163 (n=5607)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2477 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.031` → IC=+0.204 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.031 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.732` → IC=+0.182 (n=8736)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.732 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.161 (n=2730)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7051 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.242 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6325` → IC=+0.193 (n=2758)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6325 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.193 (n=5316)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 48.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.209 (n=562)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.223 (n=562)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3544` → IC=+0.190 (n=1686)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3544 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=807)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=1147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.539` → IC=+0.343 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.539 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.255 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.55` → IC=+0.182 (n=700)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.55 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.2431` → IC=+0.196 (n=721)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2431 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=1018)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.259 (n=1320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.263 (n=1181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1294` → IC=+0.286 (n=581)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1294 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=1209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3451` → IC=+0.289 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3451 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.466` → IC=+0.263 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.466 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.283 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.5466` → IC=+0.255 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5466 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `1.8654` → IC=+0.271 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8654 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1800.5095` → IC=+0.264 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1800.5095 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.192 (n=533)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0845` → IC=+0.160 (n=530)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0845 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3107` → IC=+0.203 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3107 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.3442` → IC=+0.196 (n=640)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3442 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.168 (n=365)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.242` → IC=+0.153 (n=1426)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.242 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6305` → IC=+0.179 (n=530)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6305 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2676` → IC=+0.203 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2676 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1149` → IC=+0.161 (n=1350)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1149 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7577` → IC=+0.155 (n=1023)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7577 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `15727.0012` → IC=+0.157 (n=721)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 15727.0012 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `477.0` → IC=+0.158 (n=1466)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 477.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=1377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0057 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.166 (n=1212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.2685` → IC=+0.237 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2685 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1334` → IC=+0.168 (n=1245)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1334 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.493` → IC=+0.165 (n=231)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.493 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.164 (n=1377)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1954 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1514` → IC=+0.198 (n=372)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1514 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4046` → IC=+0.161 (n=1279)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4046 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.7532` → IC=+0.162 (n=852)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7532 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `422.0` → IC=+0.159 (n=1039)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 422.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.243 (n=535)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=1678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=1633)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.6697` → IC=+0.256 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6697 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.809` → IC=+0.294 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.809 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` < `0.2118` → IC=+0.221 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2118 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.8416` → IC=+0.240 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8416 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.227 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.239 (n=1503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1662` → IC=+0.238 (n=661)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1662 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.236 (n=714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.36` → IC=+0.270 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.36 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.758` → IC=+0.279 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.758 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.302 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7551` → IC=+0.234 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7551 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1905` → IC=+0.237 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1905 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1882.4784` → IC=+0.247 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.4784 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.230 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.180 (n=567)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0035 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4373` → IC=+0.144 (n=1690)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4373 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=1763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.877` → IC=+0.260 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.877 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.5779` → IC=+0.168 (n=471)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.5779 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.205` → IC=+0.160 (n=706)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.205 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8764` → IC=+0.154 (n=1127)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8764 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2374` → IC=+0.213 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2374 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.5214` → IC=+0.148 (n=720)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5214 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7649` → IC=+0.147 (n=1090)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7649 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8031.121` → IC=+0.232 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8031.121 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.146 (n=523)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 79.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.156 (n=1386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4484` → IC=+0.155 (n=1385)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4484 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7022` → IC=+0.183 (n=1385)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7022 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.6016` → IC=+0.144 (n=1535)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.6016 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.14` → IC=+0.178 (n=203)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.14 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6969` → IC=+0.149 (n=610)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6969 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.1921` → IC=+0.144 (n=462)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1921 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.248 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.152 (n=1313)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `10917.9028` → IC=+0.211 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10917.9028 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.146 (n=1312)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 179.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.132 (n=1120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0081 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=1718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.188 (n=1679)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4706 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `1.0792` → IC=+0.202 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0792 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.451` → IC=+0.230 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.451 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.8929` → IC=+0.133 (n=1118)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8929 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=1688)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2898.8632` → IC=+0.247 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2898.8632 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.129 (n=1290)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 54.0 (IC base=+0.110)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.174 (n=548)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0057 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1326` → IC=+0.158 (n=548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1326 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=1695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.204 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.132 (n=1344)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2197 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.469` → IC=+0.124 (n=1587)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.469 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.72` → IC=+0.153 (n=724)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.72 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2238` → IC=+0.168 (n=254)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2238 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4462` → IC=+0.141 (n=494)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4462 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.5014` → IC=+0.129 (n=494)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5014 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2831.1065` → IC=+0.165 (n=547)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2831.1065 (IC base=+0.113)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0193` → IC=+0.218 (n=1119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0193 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.209 (n=1501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.5143` → IC=+0.249 (n=1679)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5143 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.5017` → IC=+0.240 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5017 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.275` → IC=+0.267 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.275 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.0709` → IC=+0.210 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0709 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.6382` → IC=+0.215 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6382 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.248 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.5092` → IC=+0.236 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5092 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.216 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2622.2916` → IC=+0.221 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2622.2916 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.226 (n=601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0089 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.220 (n=601)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.207 (n=1263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5172` → IC=+0.255 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5172 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `1.2407` → IC=+0.202 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2407 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.9187` → IC=+0.203 (n=2009)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9187 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.834` → IC=+0.258 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.834 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2355` → IC=+0.233 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2355 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.265 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2014` → IC=+0.195 (n=1423)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2014 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4305` → IC=+0.196 (n=1617)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4305 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=3005)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.156 (n=2512)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0092 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.150 (n=2550)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0056 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.5223` → IC=+0.159 (n=2853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5223 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=1135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.164 (n=1285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 6.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.210 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.186` → IC=+0.156 (n=1039)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.186 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.4908` → IC=+0.142 (n=1732)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.4908 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.174` → IC=+0.177 (n=468)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.174 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.9005` → IC=+0.159 (n=1229)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.9005 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1723` → IC=+0.183 (n=781)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1723 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4563` → IC=+0.158 (n=940)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4563 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.8832` → IC=+0.161 (n=1879)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8832 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3744.121` → IC=+0.150 (n=1902)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3744.121 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.196 (n=760)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.155 (n=2266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.163 (n=770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.0851` → IC=+0.173 (n=756)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.0851 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6922` → IC=+0.150 (n=429)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6922 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.431` → IC=+0.131 (n=2250)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.431 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.27` → IC=+0.147 (n=2257)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.27 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2467` → IC=+0.143 (n=2164)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2467 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.139 (n=2049)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.073` → IC=+0.144 (n=1050)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.073 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4252` → IC=+0.150 (n=746)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4252 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.8123` → IC=+0.142 (n=1491)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8123 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=3005)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `7113.8822` → IC=+0.151 (n=2024)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7113.8822 (IC base=+0.137)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.161 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0043 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.172 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0065 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0895` → IC=+0.190 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.0895 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5452` → IC=+0.185 (n=252)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.5452 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.3916` → IC=+0.157 (n=368)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.3916 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.401` → IC=+0.162 (n=400)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 2.401 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2719` → IC=+0.152 (n=377)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2719 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.8487` → IC=+0.184 (n=251)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8487 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.3101` → IC=+0.291 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3101 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.188 (n=126)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.6755` → IC=+0.203 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6755 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `12451.0907` → IC=+0.190 (n=337)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 12451.0907 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.212 (n=408)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1125` → IC=+0.173 (n=408)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1125 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.172 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.176 (n=408)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.1382 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.142 (n=420)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6084 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6994` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6994 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.219` → IC=+0.138 (n=948)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.219 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.107` → IC=+0.152 (n=1013)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 9.107 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8817` → IC=+0.184 (n=618)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8817 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.166 (n=435)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.422` → IC=+0.145 (n=308)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.422 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.147 (n=615)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `11389.4654` → IC=+0.149 (n=926)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 11389.4654 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `706.0` → IC=+0.144 (n=880)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 706.0 (IC base=+0.137)

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
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.151 (n=787)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0074 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.160 (n=894)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0043 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.3887` → IC=+0.153 (n=787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3887 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.165 (n=317)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5623` → IC=+0.155 (n=596)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5623 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.7903` → IC=+0.166 (n=405)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.7903 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.9851` → IC=+0.165 (n=198)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.9851 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.4248` → IC=+0.164 (n=833)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.4248 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.684` → IC=+0.160 (n=896)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.684 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.0865` → IC=+0.154 (n=787)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0865 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.7182` → IC=+0.154 (n=798)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7182 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.1099` → IC=+0.153 (n=825)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1099 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.0781` → IC=+0.161 (n=384)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0781 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4349` → IC=+0.163 (n=292)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4349 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=881)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.158 (n=673)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0071 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3946` → IC=+0.170 (n=673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3946 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.155 (n=520)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 10.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.7363` → IC=+0.144 (n=765)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.7363 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.0998` → IC=+0.148 (n=765)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.0998 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.6358` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6358 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.3871` → IC=+0.141 (n=783)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3871 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.774` → IC=+0.143 (n=124)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.774 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.639` → IC=+0.145 (n=789)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.639 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6473` → IC=+0.177 (n=255)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6473 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.7274` → IC=+0.142 (n=683)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7274 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.166 (n=324)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1956` → IC=+0.157 (n=660)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1956 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7791` → IC=+0.147 (n=500)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7791 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7572.3913` → IC=+0.166 (n=765)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7572.3913 (IC base=+0.140)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.223 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.247` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 9.247 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `3417.5406` → IC=+0.135 (n=195)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3417.5406 (IC base=+0.086)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.148 (n=214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0068 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.5355` → IC=+0.139 (n=189)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.5355 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.162 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 10.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1429 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.5982` → IC=+0.176 (n=100)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.5982 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.699` → IC=+0.133 (n=118)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.699 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` < `0.092` → IC=+0.175 (n=164)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.092 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.8499` → IC=+0.131 (n=139)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8499 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3291.3893` → IC=+0.143 (n=214)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3291.3893 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.159 (n=203)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 60.0 (IC base=+0.113)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.213 (n=120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=363)

- **FILTRO** `dist_vwap_pct` > `0.182` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.182
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=315)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.194 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.004 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.128 (n=834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.207 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6757 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1492` → IC=+0.161 (n=440)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1492 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.202 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.189 (n=104)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `2.0834` → IC=+0.136 (n=614)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.0834 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=652)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.02 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2424.4386` → IC=+0.142 (n=356)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2424.4386 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.0508` → IC=+0.266 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0508 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.0685` → IC=+0.203 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0685 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.1644` → IC=+0.134 (n=200)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1644 (IC base=+0.003)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.163 (n=307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.006 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.52` → IC=+0.183 (n=276)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.52 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.1343` → IC=+0.185 (n=144)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1343 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `1.0669` → IC=+0.124 (n=243)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.0669 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` < `0.0677` → IC=+0.139 (n=211)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.0677 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `2.0118` → IC=+0.173 (n=209)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.0118 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.0889` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0889 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.732` → IC=+0.148 (n=103)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.732 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.6103` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6103 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.3732` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.3732 (IC base=+0.051)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.237 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=115)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=116)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.179 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.004 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.6816` → IC=+0.234 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6816 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1272` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1272 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.853` → IC=+0.303 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.853 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `0.9516` → IC=+0.138 (n=125)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.9516 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.7281` → IC=+0.171 (n=150)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.7281 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=185)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `1749.1894` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1749.1894 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.267 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=-0.016)

- **PATRÓN** `dist_vwap_pct` < `0.1269` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1269 (IC base=-0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.842` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.842 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.3094` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.3094 (IC base=-0.016)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=-0.016)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.271 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=90)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.250 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=106)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.129 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 13.0 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.6731` → IC=+0.178 (n=231)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6731 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.155 (n=146)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.438` → IC=+0.170 (n=101)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 5.438 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.0643` → IC=+0.171 (n=86)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0643 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.072)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.181 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0057 (IC base=-0.043)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=-0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.25` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.25 (IC base=-0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.1368` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1368 (IC base=-0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.5569` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.5569 (IC base=-0.043)

- **PATRÓN** `volumen_spike_ratio` > `1.3803` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.3803 (IC base=-0.043)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `9.0` → IC=-0.396 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=153)

- **FILTRO** `dist_vwap_pct` > `0.2352` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2352
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=183)

- **FILTRO** `volumen_regimen` < `0.7506` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7506
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=134)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.379 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=114)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=149)

- **FILTRO** `sigma_ewma_delta_pct` > `5.949` → IC=-0.304 (n=49)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.949
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=121)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=69)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=53)

- **FILTRO** `ibs_20min` < `0.0648` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0648
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=47)

- **FILTRO** `volumen_spike_ratio` > `3.7991` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.7991
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

- **FILTRO** `sigma_h` < `0.0017` → IC=-0.289 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0017
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=54)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.292 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=25)

- **FILTRO** `volumen_regimen` > `0.9309` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9309
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=54)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8831` → IC=-0.411 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8831
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

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

- **PATRÓN** `ibs_20min` > `0.9883` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9883 (IC base=-0.221)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.441 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=47)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1906` → IC=-0.123 (n=120)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1906
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=234)

- **FILTRO** `dist_vwap_pct` > `0.4433` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4433
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=316)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.155 (n=114)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0058 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.163 (n=250)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.6522 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.4941` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.4941 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.121 (n=130)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1906` → IC=+0.136 (n=234)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.1906 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.944` → IC=+0.140 (n=109)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 5.944 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `3787.1326` → IC=+0.159 (n=121)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3787.1326 (IC base=+0.048)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.576` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.576
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=82)

- **FILTRO** `volumen_regimen` < `0.7924` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7924
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=82)

- **PATRÓN** `drift_60min` |x|≤ `0.2204` → IC=+0.157 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2204 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.161 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.113` → IC=+0.188 (n=107)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.113 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.3016` → IC=+0.122 (n=146)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.3016 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` < `0.1813` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.1813 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `2.8706` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.8706 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.114)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.1906` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1906
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=75)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.190 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.058)

- **PATRÓN** `drift_60min` |x|≤ `0.2855` → IC=+0.121 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.2855 (IC base=+0.058)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.7272` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7272 (IC base=+0.058)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `1549.4073` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1549.4073 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.013)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.210 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.220 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.218 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.9714` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9714 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.835` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.835 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.281 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.4627` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4627 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.199 (n=81)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.06 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.0808` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0808 (IC base=-0.037)

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

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.3 (IC base=+0.208)

- **PATRÓN** `drift_15min` |x|≤ `2.4512` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.4512 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.308 (n=24)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.208)

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

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.3 (IC base=+0.208)

- **PATRÓN** `drift_15min` |x|≤ `2.4512` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.4512 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.308 (n=24)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.208)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2917.3018` → IC=+0.167 (n=232)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2917.3018 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2917.3018` → IC=+0.167 (n=232)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2917.3018 (IC base=+0.103)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=80)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=133)

- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.173 (n=111)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=209)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=195)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1730)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9583` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9583
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=76)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.127 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 14.0 (IC base=+0.045)

### LIQUIDACIONES_5M#BTC#5min
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

- **PATRÓN** `liq_n` > `18.0` → IC=+0.200 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.025)

- **PATRÓN** `liq_usd_total` > `80505.33` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `liq_usd_total` > 80505.33 (IC base=+0.025)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=770)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=724)

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
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=626)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=626)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=498)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=348)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=348)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.148 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=277)

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

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=102)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=202)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=80)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=83)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=237)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=237)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=126)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.42` → IC=-0.182 (n=221)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=259)

- **FILTRO** `restante_min` < `3.45` → IC=-0.145 (n=119)

  - _Acción_: SKIP cuando `restante_min` < 3.45
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=361)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.144 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=381)

- **FILTRO** `profundidad_ratio` < `42.3` → IC=-0.132 (n=240)

  - _Acción_: SKIP cuando `profundidad_ratio` < 42.3
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=240)

- **PATRÓN** `py_entrada` < `0.57` → IC=+0.132 (n=229)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.57 (IC base=+0.035)

- **PATRÓN** `profundidad_ratio` > `100.0` → IC=+0.184 (n=112)

  - _Acción_: Kelly boost +0.92€ cuando `profundidad_ratio` > 100.0 (IC base=+0.035)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **PATRÓN** `py_entrada` < `0.52` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.52 (IC base=+0.097)

- **PATRÓN** `restante_min` > `10.28` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` > 10.28 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.136 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 10.0 (IC base=+0.097)

- **PATRÓN** `lag_apertura_s` < `252.54` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 252.54 (IC base=+0.097)

- **PATRÓN** `profundidad_ratio` > `239.4` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `profundidad_ratio` > 239.4 (IC base=+0.097)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.59` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.59 (IC base=+0.132)

- **PATRÓN** `restante_min` > `3.99` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `restante_min` > 3.99 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.196 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 8.0 (IC base=+0.132)

- **PATRÓN** `lag_apertura_s` < `60.77` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 60.77 (IC base=+0.132)

- **PATRÓN** `profundidad_ratio` > `79.6` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `profundidad_ratio` > 79.6 (IC base=+0.132)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` > `0.41` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `restante_min` > `11.54` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `restante_min` > 11.54
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.237 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=30)

- **FILTRO** `profundidad_ratio` < `56.2` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `profundidad_ratio` < 56.2
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

- **FILTRO** `restante_min` < `13.0` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `restante_min` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `lag_apertura_s` > `126.34` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `lag_apertura_s` > 126.34
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `restante_min` < `3.8` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `restante_min` < 3.8
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `lag_apertura_s` > `60.81` → IC=-0.250 (n=34)

  - _Acción_: SKIP cuando `lag_apertura_s` > 60.81
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.037)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `restante_min` < `13.48` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `restante_min` < 13.48
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

- **FILTRO** `lag_apertura_s` > `90.91` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `lag_apertura_s` > 90.91
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.218 (n=37)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.240 (n=48)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=29)

- **FILTRO** `restante_min` < `2.74` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `restante_min` < 2.74
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=58)

- **FILTRO** `lag_apertura_s` > `135.64` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `lag_apertura_s` > 135.64
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=58)

- **FILTRO** `profundidad_ratio` < `26.8` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `profundidad_ratio` < 26.8
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=26)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=7479)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.167 (n=3480)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=10462)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.167 (n=3610)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=10868)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.210 (n=598)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1822)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.190 (n=611)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=1851)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=632)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=1957)

- **FILTRO** `ibs_20min` > `0.281` → IC=-0.163 (n=647)

  - _Acción_: SKIP cuando `ibs_20min` > 0.281
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=1942)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.173 (n=597)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=1807)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=633)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1959)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=2746)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2927)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2933)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.164 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=381)

- **FILTRO** `libro_liquidez` < `16966.265` → IC=-0.143 (n=225)

  - _Acción_: SKIP cuando `libro_liquidez` < 16966.265
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=675)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=245)

- **FILTRO** `ibs_20min` < `0.1111` → IC=-0.237 (n=78)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1111
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=235)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.279 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=239)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.227 (n=192)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=588)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=9940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=22048)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=7817)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=24171)

- **FILTRO** `ibs_7min` < `0.2841` → IC=-0.235 (n=7997)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2841
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=23991)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=10871)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=21117)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9833)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=30293)

- **FILTRO** `ibs_7min` > `0.2922` → IC=-0.178 (n=10031)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2922
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=30095)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=1628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=3656)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=1262)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4022)

- **FILTRO** `ibs_7min` < `0.7099` → IC=-0.249 (n=1742)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7099
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3542)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.184 (n=1215)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4069)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.260 (n=1701)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=5190)

- **FILTRO** `drift_7min_pct` |x|> `0.1121` → IC=-0.124 (n=2342)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1121
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4549)

- **FILTRO** `ibs_7min` > `0.7882` → IC=-0.205 (n=1722)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7882
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=5169)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=4227)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1333)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4193)

- **FILTRO** `ibs_7min` < `0.7478` → IC=-0.193 (n=1381)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7478
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4145)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.175 (n=1375)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4151)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.253 (n=1397)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=4212)

- **FILTRO** `ibs_7min` > `0.2599` → IC=-0.176 (n=1402)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2599
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4207)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.181 (n=1395)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4214)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.165 (n=1430)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=3581)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.306 (n=1230)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=3781)

- **FILTRO** `ibs_7min` < `0.1935` → IC=-0.258 (n=1252)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1935
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3759)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.219 (n=1166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3845)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.236 (n=1683)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=5694)

- **FILTRO** `ibs_7min` > `0.7442` → IC=-0.175 (n=1843)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7442
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=5534)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1705)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=3569)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.231 (n=1563)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=3711)

- **FILTRO** `ibs_7min` < `0.7407` → IC=-0.182 (n=1318)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3956)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.170 (n=1302)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=3972)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1346)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4042)

- **FILTRO** `ibs_7min` > `0.2747` → IC=-0.177 (n=1346)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4042)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.185 (n=1333)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4055)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.257 (n=1358)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=4230)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.239 (n=1394)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4194)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.177 (n=1813)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=5818)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.255 (n=1709)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3596)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.227 (n=1313)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3992)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1290)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4015)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.204 (n=1729)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=5501)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1070)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=531)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=555)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.139 (n=491)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.127 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 14.0 (IC base=+0.110)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.144 (n=57)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.134 (n=151)

  - _Acción_: Kelly boost +0.67€ cuando `total_vol_5m` < 451.687 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2532.1776` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2532.1776 (IC base=+0.130)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.121 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 12.0 (IC base=+0.096)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.167 (n=100)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.082)

- **PATRÓN** `total_vol_5m` < `394.3776` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `total_vol_5m` < 394.3776 (IC base=+0.082)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.172 (n=129)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.196 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.164 (n=114)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 6300.756 (IC base=+0.132)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.134 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 13.0 (IC base=+0.102)

- **PATRÓN** `total_vol_5m` < `262739.3` → IC=+0.149 (n=95)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 262739.3 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3566.692` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3566.692 (IC base=+0.102)

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
- **FILTRO** `T_h` > `109.663` → IC=-0.149 (n=186)

  - _Acción_: SKIP cuando `T_h` > 109.663
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=187)

- **FILTRO** `pct_vs_K` |x|> `4.167` → IC=-0.258 (n=93)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.167
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=280)

- **FILTRO** `pct_vs_K` |x|> `3.325` → IC=-0.436 (n=108)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.325
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=212)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.004` → IC=-0.206 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=99)

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

- **FILTRO** `T_h` > `49.1198` → IC=-0.310 (n=77)

  - _Acción_: SKIP cuando `T_h` > 49.1198
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

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

- **PATRÓN** `edge` > `0.097` → IC=+0.457 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.097 (IC base=+0.419)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.457 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.419)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.419)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.438 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.419)

- **PATRÓN** `dist_50` > `0.4027` → IC=+0.486 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4027 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.468 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.419)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1134` → IC=+0.444 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1134 (IC base=+0.411)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.395 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.411)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.411)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.444 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.411)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.472 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.411)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.429 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.411)

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

- **PATRÓN** `edge` > `0.096` → IC=+0.478 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.470)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.478 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.470)

- **PATRÓN** `T_h` < `0.8294` → IC=+0.469 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8294 (IC base=+0.470)

- **PATRÓN** `T_h` > `1.2259` → IC=+0.468 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2259 (IC base=+0.470)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.488 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.470)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.476 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.470)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=176)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=286)

- **PATRÓN** `streak_estiramiento` < `0.4086` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.4086 (IC base=+0.029)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.164 (n=123)

  - _Acción_: Kelly boost +0.82€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.037)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=16)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.015)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.5576` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.5576
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=32)

- **FILTRO** `ballena_activa_n` > `52.0` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 52.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=34)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_racha` < 990711.2 (IC base=-0.009)

- **PATRÓN** `streak_estiramiento` < `0.5576` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.5576 (IC base=-0.009)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.122 (n=88)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 49.0 (IC base=+0.051)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=84)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=90)

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
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=777)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=783)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=391)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=594)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1108)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=739)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=719)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2880)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1464)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1472)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.221 (n=525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.204 (n=525)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.185)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2128` → IC=+0.196 (n=525)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.2128 (IC base=+0.185)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1267` → IC=+0.227 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1267 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=1464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.185)

- **PATRÓN** `ibs_15` > `0.6047` → IC=+0.265 (n=1576)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6047 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.3002` → IC=+0.191 (n=545)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.3002 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.6102` → IC=+0.176 (n=1512)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.6102 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.822` → IC=+0.276 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.822 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2975.4354` → IC=+0.193 (n=1050)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2975.4354 (IC base=+0.185)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=600)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.215 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.295 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.204)

- **PATRÓN** `drift_15min` |x|≤ `0.3839` → IC=+0.205 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3839 (IC base=+0.204)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.254 (n=120)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.204)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1446` → IC=+0.264 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1446 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.234 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.204)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.270 (n=359)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.4066` → IC=+0.250 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4066 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.385` → IC=+0.270 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.385 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `16049.3542` → IC=+0.246 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.3542 (IC base=+0.204)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `25.169` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 25.169
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=367)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.152 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0041 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.160 (n=245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0051 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.146 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.134)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2316` → IC=+0.180 (n=123)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.2316 (IC base=+0.134)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.258` → IC=+0.158 (n=261)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.258 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `ibs_15` > `0.6604` → IC=+0.249 (n=329)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6604 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.5785` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.5785 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.147 (n=290)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.257` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.257 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `9553.1781` → IC=+0.157 (n=167)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 9553.1781 (IC base=+0.134)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.136 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=82)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.297 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.1498` → IC=+0.211 (n=164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1498 (IC base=+0.176)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.210 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.176)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2704` → IC=+0.228 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2704 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.215 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.176)

- **PATRÓN** `ibs_15` > `0.6122` → IC=+0.261 (n=186)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6122 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.2696` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2696 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.532` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.532 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=143)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `3071.8702` → IC=+0.282 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3071.8702 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.230 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.176)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5688` → IC=-0.135 (n=124)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5688
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=899)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.788` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.788 (IC base=+0.012)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.259 (n=139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0864` → IC=+0.211 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0864 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0389` → IC=+0.192 (n=417)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0389 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.243 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.229 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.283 (n=417)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.1302` → IC=+0.210 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1302 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.8104` → IC=+0.186 (n=482)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.8104 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.866` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.866 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.785` → IC=+0.189 (n=416)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 10.785 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `2914.5894` → IC=+0.273 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2914.5894 (IC base=+0.186)

- **PATRÓN** `ibs_15` < `0.1163` → IC=+0.160 (n=468)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1163 (IC base=+0.048)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.339 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.377 (n=185)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.338)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.347 (n=272)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.338)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.364 (n=271)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.338)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.13` → IC=+0.375 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.13 (IC base=+0.338)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.385 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.338)

- **PATRÓN** `ibs_15` > `0.7863` → IC=+0.383 (n=407)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7863 (IC base=+0.338)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.386 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.338)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.338 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.188` → IC=+0.342 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.188 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.339 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.338)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.344 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.338)

- **PATRÓN** `libro_liquidez` > `3525.4286` → IC=+0.353 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3525.4286 (IC base=+0.338)

- **PATRÓN** `ballena_activa_n` < `463.0` → IC=+0.360 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 463.0 (IC base=+0.338)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.351 (n=200)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.342)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.372 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.342)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.372 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.342)

- **PATRÓN** `drift_15min` |x|≤ `0.4288` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4288 (IC base=+0.342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1503` → IC=+0.363 (n=151)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1503 (IC base=+0.342)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.383 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.342)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.368 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.342)

- **PATRÓN** `ibs_15` > `0.8166` → IC=+0.378 (n=227)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8166 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` > `0.4066` → IC=+0.409 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4066 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.763` → IC=+0.346 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.763 (IC base=+0.342)

- **PATRÓN** `libro_liquidez` > `15700.521` → IC=+0.359 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15700.521 (IC base=+0.342)

- **PATRÓN** `ballena_activa_n` < `574.0` → IC=+0.390 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 574.0 (IC base=+0.342)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.369 (n=120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.345 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.331)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.354 (n=162)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.331)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.360 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.331)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.395 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.331)

- **PATRÓN** `ibs_15` > `0.7403` → IC=+0.390 (n=180)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7403 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.379 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` < `0.1227` → IC=+0.339 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1227 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.344 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.334 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.331)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.344 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.331)

- **PATRÓN** `libro_liquidez` > `3532.4883` → IC=+0.352 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3532.4883 (IC base=+0.331)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.343 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=+0.331)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.013` → IC=-0.219 (n=649)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1951)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.191 (n=877)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1723)

- **FILTRO** `libro_liquidez` < `3915.9217` → IC=-0.137 (n=1716)

  - _Acción_: SKIP cuando `libro_liquidez` < 3915.9217
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=884)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.254 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.061)

- **PATRÓN** `ibs_15` > `0.6371` → IC=+0.273 (n=624)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6371 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` < `0.2788` → IC=+0.183 (n=494)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.2788 (IC base=-0.061)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1199` → IC=+0.245 (n=1146)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1199 (IC base=-0.033)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.177` → IC=+0.235 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.177 (IC base=-0.033)

- **PATRÓN** `ibs_15` < `0.3455` → IC=+0.278 (n=1720)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3455 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` > `0.6876` → IC=+0.287 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6876 (IC base=-0.033)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.219 (n=396)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1189)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.231 (n=396)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1189)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.208 (n=1000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=585)

- **FILTRO** `sigma_ewma_delta_pct` > `19.79` → IC=-0.245 (n=284)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.79
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1301)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.162 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0028 (IC base=+0.081)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.285 (n=77)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.081)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.7466` → IC=+0.326 (n=170)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7466 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.283 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.5746` → IC=+0.274 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5746 (IC base=+0.081)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6675` → IC=-0.193 (n=99)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6675
  - _Potencial_: sin este filtro IC_bueno=+0.267 (n=298)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=380)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.192 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0051 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0757` → IC=+0.216 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0757 (IC base=+0.152)

- **PATRÓN** `drift_15min` |x|≤ `0.4223` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.4223 (IC base=+0.152)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1323` → IC=+0.157 (n=199)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.1323 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.238 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.6675` → IC=+0.267 (n=298)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6675 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.4805` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.4805 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1187` → IC=+0.185 (n=214)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1187 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.857` → IC=+0.165 (n=237)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.857 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=380)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.201 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.263 (n=226)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.225)

- **PATRÓN** `drift_15min` |x|≤ `0.7901` → IC=+0.229 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7901 (IC base=+0.225)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2036` → IC=+0.257 (n=307)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2036 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.238 (n=303)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.225)

- **PATRÓN** `ibs_15` < `0.3453` → IC=+0.266 (n=676)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3453 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.7773` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7773 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.806` → IC=+0.248 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.806 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.251` → IC=+0.230 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.251 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `3551.8492` → IC=+0.225 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3551.8492 (IC base=+0.225)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1671` → IC=-0.219 (n=208)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1671
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=405)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.261 (n=153)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=460)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.167)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0758` → IC=+0.228 (n=274)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0758 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.267 (n=307)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.2005` → IC=+0.225 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2005 (IC base=-0.041)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.260 (n=382)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=383)

- **FILTRO** `drift_15min` |x|> `1.2489` → IC=-0.262 (n=191)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2489
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=574)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=185)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=580)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1326` → IC=+0.278 (n=210)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1326 (IC base=-0.044)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1021` → IC=+0.336 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1021 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3429` → IC=+0.305 (n=460)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3429 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.8964` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8964 (IC base=-0.044)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.052)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1565` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1565 (IC base=+0.052)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.299 (n=436)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.293 (n=297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.327 (n=218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.309 (n=218)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.347 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.328 (n=654)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.321 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.330 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.296 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `13081.1746` → IC=+0.306 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13081.1746 (IC base=+0.293)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.299 (n=242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.290 (n=165)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.345 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2603` → IC=+0.313 (n=121)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2603 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3807` → IC=+0.307 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3807 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.304 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.316 (n=363)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.444` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.444 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.357 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.329 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.306 (n=292)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.300)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.307 (n=195)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.300)

- **PATRÓN** `delta_ratio_macro` |x|> `0.226` → IC=+0.318 (n=97)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.226 (IC base=+0.300)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.338 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.300)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.333 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.300)

- **PATRÓN** `ibs_15` > `0.8486` → IC=+0.340 (n=291)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8486 (IC base=+0.300)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.300)

- **PATRÓN** `dist_vwap_pct` < `0.167` → IC=+0.300 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.167 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.221` → IC=+0.320 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.221 (IC base=+0.300)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.311 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.300)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.186 (n=68)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=207)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1131` → IC=-0.171 (n=68)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1131
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=207)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.173 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=331)

- **FILTRO** `drift_15min` |x|> `0.5254` → IC=-0.140 (n=109)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5254
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=330)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=108)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2228` → IC=-0.259 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2228
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

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

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.103` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.103
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `drift_15min` |x|> `0.1344` → IC=-0.241 (n=25)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1344
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6047 sube el IC de +0.185 a +0.265 en UPDOWN_GBM#15min (n=1576). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.204 a +0.270 en UPDOWN_GBM#BTC#15min (n=359). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6604 sube el IC de +0.134 a +0.249 en UPDOWN_GBM#ETH#15min (n=329). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6122 sube el IC de +0.176 a +0.261 en UPDOWN_GBM#SOL#15min (n=186). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.186 a +0.283 en UPDOWN_GBM#XRP#15min (n=417). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1163 sube el IC de +0.048 a +0.160 en UPDOWN_GBM#XRP#15min (n=468). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6371 sube el IC de -0.061 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=624). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3455 sube el IC de -0.033 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1720). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7466 sube el IC de +0.081 a +0.326 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=170). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6675 sube el IC de +0.152 a +0.267 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=298). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3453 sube el IC de +0.225 a +0.266 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=676). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.167 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.041 a +0.267 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=307). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3429 sube el IC de -0.044 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=460). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.293 a +0.328 en UPDOWN_GBM_IBS_ALTO (n=654). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.286 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=363). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8486 sube el IC de +0.300 a +0.340 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=291). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7863 sube el IC de +0.338 a +0.383 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=407). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8166 sube el IC de +0.342 a +0.378 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=227). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7403 sube el IC de +0.331 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=180). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1311 | +0.099 | +195.95€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1311 | +0.099 | +195.95€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 977 | +0.109 | +170.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 977 | +0.109 | +170.04€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 248 | +0.052 | +7.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 248 | +0.052 | +7.26€ | 6 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 24954 | -0.092 | -3195.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1444 | -0.049 | -221.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 23510 | -0.095 | -2973.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3683 | -0.092 | -588.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3683 | -0.092 | -588.60€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1444 | -0.049 | -221.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1444 | -0.049 | -221.33€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7215 | -0.025 | -679.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7215 | -0.025 | -679.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6707 | -0.099 | -464.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6707 | -0.099 | -464.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5531 | -0.181 | -1079.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5531 | -0.181 | -1079.97€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 17881 | -0.028 | +4061.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4676 | +0.000 | +1829.25€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 13205 | -0.038 | +2232.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 17881 | -0.028 | +4061.79€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4676 | +0.000 | +1829.25€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 13205 | -0.038 | +2232.53€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1471 | -0.102 | -187.97€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1303 | -0.108 | -166.62€ | 0 | 0 |
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
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 59 | -0.172 | -6.50€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 59 | -0.172 | -6.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 91857 | +0.112 | -4695.16€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13895 | +0.185 | -436.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 369 | -0.088 | -51.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 71606 | +0.100 | -3985.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5987 | +0.108 | -220.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11910 | +0.098 | -1014.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 45 | -0.160 | -0.32€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11850 | +0.099 | -1002.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 18579 | +0.132 | -380.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4371 | +0.203 | -142.91€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11871 | +0.111 | -185.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2295 | +0.105 | -29.33€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11950 | +0.089 | -1116.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 52 | -0.093 | -6.98€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11883 | +0.090 | -1097.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 19554 | +0.123 | -405.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5378 | +0.174 | -84.67€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11998 | +0.105 | -258.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2166 | +0.098 | -54.27€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 17940 | +0.113 | -1066.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4003 | +0.188 | -211.33€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 272 | -0.047 | +2.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 12139 | +0.091 | -719.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1526 | +0.126 | -137.15€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11924 | +0.100 | -713.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 46 | -0.021 | +9.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11865 | +0.101 | -722.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 14574 | +0.191 | -970.94€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 14574 | +0.191 | -970.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3478 | +0.167 | -368.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3478 | +0.167 | -368.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1191 | +0.194 | -12.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1191 | +0.194 | -12.42€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3422 | +0.179 | -299.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3422 | +0.179 | -299.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3047 | +0.239 | -98.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3047 | +0.239 | -98.57€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3357 | +0.192 | -205.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3357 | +0.192 | -205.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 684 | +0.429 | -20.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 684 | +0.429 | -20.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 262 | +0.436 | -3.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 262 | +0.436 | -3.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 258 | +0.435 | -3.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 258 | +0.435 | -3.66€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 155 | +0.405 | -10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 155 | +0.405 | -10.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 50150 | +0.196 | -4021.35€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 50150 | +0.196 | -4021.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8681 | +0.175 | -1021.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8681 | +0.175 | -1021.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8007 | +0.221 | -312.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8007 | +0.221 | -312.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8659 | +0.171 | -1056.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8659 | +0.171 | -1056.26€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8105 | +0.218 | -328.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8105 | +0.218 | -328.92€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8285 | +0.202 | -561.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8285 | +0.202 | -561.87€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8413 | +0.193 | -739.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8413 | +0.193 | -739.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 18915 | +0.119 | +196.81€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 18915 | +0.119 | +196.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9390 | +0.123 | +165.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9390 | +0.123 | +165.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9525 | +0.114 | +31.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9525 | +0.114 | +31.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1452 | +0.292 | -9.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1452 | +0.292 | -9.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 648 | +0.279 | -15.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 648 | +0.279 | -15.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 699 | +0.295 | +4.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 699 | +0.295 | +4.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 105 | +0.341 | +2.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 105 | +0.341 | +2.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 636 | +0.439 | +1.18€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 636 | +0.439 | +1.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 300 | +0.437 | -0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 300 | +0.437 | -0.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 295 | +0.443 | +2.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 295 | +0.443 | +2.14€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 41 | +0.384 | +0.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 41 | +0.384 | +0.01€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1099 | +0.076 | -41.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 381 | +0.064 | -28.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 718 | +0.082 | -13.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 867 | +0.082 | -16.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 149 | +0.083 | -3.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 718 | +0.082 | -13.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 171 | +0.026 | -28.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 171 | +0.026 | -28.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 34998 | +0.097 | -1110.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2895 | +0.090 | +25.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 32103 | +0.097 | -1135.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 19671 | +0.101 | -330.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2895 | +0.090 | +25.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 16776 | +0.103 | -356.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6556 | +0.107 | -36.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6556 | +0.107 | -36.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8771 | +0.079 | -742.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8771 | +0.079 | -742.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 797 | +0.213 | -100.04€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 797 | +0.213 | -100.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 797 | +0.213 | -100.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 797 | +0.213 | -100.04€ | 2 | 4 |
| ✅ GBM_LATE_15M | 25149 | +0.082 | +11893.60€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 25149 | +0.082 | +11893.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4204 | +0.192 | +3035.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4204 | +0.192 | +3035.98€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 3725 | +0.177 | +2579.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3725 | +0.177 | +2579.79€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 4367 | +0.198 | +3250.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4367 | +0.198 | +3250.26€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 3716 | +0.019 | +778.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3716 | +0.019 | +778.97€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3606 | -0.032 | +832.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3606 | -0.032 | +832.16€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 5531 | -0.041 | +1416.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5531 | -0.041 | +1416.44€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 26557 | +0.085 | +13812.51€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 26557 | +0.085 | +13812.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5031 | +0.018 | +2668.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5031 | +0.018 | +2668.01€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5531 | +0.015 | +1141.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5531 | +0.015 | +1141.32€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3777 | +0.261 | +3780.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3777 | +0.261 | +3780.91€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4308 | +0.002 | +805.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4308 | +0.002 | +805.17€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4320 | +0.027 | +1619.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4320 | +0.027 | +1619.71€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3590 | +0.273 | +3797.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3590 | +0.273 | +3797.39€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 20287 | +0.167 | +15061.81€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 20287 | +0.167 | +15061.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3055 | +0.205 | +2407.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3055 | +0.205 | +2407.76€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3228 | +0.149 | +2362.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3228 | +0.149 | +2362.61€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3184 | +0.206 | +2510.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3184 | +0.206 | +2510.80€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3410 | +0.132 | +2353.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3410 | +0.132 | +2353.76€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3771 | +0.116 | +2568.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3771 | +0.116 | +2568.60€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3639 | +0.203 | +2858.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3639 | +0.203 | +2858.27€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5044 | +0.126 | +2094.78€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5044 | +0.126 | +2094.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 188 | +0.121 | +82.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 188 | +0.121 | +82.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1437 | +0.122 | +641.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1437 | +0.122 | +641.71€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1482 | +0.141 | +649.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1482 | +0.141 | +649.24€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1060 | +0.101 | +327.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1060 | +0.101 | +327.94€ | 2 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 25259 | +0.174 | +18703.64€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 25259 | +0.174 | +18703.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4006 | +0.219 | +3360.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4006 | +0.219 | +3360.46€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3953 | +0.150 | +2613.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3953 | +0.150 | +2613.07€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4142 | +0.225 | +3554.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4142 | +0.225 | +3554.32€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4098 | +0.137 | +2777.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4098 | +0.137 | +2777.89€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4423 | +0.111 | +2773.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4423 | +0.111 | +2773.56€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4637 | +0.204 | +3624.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4637 | +0.204 | +3624.32€ | 0 | 24 |
| ✅ GBM_LATE_5M | 6823 | +0.144 | +3813.26€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 6823 | +0.144 | +3813.26€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1736 | +0.141 | +1109.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1736 | +0.141 | +1109.56€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2210 | +0.146 | +1211.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2210 | +0.146 | +1211.42€ | 0 | 32 |
| ✅ GBM_LATE_5M#SOL | 575 | +0.100 | +194.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 575 | +0.100 | +194.89€ | 0 | 14 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1684 | +0.069 | +728.28€ | 2 | 12 |
| ✅ GBM_LATE_60M#60min | 1684 | +0.069 | +728.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 605 | +0.088 | +255.55€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 605 | +0.088 | +255.55€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 559 | +0.072 | +285.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 559 | +0.072 | +285.07€ | 2 | 16 |
| ✅ GBM_LATE_60M#SOL | 520 | +0.042 | +187.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 520 | +0.042 | +187.66€ | 2 | 12 |
| 🚫 GBM_LATE_60M_FADE | 369 | -0.257 | -25.96€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 369 | -0.257 | -25.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 141 | -0.227 | -11.75€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 141 | -0.227 | -11.75€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 122 | -0.250 | -6.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 122 | -0.250 | -6.90€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 106 | -0.296 | -7.30€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 106 | -0.296 | -7.30€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 687 | +0.069 | +141.22€ | 2 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 687 | +0.069 | +141.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 270 | +0.059 | +46.83€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 270 | +0.059 | +46.83€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 197 | +0.033 | +1.40€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 197 | +0.033 | +1.40€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 220 | +0.113 | +93.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 220 | +0.113 | +93.00€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 96 | +0.255 | +77.56€ | 0 | 9 |
| ✅ LATE_WINDOW_5MIN#5min | 96 | +0.255 | +77.56€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 96 | +0.255 | +77.56€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 96 | +0.255 | +77.56€ | 0 | 9 |
| ✅ LEADLAG_BTC_XRP_15M | 1905 | +0.097 | +505.05€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1905 | +0.097 | +505.05€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1905 | +0.097 | +505.05€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1905 | +0.097 | +505.05€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 379 | -0.077 | -33.28€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 379 | -0.077 | -33.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 96 | -0.061 | -5.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 96 | -0.061 | -5.23€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 135 | -0.018 | -3.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 135 | -0.018 | -3.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1928 | +0.004 | +11.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1928 | +0.004 | +11.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 103 | +0.024 | +0.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 103 | +0.024 | +0.01€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 211 | -0.007 | +10.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 211 | -0.007 | +10.22€ | 4 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 155 | -0.041 | -8.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 155 | -0.041 | -8.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 817 | +0.026 | +22.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 817 | +0.026 | +22.74€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 467 | -0.001 | -5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 467 | -0.001 | -5.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 175 | -0.042 | -8.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 175 | -0.042 | -8.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 1069 | -0.043 | -26.28€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1069 | -0.043 | -26.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 304 | -0.039 | -11.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 304 | -0.039 | -11.92€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 357 | -0.029 | -2.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 357 | -0.029 | -2.07€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 408 | -0.059 | -12.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 408 | -0.059 | -12.29€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 925 | -0.037 | -13.08€ | 4 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 432 | -0.037 | -6.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 493 | -0.037 | -6.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 31 | -0.015 | +1.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 18 | +0.045 | +2.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 13 | -0.065 | -1.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 229 | +0.054 | +45.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 104 | +0.038 | +16.00€ | 0 | 5 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 125 | +0.067 | +29.68€ | 0 | 6 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 142 | -0.083 | -17.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 65 | -0.082 | -8.34€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 77 | -0.082 | -9.00€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 158 | -0.087 | -18.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 73 | -0.087 | -8.21€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 85 | -0.086 | -10.05€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 144 | -0.034 | -3.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 76 | -0.026 | +1.88€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 68 | -0.043 | -4.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 221 | -0.070 | -21.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 96 | -0.071 | -10.40€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 125 | -0.067 | -11.33€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M | 14343 | -0.011 | -203.99€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14343 | -0.011 | -203.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3060 | -0.020 | -57.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3060 | -0.020 | -57.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 28420 | -0.007 | +1275.95€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 28420 | -0.007 | +1275.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5011 | +0.017 | +617.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5011 | +0.017 | +617.43€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4416 | -0.028 | -49.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4416 | -0.028 | -49.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5051 | +0.015 | +459.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5051 | +0.015 | +459.68€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4192 | -0.051 | -142.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4192 | -0.051 | -142.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4754 | -0.011 | +176.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4754 | -0.011 | +176.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4996 | +0.007 | +215.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4996 | +0.007 | +215.09€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5774 | -0.057 | -128.51€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5774 | -0.057 | -128.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1204 | +0.001 | -14.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1204 | +0.001 | -14.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1398 | -0.080 | -34.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1398 | -0.080 | -34.70€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 618 | -0.113 | -18.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 618 | -0.113 | -18.25€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1663 | -0.076 | -29.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1663 | -0.076 | -29.65€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 72114 | -0.072 | +1777.17€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 72114 | -0.072 | +1777.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 12175 | -0.079 | +735.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 12175 | -0.079 | +735.89€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 11135 | -0.092 | -472.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 11135 | -0.092 | -472.51€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 12388 | -0.066 | +706.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 12388 | -0.066 | +706.42€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 10662 | -0.093 | -156.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 10662 | -0.093 | -156.55€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 13219 | -0.048 | +388.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 13219 | -0.048 | +388.80€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 12535 | -0.062 | +575.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 12535 | -0.062 | +575.12€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7578 | -0.023 | -113.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7578 | -0.023 | -113.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1662 | -0.026 | -0.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1662 | -0.026 | -0.93€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2144 | -0.018 | -23.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2144 | -0.018 | -23.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1035 | -0.040 | -14.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1035 | -0.040 | -14.46€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1115 | +0.103 | +356.40€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#5min | 979 | +0.110 | +343.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 228 | +0.130 | +107.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 228 | +0.130 | +107.06€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 191 | +0.096 | +45.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 191 | +0.096 | +45.61€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 199 | +0.082 | +56.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 199 | +0.082 | +56.77€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#SOL | 172 | +0.132 | +78.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 172 | +0.132 | +78.55€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 189 | +0.102 | +55.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 189 | +0.102 | +55.82€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 463 | -0.063 | -58.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 463 | -0.063 | -58.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 99 | -0.015 | +0.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 99 | -0.015 | +0.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 57 | -0.127 | -16.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 57 | -0.127 | -16.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 136 | -0.087 | -28.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 136 | -0.087 | -28.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 97 | -0.005 | -0.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 97 | -0.005 | -0.11€ | 0 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 208 | -0.233 | -27.06€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 168 | -0.194 | +16.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 152 | -0.195 | +12.09€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 608 | -0.210 | -41.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 289 | +0.411 | +221.68€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 78 | +0.375 | +58.57€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 78 | +0.375 | +58.57€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 182 | +0.478 | +167.34€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 182 | +0.478 | +167.34€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#sniper | 289 | +0.411 | +221.68€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 500 | +0.034 | +15.36€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 500 | +0.034 | +15.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 234 | +0.038 | +6.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 234 | +0.038 | +6.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 34 | +0.056 | -0.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 34 | +0.056 | -0.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 54 | +0.000 | -0.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 54 | +0.000 | -0.99€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 178 | +0.033 | +9.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 178 | +0.033 | +9.85€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2755 | -0.023 | -114.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2755 | -0.023 | -114.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 568 | -0.023 | -23.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 568 | -0.023 | -23.29€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1228 | -0.022 | -49.08€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1228 | -0.022 | -49.08€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 73 | -0.060 | -7.39€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 73 | -0.060 | -7.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 35 | -0.013 | -2.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7685 | +0.023 | +115.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7685 | +0.023 | +115.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2135 | +0.021 | +20.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2135 | +0.021 | +20.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1722 | +0.036 | +53.55€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1722 | +0.036 | +53.55€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2328 | +0.012 | +2.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2328 | +0.012 | +2.56€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1500 | +0.030 | +38.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1500 | +0.030 | +38.74€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7216 | +0.012 | -39.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7216 | +0.012 | -39.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2899 | +0.016 | -7.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2899 | +0.016 | -7.57€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2821 | +0.012 | -17.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2821 | +0.012 | -17.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1496 | +0.005 | -14.86€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1496 | +0.005 | -14.86€ | 2 | 0 |
| ✅ UPDOWN_GBM | 36587 | +0.029 | +2124.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 9869 | +0.066 | +1754.62€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 1351 | +0.004 | +5.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 23003 | +0.018 | +341.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2225 | +0.006 | +22.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3736 | +0.066 | +396.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 648 | +0.148 | +252.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 31 | -0.015 | -0.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3057 | +0.049 | +144.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6751 | +0.035 | +455.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1246 | +0.083 | +276.67€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 366 | +0.019 | +7.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 4088 | +0.031 | +151.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 998 | +0.004 | +19.56€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 53 | -0.100 | +0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4259 | +0.039 | +247.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 603 | +0.138 | +209.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 27 | -0.017 | -2.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3629 | +0.022 | +40.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7783 | +0.016 | +266.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2538 | +0.044 | +263.25€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 354 | +0.006 | +6.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 4088 | +0.004 | -2.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 758 | +0.003 | -4.03€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 45 | -0.138 | +3.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8746 | +0.015 | +216.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2410 | +0.027 | +170.24€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 348 | -0.006 | -2.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5480 | +0.011 | +43.89€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 469 | +0.016 | +7.14€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 39 | -0.159 | -2.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5310 | +0.035 | +544.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2424 | +0.080 | +582.77€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 225 | -0.002 | -3.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2661 | -0.004 | -35.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 137 | -0.133 | +2.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 542 | +0.338 | +160.69€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 542 | +0.338 | +160.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 302 | +0.342 | +85.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 302 | +0.342 | +85.98€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 240 | +0.331 | +74.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 240 | +0.331 | +74.71€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 11748 | -0.039 | +2498.73€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 11748 | -0.039 | +2498.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 745 | -0.037 | +358.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 745 | -0.037 | +358.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2177 | -0.121 | +29.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2177 | -0.121 | +29.71€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 373 | +0.180 | +249.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 373 | +0.180 | +249.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1297 | +0.203 | +747.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1297 | +0.203 | +747.48€ | 2 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3570 | -0.062 | +559.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3570 | -0.062 | +559.31€ | 2 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3586 | -0.077 | +554.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3586 | -0.077 | +554.86€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 141 | +0.038 | +8.84€ | 2 | 2 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 141 | +0.038 | +8.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 141 | +0.038 | +8.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 141 | +0.038 | +8.84€ | 2 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO | 871 | +0.293 | +706.56€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 871 | +0.293 | +706.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 483 | +0.286 | +366.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 483 | +0.286 | +366.79€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 388 | +0.300 | +339.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 388 | +0.300 | +339.77€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 714 | -0.109 | -81.60€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 714 | -0.109 | -81.60€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 202 | -0.073 | -13.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 202 | -0.073 | -13.81€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 69 | -0.162 | -8.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 69 | -0.162 | -8.81€ | 2 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 65 | -0.202 | -9.44€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 65 | -0.202 | -9.44€ | 2 | 0 |
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
  - _Estado_: IC=+0.018 n=477 — no justifica filtro, seguir monitorizando
  - _Datos_: n=477 IC=+0.018 PNL=+22.99€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 518 celda(s) pasan gate riguroso completo de 2225 evaluadas (n>=40) y 3212 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.027 < 0.08 — monitorear
  - _Datos_: n=2410 IC=+0.027 PNL=+170.24€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.106 n=305/60 | contraria IC=+0.146 n=295 | gap=-0.041 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=283, boost estimado=+0.000. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=758/40 IC=+0.003 PNL=-4.03€ | BTC#60min: n=998/40 IC=+0.004 PNL=+19.56€ | SOL#60min: n=469/40 IC=+0.016 PNL=+7.14€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=330027 | tras_1loss IC=+0.077 n=257187 | tras_2loss IC=+0.047 n=108630/40 | gap=+0.004 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.08 con n=319 PNL=+206.87€
  - _Datos_: n=319 IC=+0.182 PNL=+206.87€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.08 con n=373 PNL=+273.31€
  - _Datos_: n=373 IC=+0.220 PNL=+273.31€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.238 > 0.08 con n=40 PNL=+29.59€
  - _Datos_: n=40 IC=+0.238 PNL=+29.59€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.327 > 0.1 con n=1919 PNL=+1069.33€
  - _Datos_: n=1919 IC=+0.327 PNL=+1069.33€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=274 IC=+0.080 PNL=+34.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=274 IC=+0.080 PNL=+34.60€

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
  - _Estado_: n=1571 IC=+0.014 PNL=+11.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1571 IC=+0.014 PNL=+11.81€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=654 IC=-0.012 PNL=+10.86€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=654 IC=-0.012 PNL=+10.86€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=477 IC=+0.018 PNL=+22.99€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=477 IC=+0.018 PNL=+22.99€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.185 > 0.1 con n=2099 PNL=+1297.22€
  - _Datos_: n=2099 IC=+0.185 PNL=+1297.22€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1246 IC=+0.083 PNL=+276.67€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1246 IC=+0.083 PNL=+276.67€

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
  - _Estado_: n=539 IC=+0.010 PNL=+35.26€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=539 IC=+0.010 PNL=+35.26€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=50 IC=+0.058 PNL=+3.56€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=50 IC=+0.058 PNL=+3.56€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.255 n=96) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=96 IC=+0.255 PNL=+77.56€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.02 con n=636 PNL=+237.06€
  - _Datos_: n=636 IC=+0.119 PNL=+237.06€

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
  - _Estado_: n=12716 IC=+0.052 PNL=+1507.45€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=12716 IC=+0.052 PNL=+1507.45€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.157 < -0.1 con n=228 PNL=+21.18€
  - _Datos_: n=228 IC=-0.157 PNL=+21.18€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1868 IC=+0.048 PNL=+195.70€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1868 IC=+0.048 PNL=+195.70€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.1 con n=398 PNL=+112.88€
  - _Datos_: n=398 IC=+0.128 PNL=+112.88€

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
  - _Estado_: n=17602 IC=-0.138 PNL=+1150.36€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=17602 IC=-0.138 PNL=+1150.36€

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
  - _Estado_: n=1902 IC=+0.140 PNL=+1041.33€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1902 IC=+0.140 PNL=+1041.33€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=3905 IC=+0.019 PNL=+117.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3905 IC=+0.019 PNL=+117.24€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=2056 PNL=+1064.56€
  - _Datos_: n=2056 IC=+0.086 PNL=+1064.56€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.240 < -0.1 con n=1715 PNL=-194.17€
  - _Datos_: n=1715 IC=-0.240 PNL=-194.17€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.091 n=978) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=978 IC=+0.091 PNL=+222.16€

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
  - _Estado_: n=8675 IC=+0.175 PNL=-1019.40€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8675 IC=+0.175 PNL=-1019.40€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.1 con n=132 PNL=+75.67€
  - _Datos_: n=132 IC=+0.194 PNL=+75.67€
