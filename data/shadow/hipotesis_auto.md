# Hipótesis automáticas — 2026-10-09 07:19 UTC
_Generado por shadow_postmortem.py sobre 819038 resoluciones (PNL=+102130.88€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.233 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.121)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.198 (n=233)

  - _Acción_: Kelly boost +0.99€ cuando `n_total_lado` > 69.0 (IC base=+0.121)

- **PATRÓN** `banda_hit_calibrado` > `0.6165` → IC=+0.235 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6165 (IC base=+0.121)

- **PATRÓN** `banda_z` > `8.922` → IC=+0.188 (n=229)

  - _Acción_: Kelly boost +0.94€ cuando `banda_z` > 8.922 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=732)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.121)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.229 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8118` → IC=+0.262 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8118 (IC base=+0.125)

- **PATRÓN** `banda_z` > `9.53` → IC=+0.182 (n=187)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 9.53 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=634)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.125)

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

- **FILTRO** `py_entrada` > `0.5` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=97)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=110)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.125)

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

- **PATRÓN** `libro_liquidez` > `1207.4096` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1207.4096 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.000)

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
- **FILTRO** `restante_s_al_confirmar` < `144.17` → IC=-0.208 (n=8893)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.17
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=26684)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.93` → IC=-0.266 (n=1105)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.93
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3316)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `123.47` → IC=-0.304 (n=1024)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 123.47
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3073)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `164.85` → IC=-0.229 (n=2274)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 164.85
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=6825)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.21` → IC=-0.301 (n=1736)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.21
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=5210)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.207 (n=18508)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=3992)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `9525.0954` → IC=+0.182 (n=1777)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9525.0954 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.134 (n=15318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=18706)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=14169)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=6554)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7491.8455` → IC=+0.166 (n=2521)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7491.8455 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2361)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `16120.1033` → IC=+0.210 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16120.1033 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=1694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=1881)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=2413)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `16052.1822` → IC=+0.205 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16052.1822 (IC base=+0.192)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.162 (n=412)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.61 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `4988.4492` → IC=+0.126 (n=228)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 4988.4492 (IC base=+0.088)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.089)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=986)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.089)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.365 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.228 (n=1603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.361 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.141 (n=769)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.252 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=990)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2155.3043` → IC=+0.152 (n=389)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2155.3043 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=857)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.409 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=1248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=823)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.376 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.223 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=68)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=15298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=13003)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.230 (n=6448)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=3590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=3397)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.179 (n=3462)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=1576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.229 (n=1572)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.315 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.226)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=3522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=3367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.190 (n=1952)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=3082)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.332 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.242)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=3446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2214)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.190 (n=2633)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.71 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.426 (n=609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `2788.1377` → IC=+0.432 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2788.1377 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.445 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `17937.2119` → IC=+0.435 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 17937.2119 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.441 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.435 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `3408.2761` → IC=+0.437 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3408.2761 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.405)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.408 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.405)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.405)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.410 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.405)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `6345.2155` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 6345.2155
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=19716)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=20026)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=9270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=6320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.199 (n=8733)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=4107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.282 (n=2893)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.180 (n=8287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=6304)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=8356)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=4142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=2838)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=7574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.203 (n=6058)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=2976)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=3283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.194 (n=2857)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 5.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=3466)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=7034)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.125 (n=6528)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.2 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.137 (n=6859)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=8680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.45` → IC=+0.137 (n=6501)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.45 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=3494)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.126 (n=3230)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=3452)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=4298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.05` → IC=+0.146 (n=3229)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.05 (IC base=+0.122)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=3540)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.131 (n=3750)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.135 (n=3278)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.291 (n=1428)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1560.0097` → IC=+0.294 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1560.0097 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.340 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `5357.3376` → IC=+0.307 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5357.3376 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1451.8749` → IC=+0.305 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1451.8749 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.350)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.375 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.350)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.350)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.354 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.350)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.350)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.443 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=304)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.449 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `5263.5488` → IC=+0.442 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5263.5488 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.462 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `2133.31` → IC=+0.459 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2133.31 (IC base=+0.443)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=78)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=78)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.297 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `983.8593` → IC=+0.277 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 983.8593 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.3712` → IC=+0.136 (n=9657)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3712 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.243 (n=3658)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2202` → IC=+0.253 (n=2537)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2202 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.427` → IC=+0.194 (n=2854)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 8.427 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.853` → IC=+0.249 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.853 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.253 (n=3084)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.3009` → IC=+0.229 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3009 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.323` → IC=+0.218 (n=3494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.323 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.5652` → IC=+0.141 (n=13430)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5652 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.5827` → IC=+0.203 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5827 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.151` → IC=+0.183 (n=4652)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.151 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` < `1.1916` → IC=+0.182 (n=4990)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1916 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.0523` → IC=+0.181 (n=2263)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0523 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.228 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` > `1.448` → IC=+0.203 (n=8553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.448 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.217 (n=8364)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.072)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.218 (n=815)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.191 (n=813)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0081 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3504` → IC=+0.188 (n=2438)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3504 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=1183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.184 (n=1635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.782` → IC=+0.295 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.782 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.237 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.183 (n=2310)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2531)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.233 (n=1322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.242 (n=1774)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.267 (n=662)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.062` → IC=+0.277 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.062 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.248 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.39` → IC=+0.236 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.39 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.234 (n=1748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2861` → IC=+0.256 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2861 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.6147` → IC=+0.255 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6147 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.233 (n=862)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1081` → IC=+0.252 (n=860)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1081 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=2057)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.3188` → IC=+0.233 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3188 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1964` → IC=+0.221 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1964 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.572` → IC=+0.259 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.572 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `1.244` → IC=+0.220 (n=1955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.244 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.6209` → IC=+0.223 (n=1955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6209 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.246 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7608` → IC=+0.220 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7608 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.4076` → IC=+0.239 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4076 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.179 (n=653)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0026 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.168 (n=651)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7242` → IC=+0.178 (n=1950)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7242 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.157 (n=1796)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1327 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.229` → IC=+0.155 (n=311)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.229 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.282` → IC=+0.143 (n=1787)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.282 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.186` → IC=+0.146 (n=1950)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.186 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6232` → IC=+0.138 (n=1950)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6232 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.165 (n=709)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.449` → IC=+0.148 (n=1835)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.449 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.145 (n=1225)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.176 (n=775)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 229.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.201 (n=2474)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=2598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=2213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.414` → IC=+0.259 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.414 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.194 (n=2173)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3464` → IC=+0.191 (n=325)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.3464 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.1499` → IC=+0.200 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1499 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2948)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.226 (n=1463)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.1328` → IC=+0.231 (n=731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1328 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=1024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.0654` → IC=+0.238 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0654 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.255 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3448` → IC=+0.254 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3448 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.7149` → IC=+0.220 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7149 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7161` → IC=+0.227 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7161 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.216 (n=2019)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.214)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.144 (n=133)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2951)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.149 (n=462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0036 (IC base=+0.044)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.220 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` < `0.188` → IC=+0.324 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.188 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.981` → IC=+0.179 (n=969)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 4.981 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8536` → IC=+0.327 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8536 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.346 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2251 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.339 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.354 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.322 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.322 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.0986` → IC=+0.167 (n=772)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.0986 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.3038` → IC=+0.191 (n=335)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.3038 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.8486` → IC=+0.151 (n=832)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8486 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.204 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5239` → IC=+0.165 (n=1064)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5239 (IC base=+0.031)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.179 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=457)

- **FILTRO** `ibs_20min` < `0.3056` → IC=-0.191 (n=134)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3056
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=402)

- **FILTRO** `ibs_20min` > `0.2262` → IC=-0.127 (n=2985)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2262
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=1473)

- **FILTRO** `sigma_ewma_delta_pct` > `8.753` → IC=-0.219 (n=457)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.753
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=4001)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.8 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `1.7756` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.7756 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.133 (n=186)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.57` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.57 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `1.0233` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0233 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.0752` → IC=+0.285 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0752 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.5152` → IC=+0.280 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5152 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.272 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.2262` → IC=+0.142 (n=1473)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.2262 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.1878` → IC=+0.277 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1878 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.7007` → IC=+0.283 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7007 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.298 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.371` → IC=+0.295 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.371 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6416` → IC=-0.184 (n=776)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6416
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=2329)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.207 (n=879)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2226)

- **FILTRO** `ibs_20min` > `0.763` → IC=-0.207 (n=1158)

  - _Acción_: SKIP cuando `ibs_20min` > 0.763
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=3476)

- **PATRÓN** `dist_vwap_pct` > `0.4652` → IC=+0.317 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4652 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` < `0.279` → IC=+0.312 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.279 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` < `0.9898` → IC=+0.297 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9898 (IC base=-0.073)

- **PATRÓN** `volumen_regimen` > `0.6389` → IC=+0.313 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6389 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.301 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.301 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.4802` → IC=+0.299 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4802 (IC base=-0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.1721` → IC=+0.306 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1721 (IC base=-0.073)

- **PATRÓN** `dist_vwap_pct` > `0.8232` → IC=+0.286 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8232 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` > `1.0756` → IC=+0.276 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0756 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.1035` → IC=+0.272 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1035 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `2.1684` → IC=+0.256 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1684 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.4259` → IC=+0.259 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4259 (IC base=-0.011)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.201 (n=4832)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4663` → IC=+0.186 (n=12928)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4663 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.6744` → IC=+0.285 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6744 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.689` → IC=+0.154 (n=6511)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.689 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.1726` → IC=+0.249 (n=5299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1726 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.256 (n=4735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` < `0.0795` → IC=+0.245 (n=7841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0795 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.259 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4634` → IC=+0.247 (n=2846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4634 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6278` → IC=+0.256 (n=2846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6278 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.279 (n=8095)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.166 (n=4659)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0089 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.5412` → IC=+0.160 (n=12296)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.5412 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.1972` → IC=+0.261 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1972 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.307 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `1.5859` → IC=+0.282 (n=2634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5859 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.285 (n=5886)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.076)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2583` → IC=-0.170 (n=1010)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2583
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=3030)

- **FILTRO** `ibs_20min` > `0.7546` → IC=-0.180 (n=833)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7546
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=2500)

- **FILTRO** `sigma_ewma_delta_pct` > `4.621` → IC=-0.182 (n=733)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.621
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=2600)

- **PATRÓN** `ibs_20min` > `0.9093` → IC=+0.278 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9093 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.325` → IC=+0.202 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.325 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2276` → IC=+0.284 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2276 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.219 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `2.2071` → IC=+0.240 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2071 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.239 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.1591` → IC=+0.151 (n=834)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1591 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.416 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.6091` → IC=+0.406 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6091 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.5396` → IC=+0.406 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5396 (IC base=-0.025)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.403 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.025)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8632` → IC=+0.151 (n=976)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.8632 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1204` → IC=+0.194 (n=720)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1204 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.197` → IC=+0.170 (n=1384)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.197 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.6787` → IC=+0.180 (n=1237)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6787 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.213 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.202 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.4169` → IC=+0.189 (n=454)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4169 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `225.0` → IC=+0.231 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 225.0 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.1608` → IC=+0.230 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1608 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.234 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0722` → IC=+0.227 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0722 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.273` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.273 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5536` → IC=+0.235 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5536 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1745` → IC=+0.236 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1745 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.272 (n=2173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.259 (n=2176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.254 (n=1938)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.805` → IC=+0.283 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.805 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.1316` → IC=+0.266 (n=1974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1316 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `1.6035` → IC=+0.257 (n=2082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6035 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.303 (n=1830)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.1838` → IC=+0.307 (n=806)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1838 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.322 (n=610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.3651` → IC=+0.293 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3651 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.672` → IC=+0.302 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.672 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` < `0.1942` → IC=+0.285 (n=1788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1942 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.3376` → IC=+0.297 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3376 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `1.7078` → IC=+0.304 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7078 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `2.6195` → IC=+0.292 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6195 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.288 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.288)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7611` → IC=-0.180 (n=839)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7611
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=2518)

- **PATRÓN** `ibs_20min` > `0.8024` → IC=+0.147 (n=1054)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.8024 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `1.0082` → IC=+0.234 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0082 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.1683` → IC=+0.227 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1683 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.226 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4092` → IC=+0.255 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4092 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.289 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1265` → IC=+0.221 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1265 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` < `1.1978` → IC=+0.226 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1978 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.284 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.845` → IC=+0.265 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.845 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `134.0` → IC=+0.254 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 134.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7647` → IC=-0.190 (n=1541)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7647
  - _Potencial_: sin este filtro IC_bueno=+0.290 (n=1541)

- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.247 (n=752)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=2349)

- **FILTRO** `sigma_ewma_delta_pct` > `8.642` → IC=-0.230 (n=354)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.642
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=2747)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.290 (n=1541)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7647 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.2116` → IC=+0.323 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2116 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.692` → IC=+0.169 (n=484)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.692 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8515` → IC=+0.318 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8515 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6339` → IC=+0.308 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6339 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.306 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.336 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.327 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.335 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.5614` → IC=+0.136 (n=2049)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5614 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.2041` → IC=+0.241 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2041 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.260 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.234 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.256 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.253 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4232 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.266 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.025)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.336 (n=1531)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.308 (n=810)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.325 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2135` → IC=+0.319 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2135 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.314 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.02` → IC=+0.293 (n=1939)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.02 (IC base=+0.292)

- **PATRÓN** `volumen_regimen` > `0.6267` → IC=+0.303 (n=1710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6267 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.341 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `1.4314` → IC=+0.304 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4314 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `2992.5648` → IC=+0.313 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2992.5648 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.329 (n=1435)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.322 (n=1213)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.1867` → IC=+0.291 (n=799)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1867 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.296 (n=1725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.3675` → IC=+0.317 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3675 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.3099` → IC=+0.294 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3099 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.484` → IC=+0.303 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.484 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.033` → IC=+0.292 (n=2168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.033 (IC base=+0.291)

- **PATRÓN** `volumen_regimen` < `0.8901` → IC=+0.291 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8901 (IC base=+0.291)

- **PATRÓN** `volumen_regimen` > `1.2272` → IC=+0.321 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2272 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.340 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `2.4531` → IC=+0.291 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4531 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `2.1367` → IC=+0.291 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1367 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2865.9542` → IC=+0.292 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2865.9542 (IC base=+0.291)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.185 (n=3574)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.213 (n=3564)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3518` → IC=+0.186 (n=9407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3518 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=11145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.5636` → IC=+0.228 (n=10690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5636 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.1715` → IC=+0.201 (n=4479)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1715 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.483` → IC=+0.251 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.483 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.1983` → IC=+0.168 (n=7105)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1983 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` > `0.6282` → IC=+0.162 (n=7105)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6282 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.193 (n=1577)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.175 (n=4542)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.5936` → IC=+0.182 (n=3441)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.5936 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2520.254` → IC=+0.177 (n=7126)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2520.254 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.191 (n=9603)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 103.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.189 (n=6844)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0066 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.223 (n=3421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=3860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.4884` → IC=+0.233 (n=10263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4884 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.271` → IC=+0.199 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.271 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1803` → IC=+0.166 (n=7348)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1803 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.223 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6103` → IC=+0.180 (n=3182)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.6103 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.187 (n=9225)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 106.0 (IC base=+0.177)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.233 (n=604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.206 (n=601)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.3411` → IC=+0.220 (n=1795)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3411 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=1202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9174` → IC=+0.286 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9174 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.332` → IC=+0.331 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.332 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.258 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.198 (n=1685)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.248 (n=1217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.245 (n=1386)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1024` → IC=+0.299 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1024 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.243 (n=692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3517` → IC=+0.258 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3517 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.223` → IC=+0.245 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.223 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0996` → IC=+0.239 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0996 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.275 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4252` → IC=+0.247 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4252 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.631` → IC=+0.245 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.631 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=1524)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.221 (n=539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.185 (n=1077)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=1705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.3744` → IC=+0.224 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3744 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2003` → IC=+0.212 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2003 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.230 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.168 (n=711)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6892 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2817` → IC=+0.189 (n=255)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2817 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.182 (n=526)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.4724` → IC=+0.157 (n=525)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4724 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.169 (n=681)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 233.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1702)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2334` → IC=+0.176 (n=1497)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2334 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6004` → IC=+0.201 (n=1702)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6004 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.75` → IC=+0.206 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.75 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.164 (n=1702)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2025 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.2284` → IC=+0.146 (n=1757)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.2284 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1593` → IC=+0.146 (n=518)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1593 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4911` → IC=+0.153 (n=1585)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4911 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7682` → IC=+0.144 (n=1056)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.7682 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.169 (n=505)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 207.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.233 (n=598)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.4087` → IC=+0.218 (n=1575)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4087 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.557` → IC=+0.281 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.557 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.207 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1276` → IC=+0.207 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1276 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.7649` → IC=+0.210 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7649 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.6772` → IC=+0.213 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6772 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.246 (n=1349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.230)

- **PATRÓN** `drift_60min` |x|≤ `0.1453` → IC=+0.268 (n=675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1453 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.277 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.252 (n=1533)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.649` → IC=+0.262 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.649 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.266 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.7067` → IC=+0.249 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7067 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.7152` → IC=+0.235 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7152 (IC base=+0.230)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.232 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.230)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.179 (n=1511)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0064 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.199 (n=573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1788)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.3279` → IC=+0.206 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3279 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1399` → IC=+0.189 (n=1080)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1399 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.202 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.163 (n=1145)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8546 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1013` → IC=+0.170 (n=716)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1013 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.4305` → IC=+0.161 (n=561)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4305 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5072` → IC=+0.155 (n=561)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5072 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5139.067` → IC=+0.198 (n=1145)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 5139.067 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.153 (n=1658)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 149.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.159 (n=1810)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0071 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3868` → IC=+0.149 (n=1809)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3868 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6725` → IC=+0.186 (n=1809)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6725 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.842` → IC=+0.162 (n=625)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.842 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.162 (n=1206)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.856 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.190 (n=275)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.81` → IC=+0.137 (n=1120)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.81 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4186` → IC=+0.131 (n=1679)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4186 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `4554.3674` → IC=+0.166 (n=1206)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4554.3674 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.127 (n=1623)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 148.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.167 (n=886)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0099 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1485` → IC=+0.132 (n=860)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.1485 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=1996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.215 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.2013` → IC=+0.187 (n=1169)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.2013 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.935` → IC=+0.261 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.935 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.145 (n=1954)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1954 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.134 (n=1788)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.5464` → IC=+0.146 (n=832)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.5464 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.48` → IC=+0.133 (n=630)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.48 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=2050)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2390.1268` → IC=+0.193 (n=1302)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2390.1268 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.163 (n=589)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 21.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.144 (n=1733)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0091 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1059` → IC=+0.178 (n=657)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1059 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=1988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.220 (n=1969)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.335` → IC=+0.131 (n=594)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 5.335 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.57` → IC=+0.125 (n=1737)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 2.57 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1785` → IC=+0.136 (n=1969)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1785 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2754` → IC=+0.164 (n=248)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2754 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4467` → IC=+0.139 (n=605)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4467 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.8124` → IC=+0.130 (n=1208)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.8124 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2178.1059` → IC=+0.174 (n=1313)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2178.1059 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.135 (n=1760)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 51.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.234 (n=1821)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1767` → IC=+0.226 (n=802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1767 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=1232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.249 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.216 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.2837` → IC=+0.212 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2837 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.611` → IC=+0.244 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.611 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.1839` → IC=+0.216 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1839 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.220 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.267 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.216 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.8057` → IC=+0.225 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8057 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2665.456` → IC=+0.220 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2665.456 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.230 (n=823)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.222 (n=848)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.246 (n=624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0205` → IC=+0.290 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0205 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `1.1734` → IC=+0.232 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1734 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.402` → IC=+0.246 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.402 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6385` → IC=+0.230 (n=1869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6385 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.280 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `2.1966` → IC=+0.213 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1966 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.220 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.220)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.192 (n=1232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0041 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3355` → IC=+0.179 (n=2460)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3355 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.205 (n=1389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.3274` → IC=+0.197 (n=2795)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3274 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.784` → IC=+0.183 (n=424)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.784 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.743` → IC=+0.194 (n=1192)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.743 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8658` → IC=+0.187 (n=1677)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8658 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `1.2005` → IC=+0.179 (n=838)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.2005 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1024` → IC=+0.177 (n=1001)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1024 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4361` → IC=+0.188 (n=905)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4361 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.5109` → IC=+0.172 (n=905)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5109 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=2592)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.187 (n=2576)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 151.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.164 (n=963)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0036 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=2713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.0769` → IC=+0.195 (n=960)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.0769 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2192` → IC=+0.120 (n=2621)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2192 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.124 (n=1102)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4331` → IC=+0.147 (n=932)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4331 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `5154.5272` → IC=+0.141 (n=1919)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 5154.5272 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.134 (n=935)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 21.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.200 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1013` → IC=+0.202 (n=357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1013 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.6264` → IC=+0.208 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6264 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.176 (n=251)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.137` → IC=+0.173 (n=341)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.137 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.8799` → IC=+0.175 (n=540)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8799 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.161 (n=317)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.2101` → IC=+0.162 (n=697)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.2101 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.4164` → IC=+0.152 (n=792)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4164 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `14721.2123` → IC=+0.162 (n=540)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 14721.2123 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.206 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 150.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.206 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.2658` → IC=+0.162 (n=833)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2658 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.155 (n=851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.146 (n=957)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6119` → IC=+0.184 (n=833)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6119 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.494` → IC=+0.149 (n=998)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.494 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2002` → IC=+0.149 (n=947)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2002 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.6986` → IC=+0.158 (n=846)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6986 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.193 (n=252)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.1165` → IC=+0.160 (n=824)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1165 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=1227)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `289.0` → IC=+0.159 (n=805)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 289.0 (IC base=+0.146)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.235 (n=594)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.2084` → IC=+0.213 (n=594)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2084 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=936)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.3404` → IC=+0.235 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3404 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.3604` → IC=+0.204 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3604 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.2092` → IC=+0.205 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2092 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.007` → IC=+0.218 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.007 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.8389` → IC=+0.203 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8389 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.1824` → IC=+0.219 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1824 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.16` → IC=+0.227 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.16 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.236 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.4481` → IC=+0.215 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4481 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.163 (n=378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0038 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.0876` → IC=+0.164 (n=287)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.0876 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.6876` → IC=+0.155 (n=378)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6876 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.223` → IC=+0.141 (n=140)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.223 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `7692.4254` → IC=+0.141 (n=572)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7692.4254 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.129 (n=370)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.107)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.159 (n=417)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0072 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.171 (n=624)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0051 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.193 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.9607` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9607 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.329` → IC=+0.216 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.329 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.0652` → IC=+0.176 (n=550)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0652 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.6526` → IC=+0.163 (n=624)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6526 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1691` → IC=+0.172 (n=175)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1691 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4583` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4583 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.1945` → IC=+0.173 (n=273)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1945 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=664)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3082.2108` → IC=+0.195 (n=208)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3082.2108 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.4667` → IC=+0.148 (n=532)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.4667 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.5684` → IC=+0.128 (n=253)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5684 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `2425.9013` → IC=+0.130 (n=403)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2425.9013 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.148 (n=248)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 15.0 (IC base=+0.058)

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

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.162 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0119 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.133 (n=213)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.025` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.025 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.128 (n=213)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6515 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.8124` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.8124 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 17.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.179 (n=4634)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.216 (n=4629)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=14500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.4544` → IC=+0.225 (n=13878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4544 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1655` → IC=+0.188 (n=5083)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1655 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.443` → IC=+0.247 (n=3408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.443 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.2303` → IC=+0.167 (n=9304)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2303 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.198 (n=1874)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.5941` → IC=+0.195 (n=4481)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.5941 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2481.7994` → IC=+0.182 (n=9252)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2481.7994 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.205 (n=11015)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.196 (n=5535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1473` → IC=+0.196 (n=5518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1473 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=4708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.4545` → IC=+0.251 (n=11046)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4545 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.07` → IC=+0.211 (n=1760)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.07 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.714` → IC=+0.187 (n=12098)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.714 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.164 (n=3732)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7049 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.251 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6065` → IC=+0.196 (n=3918)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6065 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.209 (n=7715)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.250 (n=766)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.228 (n=769)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3555` → IC=+0.213 (n=2295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3555 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=1111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=1546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.776` → IC=+0.346 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.776 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2734` → IC=+0.270 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2734 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.5787` → IC=+0.227 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5787 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.265 (n=1277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.261 (n=1916)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1243` → IC=+0.273 (n=843)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1243 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.265 (n=1734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3617` → IC=+0.284 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3617 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.478` → IC=+0.264 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.478 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.286 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6294` → IC=+0.280 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6294 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=2109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.201 (n=747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1783` → IC=+0.165 (n=1492)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1783 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.2728` → IC=+0.207 (n=2237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2728 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1319` → IC=+0.187 (n=1207)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1319 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.715` → IC=+0.168 (n=375)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.715 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.2` → IC=+0.153 (n=2046)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.2 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6278` → IC=+0.175 (n=746)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6278 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.27` → IC=+0.189 (n=319)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.27 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1465` → IC=+0.159 (n=1918)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1465 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.525` → IC=+0.153 (n=1948)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.525 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `273.0` → IC=+0.183 (n=935)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 273.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1852)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2565` → IC=+0.164 (n=1630)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2565 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6888` → IC=+0.197 (n=1852)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6888 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.135` → IC=+0.167 (n=1718)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.135 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.496` → IC=+0.164 (n=313)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.496 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.158 (n=1853)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1817 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1535` → IC=+0.199 (n=493)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1535 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.154 (n=1750)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.160 (n=1167)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `256.0` → IC=+0.147 (n=554)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 256.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.250 (n=761)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=2046)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.306 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.522` → IC=+0.307 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.522 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.2051` → IC=+0.226 (n=2309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2051 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.7625` → IC=+0.228 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7625 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2717)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.243 (n=1432)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.1846` → IC=+0.257 (n=944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1846 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.237 (n=1006)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0152` → IC=+0.303 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0152 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.949` → IC=+0.290 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.949 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3403` → IC=+0.301 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3403 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.705` → IC=+0.242 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.705 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.1254` → IC=+0.243 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1254 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.257 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.236)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=1046)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.3321` → IC=+0.153 (n=2087)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3321 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=2473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.266` → IC=+0.192 (n=2372)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.266 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.5525` → IC=+0.165 (n=606)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5525 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.181` → IC=+0.155 (n=968)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.181 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8719` → IC=+0.164 (n=1582)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8719 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.174 (n=422)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.165 (n=1017)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5223 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.1716` → IC=+0.153 (n=1048)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1716 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `7338.742` → IC=+0.237 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7338.742 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.180 (n=776)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 70.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.196 (n=640)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0033 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.3454` → IC=+0.145 (n=1689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3454 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.735` → IC=+0.188 (n=1919)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.735 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.285` → IC=+0.178 (n=293)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.285 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6236` → IC=+0.149 (n=640)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6236 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.234 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.2464` → IC=+0.137 (n=1620)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2464 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4408` → IC=+0.145 (n=1841)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4408 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5620.3886` → IC=+0.198 (n=870)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 5620.3886 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.135 (n=1842)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 164.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.137 (n=2393)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0056 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4521` → IC=+0.203 (n=2392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4521 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `1.0324` → IC=+0.209 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0324 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.567` → IC=+0.243 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.567 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.2292` → IC=+0.142 (n=2392)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2292 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.0973` → IC=+0.132 (n=2238)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.0973 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8368` → IC=+0.129 (n=1553)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8368 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.1879` → IC=+0.138 (n=1056)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.1879 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=2446)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2932.5833` → IC=+0.256 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2932.5833 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.150 (n=770)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 27.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.174 (n=765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0056 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1316` → IC=+0.167 (n=764)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1316 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=2359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.235 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.2183` → IC=+0.141 (n=1932)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2183 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.231` → IC=+0.131 (n=315)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 9.231 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.446` → IC=+0.136 (n=2211)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.446 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.7133` → IC=+0.156 (n=1008)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.7133 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2225` → IC=+0.184 (n=372)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2225 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4341` → IC=+0.156 (n=708)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4341 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2831.6215` → IC=+0.206 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2831.6215 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.143 (n=1848)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 49.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.237 (n=2304)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=2407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.224 (n=1666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.267 (n=2068)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.2063` → IC=+0.236 (n=1285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2063 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.791` → IC=+0.265 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.791 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2336` → IC=+0.226 (n=2304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2336 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.224 (n=2304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.242 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.5119` → IC=+0.246 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5119 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=2089)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2672.4108` → IC=+0.233 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2672.4108 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.221 (n=808)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.234 (n=1098)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.231 (n=1718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.416` → IC=+0.267 (n=2130)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.416 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.95` → IC=+0.255 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.95 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.248 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.288 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.432` → IC=+0.220 (n=2229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.432 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2660.1876` → IC=+0.218 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2660.1876 (IC base=+0.218)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=4126)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.230 (n=1402)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.4987` → IC=+0.202 (n=4198)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4987 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=1550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=1913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.9407` → IC=+0.242 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9407 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1713` → IC=+0.196 (n=1540)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1713 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.2454` → IC=+0.194 (n=2569)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2454 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.238` → IC=+0.215 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.238 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.703` → IC=+0.205 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.703 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `1.2489` → IC=+0.195 (n=986)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.2489 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.1682` → IC=+0.217 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1682 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.202 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.8508` → IC=+0.196 (n=2758)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8508 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=3165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `3869.3127` → IC=+0.204 (n=2799)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3869.3127 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.222 (n=1036)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.4856` → IC=+0.189 (n=3106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.4856 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=1076)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=1417)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.1758` → IC=+0.195 (n=1367)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1758 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.6484` → IC=+0.181 (n=534)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6484 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.169` → IC=+0.180 (n=3105)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 6.169 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.1012` → IC=+0.182 (n=2564)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1012 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.177 (n=2832)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.178 (n=1415)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.5352` → IC=+0.178 (n=1348)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.5352 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `1.8181` → IC=+0.181 (n=2041)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8181 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=4126)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.184 (n=1342)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 36.0 (IC base=+0.173)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.239 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0834` → IC=+0.260 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0834 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.5153` → IC=+0.236 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5153 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.7702` → IC=+0.216 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7702 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.179` → IC=+0.216 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.179 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.039` → IC=+0.236 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.039 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.215 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.222 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.8398` → IC=+0.228 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8398 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4501` → IC=+0.232 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4501 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `12545.7532` → IC=+0.237 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12545.7532 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.227 (n=471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1125` → IC=+0.181 (n=471)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1125 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.200 (n=358)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.1518` → IC=+0.181 (n=471)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1518 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.155 (n=485)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.6078 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6676` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6676 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.2124` → IC=+0.152 (n=1086)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2124 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.168 (n=1054)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8802` → IC=+0.189 (n=714)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8802 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.2713` → IC=+0.152 (n=1260)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.2713 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.184 (n=223)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.5375` → IC=+0.156 (n=1066)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5375 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.169 (n=711)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `11538.1781` → IC=+0.164 (n=1070)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 11538.1781 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `699.0` → IC=+0.163 (n=1024)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 699.0 (IC base=+0.150)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.200 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.186 (n=313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0098 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.581` → IC=+0.179 (n=689)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.581 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.494` → IC=+0.222 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.494 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2079` → IC=+0.222 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2079 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.6744` → IC=+0.172 (n=230)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.6744 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `3.3613` → IC=+0.184 (n=229)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.3613 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.241 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.295 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.237)

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

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.211 (n=1112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.206 (n=1264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5224` → IC=+0.212 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5224 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.8799` → IC=+0.204 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8799 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.148` → IC=+0.205 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.148 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.207 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2383` → IC=+0.204 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2383 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.200 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.209 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.216 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.230 (n=339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.196 (n=1012)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.184 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 10.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.7538` → IC=+0.179 (n=1012)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.7538 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.0863` → IC=+0.174 (n=1011)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.0863 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.6347` → IC=+0.194 (n=194)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6347 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.654` → IC=+0.177 (n=1035)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 6.654 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.101` → IC=+0.187 (n=890)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.101 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.7214` → IC=+0.176 (n=905)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.7214 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` < `0.1511` → IC=+0.174 (n=1045)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.1511 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.195 (n=428)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `2.1746` → IC=+0.186 (n=871)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.1746 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `7393.6792` → IC=+0.191 (n=1011)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7393.6792 (IC base=+0.173)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.215 (n=363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3011` → IC=+0.176 (n=362)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3011 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.194 (n=553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 3.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.245 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1914` → IC=+0.205 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1914 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.559` → IC=+0.215 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.559 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.694` → IC=+0.205 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.694 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.216 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5465` → IC=+0.213 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5465 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.180 (n=649)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3406.9619` → IC=+0.220 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3406.9619 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.185 (n=531)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 58.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.213 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.206 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.372` → IC=+0.236 (n=267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.372 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.217 (n=270)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.1837` → IC=+0.242 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1837 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.772` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.772 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.035` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.035 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.985` → IC=+0.191 (n=347)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.985 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.756` → IC=+0.202 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.756 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` > `0.6799` → IC=+0.187 (n=400)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6799 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.223 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.6271` → IC=+0.194 (n=171)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.6271 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.202 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `3873.4371` → IC=+0.199 (n=267)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3873.4371 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.223 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.186)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.153 (n=597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0038 (IC base=+0.073)

- **PATRÓN** `ibs_20min` > `0.4221` → IC=+0.148 (n=1265)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.4221 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1458` → IC=+0.138 (n=667)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1458 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.484` → IC=+0.174 (n=286)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.484 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2771` → IC=+0.169 (n=176)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2771 (IC base=+0.073)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.121 (n=428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0045 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.1923` → IC=+0.260 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1923 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` < `0.089` → IC=+0.134 (n=561)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.089 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.1463` → IC=+0.194 (n=142)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1463 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4646` → IC=+0.138 (n=222)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4646 (IC base=+0.055)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.140 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0058 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.140 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 18.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.3879` → IC=+0.171 (n=432)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3879 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.159 (n=221)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.091)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.123 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0046 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.0544` → IC=+0.290 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0544 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.111` → IC=+0.137 (n=276)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.111 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.245` → IC=+0.139 (n=258)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 7.245 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.164 (n=105)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.135 (n=242)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.079)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6934` → IC=-0.191 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6934
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=162)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.142 (n=297)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0046 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.124 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.6816` → IC=+0.204 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6816 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1239` → IC=+0.174 (n=219)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1239 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.74` → IC=+0.250 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.74 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `1188.5183` → IC=+0.139 (n=366)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1188.5183 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.1031` → IC=+0.281 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1031 (IC base=+0.004)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0097` → IC=-0.207 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0097
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=170)

- **FILTRO** `ibs_20min` > `0.15` → IC=-0.271 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.266 (n=139)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.167 (n=280)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.76 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.721` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.721 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2436` → IC=+0.182 (n=83)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2436 (IC base=+0.039)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.180 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0081 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.15` → IC=+0.266 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.15 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.196` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.196 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.936` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.936 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.8193` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8193 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `0.9765` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.9765 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.1476` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1476 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.18` → IC=+0.186 (n=103)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.18 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.5569` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5569 (IC base=+0.070)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.210 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `775.9989` → IC=+0.179 (n=82)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 775.9989 (IC base=+0.070)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1826` → IC=-0.306 (n=65)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1826
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=197)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=249)

- **FILTRO** `volumen_regimen` < `0.7468` → IC=-0.338 (n=66)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=198)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.381 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=172)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.300 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=161)

- **FILTRO** `dist_vwap_pct` > `0.3328` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3328
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=196)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=199)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=124)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=66)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.233 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=59)

- **FILTRO** `volumen_spike_ratio` > `3.7991` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.7991
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=49)

- **FILTRO** `drift_60min` |x|> `0.1024` → IC=-0.300 (n=48)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1024
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=50)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=76)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.375 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=66)

- **FILTRO** `ibs_20min` < `0.6037` → IC=-0.435 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6037
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=59)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.354 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=45)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=35)

- **PATRÓN** `ibs_20min` > `0.9508` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.9508 (IC base=-0.156)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `volumen_spike_ratio` < `1.5614` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5614
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=48)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=63)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.168 (n=194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0057 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.127 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6645` → IC=+0.137 (n=425)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.6645 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.4857` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4857 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6589` → IC=+0.139 (n=142)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6589 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` < `0.166` → IC=+0.123 (n=324)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.166 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `2.5067` → IC=+0.128 (n=323)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.5067 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.1644` → IC=+0.172 (n=416)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1644 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.376` → IC=+0.203 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.376 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `2835.5539` → IC=+0.156 (n=315)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2835.5539 (IC base=+0.077)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6528` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6528
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=130)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.226 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.1414` → IC=+0.210 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1414 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.36` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.36 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.879` → IC=+0.171 (n=168)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 4.879 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.6912` → IC=+0.181 (n=189)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6912 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.1891` → IC=+0.179 (n=182)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.1891 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.2815` → IC=+0.177 (n=159)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.2815 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.170 (n=180)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.151)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1492` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1492
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=125)

- **PATRÓN** `volumen_spike_ratio` < `1.7926` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7926 (IC base=+0.062)

- **PATRÓN** `libro_liquidez` > `1535.3678` → IC=+0.135 (n=143)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1535.3678 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.2345` → IC=+0.150 (n=155)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2345 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.629` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.629 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.218` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.218 (IC base=+0.059)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1679` → IC=-0.207 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1679
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=58)

- **FILTRO** `dist_vwap_pct` > `0.2725` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2725
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=92)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.288 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.264 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.250 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.6388` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6388 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` < `0.1413` → IC=+0.244 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1413 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.349` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.349 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.2519` → IC=+0.291 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2519 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.1062` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1062 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.239 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.069)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.283)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.283)

- **PATRÓN** `drift_15min` |x|≤ `0.9257` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.9257 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.351 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.283)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.212)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.212)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.263 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.212)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.212)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.283)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.283)

