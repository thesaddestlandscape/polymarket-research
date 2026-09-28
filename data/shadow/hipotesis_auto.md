# Hipótesis automáticas — 2026-09-28 15:18 UTC
_Generado por shadow_postmortem.py sobre 652343 resoluciones (PNL=+76234.72€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=529)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.233 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.8033` → IC=+0.253 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8033 (IC base=+0.136)

- **PATRÓN** `banda_z` > `4.083` → IC=+0.159 (n=567)

  - _Acción_: Kelly boost +0.80€ cuando `banda_z` > 4.083 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=604)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4804.7376` → IC=+0.165 (n=189)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4804.7376 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.125 (n=529)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.057)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.140 (n=170)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=438)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=394)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.257 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.146)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.146)

- **PATRÓN** `banda_hit_calibrado` > `0.7991` → IC=+0.265 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7991 (IC base=+0.146)

- **PATRÓN** `banda_z` > `10.478` → IC=+0.214 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.478 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.166 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=515)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3313.2914` → IC=+0.150 (n=304)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3313.2914 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.160 (n=154)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 94.0 (IC base=+0.060)

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
- **FILTRO** `restante_s_al_confirmar` < `145.98` → IC=-0.217 (n=7496)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.98
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=22497)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.36` → IC=-0.246 (n=973)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.36
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=2919)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.83` → IC=-0.308 (n=882)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.83
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2651)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.28` → IC=-0.203 (n=1830)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.28
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=5492)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.48` → IC=-0.335 (n=1471)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.48
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=4414)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.230 (n=357)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=408)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=174)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=540)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=564)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.207 (n=14708)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3653)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5614.1784` → IC=+0.176 (n=2341)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5614.1784 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=12307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=15166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=11716)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=5938)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7798.6476` → IC=+0.173 (n=2258)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7798.6476 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.212 (n=1719)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1761)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `15909.0735` → IC=+0.237 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15909.0735 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=1592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1777)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.262 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `15820.2665` → IC=+0.211 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15820.2665 (IC base=+0.197)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.176 (n=341)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.62 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.142 (n=241)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.097)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.135 (n=563)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 11.0 (IC base=+0.102)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=862)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5754.4405` → IC=+0.167 (n=226)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5754.4405 (IC base=+0.102)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=3009)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.345 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.229)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.365 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.234 (n=1569)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `3696.0986` → IC=+0.229 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3696.0986 (IC base=+0.229)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.134 (n=643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 15.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.247 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=812)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `1313.4858` → IC=+0.146 (n=709)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1313.4858 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.403 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.161 (n=617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=755)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.154)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.176 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.370 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `1244.1621` → IC=+0.154 (n=232)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1244.1621 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.209 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.76` → IC=-0.289 (n=131)

  - _Acción_: SKIP cuando `py_entrada` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=65)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=12492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=11937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.227 (n=4047)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `3571.1845` → IC=+0.331 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3571.1845 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=2999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.171 (n=2846)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.174 (n=2848)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.251 (n=1037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.249 (n=1032)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.245)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.340 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.245)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=2788)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2810)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2379)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.251 (n=2594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.324 (n=842)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=2865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.196 (n=2145)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.434 (n=576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.463 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `11247.6748` → IC=+0.458 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11247.6748 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.445 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.457 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `14179.602` → IC=+0.446 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14179.602 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.449 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.462 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.425 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `3322.2122` → IC=+0.445 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3322.2122 (IC base=+0.427)

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
- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=37129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.236 (n=16464)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=7536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=6960)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=6686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=6668)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.263 (n=3797)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=6764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6760)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2306)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=2464)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.195 (n=6584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=2860)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5642)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.125 (n=5250)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.17 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=5301)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=6957)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.61` → IC=+0.139 (n=5229)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.61 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=2840)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.13` → IC=+0.125 (n=2607)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.13 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=2606)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=3433)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.29` → IC=+0.142 (n=2600)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.29 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=2802)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.128 (n=2639)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.2 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=2937)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.137 (n=2640)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `4107.9466` → IC=+0.305 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4107.9466 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.330 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `4258.3281` → IC=+0.295 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4258.3281 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.323 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1726.8276` → IC=+0.313 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1726.8276 (IC base=+0.287)

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
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.439 (n=472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.434 (n=466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.435 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.436 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.434 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.434 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.454 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `1978.9685` → IC=+0.464 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.9685 (IC base=+0.438)

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
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

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
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4864` → IC=+0.126 (n=8807)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.4864 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.242 (n=2937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.2196` → IC=+0.257 (n=1955)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2196 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.343` → IC=+0.190 (n=2334)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 8.343 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.251 (n=2424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` > `1.0466` → IC=+0.259 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0466 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.3021` → IC=+0.226 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3021 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.9003` → IC=+0.210 (n=4062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9003 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.5701` → IC=+0.134 (n=10661)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5701 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.6051` → IC=+0.204 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6051 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.6995` → IC=+0.185 (n=1670)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6995 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `0.8705` → IC=+0.177 (n=2530)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8705 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.225 (n=1824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.5692` → IC=+0.200 (n=5759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5692 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.213 (n=6237)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=+0.067)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.196 (n=659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0049 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.172 (n=657)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0081 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3487` → IC=+0.173 (n=1972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3487 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.172 (n=1330)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.186` → IC=+0.269 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.186 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.206 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.4398` → IC=+0.168 (n=1852)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4398 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.182 (n=1987)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.257 (n=694)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.125` → IC=+0.272 (n=673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.125 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.247 (n=1045)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.290 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.497` → IC=+0.241 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.497 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.479` → IC=+0.246 (n=1599)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.479 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0697` → IC=+0.233 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0697 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.269 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4339` → IC=+0.233 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4339 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.5977` → IC=+0.245 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5977 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1814.1` → IC=+0.237 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1814.1 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.239 (n=677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1107` → IC=+0.243 (n=676)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1107 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=1537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.221 (n=1565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.8983` → IC=+0.265 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8983 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.347` → IC=+0.224 (n=1442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.347 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.469` → IC=+0.268 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.469 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.2558` → IC=+0.222 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2558 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `1.0825` → IC=+0.229 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0825 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.243 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7515` → IC=+0.219 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7515 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.3804` → IC=+0.234 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3804 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `11027.9657` → IC=+0.224 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11027.9657 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.175 (n=531)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.165 (n=527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5683` → IC=+0.176 (n=1389)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.5683 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1289` → IC=+0.152 (n=1426)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1289 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.323` → IC=+0.153 (n=249)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.323 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.346` → IC=+0.143 (n=1449)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.346 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.148 (n=1579)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2116 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8593` → IC=+0.141 (n=1052)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.8593 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.179 (n=418)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.152 (n=1468)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.146 (n=979)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `14023.3095` → IC=+0.144 (n=1052)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 14023.3095 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.172 (n=613)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 233.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.210 (n=657)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=2072)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=1772)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.259 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.0991` → IC=+0.190 (n=1717)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0991 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3553` → IC=+0.202 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3553 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.7734` → IC=+0.195 (n=1681)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7734 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2337)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.219 (n=1714)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6238` → IC=+0.215 (n=1713)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6238 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.219 (n=802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.244 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.703` → IC=+0.230 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.703 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.512` → IC=+0.213 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.512 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.262 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7535` → IC=+0.207 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7535 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.175` → IC=+0.217 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.175 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1910.6932` → IC=+0.215 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.6932 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.221 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.212)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=108)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=2390)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.139 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0037 (IC base=+0.034)

- **PATRÓN** `ibs_20min` > `0.9463` → IC=+0.221 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9463 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1948` → IC=+0.332 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1948 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.805` → IC=+0.168 (n=779)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.805 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.339 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8653 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.332 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.3097` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3097 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.352 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.335 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.331 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.6579` → IC=+0.214 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6579 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.8511` → IC=+0.154 (n=626)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8511 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.1641` → IC=+0.154 (n=313)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.1641 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2309` → IC=+0.211 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2309 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5277` → IC=+0.170 (n=791)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.5277 (IC base=+0.021)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.182 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=356)

- **FILTRO** `ibs_20min` < `0.2941` → IC=-0.201 (n=105)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=315)

- **FILTRO** `ibs_20min` > `0.25` → IC=-0.126 (n=2359)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=1196)