- **PATRÓN** `drift_15min` |x|≤ `0.9257` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.9257 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.351 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.283)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.212)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.212)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `1.251` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.251 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.263 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.212)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.212)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=1034)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=1034)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=159)

- **FILTRO** `libro_liquidez` < `2669.5667` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `libro_liquidez` < 2669.5667
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=132)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=56)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

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

- **FILTRO** `libro_liquidez` < `2892.3985` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2892.3985
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2913)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=98)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=55)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=87)

- **FILTRO** `ballena_activa_n` > `98.0` → IC=-0.208 (n=63)

  - _Acción_: SKIP cuando `ballena_activa_n` > 98.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=22)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=116)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.130 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 13.0 (IC base=+0.041)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=188)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.039)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1077)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1031)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9855` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9855
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `142.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 142.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=678)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=360)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=341)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.159 (n=130)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.495 (IC base=+0.024)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=784)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=784)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=618)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=606)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=606)

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

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=145)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=151)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=175)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=242)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=178)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=309)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=309)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=216)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.145 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=157)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=1493)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1567)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` > `0.45` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `restante_min` < `3.89` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.140 (n=195)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=102)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.156 (n=59)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=310)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.46 (IC base=+0.042)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.122 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=52)

- **FILTRO** `restante_min` < `12.46` → IC=-0.133 (n=96)

  - _Acción_: SKIP cuando `restante_min` < 12.46
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **FILTRO** `lag_apertura_s` > `152.45` → IC=-0.133 (n=96)

  - _Acción_: SKIP cuando `lag_apertura_s` > 152.45
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.128 (n=127)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=73)

- **FILTRO** `lag_apertura_s` > `76.6` → IC=-0.144 (n=99)

  - _Acción_: SKIP cuando `lag_apertura_s` > 76.6
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=101)

- **PATRÓN** `py_entrada` < `0.54` → IC=+0.128 (n=41)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.54 (IC base=+0.053)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.144 (n=203)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=70)

- **FILTRO** `profundidad_ratio` < `37.6` → IC=-0.200 (n=68)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.6
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=205)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.240 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=211)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.125 (n=222)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=127)

- **FILTRO** `restante_min` < `3.34` → IC=-0.192 (n=115)

  - _Acción_: SKIP cuando `restante_min` < 3.34
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=234)

- **FILTRO** `lag_apertura_s` > `98.43` → IC=-0.200 (n=118)

  - _Acción_: SKIP cuando `lag_apertura_s` > 98.43
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=231)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.132 (n=55)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=210)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=-0.002)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=207)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=109)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.159 (n=174)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=221)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.162 (n=4980)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=14967)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.166 (n=5151)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=15482)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.189 (n=888)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=2664)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.153 (n=863)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=2836)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.172 (n=714)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2262)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.174 (n=892)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2714)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=928)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=2814)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.159 (n=855)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=2706)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2568)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=3308)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `libro_liquidez` < `16920.0467` → IC=-0.163 (n=176)

  - _Acción_: SKIP cuando `libro_liquidez` < 16920.0467
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=359)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=313)

- **FILTRO** `libro_liquidez` < `2884.1832` → IC=-0.193 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 2884.1832
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=300)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `2028.3639` → IC=-0.163 (n=339)

  - _Acción_: SKIP cuando `libro_liquidez` < 2028.3639
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=690)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=232)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.037)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=13916)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=30831)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=10611)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=34136)

- **FILTRO** `ibs_7min` < `0.2533` → IC=-0.233 (n=11186)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2533
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=33561)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=14994)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=29753)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.235 (n=13696)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=43277)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.178 (n=14231)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=42742)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.144 (n=2254)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=5363)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=1827)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=5790)

- **FILTRO** `ibs_7min` < `0.708` → IC=-0.250 (n=2512)

  - _Acción_: SKIP cuando `ibs_7min` < 0.708
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=5105)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.191 (n=1591)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6026)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.269 (n=2405)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=7503)

- **FILTRO** `ibs_7min` > `0.7778` → IC=-0.211 (n=2473)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=7435)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.130 (n=1836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=5808)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.246 (n=1892)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=5752)

- **FILTRO** `ibs_7min` < `0.7392` → IC=-0.196 (n=1911)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7392
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=5733)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.184 (n=1901)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=5743)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=1848)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5921)

- **FILTRO** `ibs_7min` > `0.266` → IC=-0.192 (n=1942)

  - _Acción_: SKIP cuando `ibs_7min` > 0.266
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=5827)

- **FILTRO** `ballena_activa_n` > `148.0` → IC=-0.187 (n=1927)

  - _Acción_: SKIP cuando `ballena_activa_n` > 148.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=5842)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.164 (n=2068)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=5202)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=1735)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=5535)

- **FILTRO** `ibs_7min` < `0.703` → IC=-0.248 (n=2397)

  - _Acción_: SKIP cuando `ibs_7min` < 0.703
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=4873)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.221 (n=1617)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=5653)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.245 (n=2370)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=8149)

- **FILTRO** `ibs_7min` > `0.7354` → IC=-0.173 (n=2629)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7354
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=7890)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=2397)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=4959)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.240 (n=2197)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=5159)

- **FILTRO** `ibs_7min` < `0.7382` → IC=-0.185 (n=1839)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7382
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5517)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.186 (n=1803)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=5553)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.267 (n=1870)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=5721)

- **FILTRO** `ibs_7min` > `0.2764` → IC=-0.179 (n=1897)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2764
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5694)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.179 (n=1891)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5700)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=1788)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5731)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.234 (n=1879)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5640)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.174 (n=2711)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=8153)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.279 (n=1769)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=5572)

- **FILTRO** `ibs_7min` < `0.2364` → IC=-0.222 (n=1835)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2364
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5506)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.201 (n=1771)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5570)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.207 (n=2503)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=7819)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=969)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1253)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.153 (n=148)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=523)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1162)

- **FILTRO** `libro_liquidez` < `7941.0101` → IC=-0.131 (n=348)

  - _Acción_: SKIP cuando `libro_liquidez` < 7941.0101
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=709)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=363)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.146 (n=156)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=309)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=417)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=599)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.155 (n=166)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=501)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=297)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3979` → IC=+0.141 (n=977)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.3979 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.136 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.131 (n=367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `443.866` → IC=+0.155 (n=326)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 443.866 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3779.4381` → IC=+0.129 (n=443)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3779.4381 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.149 (n=320)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 14.0 (IC base=+0.127)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4372` → IC=+0.154 (n=76)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4372 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.223 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2659.7686` → IC=+0.244 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2659.7686 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.201 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.143)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.129 (n=192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 16.0 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 10.0 (IC base=+0.113)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4146` → IC=+0.181 (n=133)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio` |x|> 0.4146 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `390.044` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 390.044 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7275.4252` → IC=+0.133 (n=178)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7275.4252 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.126)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4335` → IC=+0.228 (n=79)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4335 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.233 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.148)

- **PATRÓN** `total_vol_5m` < `4970.298` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 4970.298 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `3420.0004` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3420.0004 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 28.0 (IC base=+0.148)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.139 (n=167)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.125 (n=166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 13.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=116)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3657.3836` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3657.3836 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.6961` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.6961
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=122)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.266 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=278)

- **FILTRO** `T_h` > `129.5932` → IC=-0.257 (n=138)

  - _Acción_: SKIP cuando `T_h` > 129.5932
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=416)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.221 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.272 (n=55)

- **FILTRO** `T_h` > `88.6373` → IC=-0.357 (n=40)

  - _Acción_: SKIP cuando `T_h` > 88.6373
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=124)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.272 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.054)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.054)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.128 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `pct_vs_K` |x|> `8.3214` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.3214
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.186 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=34)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.214 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=-0.077)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.202 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=126)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.307 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=329)

- **FILTRO** `pct_vs_K` |x|> `3.4531` → IC=-0.445 (n=107)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4531
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=329)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.384 (n=41)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=133)

- **FILTRO** `pct_vs_K` |x|> `1.9209` → IC=-0.389 (n=79)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.9209
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=81)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` < `87.9882` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` < 87.9882
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=95)

- **FILTRO** `pct_vs_K` |x|> `3.1362` → IC=-0.457 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1362
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=88)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.006` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0078` → IC=-0.197 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=94)

- **FILTRO** `T_h` > `113.0501` → IC=-0.156 (n=62)

  - _Acción_: SKIP cuando `T_h` > 113.0501
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=63)

- **FILTRO** `sigma_h` > `0.0132` → IC=-0.344 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=59)

- **FILTRO** `T_h` > `36.4645` → IC=-0.382 (n=66)

  - _Acción_: SKIP cuando `T_h` > 36.4645
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1221` → IC=+0.460 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1221 (IC base=+0.332)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.380 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.332)

- **PATRÓN** `T_h` < `1.0173` → IC=+0.349 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0173 (IC base=+0.332)

- **PATRÓN** `T_h` > `0.8229` → IC=+0.393 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8229 (IC base=+0.332)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.347 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.332)

- **PATRÓN** `edge` > `0.095` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.095 (IC base=+0.422)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.430 (n=169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0121 (IC base=+0.422)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.446 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.422)

- **PATRÓN** `T_h` > `1.48` → IC=+0.455 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.48 (IC base=+0.422)

- **PATRÓN** `dist_50` > `0.3811` → IC=+0.474 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3811 (IC base=+0.422)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.422)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.429)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.417 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.429)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.458 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.429)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.429)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.429)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.429)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.439 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.429)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1885` → IC=+0.480 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1885 (IC base=+0.427)

- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.461 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0161 (IC base=+0.427)

- **PATRÓN** `T_h` > `0.7758` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7758 (IC base=+0.427)

- **PATRÓN** `dist_50` > `0.3288` → IC=+0.461 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3288 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.427)

- **PATRÓN** `edge` > `0.2005` → IC=+0.477 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.477 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.2259` → IC=+0.477 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2259 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.492 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=257)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=343)

- **PATRÓN** `streak_estiramiento` < `0.4511` → IC=+0.125 (n=86)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.4511 (IC base=+0.022)