- **FILTRO** `sigma_ewma_delta_pct` > `8.705` → IC=-0.216 (n=378)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.705
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3177)

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

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.125 (n=1196)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.25 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7328` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7328 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.4579` → IC=+0.232 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4579 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `0.6774` → IC=+0.272 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6774 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` > `0.8913` → IC=+0.231 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8913 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.159` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.159 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.281 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6576` → IC=-0.180 (n=620)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6576
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1864)

- **FILTRO** `ibs_20min` < `0.7191` → IC=-0.154 (n=1639)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7191
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=845)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.196 (n=518)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1966)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.207 (n=909)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=2767)

- **PATRÓN** `dist_vwap_pct` > `0.4581` → IC=+0.315 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4581 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2822` → IC=+0.314 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2822 (IC base=-0.068)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.310 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=-0.068)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.301 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.4256` → IC=+0.300 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4256 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.298 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.5647` → IC=+0.275 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5647 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` < `0.7344` → IC=+0.258 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7344 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` > `1.0842` → IC=+0.273 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0842 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.101` → IC=+0.263 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.101 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.1378` → IC=+0.262 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1378 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.5237` → IC=+0.247 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5237 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.196 (n=3746)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0098 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4741` → IC=+0.186 (n=10033)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4741 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `1.0255` → IC=+0.290 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0255 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.628` → IC=+0.159 (n=5215)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.628 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.254 (n=3594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.272 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4643` → IC=+0.241 (n=2174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4643 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6559` → IC=+0.251 (n=2174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6559 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.272 (n=6043)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.165 (n=3685)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0091 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5488` → IC=+0.154 (n=9709)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5488 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.7144` → IC=+0.247 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7144 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2496` → IC=+0.246 (n=3156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2496 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.7099` → IC=+0.247 (n=1450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7099 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.2049` → IC=+0.250 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2049 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2414` → IC=+0.302 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2414 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.6339` → IC=+0.263 (n=4427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6339 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.2837` → IC=+0.263 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2837 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.274 (n=4304)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 83.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2558` → IC=-0.153 (n=776)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2558
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2328)

- **FILTRO** `sigma_ewma_delta_pct` > `4.535` → IC=-0.167 (n=589)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.535
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1958)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.272 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.846` → IC=+0.207 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.846 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2226` → IC=+0.263 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2226 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.189 (n=332)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.1694` → IC=+0.211 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1694 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.204 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.2144` → IC=+0.463 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2144 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.3871` → IC=+0.452 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3871 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.4836` → IC=+0.457 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4836 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.486 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8658` → IC=+0.165 (n=753)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8658 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.2998` → IC=+0.177 (n=397)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2998 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6762` → IC=+0.178 (n=931)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6762 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.241 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.197 (n=341)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4012` → IC=+0.173 (n=341)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4012 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.204 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 236.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1524` → IC=+0.223 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1524 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.8607` → IC=+0.235 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8607 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2677` → IC=+0.302 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2677 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.4375` → IC=+0.218 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4375 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1626` → IC=+0.236 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1626 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `459.0` → IC=+0.221 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 459.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.289 (n=581)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.248)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.252 (n=1749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.251 (n=660)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.248)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.741` → IC=+0.284 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.741 (IC base=+0.248)

- **PATRÓN** `volumen_pendiente_norm` < `0.1009` → IC=+0.261 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1009 (IC base=+0.248)

- **PATRÓN** `volumen_spike_ratio` > `3.3381` → IC=+0.267 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3381 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2049)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.248)

- **PATRÓN** `libro_liquidez` > `1912.5584` → IC=+0.259 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.5584 (IC base=+0.248)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.315 (n=646)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.6196` → IC=+0.287 (n=1424)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6196 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.326 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.3456` → IC=+0.292 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3456 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.684` → IC=+0.295 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.684 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.707` → IC=+0.285 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.707 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.3385` → IC=+0.296 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3385 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.5856` → IC=+0.293 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5856 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.6923` → IC=+0.291 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6923 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `1903.9584` → IC=+0.298 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.9584 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.292 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.284)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.3037` → IC=-0.160 (n=562)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3037
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=1689)

- **FILTRO** `ibs_20min` > `0.773` → IC=-0.184 (n=659)

  - _Acción_: SKIP cuando `ibs_20min` > 0.773
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=1978)

- **PATRÓN** `ibs_20min` > `0.9128` → IC=+0.178 (n=563)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9128 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` < `0.1824` → IC=+0.229 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1824 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` < `0.9984` → IC=+0.246 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9984 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` > `0.5902` → IC=+0.224 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5902 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.261 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.272 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` > `1.7573` → IC=+0.238 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7573 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.278 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` > `0.1485` → IC=+0.219 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1485 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `1.1663` → IC=+0.217 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1663 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.257 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8106 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1331` → IC=+0.250 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1331 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.265 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.194 (n=1192)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.281 (n=1192)

- **FILTRO** `ibs_20min` > `0.6818` → IC=-0.234 (n=600)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6818
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1808)