- **PATRÓN** `streak_estiramiento` < `0.4302` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4302 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `2507.3405` → IC=+0.122 (n=125)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2507.3405 (IC base=+0.038)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `982893.6` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `volumen_racha` > 982893.6
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=42)

- **FILTRO** `streak_estiramiento` > `0.479` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.479
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=58)

- **PATRÓN** `volumen_racha` < `982893.6` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_racha` < 982893.6 (IC base=+0.018)

- **PATRÓN** `streak_estiramiento` < `0.4177` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.4177 (IC base=+0.018)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.141 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 10.0 (IC base=+0.082)

- **PATRÓN** `streak_estiramiento` < `0.3368` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.3368 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.148 (n=103)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 47.0 (IC base=+0.082)

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
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=616)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `volumen_racha` > `9229.0178` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 9229.0178
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=840)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1320)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=983)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=991)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3538)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1891)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.200 (n=907)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.233 (n=907)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1635` → IC=+0.201 (n=2394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1635 (IC base=+0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3456` → IC=+0.207 (n=2388)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3456 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.203 (n=2494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.265 (n=2735)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.122` → IC=+0.192 (n=1280)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.122 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.921` → IC=+0.272 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.921 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `6679.6663` → IC=+0.202 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6679.6663 (IC base=+0.193)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=1137)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.226 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.275 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.215)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2425` → IC=+0.244 (n=170)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2425 (IC base=+0.215)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1446` → IC=+0.240 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1446 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_15` > `0.7143` → IC=+0.277 (n=509)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7143 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.245 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.289 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `16282.4193` → IC=+0.256 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16282.4193 (IC base=+0.215)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=656)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.168 (n=188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.156 (n=248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2372` → IC=+0.158 (n=188)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.2372 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1226` → IC=+0.161 (n=216)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1226 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.142 (n=590)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.5749` → IC=+0.235 (n=564)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5749 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1542` → IC=+0.144 (n=304)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1542 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.028` → IC=+0.271 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.028 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7695.019` → IC=+0.155 (n=256)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 7695.019 (IC base=+0.139)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `20.209` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.209
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=231)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.147 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0056 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.197 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0093 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2271` → IC=+0.172 (n=461)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2271 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0624` → IC=+0.156 (n=460)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.0624 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3414` → IC=+0.171 (n=411)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3414 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.161 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.322 (n=155)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.7125` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.7125 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1959` → IC=+0.154 (n=417)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1959 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.97` → IC=+0.203 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.97 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=287)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.143)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.256` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.256 (IC base=+0.026)

- **PATRÓN** `libro_liquidez` > `3393.3002` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3393.3002 (IC base=+0.026)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.260 (n=573)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.1659` → IC=+0.219 (n=564)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1659 (IC base=+0.216)

- **PATRÓN** `delta_ratio_macro` |x|> `0.067` → IC=+0.222 (n=573)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.067 (IC base=+0.216)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0894` → IC=+0.272 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0894 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.229 (n=570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.216)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.297 (n=643)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.2002` → IC=+0.226 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2002 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.758` → IC=+0.256 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.758 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2988.5082` → IC=+0.292 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2988.5082 (IC base=+0.216)

- **PATRÓN** `ibs_15` < `0.1071` → IC=+0.164 (n=679)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` < 0.1071 (IC base=+0.068)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.366 (n=365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.367 (n=547)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.1114` → IC=+0.361 (n=365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1114 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.385 (n=364)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.393 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.377 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.406 (n=489)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.4169` → IC=+0.389 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4169 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.374 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.360)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `3489.2833` → IC=+0.369 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3489.2833 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `440.0` → IC=+0.379 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 440.0 (IC base=+0.360)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.359 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.361 (n=294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0025 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.361 (n=99)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.358)

- **PATRÓN** `drift_15min` |x|≤ `0.5096` → IC=+0.359 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5096 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1529` → IC=+0.379 (n=196)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1529 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.387 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.379 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.385 (n=294)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.398 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.481` → IC=+0.364 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.481 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` < `25.57` → IC=+0.358 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 25.57 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `15251.8586` → IC=+0.382 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15251.8586 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `497.0` → IC=+0.404 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 497.0 (IC base=+0.358)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.360 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.380 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.371 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0902` → IC=+0.377 (n=226)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0902 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.385 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.418 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.406 (n=253)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.365 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.380 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.828` → IC=+0.360 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.828 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `4304.5454` → IC=+0.385 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4304.5454 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.368 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.361)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.217 (n=934)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2804)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1415)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=2323)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1409` → IC=+0.189 (n=599)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1409 (IC base=-0.067)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.225 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6335` → IC=+0.280 (n=899)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6335 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.203 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2631` → IC=+0.196 (n=760)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2631 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2224` → IC=+0.268 (n=1002)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2224 (IC base=-0.012)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3249` → IC=+0.253 (n=2941)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3249 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3519` → IC=+0.280 (n=3005)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3519 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.6509` → IC=+0.294 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6509 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.210 (n=526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1582)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.229 (n=526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1582)

- **FILTRO** `sigma_ewma_delta_pct` > `23.635` → IC=-0.265 (n=300)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.635
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=1808)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.195 (n=57)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=2051)

- **FILTRO** `libro_liquidez` < `16314.2338` → IC=-0.197 (n=1391)

  - _Acción_: SKIP cuando `libro_liquidez` < 16314.2338
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=717)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.171 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0028 (IC base=+0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1988` → IC=+0.315 (n=122)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1988 (IC base=+0.089)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.309 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.089)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.333 (n=267)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.303 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.3639` → IC=+0.290 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3639 (IC base=+0.089)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.236 (n=51)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.190)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.311 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.190)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.190)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.190)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=583)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.152 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0058 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.166 (n=402)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0038 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1111` → IC=+0.183 (n=301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1111 (IC base=+0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.156 (n=300)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.195 (n=336)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.174 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.252 (n=450)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1541` → IC=+0.149 (n=243)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1541 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.148 (n=328)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.247 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=583)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `10970.0273` → IC=+0.171 (n=150)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 10970.0273 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.250 (n=699)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.243 (n=922)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.7547` → IC=+0.252 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7547 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1552` → IC=+0.257 (n=698)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1552 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.268 (n=351)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3647` → IC=+0.270 (n=1048)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3647 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.7713` → IC=+0.303 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7713 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.574` → IC=+0.255 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.574 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.598` → IC=+0.244 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.598 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.172` → IC=-0.253 (n=293)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.172
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=571)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.274 (n=215)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=649)