- **FILTRO** `sigma_ewma_delta_pct` > `4.739` → IC=-0.191 (n=526)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.739
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=1882)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.281 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.8477` → IC=+0.324 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8477 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.655` → IC=+0.169 (n=376)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.655 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.306 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `0.6422` → IC=+0.298 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6422 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1016` → IC=+0.298 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1016 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2708` → IC=+0.298 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2708 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4355` → IC=+0.327 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4355 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.321 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.5789` → IC=+0.126 (n=1590)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.5789 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` < `0.2196` → IC=+0.232 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2196 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.256 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.221 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.231 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.456` → IC=+0.239 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.456 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.246 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.017)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.319 (n=951)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.281)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.297 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` > `0.7388` → IC=+0.325 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7388 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2166` → IC=+0.315 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2166 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.662` → IC=+0.305 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.662 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.295 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.329 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.290 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `2462.822` → IC=+0.290 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2462.822 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.321 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.307 (n=1016)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.1984` → IC=+0.283 (n=671)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1984 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.289 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.281 (n=762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.2903` → IC=+0.316 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2903 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.3162` → IC=+0.287 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3162 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.2297` → IC=+0.279 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2297 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.08` → IC=+0.299 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.08 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` < `0.642` → IC=+0.283 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.642 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.308 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.235` → IC=+0.331 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.235 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.289 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.139` → IC=+0.277 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.139 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `2404.9954` → IC=+0.284 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2404.9954 (IC base=+0.278)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.179 (n=2869)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.202 (n=2852)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3589` → IC=+0.177 (n=7527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3589 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=8944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.220 (n=8564)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1755` → IC=+0.193 (n=3672)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1755 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.35` → IC=+0.255 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.35 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2078` → IC=+0.163 (n=5680)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2078 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6307` → IC=+0.161 (n=5681)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6307 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2422` → IC=+0.197 (n=1728)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2422 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5592` → IC=+0.168 (n=3616)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5592 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6115` → IC=+0.176 (n=2739)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6115 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `1949.8506` → IC=+0.170 (n=7641)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1949.8506 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.182 (n=7468)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 110.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.183 (n=5494)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0067 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0816` → IC=+0.212 (n=2747)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0816 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=3934)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.4833` → IC=+0.226 (n=8237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4833 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.2359` → IC=+0.162 (n=5990)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2359 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.195 (n=1394)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.1775` → IC=+0.155 (n=5929)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1775 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.213 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5609` → IC=+0.171 (n=3322)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5609 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6202` → IC=+0.171 (n=2516)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.6202 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.178 (n=7197)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 110.0 (IC base=+0.170)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.221 (n=485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.3411` → IC=+0.212 (n=1444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3411 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=1525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=969)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.18` → IC=+0.329 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.18 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.238 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.185 (n=1341)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.239 (n=962)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.249 (n=974)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.290 (n=726)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1049)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=1007)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3469` → IC=+0.258 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3469 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.305` → IC=+0.250 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.305 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.236 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.247 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4215` → IC=+0.267 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4215 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1814.26` → IC=+0.244 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1814.26 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.241 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0719` → IC=+0.198 (n=425)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0719 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=1278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.4007` → IC=+0.229 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4007 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.210 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.472` → IC=+0.237 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.472 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.6891` → IC=+0.171 (n=561)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6891 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.0767` → IC=+0.167 (n=577)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0767 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.203 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5038` → IC=+0.179 (n=544)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5038 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.167 (n=412)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `10581.1275` → IC=+0.170 (n=1273)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10581.1275 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `444.0` → IC=+0.162 (n=1195)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 444.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.163 (n=1203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0049 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.2922` → IC=+0.163 (n=1367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2922 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.583` → IC=+0.189 (n=1367)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.583 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.161 (n=1368)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.901` → IC=+0.207 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.901 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.157 (n=1367)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2129 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1561` → IC=+0.152 (n=418)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1561 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.148 (n=1255)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.168 (n=393)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 213.0 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.214 (n=649)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.239` → IC=+0.218 (n=954)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.239 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.279 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2018` → IC=+0.207 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2018 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.7973` → IC=+0.198 (n=601)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.7973 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.7741` → IC=+0.217 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7741 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.209 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.236 (n=1075)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1015` → IC=+0.256 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1015 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.246 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.679` → IC=+0.251 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.679 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3553` → IC=+0.253 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3553 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7569` → IC=+0.222 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7569 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `3.3633` → IC=+0.236 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3633 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1907.66` → IC=+0.221 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1907.66 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.215 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.219)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.178 (n=1205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0066 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4253` → IC=+0.159 (n=1369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4253 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3687` → IC=+0.197 (n=1369)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3687 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1517` → IC=+0.176 (n=892)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1517 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.227 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.155 (n=914)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.856 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6209` → IC=+0.145 (n=1369)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6209 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.199 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.159 (n=447)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5072` → IC=+0.166 (n=447)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5072 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5442.8585` → IC=+0.186 (n=913)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 5442.8585 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.148 (n=1305)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 159.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=1443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.144 (n=1443)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6509` → IC=+0.171 (n=1443)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6509 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.961` → IC=+0.164 (n=510)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.961 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8526` → IC=+0.147 (n=962)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8526 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.179 (n=216)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.8129` → IC=+0.138 (n=880)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8129 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `9877.5526` → IC=+0.166 (n=654)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 9877.5526 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.123 (n=1257)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 156.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.152 (n=708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0101 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=1601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.204 (n=1574)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.8398` → IC=+0.207 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8398 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.76` → IC=+0.254 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.76 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2087` → IC=+0.132 (n=1560)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2087 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1638` → IC=+0.125 (n=1565)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1638 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.0983` → IC=+0.125 (n=593)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0983 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.5438` → IC=+0.135 (n=663)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.5438 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1621)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2883.9504` → IC=+0.195 (n=707)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2883.9504 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.137 (n=1201)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 48.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.159 (n=698)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0062 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.169 (n=529)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5758` → IC=+0.214 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5758 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2057` → IC=+0.145 (n=1459)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2057 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.13` → IC=+0.136 (n=256)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 9.13 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6379` → IC=+0.146 (n=529)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6379 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2309` → IC=+0.156 (n=280)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2309 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4572` → IC=+0.142 (n=479)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4572 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.134 (n=479)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2737.6784` → IC=+0.163 (n=720)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2737.6784 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.227 (n=1322)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.1351` → IC=+0.204 (n=494)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1351 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.208 (n=666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.7381` → IC=+0.261 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7381 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.5177` → IC=+0.217 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5177 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.241 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.207 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2068 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.8564` → IC=+0.222 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8564 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2303` → IC=+0.264 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2303 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.1457` → IC=+0.213 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1457 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4039` → IC=+0.210 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4039 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.206 (n=1520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2446.4744` → IC=+0.204 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2446.4744 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.222 (n=675)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.220 (n=695)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0961` → IC=+0.228 (n=512)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0961 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.0205` → IC=+0.301 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0205 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.2245` → IC=+0.224 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2245 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.402` → IC=+0.247 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.402 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6338` → IC=+0.216 (n=1533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6338 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.279 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1933` → IC=+0.199 (n=1223)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1933 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.202 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2378.577` → IC=+0.211 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2378.577 (IC base=+0.207)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.196 (n=724)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.169 (n=723)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0086 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.342` → IC=+0.165 (n=1906)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.342 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.5182` → IC=+0.193 (n=1935)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5182 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.8238` → IC=+0.177 (n=345)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.8238 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.731` → IC=+0.187 (n=968)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.731 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.8726` → IC=+0.179 (n=1288)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.8726 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.2081` → IC=+0.163 (n=644)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.2081 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.174 (n=594)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.169 (n=699)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.5338` → IC=+0.167 (n=700)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5338 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=2447)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `2202.5644` → IC=+0.161 (n=2166)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2202.5644 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.175 (n=1943)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 148.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.137 (n=1482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0057 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.130 (n=1949)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.127 (n=2219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.0596` → IC=+0.190 (n=739)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0596 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2134` → IC=+0.123 (n=2012)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.2134 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2261` → IC=+0.123 (n=2011)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2261 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.135 (n=549)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4488` → IC=+0.151 (n=714)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4488 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2755.5763` → IC=+0.124 (n=1979)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2755.5763 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.133 (n=922)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 28.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.147 (n=477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0047 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3292` → IC=+0.145 (n=542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3292 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.172 (n=508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.656` → IC=+0.203 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.656 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.291` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.291 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1618` → IC=+0.133 (n=477)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1618 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.148 (n=245)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6213` → IC=+0.183 (n=181)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6213 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.1569` → IC=+0.128 (n=560)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1569 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0915` → IC=+0.146 (n=193)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0915 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.2101` → IC=+0.135 (n=464)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2101 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.5112` → IC=+0.132 (n=471)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.5112 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `10554.1348` → IC=+0.145 (n=542)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 10554.1348 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.156 (n=344)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 231.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.206 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3387` → IC=+0.156 (n=684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3387 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6119` → IC=+0.184 (n=602)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6119 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1832` → IC=+0.153 (n=676)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1832 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.437` → IC=+0.150 (n=258)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.437 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.177` → IC=+0.138 (n=622)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.177 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2266` → IC=+0.144 (n=684)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2266 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.7175` → IC=+0.149 (n=611)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.7175 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.161 (n=593)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4135` → IC=+0.143 (n=674)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4135 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `12256.7944` → IC=+0.136 (n=611)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 12256.7944 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `318.0` → IC=+0.150 (n=575)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 318.0 (IC base=+0.136)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.273 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2022` → IC=+0.219 (n=454)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2022 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.9648` → IC=+0.269 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9648 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1455` → IC=+0.210 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1455 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2163` → IC=+0.208 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2163 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.949` → IC=+0.231 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.949 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.8358` → IC=+0.213 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8358 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.1625` → IC=+0.229 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1625 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.1546` → IC=+0.255 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1546 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4099` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4099 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.1032` → IC=+0.239 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1032 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `12351.8233` → IC=+0.207 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12351.8233 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.120 (n=559)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0062 (IC base=+0.094)

- **PATRÓN** `drift_60min` |x|≤ `0.0997` → IC=+0.136 (n=212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.0997 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.0839` → IC=+0.154 (n=212)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.0839 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6887` → IC=+0.138 (n=280)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6887 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2277` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2277 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `9091.9696` → IC=+0.121 (n=423)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 9091.9696 (IC base=+0.094)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.148 (n=475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0058 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.5372` → IC=+0.135 (n=532)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.5372 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.170 (n=495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.9868` → IC=+0.237 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9868 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.556` → IC=+0.193 (n=285)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.556 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.069` → IC=+0.155 (n=468)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.069 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.7219` → IC=+0.139 (n=475)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.7219 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.162 (n=72)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4824` → IC=+0.142 (n=171)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4824 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `2.212` → IC=+0.167 (n=232)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.212 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.139 (n=554)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2963.0907` → IC=+0.187 (n=241)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2963.0907 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.4188` → IC=+0.171 (n=432)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.4188 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.22` → IC=+0.123 (n=491)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.22 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.8498` → IC=+0.165 (n=311)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.8498 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2918.7797` → IC=+0.153 (n=223)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2918.7797 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.143 (n=441)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 40.0 (IC base=+0.099)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.175 (n=3699)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0047 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.208 (n=3685)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=11550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=3684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.939` → IC=+0.201 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.939 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.875` → IC=+0.238 (n=4038)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.875 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.8807` → IC=+0.170 (n=4932)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8807 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.201 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5905` → IC=+0.192 (n=3551)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5905 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `1788.6777` → IC=+0.176 (n=11049)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1788.6777 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.198 (n=8527)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 83.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.191 (n=6682)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1497` → IC=+0.190 (n=4402)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1497 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=3748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=4655)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.4497` → IC=+0.247 (n=8804)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4497 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2512` → IC=+0.162 (n=6257)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2512 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.061` → IC=+0.201 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.061 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.739` → IC=+0.184 (n=9676)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.739 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.162 (n=3009)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7056 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.240 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6125` → IC=+0.190 (n=3082)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6125 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.199 (n=5927)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 46.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.218 (n=619)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.208 (n=1236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.3541` → IC=+0.196 (n=1852)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3541 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.211 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.199 (n=1258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.6` → IC=+0.346 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.6 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2272` → IC=+0.249 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2272 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.561` → IC=+0.199 (n=585)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.561 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.260 (n=990)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.263 (n=1484)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.126` → IC=+0.287 (n=654)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.126 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=1340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.259 (n=1357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.3551` → IC=+0.283 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3551 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.507` → IC=+0.264 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.507 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.286 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.5484` → IC=+0.257 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5484 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.622` → IC=+0.276 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.622 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1998.7` → IC=+0.267 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1998.7 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.204 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.165 (n=779)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3058` → IC=+0.205 (n=1767)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3058 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.126` → IC=+0.187 (n=984)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.126 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.699` → IC=+0.177 (n=400)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.699 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.167` → IC=+0.154 (n=1601)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.167 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6277` → IC=+0.186 (n=590)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6277 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2665` → IC=+0.195 (n=257)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2665 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1149` → IC=+0.163 (n=1507)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1149 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.7577` → IC=+0.160 (n=1141)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7577 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `11197.4423` → IC=+0.160 (n=1579)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11197.4423 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `470.0` → IC=+0.163 (n=1644)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 470.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.188 (n=510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0026 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.32` → IC=+0.161 (n=1522)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.32 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=690)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.2856` → IC=+0.234 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2856 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6691` → IC=+0.157 (n=240)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6691 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1321` → IC=+0.162 (n=1394)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1321 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.52` → IC=+0.164 (n=254)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.52 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.327` → IC=+0.151 (n=1386)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.327 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.162 (n=1522)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1954 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.197 (n=404)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.4038` → IC=+0.159 (n=1424)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4038 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.757` → IC=+0.160 (n=949)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.757 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `415.0` → IC=+0.153 (n=1167)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 415.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.253 (n=601)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=1890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=1830)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.304 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1345` → IC=+0.218 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1345 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.6227` → IC=+0.226 (n=1723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6227 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1916.24` → IC=+0.223 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1916.24 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.239 (n=1688)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1774` → IC=+0.241 (n=742)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1774 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.240 (n=797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3584` → IC=+0.265 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3584 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.758` → IC=+0.273 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.758 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3431` → IC=+0.300 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3431 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.232 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1608` → IC=+0.238 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1608 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1908.002` → IC=+0.243 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.002 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.258 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.188 (n=829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4318` → IC=+0.151 (n=1885)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4318 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=1968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.873` → IC=+0.262 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.873 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3624` → IC=+0.161 (n=723)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3624 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.523` → IC=+0.169 (n=309)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.523 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8727` → IC=+0.159 (n=1257)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8727 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2798` → IC=+0.213 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2798 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5207` → IC=+0.154 (n=805)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5207 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.4717` → IC=+0.157 (n=610)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4717 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7831.4295` → IC=+0.236 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7831.4295 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.173 (n=592)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 75.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.166 (n=1023)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0052 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4386` → IC=+0.146 (n=1533)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4386 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=705)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.5853` → IC=+0.198 (n=1349)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5853 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1596` → IC=+0.136 (n=1340)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1596 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.285` → IC=+0.162 (n=229)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.285 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6987` → IC=+0.150 (n=676)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6987 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.2015` → IC=+0.139 (n=511)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.2015 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.232 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4439` → IC=+0.144 (n=1460)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4439 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `7029.3381` → IC=+0.193 (n=695)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7029.3381 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `172.0` → IC=+0.137 (n=1456)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 172.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.139 (n=1253)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0081 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.463` → IC=+0.192 (n=1880)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.463 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.0849` → IC=+0.203 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0849 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.529` → IC=+0.241 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.529 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.8929` → IC=+0.140 (n=1254)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8929 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=1893)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2884.9328` → IC=+0.255 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2884.9328 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.135 (n=1472)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 53.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.174 (n=603)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0058 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1336` → IC=+0.156 (n=602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1336 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.205 (n=1805)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2221` → IC=+0.133 (n=1482)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2221 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.449` → IC=+0.126 (n=1742)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.449 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.155 (n=795)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7144 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.221` → IC=+0.169 (n=282)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.221 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.142 (n=548)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2767.152` → IC=+0.175 (n=602)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2767.152 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.126 (n=1432)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 51.0 (IC base=+0.114)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0272` → IC=+0.213 (n=1867)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0272 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.230 (n=1667)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=1954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.213 (n=1677)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.263 (n=1671)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.2144` → IC=+0.233 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2144 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.245` → IC=+0.267 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.245 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2484` → IC=+0.215 (n=1867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2484 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6423` → IC=+0.223 (n=1866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6423 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2322` → IC=+0.248 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2322 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.4384` → IC=+0.220 (n=1806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4384 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1888)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2436.9552` → IC=+0.218 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2436.9552 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.221 (n=660)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.229 (n=661)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.217 (n=1389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.265 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `1.2367` → IC=+0.207 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2367 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.2159` → IC=+0.211 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2159 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.261 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `1.2365` → IC=+0.237 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2365 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.270 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.176` → IC=+0.203 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.176 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4282` → IC=+0.202 (n=1790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4282 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2385.287` → IC=+0.207 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2385.287 (IC base=+0.206)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=3399)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.185 (n=2979)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0092 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.3994` → IC=+0.180 (n=2979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3994 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=1303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.177 (n=1518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.235 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1852` → IC=+0.182 (n=1218)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1852 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.4754` → IC=+0.168 (n=2143)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.4754 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.157` → IC=+0.200 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.157 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.7075` → IC=+0.167 (n=990)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.7075 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.8924` → IC=+0.175 (n=1499)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8924 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1701` → IC=+0.203 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1701 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.4558` → IC=+0.181 (n=1116)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4558 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.869` → IC=+0.179 (n=2229)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.869 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=2412)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `2819.2566` → IC=+0.174 (n=3024)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2819.2566 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.202 (n=859)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3834` → IC=+0.176 (n=2254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3834 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.174 (n=1142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.1794` → IC=+0.180 (n=1127)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1794 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.6833` → IC=+0.175 (n=469)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.6833 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.203` → IC=+0.164 (n=2560)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.203 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.1012` → IC=+0.162 (n=2116)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1012 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.159 (n=2333)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.5391` → IC=+0.165 (n=1113)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5391 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.161 (n=1686)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=3399)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `12357.2708` → IC=+0.160 (n=854)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12357.2708 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.160 (n=1663)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 86.0 (IC base=+0.154)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.201 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0866` → IC=+0.232 (n=140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0866 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.193 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5452` → IC=+0.208 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5452 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1455` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1455 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.3655` → IC=+0.190 (n=407)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.3655 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.188 (n=443)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.8386` → IC=+0.212 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8386 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2983` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2983 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.211 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6272` → IC=+0.204 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6272 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `12545.7532` → IC=+0.221 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12545.7532 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.217 (n=425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.176 (n=322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.175 (n=367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.181 (n=424)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1409 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6109` → IC=+0.146 (n=436)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6109 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6926` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6926 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.162 (n=942)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8794` → IC=+0.187 (n=641)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8794 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0686` → IC=+0.166 (n=447)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0686 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4202` → IC=+0.146 (n=320)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4202 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.150 (n=639)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `14904.1418` → IC=+0.160 (n=436)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 14904.1418 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `707.0` → IC=+0.144 (n=916)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 707.0 (IC base=+0.139)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.187 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.178 (n=284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.01 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.5778` → IC=+0.172 (n=627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.5778 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.235 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.732` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.732 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.3498` → IC=+0.168 (n=754)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.3498 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.201 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.6744` → IC=+0.168 (n=209)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.6744 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.825` → IC=+0.168 (n=559)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.825 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2426.4931` → IC=+0.196 (n=284)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2426.4931 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.324 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.261 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.273 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.158` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.158 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `2362.106` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.106 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.183 (n=928)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0072 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3745` → IC=+0.181 (n=928)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3745 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.183 (n=361)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 4.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.190 (n=704)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5305 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.8825` → IC=+0.184 (n=352)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8825 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.2131` → IC=+0.182 (n=876)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2131 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.19` → IC=+0.185 (n=943)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 4.19 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.0828` → IC=+0.176 (n=928)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0828 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.177 (n=1055)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6398 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.194 (n=318)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.4754` → IC=+0.180 (n=1036)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.4754 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.176 (n=927)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=1051)

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
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.160 (n=280)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0109 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3752` → IC=+0.137 (n=213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3752 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.162 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 4.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.139 (n=322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 14.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.95` → IC=+0.255 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.95 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.2235` → IC=+0.193 (n=216)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2235 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `1.392` → IC=+0.137 (n=342)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 1.392 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.028` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.028 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8838` → IC=+0.170 (n=213)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8838 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.224 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5448` → IC=+0.145 (n=136)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5448 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.424` → IC=+0.156 (n=309)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.424 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=377)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3057.4549` → IC=+0.156 (n=318)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3057.4549 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.155 (n=265)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 53.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.184 (n=270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0069 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.198 (n=180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.179 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 10.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.2647` → IC=+0.227 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2647 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.6343` → IC=+0.235 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6343 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.669` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.669 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.258` → IC=+0.165 (n=261)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 5.258 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.756` → IC=+0.178 (n=119)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.756 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.224 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.522` → IC=+0.178 (n=88)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.522 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `3214.2568` → IC=+0.195 (n=270)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3214.2568 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.200 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.154)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.196 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=416)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.171 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0039 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.649` → IC=+0.186 (n=843)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.649 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.1475` → IC=+0.141 (n=500)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1475 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.189 (n=220)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.188 (n=126)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.080)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.124 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0045 (IC base=+0.029)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.301 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1816` → IC=+0.134 (n=383)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1816 (IC base=+0.029)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.121` → IC=+0.139 (n=128)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.121 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.138` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.138 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.139 (n=278)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.437` → IC=+0.136 (n=248)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.437 (IC base=+0.029)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=287)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.029)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.143 (n=357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0058 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.4669` → IC=+0.180 (n=326)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4669 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.175 (n=167)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `2.392` → IC=+0.139 (n=286)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.392 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.133 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0044 (IC base=+0.076)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.160 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.0673` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0673 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.92` → IC=+0.185 (n=147)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 6.92 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `1.1209` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1209 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.0669` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0669 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.076)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6606` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6606
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=285)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=134)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.138 (n=233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0049 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.123 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.6606` → IC=+0.214 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6606 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.3353` → IC=+0.177 (n=122)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.3353 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.74` → IC=+0.288 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.74 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.7387` → IC=+0.142 (n=177)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.7387 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `1126.4134` → IC=+0.143 (n=281)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1126.4134 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.1674` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1674 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` < `0.1283` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1283 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.256` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.256 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.3281` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.3281 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.1925` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.1925 (IC base=+0.009)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=93)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.009)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.265 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=98)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.236 (n=70)

- **PATRÓN** `ibs_20min` > `0.7843` → IC=+0.183 (n=200)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7843 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.204` → IC=+0.123 (n=83)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 8.204 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.052)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.145 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0066 (IC base=-0.024)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=-0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.815` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.815 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1002` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1002 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.4839` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.4839 (IC base=-0.024)

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

- **FILTRO** `sigma_h` > `0.005` → IC=-0.357 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=121)

- **FILTRO** `drift_60min` |x|> `0.2212` → IC=-0.322 (n=43)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2212
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=133)

- **FILTRO** `dist_vwap_pct` > `0.338` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.338
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=150)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=80)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.250 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=39)

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
- **FILTRO** `ibs_20min` > `0.1667` → IC=-0.132 (n=131)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1667
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=256)

- **FILTRO** `dist_vwap_pct` > `0.6344` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6344
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=361)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.154 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0059 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.6417` → IC=+0.143 (n=281)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6417 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.5013` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.5013 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.178 (n=256)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1667 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.179 (n=132)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.073)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=101)

- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=93)

- **FILTRO** `volumen_regimen` < `0.7924` → IC=-0.188 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7924
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=93)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.170 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0034 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.206 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.101` → IC=+0.217 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.101 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.0646` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.0646 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.611` → IC=+0.145 (n=108)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.611 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.138` → IC=+0.147 (n=134)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.138 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.2815` → IC=+0.174 (n=90)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.2815 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.154 (n=102)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.133)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6191` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6191
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=77)

- **FILTRO** `volumen_pendiente_norm` > `0.0671` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0671
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=42)

- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=84)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.194 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0022 (IC base=+0.010)

- **PATRÓN** `ibs_20min` > `0.8782` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.8782 (IC base=+0.010)

- **PATRÓN** `libro_liquidez` > `1624.9844` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1624.9844 (IC base=+0.010)

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
- **FILTRO** `ibs_20min` > `0.1837` → IC=-0.174 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1837
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.256 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.217 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.7027` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7027 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.397 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.0984` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0984 (IC base=-0.041)

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

- **PATRÓN** `elapsed_s` > `184.2` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.2 (IC base=+0.222)

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

- **PATRÓN** `elapsed_s` > `184.2` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.2 (IC base=+0.222)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=795)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2903.2529` → IC=+0.161 (n=272)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2903.2529 (IC base=+0.105)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=795)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2903.2529` → IC=+0.161 (n=272)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2903.2529 (IC base=+0.105)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.199 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=85)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=140)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=219)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=205)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=44)

- **FILTRO** `libro_liquidez` < `10452.0502` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 10452.0502
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

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

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=89)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1972)

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
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=87)

- **PATRÓN** `libro_liquidez` > `2413.9166` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2413.9166 (IC base=+0.040)

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

- **PATRÓN** `liq_n` > `18.0` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.016)

- **PATRÓN** `liq_usd_total` > `68754.71` → IC=+0.164 (n=108)

  - _Acción_: Kelly boost +0.82€ cuando `liq_usd_total` > 68754.71 (IC base=+0.016)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=147)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=857)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=811)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=450)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=206)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.495 (IC base=+0.013)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=669)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=669)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=407)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=407)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=178)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=178)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.141 (n=62)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=131)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=98)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=122)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=223)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=100)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=103)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=253)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=253)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.152 (n=67)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=216)

- **FILTRO** `libro_liquidez` < `516.7992` → IC=-0.121 (n=93)

  - _Acción_: SKIP cuando `libro_liquidez` < 516.7992
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=190)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=145)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.140 (n=354)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=906)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.136 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=115)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.53 (IC base=+0.018)

- **PATRÓN** `profundidad_ratio` > `592.3` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `profundidad_ratio` > 592.3 (IC base=+0.018)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.56 (IC base=+0.067)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` > `13.48` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `restante_min` > 13.48
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=70)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.267 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=60)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `profundidad_ratio` < `21.7` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `profundidad_ratio` < 21.7
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=64)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.138 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 9.0 (IC base=+0.080)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.127 (n=73)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=28)

- **FILTRO** `profundidad_ratio` < `37.2` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.2
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=76)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=96)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.53 (IC base=-0.034)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=108)

- **FILTRO** `restante_min` < `3.25` → IC=-0.324 (n=32)

  - _Acción_: SKIP cuando `restante_min` < 3.25
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=101)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.233 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=90)

- **FILTRO** `lag_apertura_s` > `88.26` → IC=-0.308 (n=45)

  - _Acción_: SKIP cuando `lag_apertura_s` > 88.26
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=88)