- **FILTRO** `sigma_ewma_delta_pct` > `6.672` → IC=-0.185 (n=211)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.672
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=653)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.247 (n=89)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=775)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.178)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.178)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.178)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.178)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0794` → IC=+0.243 (n=419)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0794 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.286 (n=469)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.172` → IC=+0.248 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.172 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1276` → IC=-0.222 (n=523)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1276
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=524)

- **FILTRO** `sigma_h` > `0.0194` → IC=-0.250 (n=522)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0194
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=525)

- **FILTRO** `drift_60min` |x|> `0.1534` → IC=-0.200 (n=261)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1534
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=786)

- **FILTRO** `drift_15min` |x|> `1.2211` → IC=-0.257 (n=261)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2211
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=786)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.200)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.200)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1492` → IC=+0.279 (n=333)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1492 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1101` → IC=+0.301 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1101 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.293 (n=734)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.8057` → IC=+0.352 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8057 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.032)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1918` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1918 (IC base=+0.032)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.291 (n=797)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.329 (n=302)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.299 (n=302)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.223` → IC=+0.309 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.223 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.319 (n=906)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.320 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.354 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `12909.8374` → IC=+0.301 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12909.8374 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.307 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.325 (n=164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.283)

- **PATRÓN** `drift_15min` |x|≤ `0.4181` → IC=+0.284 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4181 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.313 (n=164)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3892` → IC=+0.296 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3892 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.311 (n=452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.311 (n=491)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2573` → IC=+0.332 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2573 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.362 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.283 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `16346.0348` → IC=+0.325 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16346.0348 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.296 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.299 (n=415)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.323 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.318 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.314 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.330 (n=416)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2788` → IC=+0.311 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2788 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.291)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0872` → IC=-0.256 (n=76)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0872
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=230)

- **FILTRO** `sigma_h` > `0.0042` → IC=-0.245 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=202)

- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.154 (n=76)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=230)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.196 (n=67)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=134)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0682` → IC=-0.145 (n=60)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0682
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.174 (n=44)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=133)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1931` → IC=-0.167 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1931
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.296` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.296
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.222 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

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
- **PATRÓN** `T_h` > `82.5234` → IC=+0.218 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 82.5234 (IC base=+0.203)

- **PATRÓN** `ratio` < `0.9763` → IC=+0.444 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9763 (IC base=+0.203)

- **PATRÓN** `T_h` > `145.7409` → IC=+0.388 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7409 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0572` → IC=+0.451 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0572 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.209 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.182)

- **PATRÓN** `ratio` < `0.972` → IC=+0.415 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.182)

- **PATRÓN** `T_h` > `109.696` → IC=+0.300 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.696 (IC base=+0.291)

- **PATRÓN** `ratio` > `1.0228` → IC=+0.330 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0228 (IC base=+0.291)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.256 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.238)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.417 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.238)