- **FILTRO** `profundidad_ratio` < `81.9` → IC=-0.221 (n=66)

  - _Acción_: SKIP cuando `profundidad_ratio` < 81.9
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=67)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.44 (IC base=+0.061)

- **PATRÓN** `profundidad_ratio` > `53.3` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `profundidad_ratio` > 53.3 (IC base=+0.061)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `restante_min` < `13.48` → IC=-0.144 (n=71)

  - _Acción_: SKIP cuando `restante_min` < 13.48
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=38)

- **FILTRO** `lag_apertura_s` > `90.99` → IC=-0.127 (n=73)

  - _Acción_: SKIP cuando `lag_apertura_s` > 90.99
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=36)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 13.48 (IC base=-0.041)

- **PATRÓN** `lag_apertura_s` < `90.99` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `lag_apertura_s` < 90.99 (IC base=-0.041)

- **PATRÓN** `lag_apertura_s` < `91.0` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 91.0 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.140 (n=98)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=57)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.5 (IC base=-0.029)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.250 (n=54)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=128)

- **FILTRO** `restante_min` < `2.81` → IC=-0.160 (n=45)

  - _Acción_: SKIP cuando `restante_min` < 2.81
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=137)

- **FILTRO** `lag_apertura_s` > `131.11` → IC=-0.160 (n=45)

  - _Acción_: SKIP cuando `lag_apertura_s` > 131.11
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=137)

- **FILTRO** `profundidad_ratio` < `6.1` → IC=-0.160 (n=45)

  - _Acción_: SKIP cuando `profundidad_ratio` < 6.1
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=137)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.168 (n=3834)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=11809)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.161 (n=3992)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=12254)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.206 (n=662)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=2074)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.187 (n=685)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2102)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=699)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2227)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.173 (n=670)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=2060)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.172 (n=721)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=2203)

- **PATRÓN** `libro_liquidez` > `2577.5669` → IC=+0.121 (n=929)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 2577.5669 (IC base=+0.022)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2222)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2322)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3062)

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
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=265)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=259)

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
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=24590)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=8822)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=26740)

- **FILTRO** `ibs_7min` < `0.2739` → IC=-0.235 (n=8890)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2739
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=26672)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=11910)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=23652)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.231 (n=11006)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=33941)

- **FILTRO** `ibs_7min` > `0.2917` → IC=-0.177 (n=11213)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2917
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33734)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=1790)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4155)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=1414)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4531)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.253 (n=1958)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3987)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.175 (n=1455)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4490)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.261 (n=1916)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=5809)

- **FILTRO** `ibs_7min` > `0.7875` → IC=-0.207 (n=1931)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7875
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=5794)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=4681)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1494)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4624)

- **FILTRO** `ibs_7min` < `0.7459` → IC=-0.198 (n=1529)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7459
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4589)

- **FILTRO** `ballena_activa_n` > `158.0` → IC=-0.180 (n=1522)

  - _Acción_: SKIP cuando `ballena_activa_n` > 158.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4596)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=1439)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4789)

- **FILTRO** `ibs_7min` > `0.2614` → IC=-0.184 (n=1556)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2614
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4672)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.181 (n=1555)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4673)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.170 (n=1385)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=4267)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.305 (n=1411)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4241)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.244 (n=1860)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3792)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.210 (n=1396)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4256)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=1912)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=6375)

- **FILTRO** `ibs_7min` > `0.7465` → IC=-0.173 (n=2071)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7465
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=6216)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=1885)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3971)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.234 (n=1725)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=4131)

- **FILTRO** `ibs_7min` < `0.741` → IC=-0.181 (n=1464)

  - _Acción_: SKIP cuando `ibs_7min` < 0.741
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4392)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.174 (n=1426)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=4430)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.256 (n=1504)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=4515)

- **FILTRO** `ibs_7min` > `0.2759` → IC=-0.175 (n=1503)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4516)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.182 (n=1489)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4530)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.262 (n=1437)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4690)

- **FILTRO** `ibs_7min` < `0.2821` → IC=-0.233 (n=1529)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2821
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4598)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.167 (n=2139)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=6433)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=1440)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4424)