- **PATRÓN** `T_h` > `111.9712` → IC=+0.347 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9712 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.0127` → IC=+0.363 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0127 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.401)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.193 a +0.265 en UPDOWN_GBM#15min (n=2735). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7143 sube el IC de +0.215 a +0.277 en UPDOWN_GBM#BTC#15min (n=509). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5749 sube el IC de +0.139 a +0.235 en UPDOWN_GBM#ETH#15min (n=564). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de +0.143 a +0.322 en UPDOWN_GBM#SOL#15min (n=155). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.216 a +0.297 en UPDOWN_GBM#XRP#15min (n=643). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1071 sube el IC de +0.068 a +0.164 en UPDOWN_GBM#XRP#15min (n=679). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6335 sube el IC de -0.067 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=899). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3519 sube el IC de -0.012 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=3005). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.089 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=267). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.190 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6326 sube el IC de +0.148 a +0.252 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=450). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3647 sube el IC de +0.241 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1048). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.178 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.039 a +0.286 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=469). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.200 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=734). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.287 a +0.319 en UPDOWN_GBM_IBS_ALTO (n=906). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.283 a +0.311 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=491). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.291 a +0.330 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=416). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.360 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=489). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.358 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=294). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.361 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=253). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1635 | +0.088 | +183.85€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1635 | +0.088 | +183.85€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1264 | +0.092 | +156.82€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1264 | +0.092 | +156.82€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 268 | +0.067 | +11.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 268 | +0.067 | +11.32€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 337 | -0.004 | +57.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 337 | -0.004 | +57.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 263 | -0.002 | +49.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 263 | -0.002 | +49.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 52 | +0.000 | +5.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 52 | +0.000 | +5.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 22 | -0.042 | +2.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 35577 | -0.084 | -4664.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1795 | -0.015 | -236.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 33782 | -0.087 | -4428.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4421 | -0.116 | -760.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4421 | -0.116 | -760.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1795 | -0.015 | -236.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1795 | -0.015 | -236.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4097 | -0.113 | -842.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4097 | -0.113 | -842.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9219 | +0.008 | -859.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9219 | +0.008 | -859.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9099 | -0.110 | -700.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9099 | -0.110 | -700.86€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6946 | -0.151 | -1265.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6946 | -0.151 | -1265.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 27911 | -0.019 | +3705.21€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7216 | +0.002 | +1763.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 20695 | -0.026 | +1941.68€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 27911 | -0.019 | +3705.21€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7216 | +0.002 | +1763.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 20695 | -0.026 | +1941.68€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 122519 | +0.113 | -5387.08€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 16776 | +0.182 | -521.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 524 | -0.040 | -62.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 97674 | +0.103 | -4528.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7545 | +0.104 | -274.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 16214 | +0.104 | -1104.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 56 | -0.155 | +9.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 16143 | +0.105 | -1101.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 24131 | +0.128 | -414.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4930 | +0.194 | -152.62€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 16194 | +0.116 | -160.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2965 | +0.088 | -79.13€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 16262 | +0.095 | -1246.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 64 | -0.106 | -4.03€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 16183 | +0.096 | -1231.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 26030 | +0.124 | -448.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6886 | +0.175 | -115.37€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 16387 | +0.106 | -269.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2745 | +0.101 | -54.74€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 23651 | +0.114 | -1293.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4782 | +0.190 | -267.30€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 427 | -0.004 | -9.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 16607 | +0.093 | -875.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1835 | +0.133 | -140.87€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 16231 | +0.102 | -880.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 58 | -0.050 | +9.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 16160 | +0.102 | -889.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 19581 | +0.194 | -1230.31€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 19581 | +0.194 | -1230.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4528 | +0.174 | -420.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4528 | +0.174 | -420.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2203 | +0.200 | -43.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2203 | +0.200 | -43.74€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4460 | +0.181 | -361.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4460 | +0.181 | -361.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3911 | +0.242 | -137.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3911 | +0.242 | -137.48€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4400 | +0.189 | -281.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4400 | +0.189 | -281.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 900 | +0.426 | -33.52€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 900 | +0.426 | -33.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 355 | +0.433 | -7.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 355 | +0.433 | -7.62€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 345 | +0.428 | -10.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 345 | +0.428 | -10.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 188 | +0.405 | -12.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 188 | +0.405 | -12.81€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 68140 | +0.200 | -5041.06€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 68140 | +0.200 | -5041.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 11722 | +0.184 | -1227.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 11722 | +0.184 | -1227.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 10979 | +0.224 | -383.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 10979 | +0.224 | -383.47€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 11695 | +0.177 | -1299.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 11695 | +0.177 | -1299.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 11041 | +0.220 | -414.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 11041 | +0.220 | -414.47€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 11287 | +0.202 | -754.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 11287 | +0.202 | -754.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 11416 | +0.194 | -961.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 11416 | +0.194 | -961.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 25975 | +0.118 | +243.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 25975 | +0.118 | +243.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 12901 | +0.122 | +199.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 12901 | +0.122 | +199.85€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 13074 | +0.114 | +43.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 13074 | +0.114 | +43.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1814 | +0.289 | -19.94€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1814 | +0.289 | -19.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 819 | +0.281 | -15.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 819 | +0.281 | -15.19€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 877 | +0.287 | -9.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 877 | +0.287 | -9.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 118 | +0.350 | +4.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 118 | +0.350 | +4.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 828 | +0.441 | +3.56€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 828 | +0.441 | +3.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 401 | +0.440 | +0.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 401 | +0.440 | +0.51€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 381 | +0.443 | +2.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 381 | +0.443 | +2.50€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1402 | +0.068 | -66.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 518 | +0.058 | -40.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 884 | +0.074 | -25.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 68 | +0.100 | +1.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 68 | +0.100 | +1.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1091 | +0.075 | -33.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 207 | +0.074 | -7.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 884 | +0.074 | -25.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 243 | +0.031 | -35.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 243 | +0.031 | -35.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 50214 | +0.100 | -1279.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4075 | +0.093 | +62.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 46139 | +0.100 | -1341.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 27800 | +0.105 | -294.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4075 | +0.093 | +62.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 23725 | +0.107 | -357.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 10042 | +0.109 | -25.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 10042 | +0.109 | -25.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 12372 | +0.081 | -959.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 12372 | +0.081 | -959.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 871 | +0.203 | -101.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 871 | +0.203 | -101.16€ | 2 | 4 |
| ✅ GBM_LATE_15M | 34970 | +0.090 | +17496.98€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 34970 | +0.090 | +17496.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5891 | +0.205 | +4580.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5891 | +0.205 | +4580.16€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 5205 | +0.178 | +3785.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5205 | +0.178 | +3785.33€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 6215 | +0.201 | +4728.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6215 | +0.201 | +4728.94€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 4926 | +0.036 | +1258.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4926 | +0.036 | +1258.05€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4994 | -0.030 | +1073.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4994 | -0.030 | +1073.30€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 7739 | -0.036 | +2071.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 7739 | -0.036 | +2071.20€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 37924 | +0.087 | +20231.30€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 37924 | +0.087 | +20231.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7373 | +0.010 | +3739.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7373 | +0.010 | +3739.85€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 7879 | +0.013 | +1695.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 7879 | +0.013 | +1695.22€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5332 | +0.269 | +5526.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5332 | +0.269 | +5526.63€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6456 | +0.013 | +1468.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6456 | +0.013 | +1468.43€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6183 | +0.038 | +2495.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6183 | +0.038 | +2495.52€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4701 | +0.292 | +5305.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4701 | +0.292 | +5305.65€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 27933 | +0.176 | +21999.74€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 27933 | +0.176 | +21999.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4235 | +0.217 | +3553.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4235 | +0.217 | +3553.89€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4420 | +0.150 | +3227.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4420 | +0.150 | +3227.06€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4429 | +0.218 | +3706.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4429 | +0.218 | +3706.12€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4700 | +0.138 | +3503.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4700 | +0.138 | +3503.31€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5229 | +0.127 | +3893.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5229 | +0.127 | +3893.56€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4920 | +0.216 | +4115.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4920 | +0.216 | +4115.80€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7563 | +0.140 | +3702.23€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7563 | +0.140 | +3702.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 341 | +0.141 | +188.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2341 | +0.149 | +1337.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2341 | +0.149 | +1337.56€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 376 | +0.140 | +173.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 376 | +0.140 | +173.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2330 | +0.153 | +1164.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2330 | +0.153 | +1164.50€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1637 | +0.109 | +596.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1637 | +0.109 | +596.59€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 538 | +0.135 | +242.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 538 | +0.135 | +242.32€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 35219 | +0.182 | +27449.18€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 35219 | +0.182 | +27449.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5610 | +0.232 | +5006.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5610 | +0.232 | +5006.01€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5451 | +0.148 | +3598.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5451 | +0.148 | +3598.98€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5900 | +0.229 | +5168.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5900 | +0.229 | +5168.72€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 5720 | +0.138 | +4024.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 5720 | +0.138 | +4024.31€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6240 | +0.127 | +4350.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6240 | +0.127 | +4350.28€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6298 | +0.219 | +5300.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6298 | +0.219 | +5300.87€ | 0 | 21 |
| ✅ GBM_LATE_5M | 9738 | +0.184 | +6885.06€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 9738 | +0.184 | +6885.06€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2133 | +0.171 | +1545.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2133 | +0.171 | +1545.14€ | 0 | 30 |
| ✅ GBM_LATE_5M#DOGE | 992 | +0.176 | +650.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 992 | +0.176 | +650.38€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 3032 | +0.187 | +2082.36€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3032 | +0.187 | +2082.36€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1255 | +0.176 | +870.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1255 | +0.176 | +870.12€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1407 | +0.179 | +923.07€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1407 | +0.179 | +923.07€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2663 | +0.068 | +930.51€ | 0 | 10 |
| ✅ GBM_LATE_60M#60min | 2663 | +0.068 | +930.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1001 | +0.086 | +357.99€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1001 | +0.086 | +357.99€ | 0 | 10 |
| ✅ GBM_LATE_60M#ETH | 837 | +0.065 | +342.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 837 | +0.065 | +342.43€ | 1 | 8 |
| ✅ GBM_LATE_60M#SOL | 825 | +0.048 | +230.08€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 825 | +0.048 | +230.08€ | 2 | 14 |
| 🚫 GBM_LATE_60M_FADE | 493 | -0.241 | -17.43€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 493 | -0.241 | -17.43€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 187 | -0.235 | -12.66€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 187 | -0.235 | -12.66€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 172 | -0.218 | +1.41€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 172 | -0.218 | +1.41€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 134 | -0.272 | -6.17€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 134 | -0.272 | -6.17€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1196 | +0.085 | +301.60€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1196 | +0.085 | +301.60€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 455 | +0.078 | +89.78€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 455 | +0.078 | +89.78€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 424 | +0.061 | +68.75€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 424 | +0.061 | +68.75€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 317 | +0.127 | +143.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 317 | +0.127 | +143.06€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 138 | +0.250 | +117.05€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 138 | +0.250 | +117.05€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 138 | +0.250 | +117.05€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 138 | +0.250 | +117.05€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 2885 | +0.100 | +733.94€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2885 | +0.100 | +733.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2885 | +0.100 | +733.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2885 | +0.100 | +733.94€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 442 | -0.068 | -31.45€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 442 | -0.068 | -31.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 125 | -0.028 | -0.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 125 | -0.028 | -0.87€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 168 | -0.029 | -5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 168 | -0.029 | -5.75€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3117 | +0.020 | +78.70€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3117 | +0.020 | +78.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 152 | +0.026 | -1.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 152 | +0.026 | -1.43€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 528 | +0.025 | +34.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 528 | +0.025 | +34.98€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1126 | +0.028 | +29.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1126 | +0.028 | +29.44€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 719 | +0.013 | +2.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 719 | +0.013 | +2.17€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 389 | +0.017 | +18.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 389 | +0.017 | +18.63€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1485 | -0.040 | -23.80€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1485 | -0.040 | -23.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 423 | -0.034 | -11.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 423 | -0.034 | -11.00€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 492 | -0.018 | +3.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 492 | -0.018 | +3.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 570 | -0.063 | -16.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 570 | -0.063 | -16.07€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 5627 | -0.021 | +81.78€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2655 | -0.026 | -1.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 2972 | -0.015 | +83.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 162 | +0.000 | +9.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 77 | +0.044 | +12.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 85 | -0.040 | -2.60€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1405 | -0.010 | +35.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 666 | -0.015 | +3.84€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 739 | -0.005 | +31.19€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 624 | -0.027 | +4.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 312 | -0.041 | -8.89€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 312 | -0.013 | +13.33€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1161 | -0.039 | -36.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 532 | -0.058 | -43.30€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 629 | -0.023 | +7.28€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1100 | -0.014 | +37.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 528 | -0.013 | +22.85€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 572 | -0.014 | +14.40€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1175 | -0.021 | +31.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 540 | -0.022 | +11.64€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 635 | -0.020 | +19.62€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 40580 | -0.002 | +1954.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 40580 | -0.002 | +1954.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7251 | +0.025 | +956.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7251 | +0.025 | +956.94€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5999 | -0.032 | -98.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5999 | -0.032 | -98.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7348 | +0.022 | +725.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7348 | +0.022 | +725.48€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5828 | -0.049 | -153.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5828 | -0.049 | -153.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 6849 | -0.007 | +208.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 6849 | -0.007 | +208.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7305 | +0.014 | +315.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7305 | +0.014 | +315.97€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6251 | -0.059 | -142.00€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6251 | -0.059 | -142.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1220 | +0.001 | -13.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1546 | -0.074 | -29.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1546 | -0.074 | -29.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 50 | -0.077 | -3.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 50 | -0.077 | -3.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 733 | -0.122 | -32.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 733 | -0.122 | -32.52€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1846 | -0.079 | -38.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1846 | -0.079 | -38.03€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3355 | +0.004 | -3.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3355 | +0.004 | -3.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1320 | +0.005 | +5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1320 | +0.005 | +5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1389 | +0.007 | -0.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1389 | +0.007 | -0.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 101720 | -0.073 | +1720.98€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 101720 | -0.073 | +1720.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 17525 | -0.074 | +913.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 17525 | -0.074 | +913.43€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 15413 | -0.098 | -827.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 15413 | -0.098 | -827.01€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 17789 | -0.066 | +1026.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 17789 | -0.066 | +1026.40€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 14947 | -0.095 | -452.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 14947 | -0.095 | -452.16€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 18383 | -0.052 | +369.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 18383 | -0.052 | +369.42€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 17663 | -0.063 | +690.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 17663 | -0.063 | +690.89€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8165 | -0.032 | -158.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8165 | -0.032 | -158.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1939 | -0.043 | -19.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1939 | -0.043 | -19.17€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2252 | -0.027 | -34.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2252 | -0.027 | -34.54€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1133 | -0.051 | -25.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1133 | -0.051 | -25.31€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 837 | -0.023 | -26.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 837 | -0.023 | -26.93€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1438 | +0.121 | +565.73€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1302 | +0.127 | +553.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 303 | +0.143 | +158.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 303 | +0.143 | +158.39€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 254 | +0.113 | +80.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 254 | +0.113 | +80.93€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 265 | +0.126 | +116.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 265 | +0.126 | +116.30€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 231 | +0.148 | +123.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 231 | +0.148 | +123.09€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 249 | +0.102 | +74.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 249 | +0.102 | +74.43€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1047 | -0.019 | -22.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1047 | -0.019 | -22.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 205 | -0.012 | +2.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 205 | -0.012 | +2.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 164 | +0.000 | +5.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 164 | +0.000 | +5.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 279 | -0.037 | -18.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 279 | -0.037 | -18.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 227 | +0.007 | +1.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 227 | +0.007 | +1.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 172 | -0.046 | -13.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 172 | -0.046 | -13.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 783 | -0.078 | -61.26€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 357 | -0.132 | -77.72€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 277 | -0.170 | -70.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 80 | +0.000 | -7.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 277 | -0.038 | +3.02€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 198 | -0.035 | +2.25€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 79 | -0.043 | +0.77€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 149 | -0.023 | +13.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 120 | -0.033 | +8.03€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 29 | +0.016 | +5.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 595 | -0.098 | -60.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 188 | -0.016 | -0.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 939 | -0.200 | -42.91€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 389 | -0.196 | -30.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 334 | -0.199 | -30.91€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 55 | -0.167 | +0.79€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 317 | -0.212 | -27.02€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 273 | -0.220 | -32.60€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 44 | -0.152 | +5.58€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 233 | -0.189 | +14.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 214 | -0.185 | +11.09€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 821 | -0.203 | -52.42€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 118 | -0.175 | +9.51€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 396 | +0.397 | +364.69€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 46 | +0.104 | +40.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 46 | +0.104 | +40.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 101 | +0.374 | +91.49€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 101 | +0.374 | +91.49€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 249 | +0.456 | +232.60€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 249 | +0.456 | +232.60€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 396 | +0.397 | +364.69€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 638 | +0.031 | +26.40€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 638 | +0.031 | +26.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 49 | +0.010 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 49 | +0.010 | -2.27€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 66 | -0.015 | -2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 66 | -0.015 | -2.23€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 227 | +0.059 | +27.47€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 227 | +0.059 | +27.47€ | 2 | 5 |
| ✅ STREAK_FADE_5M | 3285 | -0.020 | -124.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3285 | -0.020 | -124.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1048 | -0.021 | -35.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1048 | -0.021 | -35.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 585 | -0.026 | -25.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 585 | -0.026 | -25.65€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1496 | -0.015 | -48.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1496 | -0.015 | -48.48€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 93 | -0.047 | -8.86€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 93 | -0.047 | -8.86€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 39 | -0.085 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 39 | -0.085 | -3.98€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 54 | -0.018 | -4.88€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 54 | -0.018 | -4.88€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 9956 | +0.019 | +107.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9956 | +0.019 | +107.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2642 | +0.021 | +28.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2642 | +0.021 | +28.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2434 | +0.027 | +51.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2434 | +0.027 | +51.63€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2864 | +0.009 | -1.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2864 | +0.009 | -1.29€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2016 | +0.020 | +28.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2016 | +0.020 | +28.49€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9005 | +0.013 | -46.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 9005 | +0.013 | -46.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3557 | +0.018 | -4.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3557 | +0.018 | -4.45€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3523 | +0.011 | -26.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3523 | +0.011 | -26.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1925 | +0.007 | -14.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1925 | +0.007 | -14.84€ | 1 | 0 |
| ✅ UPDOWN_GBM | 63001 | +0.049 | +5255.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 15728 | +0.084 | +3506.30€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 2084 | +0.006 | +10.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 41384 | +0.043 | +1677.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3590 | +0.008 | +63.14€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6519 | +0.085 | +953.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1397 | +0.158 | +615.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 73 | -0.007 | -1.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5049 | +0.066 | +339.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 12273 | +0.052 | +1012.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1977 | +0.091 | +476.94€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 536 | +0.011 | +5.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 8060 | +0.055 | +482.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1621 | +0.005 | +44.65€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 79 | -0.080 | +1.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 7682 | +0.063 | +747.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1386 | +0.146 | +535.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 70 | +0.014 | -1.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6226 | +0.045 | +214.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 13724 | +0.039 | +801.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3689 | +0.057 | +486.65€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 529 | +0.007 | +8.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 8212 | +0.039 | +300.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1223 | +0.006 | +3.31€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 71 | -0.103 | +3.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 13871 | +0.027 | +592.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3711 | +0.037 | +352.28€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 518 | +0.000 | +0.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 8833 | +0.027 | +230.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 746 | +0.016 | +15.18€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 63 | -0.146 | -5.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 8930 | +0.058 | +1149.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3568 | +0.104 | +1040.19€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 358 | +0.008 | -0.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5004 | +0.029 | +109.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 213 | -0.109 | -0.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 729 | +0.360 | +256.51€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 729 | +0.360 | +256.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 392 | +0.358 | +128.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 392 | +0.358 | +128.15€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 337 | +0.361 | +128.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 337 | +0.361 | +128.36€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 17163 | -0.024 | +4182.41€ | 2 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 17163 | -0.024 | +4182.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1508 | -0.053 | +483.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1508 | -0.053 | +483.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2948 | -0.111 | +151.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2948 | -0.111 | +151.84€ | 5 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 853 | +0.218 | +702.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 853 | +0.218 | +702.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1996 | +0.213 | +1276.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1996 | +0.213 | +1276.50€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4902 | -0.063 | +650.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4902 | -0.063 | +650.58€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4956 | -0.063 | +917.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4956 | -0.063 | +917.97€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 187 | +0.034 | +6.83€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 187 | +0.034 | +6.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 187 | +0.034 | +6.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 187 | +0.034 | +6.83€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1207 | +0.287 | +996.36€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1207 | +0.287 | +996.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 654 | +0.283 | +509.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 654 | +0.283 | +509.36€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 553 | +0.291 | +487.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 553 | +0.291 | +487.01€ | 0 | 8 |
| ✅ UPDOWN_OU_5M | 768 | -0.114 | -84.12€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 768 | -0.114 | -84.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 226 | -0.088 | -18.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 226 | -0.088 | -18.31€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 80 | -0.159 | -7.73€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 80 | -0.159 | -7.73€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 83 | -0.194 | -8.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 83 | -0.194 | -8.02€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 3058 | +0.306 | +1505.31€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1094 | +0.259 | +157.21€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1169 | +0.299 | +524.07€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 795 | +0.378 | +824.02€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.016 n=769 — no justifica filtro, seguir monitorizando
  - _Datos_: n=769 IC=+0.016 PNL=+37.43€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 651 celda(s) pasan gate riguroso completo de 2522 evaluadas (n>=40) y 3515 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.037 < 0.08 — monitorear
  - _Datos_: n=3704 IC=+0.037 PNL=+355.71€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1169/15 IC=+0.299 PNL=+524.07€ | BTC: n=1094/15 IC=+0.259 PNL=+157.21€ | SOL: n=795/15 IC=+0.378 PNL=+824.02€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.139 n=641/60 | contraria IC=+0.200 n=664 | gap=-0.060 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=399, boost estimado=+0.012. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1222/40 IC=+0.006 PNL=+2.81€ | BTC#60min: n=1619/40 IC=+0.005 PNL=+44.64€ | SOL#60min: n=745/40 IC=+0.015 PNL=+14.69€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=463499 | tras_1loss IC=+0.091 n=354666 | tras_2loss IC=+0.060 n=145111/40 | gap=-0.012 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.08 con n=558 PNL=+453.95€
  - _Datos_: n=558 IC=+0.216 PNL=+453.95€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.209 > 0.08 con n=602 PNL=+438.54€
  - _Datos_: n=602 IC=+0.209 PNL=+438.54€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.173 > 0.08 con n=53 PNL=+27.40€
  - _Datos_: n=53 IC=+0.173 PNL=+27.40€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=2497 PNL=+1384.89€
  - _Datos_: n=2497 IC=+0.334 PNL=+1384.89€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=499 IC=+0.073 PNL=+54.48€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=499 IC=+0.073 PNL=+54.48€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=69 IC=+0.190 PNL=+47.57€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=69 IC=+0.190 PNL=+47.57€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 4/15 ops en el filtro definido (IC actual=+0.067 PNL=+7.14€)
  - _Datos_: n=4 IC=+0.067 PNL=+7.14€

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
  - _Estado_: n=2396 IC=+0.007 PNL=+4.70€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2396 IC=+0.007 PNL=+4.70€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1190 IC=+0.008 PNL=+57.44€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1190 IC=+0.008 PNL=+57.44€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=769 IC=+0.016 PNL=+37.43€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=769 IC=+0.016 PNL=+37.43€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.1 con n=3614 PNL=+2469.93€
  - _Datos_: n=3614 IC=+0.194 PNL=+2469.93€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1975 IC=+0.091 PNL=+476.94€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1975 IC=+0.091 PNL=+476.94€

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
  - _Estado_: n=805 IC=+0.034 PNL=+70.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=805 IC=+0.034 PNL=+70.88€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=87 IC=+0.051 PNL=+4.69€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=87 IC=+0.051 PNL=+4.69€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.250 n=138) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=138 IC=+0.250 PNL=+117.05€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=828 PNL=+348.90€
  - _Datos_: n=828 IC=+0.128 PNL=+348.90€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=191 IC=-0.070 PNL=+27.59€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=191 IC=-0.070 PNL=+27.59€

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
  - _Estado_: n=23750 IC=+0.071 PNL=+3385.42€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=23750 IC=+0.071 PNL=+3385.42€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.136 < -0.1 con n=374 PNL=+47.53€
  - _Datos_: n=374 IC=-0.136 PNL=+47.53€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2711 IC=+0.068 PNL=+341.79€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2711 IC=+0.068 PNL=+341.79€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=116 IC=-0.093 PNL=+5.87€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=116 IC=-0.093 PNL=+5.87€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.1 con n=643 PNL=+169.78€
  - _Datos_: n=643 IC=+0.119 PNL=+169.78€

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
  - _Estado_: n=25628 IC=-0.136 PNL=+1821.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=25628 IC=-0.136 PNL=+1821.02€

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
  - _Estado_: n=2597 IC=+0.138 PNL=+1517.57€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2597 IC=+0.138 PNL=+1517.57€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6607 IC=+0.043 PNL=+462.14€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6607 IC=+0.043 PNL=+462.14€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.088 > 0.08 con n=2888 PNL=+1514.30€
  - _Datos_: n=2888 IC=+0.088 PNL=+1514.30€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=2618 PNL=-184.99€
  - _Datos_: n=2618 IC=-0.224 PNL=-184.99€

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
  - _Estado_: n=55 IC=-0.009 PNL=+6.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=55 IC=-0.009 PNL=+6.29€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.098 n=1473) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1473 IC=+0.098 PNL=+322.34€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=513) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=513 IC=+0.411 PNL=+730.63€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=11712 IC=+0.184 PNL=-1223.80€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=11712 IC=+0.184 PNL=-1223.80€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.1 con n=191 PNL=+119.58€
  - _Datos_: n=191 IC=+0.210 PNL=+119.58€