- **FILTRO** `ibs_7min` < `0.29` → IC=-0.223 (n=1466)

  - _Acción_: SKIP cuando `ibs_7min` < 0.29
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4398)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1397)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4467)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.206 (n=1899)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=6217)

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
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=332)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=573)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.132 (n=805)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `471.727` → IC=+0.138 (n=269)

  - _Acción_: Kelly boost +0.69€ cuando `total_vol_5m` < 471.727 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.135 (n=61)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.197 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 11.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.132 (n=161)

  - _Acción_: Kelly boost +0.66€ cuando `total_vol_5m` < 445.688 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2333.2912` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2333.2912 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 14.0 (IC base=+0.129)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.192 (n=50)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 8.0 (IC base=+0.108)

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
- **PATRÓN** `delta_ratio` |x|> `0.4006` → IC=+0.146 (n=145)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4006 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.135 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 13.0 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.105)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.007` → IC=-0.325 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=276)

- **FILTRO** `T_h` > `51.9942` → IC=-0.243 (n=278)

  - _Acción_: SKIP cuando `T_h` > 51.9942
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=139)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.367 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=85)

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
- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.400 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=88)

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

- **PATRÓN** `dist_50` > `0.5` → IC=+0.484 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.5 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.467 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=203)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=308)

- **FILTRO** `streak_estiramiento` > `0.8566` → IC=-0.162 (n=66)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8566
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=201)

- **PATRÓN** `streak_estiramiento` < `0.4787` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.4787 (IC base=+0.036)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=433)

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
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=664)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1220)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=819)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=794)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3092)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1560)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1568)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.194 (n=600)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0043 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.226 (n=600)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.201 (n=600)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2173` → IC=+0.191 (n=600)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2173 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.235 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=1689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.189 (n=1872)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.6087` → IC=+0.267 (n=1799)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6087 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.184 (n=901)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.822` → IC=+0.273 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.822 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `8780.1789` → IC=+0.196 (n=600)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 8780.1789 (IC base=+0.188)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=741)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.222 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.285 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.209)

- **PATRÓN** `drift_15min` |x|≤ `0.3838` → IC=+0.218 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3838 (IC base=+0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.248 (n=133)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.209)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.282 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.242 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.209)

- **PATRÓN** `ibs_15` > `0.7061` → IC=+0.276 (n=399)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7061 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.537` → IC=+0.272 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.537 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `16060.5409` → IC=+0.233 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16060.5409 (IC base=+0.209)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.849` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.849
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=453)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.171 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0035 (IC base=+0.131)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.136 (n=281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.005 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.160 (n=186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.171 (n=141)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.131)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1251` → IC=+0.160 (n=154)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1251 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.132 (n=424)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 16.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.659` → IC=+0.252 (n=377)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.659 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1154` → IC=+0.144 (n=304)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1154 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.307` → IC=+0.217 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.307 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4165.118` → IC=+0.143 (n=281)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4165.118 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.284 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1481` → IC=+0.196 (n=189)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1481 (IC base=+0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0767` → IC=+0.184 (n=191)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio_macro` |x|> 0.0767 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.191 (n=205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.255 (n=214)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.177 (n=122)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.176 (n=208)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=154)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `3071.8702` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3071.8702 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.203 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.172)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.6927` → IC=-0.150 (n=101)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6927
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1124)

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
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.357 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.349)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.374 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.349)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.350 (n=299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.349)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.361 (n=445)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.349)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.388 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.349)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.368 (n=452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.349)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.388 (n=446)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.349)

- **PATRÓN** `dist_vwap_pct` > `0.4241` → IC=+0.389 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4241 (IC base=+0.349)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.357` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.357 (IC base=+0.349)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.351 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.349)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.352 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.349)

- **PATRÓN** `libro_liquidez` > `3813.5418` → IC=+0.365 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3813.5418 (IC base=+0.349)

- **PATRÓN** `ballena_activa_n` < `457.0` → IC=+0.369 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 457.0 (IC base=+0.349)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.363 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.381 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.371 (n=83)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.354)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.365 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0763` → IC=+0.363 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0763 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.395 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.380 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.387 (n=246)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.405 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.360 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.358 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `11121.9309` → IC=+0.373 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11121.9309 (IC base=+0.354)

- **PATRÓN** `ballena_activa_n` < `571.0` → IC=+0.400 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 571.0 (IC base=+0.354)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.371 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.340)

- **PATRÓN** `drift_60min` |x|≤ `0.1054` → IC=+0.346 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1054 (IC base=+0.340)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.362 (n=179)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.340)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.369 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.340)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.405 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.340)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.391 (n=200)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.340)

- **PATRÓN** `dist_vwap_pct` > `0.4453` → IC=+0.361 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4453 (IC base=+0.340)

- **PATRÓN** `dist_vwap_pct` < `0.1175` → IC=+0.350 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1175 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.350 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.340)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.346 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.340)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.345 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `3456.6166` → IC=+0.352 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3456.6166 (IC base=+0.340)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.223 (n=710)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2133)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.204 (n=985)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1858)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.253 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6409` → IC=+0.271 (n=679)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6409 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2685` → IC=+0.188 (n=550)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2685 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1211` → IC=+0.250 (n=1341)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1211 (IC base=-0.028)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1804` → IC=+0.242 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1804 (IC base=-0.028)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.274 (n=2012)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.6821` → IC=+0.296 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6821 (IC base=-0.028)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.213 (n=430)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=1293)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.225 (n=568)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1155)

- **FILTRO** `sigma_ewma_delta_pct` > `19.563` → IC=-0.254 (n=307)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.563
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1416)

- **FILTRO** `libro_liquidez` < `16347.0192` → IC=-0.203 (n=1137)

  - _Acción_: SKIP cuando `libro_liquidez` < 16347.0192
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=586)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.159 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0028 (IC base=+0.081)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2587` → IC=+0.276 (n=65)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2587 (IC base=+0.081)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1066` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1066 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.333 (n=195)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.099` → IC=+0.282 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.099 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.270 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2353 (IC base=+0.081)

- **PATRÓN** `ibs_15` < `0.213` → IC=+0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.213 (IC base=-0.199)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=412)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.151 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0067 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.169 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.004 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.215 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.147)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.182 (n=108)

  - _Acción_: Kelly boost +0.91€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3062` → IC=+0.236 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3062 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.6647` → IC=+0.256 (n=322)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6647 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1047` → IC=+0.175 (n=232)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1047 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.024` → IC=+0.151 (n=276)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 9.024 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=412)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `11031.3332` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 11031.3332 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.249 (n=778)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3574` → IC=+0.240 (n=684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3574 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.4747` → IC=+0.256 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4747 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2073` → IC=+0.258 (n=353)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2073 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.247 (n=299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.273` → IC=+0.281 (n=684)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.273 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.7528` → IC=+0.315 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7528 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.827` → IC=+0.250 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.827 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.346` → IC=+0.241 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.346 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.247 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=505)

- **FILTRO** `drift_60min` |x|> `0.1704` → IC=-0.221 (n=227)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1704
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=446)

- **FILTRO** `drift_15min` |x|> `0.8922` → IC=-0.271 (n=168)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8922
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=505)

- **FILTRO** `sigma_ewma_delta_pct` > `18.215` → IC=-0.138 (n=360)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.215
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2887)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.192 (n=50)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.5625 (IC base=-0.173)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0776` → IC=+0.230 (n=309)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0776 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.3462` → IC=+0.259 (n=346)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3462 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7501` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7501 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.1863` → IC=+0.225 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1863 (IC base=-0.041)

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
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.303 (n=481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.291 (n=721)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.327 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2427` → IC=+0.306 (n=240)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2427 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1083` → IC=+0.339 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1083 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=758)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8405` → IC=+0.329 (n=721)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8405 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.339 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.348 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.291 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `14480.7481` → IC=+0.298 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14480.7481 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.294 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.289 (n=353)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.343 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2631` → IC=+0.304 (n=131)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2631 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.313 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.318 (n=394)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.4139` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4139 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.367 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.328 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.310 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.312 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1511` → IC=+0.300 (n=218)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1511 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3017` → IC=+0.326 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3017 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.342 (n=327)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.4471` → IC=+0.306 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4471 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.329 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.297 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.294)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6087 sube el IC de +0.188 a +0.267 en UPDOWN_GBM#15min (n=1799). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7061 sube el IC de +0.209 a +0.276 en UPDOWN_GBM#BTC#15min (n=399). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.659 sube el IC de +0.131 a +0.252 en UPDOWN_GBM#ETH#15min (n=377). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.172 a +0.255 en UPDOWN_GBM#SOL#15min (n=214). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5695 sube el IC de +0.196 a +0.286 en UPDOWN_GBM#XRP#15min (n=465). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.053 a +0.150 en UPDOWN_GBM#XRP#15min (n=524). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6409 sube el IC de -0.067 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=679). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.028 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=2012). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.081 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=195). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.213 sube el IC de -0.199 a +0.382 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.147 a +0.256 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=322). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.273 sube el IC de +0.234 a +0.281 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=684). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.173 a +0.192 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=50). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3462 sube el IC de -0.041 a +0.259 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=346). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3391 sube el IC de -0.039 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8405 sube el IC de +0.291 a +0.329 en UPDOWN_GBM_IBS_ALTO (n=721). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.287 a +0.318 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=394). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.294 a +0.342 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=327). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.349 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=446). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.354 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.340 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=200). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1397 | +0.100 | +198.87€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1397 | +0.100 | +198.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 28 | +0.000 | -4.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 28 | +0.000 | -4.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1054 | +0.110 | +174.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1054 | +0.110 | +174.39€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 29993 | -0.083 | -3972.99€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1579 | -0.028 | -214.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 28414 | -0.086 | -3758.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3892 | -0.097 | -649.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3892 | -0.097 | -649.73€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1579 | -0.028 | -214.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1579 | -0.028 | -214.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3533 | -0.099 | -807.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3533 | -0.099 | -807.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7782 | -0.014 | -715.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7782 | -0.014 | -715.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7322 | -0.088 | -459.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7322 | -0.088 | -459.47€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5885 | -0.162 | -1125.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5885 | -0.162 | -1125.60€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 20691 | -0.025 | +3859.33€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5358 | +0.001 | +1790.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 15333 | -0.034 | +2068.67€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 20691 | -0.025 | +3859.33€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5358 | +0.001 | +1790.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 15333 | -0.034 | +2068.67€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1479 | -0.103 | -190.98€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 169 | -0.050 | -20.37€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 781 | -0.090 | -96.64€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 145 | -0.044 | -15.15€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 100625 | +0.113 | -4866.92€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14825 | +0.184 | -454.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 411 | -0.069 | -51.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 78963 | +0.101 | -4139.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6426 | +0.107 | -221.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 13125 | +0.100 | -1042.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 48 | -0.160 | +1.58€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 13062 | +0.101 | -1031.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 20255 | +0.132 | -364.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4635 | +0.201 | -139.13€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 13094 | +0.114 | -170.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2484 | +0.099 | -33.11€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13163 | +0.090 | -1170.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 54 | -0.107 | -8.00€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 13094 | +0.092 | -1150.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 21371 | +0.124 | -387.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5793 | +0.176 | -75.07€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13239 | +0.106 | -243.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2327 | +0.100 | -60.41€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 19575 | +0.114 | -1123.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4246 | +0.187 | -243.12€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 314 | -0.029 | +2.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13400 | +0.092 | -754.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1615 | +0.130 | -128.39€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13136 | +0.100 | -779.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 49 | -0.029 | +9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 13074 | +0.101 | -788.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 15983 | +0.193 | -1025.56€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 15983 | +0.193 | -1025.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3779 | +0.167 | -398.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3779 | +0.167 | -398.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1477 | +0.204 | -4.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1477 | +0.204 | -4.70€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3716 | +0.180 | -314.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3716 | +0.180 | -314.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3281 | +0.241 | -102.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3281 | +0.241 | -102.62€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3651 | +0.192 | -218.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3651 | +0.192 | -218.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 755 | +0.429 | -22.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 755 | +0.429 | -22.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 294 | +0.439 | -2.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 294 | +0.439 | -2.03€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 287 | +0.427 | -8.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 287 | +0.427 | -8.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 164 | +0.410 | -9.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 164 | +0.410 | -9.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 55250 | +0.197 | -4309.47€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 55250 | +0.197 | -4309.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9527 | +0.178 | -1080.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9527 | +0.178 | -1080.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8842 | +0.223 | -328.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8842 | +0.223 | -328.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9538 | +0.174 | -1118.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9538 | +0.174 | -1118.36€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8939 | +0.217 | -370.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8939 | +0.217 | -370.74€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9137 | +0.203 | -602.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9137 | +0.203 | -602.88€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9267 | +0.193 | -808.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9267 | +0.193 | -808.85€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 20915 | +0.117 | +170.32€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 20915 | +0.117 | +170.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10387 | +0.120 | +130.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10387 | +0.120 | +130.93€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10528 | +0.114 | +39.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10528 | +0.114 | +39.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1567 | +0.288 | -25.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1567 | +0.288 | -25.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 700 | +0.278 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 700 | +0.278 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 754 | +0.287 | -9.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 754 | +0.287 | -9.82€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 113 | +0.344 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 113 | +0.344 | +2.86€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 696 | +0.434 | -6.36€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 696 | +0.434 | -6.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 333 | +0.431 | -5.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 333 | +0.431 | -5.54€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 318 | +0.438 | -1.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 318 | +0.438 | -1.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1194 | +0.065 | -66.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 421 | +0.046 | -43.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 773 | +0.075 | -22.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 62 | +0.109 | +2.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 62 | +0.109 | +2.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 942 | +0.073 | -32.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 169 | +0.061 | -9.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 773 | +0.075 | -22.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 190 | +0.010 | -35.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 190 | +0.010 | -35.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 39265 | +0.098 | -1121.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3221 | +0.089 | +19.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 36044 | +0.099 | -1141.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 21939 | +0.102 | -321.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3221 | +0.089 | +19.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 18718 | +0.105 | -341.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7530 | +0.110 | -10.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7530 | +0.110 | -10.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9796 | +0.080 | -789.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9796 | +0.080 | -789.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 849 | +0.214 | -101.09€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 849 | +0.214 | -101.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 849 | +0.214 | -101.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 849 | +0.214 | -101.09€ | 2 | 4 |
| ✅ GBM_LATE_15M | 27895 | +0.085 | +13567.19€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 27895 | +0.085 | +13567.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4665 | +0.197 | +3463.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4665 | +0.197 | +3463.74€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4151 | +0.178 | +2966.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4151 | +0.178 | +2966.77€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 4906 | +0.198 | +3658.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4906 | +0.198 | +3658.21€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4038 | +0.026 | +952.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4038 | +0.026 | +952.03€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3975 | -0.032 | +916.14€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3975 | -0.032 | +916.14€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 6160 | -0.040 | +1610.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6160 | -0.040 | +1610.29€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 29684 | +0.086 | +15695.47€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 29684 | +0.086 | +15695.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5651 | +0.012 | +2967.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5651 | +0.012 | +2967.80€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6198 | +0.015 | +1319.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6198 | +0.015 | +1319.95€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4222 | +0.265 | +4291.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4222 | +0.265 | +4291.63€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4888 | +0.005 | +975.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4888 | +0.005 | +975.83€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4792 | +0.030 | +1884.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4792 | +0.030 | +1884.56€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3933 | +0.280 | +4255.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3933 | +0.280 | +4255.70€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 22386 | +0.170 | +17009.32€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 22386 | +0.170 | +17009.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3375 | +0.209 | +2717.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3375 | +0.209 | +2717.13€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3519 | +0.150 | +2612.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3519 | +0.150 | +2612.06€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3534 | +0.209 | +2825.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3534 | +0.209 | +2825.24€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3748 | +0.133 | +2665.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3748 | +0.133 | +2665.31€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4194 | +0.118 | +2990.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4194 | +0.118 | +2990.37€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4016 | +0.205 | +3199.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4016 | +0.205 | +3199.21€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5840 | +0.135 | +2656.48€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5840 | +0.135 | +2656.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1633 | +0.134 | +807.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1633 | +0.134 | +807.70€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1753 | +0.152 | +840.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1753 | +0.152 | +840.03€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1362 | +0.117 | +529.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1362 | +0.117 | +529.41€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 28070 | +0.177 | +21294.65€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 28070 | +0.177 | +21294.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4447 | +0.224 | +3809.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4447 | +0.224 | +3809.01€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4385 | +0.152 | +2943.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4385 | +0.152 | +2943.14€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4648 | +0.226 | +4003.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4648 | +0.226 | +4003.77€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4555 | +0.136 | +3163.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4555 | +0.136 | +3163.28€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4912 | +0.116 | +3258.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4912 | +0.116 | +3258.92€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5123 | +0.209 | +4116.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5123 | +0.209 | +4116.52€ | 0 | 26 |
| ✅ GBM_LATE_5M | 7927 | +0.164 | +5016.96€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 7927 | +0.164 | +5016.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1838 | +0.152 | +1243.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1838 | +0.152 | +1243.51€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 898 | +0.170 | +566.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 898 | +0.170 | +566.04€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2551 | +0.166 | +1586.02€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2551 | +0.166 | +1586.02€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 783 | +0.145 | +410.34€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 783 | +0.145 | +410.34€ | 0 | 29 |
| ✅ GBM_LATE_5M#XRP | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1932 | +0.065 | +714.03€ | 1 | 13 |
| ✅ GBM_LATE_60M#60min | 1932 | +0.065 | +714.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 711 | +0.089 | +260.23€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 711 | +0.089 | +260.23€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 634 | +0.068 | +282.05€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 634 | +0.068 | +282.05€ | 2 | 15 |
| ✅ GBM_LATE_60M#SOL | 587 | +0.033 | +171.76€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 587 | +0.033 | +171.76€ | 2 | 8 |
| 🚫 GBM_LATE_60M_FADE | 405 | -0.259 | -24.88€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 405 | -0.259 | -24.88€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 151 | -0.226 | -8.14€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 151 | -0.226 | -8.14€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 135 | -0.259 | -8.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 135 | -0.259 | -8.36€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 119 | -0.293 | -8.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 119 | -0.293 | -8.38€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 761 | +0.077 | +173.92€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 761 | +0.077 | +173.92€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 301 | +0.068 | +61.93€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 301 | +0.068 | +61.93€ | 3 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 228 | +0.039 | +12.27€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 228 | +0.039 | +12.27€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 232 | +0.124 | +99.72€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 232 | +0.124 | +99.72€ | 1 | 11 |
| ✅ LATE_WINDOW_5MIN | 105 | +0.257 | +87.77€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 105 | +0.257 | +87.77€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 105 | +0.257 | +87.77€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 105 | +0.257 | +87.77€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2206 | +0.103 | +596.15€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2206 | +0.103 | +596.15€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2206 | +0.103 | +596.15€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2206 | +0.103 | +596.15€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 396 | -0.075 | -33.15€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 396 | -0.075 | -33.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 102 | -0.048 | -3.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 102 | -0.048 | -3.77€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 145 | -0.024 | -4.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 145 | -0.024 | -4.56€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2171 | +0.009 | +23.14€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2171 | +0.009 | +23.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 117 | +0.021 | -2.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 117 | +0.021 | -2.45€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 250 | -0.012 | +10.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 250 | -0.012 | +10.83€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 175 | -0.025 | -5.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 175 | -0.025 | -5.87€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 904 | +0.023 | +22.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 904 | +0.023 | +22.16€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 490 | +0.006 | -2.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 490 | +0.006 | -2.00€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 235 | +0.002 | +0.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 235 | +0.002 | +0.48€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M | 1171 | -0.041 | -24.55€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1171 | -0.041 | -24.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 330 | -0.042 | -13.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 330 | -0.042 | -13.26€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 398 | -0.022 | +0.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 398 | -0.022 | +0.97€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 443 | -0.057 | -12.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 443 | -0.057 | -12.26€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 2439 | -0.016 | +57.48€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1163 | -0.019 | +19.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1276 | -0.013 | +37.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 70 | +0.014 | +6.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 39 | +0.061 | +8.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 31 | -0.045 | -2.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 572 | +0.009 | +41.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 267 | +0.006 | +14.43€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 305 | +0.011 | +26.84€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 314 | -0.032 | +0.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 152 | -0.065 | -10.40€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 162 | +0.000 | +11.11€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 472 | -0.032 | -14.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 218 | -0.027 | -4.93€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 254 | -0.035 | -9.50€ | 5 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 451 | -0.008 | +22.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 225 | -0.020 | +9.19€ | 2 | 3 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 226 | +0.004 | +13.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 560 | -0.029 | +0.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 262 | -0.023 | +2.68€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 298 | -0.033 | -1.83€ | 4 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 31889 | -0.006 | +1422.57€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 31889 | -0.006 | +1422.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5636 | +0.019 | +695.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5636 | +0.019 | +695.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4871 | -0.030 | -65.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4871 | -0.030 | -65.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5713 | +0.015 | +504.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5713 | +0.015 | +504.12€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4658 | -0.053 | -150.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4658 | -0.053 | -150.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5357 | -0.009 | +211.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5357 | -0.009 | +211.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5654 | +0.009 | +227.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5654 | +0.009 | +227.18€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE | 6002 | -0.060 | -147.91€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6002 | -0.060 | -147.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1445 | -0.084 | -40.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1445 | -0.084 | -40.56€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 679 | -0.123 | -29.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 679 | -0.123 | -29.71€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1763 | -0.078 | -33.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1763 | -0.078 | -33.42€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 80509 | -0.073 | +1736.05€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 80509 | -0.073 | +1736.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 13670 | -0.077 | +818.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 13670 | -0.077 | +818.81€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12346 | -0.095 | -636.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12346 | -0.095 | -636.28€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 13939 | -0.067 | +738.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 13939 | -0.067 | +738.96€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 11875 | -0.094 | -231.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 11875 | -0.094 | -231.00€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 14699 | -0.048 | +406.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 14699 | -0.048 | +406.67€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 13980 | -0.063 | +638.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 13980 | -0.063 | +638.90€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7789 | -0.027 | -137.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7789 | -0.027 | -137.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1774 | -0.035 | -14.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1774 | -0.035 | -14.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2202 | -0.023 | -28.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2202 | -0.023 | -28.40€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1062 | -0.045 | -20.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1062 | -0.045 | -20.52€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 752 | -0.020 | -23.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 752 | -0.020 | -23.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1209 | +0.109 | +414.39€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1073 | +0.116 | +401.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 243 | +0.129 | +112.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 243 | +0.129 | +112.54€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 207 | +0.108 | +58.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 207 | +0.108 | +58.17€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 222 | +0.098 | +75.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 222 | +0.098 | +75.75€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 185 | +0.136 | +88.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 185 | +0.136 | +88.57€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 216 | +0.105 | +66.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 216 | +0.105 | +66.77€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 613 | -0.048 | -55.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 613 | -0.048 | -55.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 125 | -0.012 | +1.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 125 | -0.012 | +1.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 82 | -0.083 | -14.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 82 | -0.083 | -14.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 180 | -0.060 | -24.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 180 | -0.060 | -24.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 122 | -0.032 | -6.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 122 | -0.032 | -6.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 104 | -0.057 | -10.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 104 | -0.057 | -10.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 611 | -0.112 | -55.61€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 280 | -0.163 | -67.41€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 227 | -0.203 | -68.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 53 | +0.009 | +0.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 212 | -0.075 | -0.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 162 | -0.079 | -6.75€ | 2 | 1 |
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
| ✅ STREAK_FADE_15M | 549 | +0.035 | +20.06€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 549 | +0.035 | +20.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 264 | +0.038 | +7.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 264 | +0.038 | +7.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 57 | -0.009 | -1.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 57 | -0.009 | -1.59€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 191 | +0.034 | +10.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 191 | +0.034 | +10.66€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2857 | -0.021 | -113.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2857 | -0.021 | -113.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 839 | -0.017 | -26.49€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 839 | -0.017 | -26.49€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 572 | -0.023 | -23.22€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 572 | -0.023 | -23.22€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1290 | -0.020 | -49.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1290 | -0.020 | -49.17€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 76 | -0.051 | -6.76€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 76 | -0.051 | -6.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 38 | +0.000 | -2.32€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 38 | +0.000 | -2.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8453 | +0.022 | +120.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8453 | +0.022 | +120.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2311 | +0.024 | +30.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2311 | +0.024 | +30.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1913 | +0.030 | +48.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1913 | +0.030 | +48.46€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2574 | +0.012 | +3.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2574 | +0.012 | +3.97€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1655 | +0.028 | +37.70€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1655 | +0.028 | +37.70€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7764 | +0.013 | -35.24€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7764 | +0.013 | -35.24€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3111 | +0.016 | -8.28€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3111 | +0.016 | -8.28€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3061 | +0.013 | -15.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3061 | +0.013 | -15.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1592 | +0.008 | -11.35€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1592 | +0.008 | -11.35€ | 2 | 0 |
| ✅ UPDOWN_GBM | 42815 | +0.035 | +2749.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11245 | +0.071 | +2128.97€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1534 | +0.004 | +5.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 27277 | +0.025 | +597.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2601 | +0.001 | +19.91€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4374 | +0.074 | +529.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 789 | +0.160 | +340.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3552 | +0.056 | +190.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 8145 | +0.041 | +600.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1439 | +0.087 | +330.66€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 410 | +0.015 | +6.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5062 | +0.041 | +234.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1174 | +0.003 | +28.05€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 60 | -0.097 | +0.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4953 | +0.041 | +313.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 746 | +0.138 | +260.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4179 | +0.024 | +54.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 9327 | +0.023 | +391.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2854 | +0.049 | +328.41€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 403 | +0.006 | +7.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5140 | +0.016 | +62.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 878 | -0.003 | -9.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 52 | -0.130 | +3.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 9779 | +0.016 | +257.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2712 | +0.027 | +190.29€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 395 | -0.004 | -2.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6079 | +0.014 | +71.17€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 549 | +0.004 | +1.81€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 44 | -0.174 | -3.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6235 | +0.040 | +659.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2705 | +0.086 | +678.72€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 265 | -0.002 | -3.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3265 | +0.004 | -15.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 156 | -0.133 | +0.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 594 | +0.349 | +193.39€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 594 | +0.349 | +193.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 328 | +0.354 | +105.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 328 | +0.354 | +105.26€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 266 | +0.340 | +88.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 266 | +0.340 | +88.13€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 13040 | -0.036 | +2876.29€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 13040 | -0.036 | +2876.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2382 | -0.121 | +39.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2382 | -0.121 | +39.82€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1465 | +0.209 | +901.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1465 | +0.209 | +901.90€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3920 | -0.064 | +587.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3920 | -0.064 | +587.78€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3915 | -0.073 | +638.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3915 | -0.073 | +638.56€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 152 | +0.039 | +8.44€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 152 | +0.039 | +8.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 152 | +0.039 | +8.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 152 | +0.039 | +8.44€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 961 | +0.291 | +772.52€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 961 | +0.291 | +772.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 525 | +0.287 | +401.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 525 | +0.287 | +401.25€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 436 | +0.294 | +371.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 436 | +0.294 | +371.27€ | 0 | 9 |
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