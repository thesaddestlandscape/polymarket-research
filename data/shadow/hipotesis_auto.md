# Hipótesis automáticas — 2026-11-28 22:05 UTC
_Generado por shadow_postmortem.py sobre 1532226 resoluciones (PNL=+218203.62€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.239 (n=236)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=738)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1125)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `60.0` → IC=+0.170 (n=365)

  - _Acción_: Kelly boost +0.85€ cuando `n_total_lado` > 60.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8114` → IC=+0.263 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8114 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.173` → IC=+0.195 (n=355)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.173 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.130 (n=1073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=1154)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=568)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=988)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.181 (n=318)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 62.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8108` → IC=+0.264 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8108 (IC base=+0.125)

- **PATRÓN** `banda_z` > `8.262` → IC=+0.197 (n=311)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.262 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.137 (n=843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 8.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=1054)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `5103.2759` → IC=+0.133 (n=423)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 5103.2759 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8583.6708` → IC=+0.126 (n=252)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 8583.6708 (IC base=+0.017)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=109)

- **FILTRO** `banda_hit_calibrado` < `0.8028` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8028
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=117)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=109)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=108)

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.239 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.8028` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8028 (IC base=+0.130)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.135 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 4.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.140 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 14.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=117)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `911.0736` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 911.0736 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.130)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` > 0.495 (IC base=+0.153)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.153)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.153)

- **PATRÓN** `banda_hit_calibrado` > `0.6072` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `banda_hit_calibrado` > 0.6072 (IC base=+0.153)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.225 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2738.3784` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2738.3784 (IC base=+0.153)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `130.35` → IC=-0.217 (n=13055)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.35
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=39175)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `122.97` → IC=-0.263 (n=1272)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.97
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3816)

### BALLENAS_TARDIAS#BTC#15min
- **PATRÓN** `restante_s_al_confirmar` < `641.33` → IC=+0.128 (n=2622)

  - _Acción_: Kelly boost +0.64€ cuando `restante_s_al_confirmar` < 641.33 (IC base=+0.086)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `114.34` → IC=-0.279 (n=1281)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 114.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3848)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.7` → IC=-0.159 (n=3736)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.7
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=11210)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `146.81` → IC=-0.256 (n=3533)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.81
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10602)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.04` → IC=-0.267 (n=2359)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.04
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=7078)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=31676)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `7610.3384` → IC=+0.149 (n=2571)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 7610.3384 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=28413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=34269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.223 (n=25595)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=9112)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=2255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=2760)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `16167.0481` → IC=+0.183 (n=717)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 16167.0481 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.184 (n=1974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.180 (n=2208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2824)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `15960.1808` → IC=+0.183 (n=729)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 15960.1808 (IC base=+0.176)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.172 (n=659)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.615 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `6823.1358` → IC=+0.122 (n=154)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 6823.1358 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.123 (n=2292)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.45 (IC base=+0.087)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=5849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.176 (n=2851)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.377 (n=1963)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=2813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.331 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=3259)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.191)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.142 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.143 (n=1011)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.65` → IC=+0.242 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.65 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=1231)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2027.9359` → IC=+0.137 (n=1011)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2027.9359 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4398.6513` → IC=+0.154 (n=157)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4398.6513 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.252 (n=1005)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.230 (n=2056)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.229)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.428 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.143)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=499)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.165 (n=499)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.55 (IC base=+0.053)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.136 (n=1100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.254 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.126)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=158)

- **FILTRO** `libro_liquidez` < `8957.4571` → IC=-0.263 (n=175)

  - _Acción_: SKIP cuando `libro_liquidez` < 8957.4571
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=59)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=26960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=23977)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.218 (n=9083)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.336 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `5024.6381` → IC=+0.335 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5024.6381 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=6486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.158)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.173 (n=6183)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.158)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=4061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=2700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.246 (n=1905)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.203)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=5970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=5324)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.174 (n=6431)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=4967)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.171)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.251 (n=2410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.362 (n=1703)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.251)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=6145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=3900)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.199 (n=1972)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.184)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=1065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.425 (n=1060)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `14011.0969` → IC=+0.451 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14011.0969 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `15188.1532` → IC=+0.446 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15188.1532 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.428 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.423 (n=399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.421)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.430 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.421)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.426 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.421)

- **PATRÓN** `libro_liquidez` > `4833.5247` → IC=+0.425 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4833.5247 (IC base=+0.421)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.399)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.398 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.399)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.419 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.399)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=38)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=37146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.237 (n=36336)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.184 (n=5557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.175 (n=11903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=17163)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=15493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.277 (n=6493)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=6373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.196 (n=13099)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=5195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=5960)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.259 (n=6284)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=14103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.251 (n=6600)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=6198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=6166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.239 (n=7623)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=13282)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=14690)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.28` → IC=+0.141 (n=12450)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.28 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=6447)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.143 (n=6678)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=8234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.71` → IC=+0.143 (n=8157)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.71 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=6835)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.135 (n=8846)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.85` → IC=+0.135 (n=8224)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.85 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.307 (n=1464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.390 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `4014.7683` → IC=+0.295 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4014.7683 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.302 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.370 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `3967.4956` → IC=+0.294 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3967.4956 (IC base=+0.283)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=1037)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1486.6908` → IC=+0.307 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1486.6908 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.369 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.347)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.393 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.347)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.347)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.378 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.347)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.439 (n=326)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.434 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `5550.9682` → IC=+0.437 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5550.9682 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.448 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.444 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `1961.5764` → IC=+0.441 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.5764 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.421 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.397 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.407)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.407)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.391 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=136)

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
- **FILTRO** `py_entrada` > `0.755` → IC=-0.391 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=136)

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
- **PATRÓN** `drift_60min` |x|≤ `0.509` → IC=+0.140 (n=21332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.509 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=21627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.127 (n=14823)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9725` → IC=+0.246 (n=7115)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9725 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.8845` → IC=+0.288 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8845 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.459` → IC=+0.189 (n=10702)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.459 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6916` → IC=+0.266 (n=5841)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6916 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3035` → IC=+0.254 (n=2201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3035 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.7506` → IC=+0.234 (n=5165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7506 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=10182)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `5051.3837` → IC=+0.149 (n=7111)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5051.3837 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.123 (n=13526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0067 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.5643` → IC=+0.144 (n=27024)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5643 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6845` → IC=+0.192 (n=1815)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6845 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1807` → IC=+0.194 (n=11151)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1807 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.8545` → IC=+0.197 (n=7531)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8545 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2966` → IC=+0.233 (n=2743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2966 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.2898` → IC=+0.213 (n=8693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2898 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.228 (n=19155)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.087)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.236 (n=2055)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3054` → IC=+0.213 (n=3990)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3054 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=2211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=3027)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9825` → IC=+0.271 (n=2055)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9825 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.412` → IC=+0.272 (n=2021)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.412 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.258 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4398` → IC=+0.213 (n=4360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4398 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=4623)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2064.8387` → IC=+0.216 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2064.8387 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.242 (n=1874)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.268 (n=1377)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.241 (n=1889)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0847` → IC=+0.274 (n=1377)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0847 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0728` → IC=+0.239 (n=3576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0728 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.249 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `1.8591` → IC=+0.241 (n=2640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8591 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=4354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.231 (n=1721)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1167` → IC=+0.243 (n=1715)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1167 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=4092)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.220 (n=2775)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8852` → IC=+0.246 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8852 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.207` → IC=+0.227 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.207 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.674` → IC=+0.259 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.674 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6957` → IC=+0.227 (n=3478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6957 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2779` → IC=+0.264 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2779 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.4452` → IC=+0.245 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4452 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.158 (n=3757)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0062 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3629` → IC=+0.145 (n=4264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3629 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=1598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.3633` → IC=+0.200 (n=2843)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3633 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.559` → IC=+0.141 (n=667)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.559 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.967` → IC=+0.141 (n=3930)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.967 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6254` → IC=+0.159 (n=1422)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6254 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0977` → IC=+0.159 (n=1548)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0977 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4504` → IC=+0.142 (n=4132)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4504 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.183 (n=1379)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 166.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.212 (n=2176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=5055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.251 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.865` → IC=+0.277 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.865 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.194 (n=4305)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.35` → IC=+0.224 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.35 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7356` → IC=+0.210 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7356 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5545)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1893.161` → IC=+0.201 (n=2174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1893.161 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.229 (n=1987)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.469` → IC=+0.227 (n=3965)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.469 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.227 (n=2045)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0549` → IC=+0.268 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0549 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.557` → IC=+0.268 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.557 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3453` → IC=+0.253 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3453 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `3.2982` → IC=+0.239 (n=1453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2982 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1878.4948` → IC=+0.224 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1878.4948 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.221 (n=2995)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.169 (n=282)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=5792)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.140 (n=785)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0041 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.9373` → IC=+0.244 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9373 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1615` → IC=+0.348 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1615 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.3799` → IC=+0.345 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3799 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.222` → IC=+0.218 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.222 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.344 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8641 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.0915` → IC=+0.359 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0915 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` < `0.1032` → IC=+0.345 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1032 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.3009` → IC=+0.356 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3009 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.365 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `2.2799` → IC=+0.347 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2799 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.352 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.0867` → IC=+0.186 (n=1519)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0867 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.3707` → IC=+0.157 (n=733)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.3707 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.1576` → IC=+0.156 (n=2879)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1576 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.823` → IC=+0.162 (n=1997)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.823 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` > `0.6679` → IC=+0.154 (n=2676)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6679 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.199 (n=380)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.1389` → IC=+0.171 (n=1309)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1389 (IC base=+0.060)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.176 (n=168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=940)

- **FILTRO** `ibs_20min` > `0.1915` → IC=-0.124 (n=5690)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1915
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=2805)

- **FILTRO** `sigma_ewma_delta_pct` > `8.314` → IC=-0.227 (n=920)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.314
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=7575)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.182 (n=378)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.75 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.9817` → IC=+0.281 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9817 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.674` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 6.674 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `1.0006` → IC=+0.312 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0006 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.281 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.7825` → IC=+0.277 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7825 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5401` → IC=+0.257 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5401 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.1915` → IC=+0.159 (n=2805)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1915 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.8369` → IC=+0.299 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8369 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.3279` → IC=+0.294 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3279 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.6932` → IC=+0.311 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6932 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0787` → IC=+0.323 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0787 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4762` → IC=+0.307 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4762 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5251` → IC=+0.302 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5251 (IC base=-0.031)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.03` → IC=-0.179 (n=1430)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=5148)

- **FILTRO** `ibs_20min` > `0.7197` → IC=-0.190 (n=2293)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7197
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=6887)

- **PATRÓN** `ibs_20min` > `0.793` → IC=+0.146 (n=2237)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.793 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `0.4566` → IC=+0.339 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4566 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.316 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.3085` → IC=+0.320 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3085 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.5382` → IC=+0.315 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5382 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.1098` → IC=+0.292 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1098 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` < `0.6347` → IC=+0.275 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6347 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.2104` → IC=+0.276 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2104 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.1081` → IC=+0.275 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1081 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.5586` → IC=+0.266 (n=2335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5586 (IC base=+0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.187 (n=9360)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0113 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8665` → IC=+0.284 (n=12711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8665 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0096` → IC=+0.303 (n=1924)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0096 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.445` → IC=+0.168 (n=12640)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.445 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6911` → IC=+0.279 (n=9389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6911 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.298 (n=2320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6654` → IC=+0.290 (n=5441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6654 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.309 (n=16014)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.136 (n=18215)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0073 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.5156` → IC=+0.175 (n=24016)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5156 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2873` → IC=+0.282 (n=9795)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2873 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.6902` → IC=+0.280 (n=4137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6902 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1855` → IC=+0.284 (n=3133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1855 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.322 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4568` → IC=+0.301 (n=4663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4568 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2835` → IC=+0.305 (n=6341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2835 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.312 (n=13970)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8221` → IC=-0.151 (n=4948)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8221
  - _Potencial_: sin este filtro IC_bueno=+0.319 (n=2549)

- **FILTRO** `ibs_20min` > `0.698` → IC=-0.244 (n=1708)

  - _Acción_: SKIP cuando `ibs_20min` > 0.698
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=5125)

- **FILTRO** `sigma_ewma_delta_pct` > `4.034` → IC=-0.241 (n=1429)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.034
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=5404)

- **PATRÓN** `ibs_20min` > `0.8221` → IC=+0.319 (n=2549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8221 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.131` → IC=+0.176 (n=2792)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 2.131 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.336 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4476` → IC=+0.295 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4476 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.2336` → IC=+0.321 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2336 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.328 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.009)

- **PATRÓN** `ibs_20min` < `0.1701` → IC=+0.171 (n=1709)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1701 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.386 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.6528` → IC=+0.387 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6528 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1851` → IC=+0.228 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1851 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.5286` → IC=+0.215 (n=3043)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5286 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.223 (n=2445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` < `0.0741` → IC=+0.215 (n=2508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0741 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.241 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4168` → IC=+0.232 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4168 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.224 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `366.0` → IC=+0.233 (n=2710)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 366.0 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.8316` → IC=+0.262 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8316 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.281 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.5339` → IC=+0.256 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5339 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1545` → IC=+0.264 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1545 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.272 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 196.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.316 (n=2546)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.539` → IC=+0.305 (n=2598)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.539 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` < `0.1308` → IC=+0.294 (n=3548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1308 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `1.6005` → IC=+0.291 (n=3714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6005 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4391)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `2008.5984` → IC=+0.301 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2008.5984 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.333 (n=2375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.189` → IC=+0.328 (n=1569)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.189 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.324 (n=1365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.308)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.314 (n=1603)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` > `0.16` → IC=+0.322 (n=2373)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.16 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.935` → IC=+0.322 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.935 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` < `0.1986` → IC=+0.309 (n=3540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1986 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3445` → IC=+0.316 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3445 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.7543` → IC=+0.326 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7543 (IC base=+0.308)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `1577.6232` → IC=+0.315 (n=3179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1577.6232 (IC base=+0.308)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1642` → IC=+0.237 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1642 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.3888` → IC=+0.230 (n=2635)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3888 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.1749` → IC=+0.233 (n=2606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1749 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.5938` → IC=+0.230 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5938 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1619` → IC=+0.234 (n=2740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1619 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2722` → IC=+0.239 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2722 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4234` → IC=+0.236 (n=2533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4234 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.4985` → IC=+0.232 (n=2262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4985 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.248 (n=2589)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 117.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.0915` → IC=+0.152 (n=1775)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0915 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.1774` → IC=+0.261 (n=1920)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1774 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `1.1729` → IC=+0.262 (n=1916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1729 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` > `0.6103` → IC=+0.258 (n=1916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6103 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.264 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.286 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `1.7898` → IC=+0.281 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7898 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` > `2.4339` → IC=+0.265 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4339 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.285 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.015)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7538` → IC=-0.247 (n=2882)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7538
  - _Potencial_: sin este filtro IC_bueno=+0.319 (n=2884)

- **FILTRO** `ibs_20min` > `0.6` → IC=-0.234 (n=1346)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.168 (n=4099)

- **FILTRO** `sigma_ewma_delta_pct` > `8.207` → IC=-0.256 (n=625)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.207
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=4820)

- **PATRÓN** `ibs_20min` > `0.7538` → IC=+0.319 (n=2884)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7538 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `1.1107` → IC=+0.351 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1107 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.445` → IC=+0.160 (n=2362)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.445 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.841` → IC=+0.351 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.841 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.6934` → IC=+0.338 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6934 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2762` → IC=+0.370 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2762 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.7972` → IC=+0.356 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7972 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.168 (n=4099)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.3302` → IC=+0.274 (n=2254)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3302 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.709` → IC=+0.138 (n=4265)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.709 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `0.6851` → IC=+0.285 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6851 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.301 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.8115` → IC=+0.282 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8115 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.5459` → IC=+0.271 (n=1883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5459 (IC base=+0.069)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.344 (n=3039)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=3064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.315 (n=3193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.651` → IC=+0.335 (n=3039)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.651 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.2231` → IC=+0.336 (n=1599)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2231 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.71` → IC=+0.344 (n=1212)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.71 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.7017` → IC=+0.327 (n=2716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7017 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2894` → IC=+0.346 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2894 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.5428` → IC=+0.327 (n=2627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5428 (IC base=+0.313)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.314 (n=3802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `2996.856` → IC=+0.324 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2996.856 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.328 (n=3271)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=3290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.326 (n=3271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3902 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `1.3076` → IC=+0.323 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3076 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` < `0.2629` → IC=+0.316 (n=3240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2629 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.585` → IC=+0.332 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.585 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` < `0.633` → IC=+0.319 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.633 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `1.2077` → IC=+0.340 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2077 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.358 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `1.4187` → IC=+0.326 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4187 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1673` → IC=+0.316 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1673 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.218 (n=6836)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1285` → IC=+0.193 (n=9013)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1285 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=21296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.534` → IC=+0.228 (n=20483)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.534 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.173` → IC=+0.205 (n=7618)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.173 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.663` → IC=+0.259 (n=4011)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.663 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1722` → IC=+0.152 (n=13664)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1722 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.150 (n=13662)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6187 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.207 (n=2946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.613` → IC=+0.185 (n=6658)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.613 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.191 (n=19435)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 85.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.193 (n=9005)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0062 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0862` → IC=+0.224 (n=6824)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0862 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.205 (n=9818)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5292` → IC=+0.237 (n=20461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5292 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.357` → IC=+0.191 (n=3221)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.357 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.481` → IC=+0.190 (n=18311)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.481 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1908` → IC=+0.166 (n=14488)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1908 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2968` → IC=+0.217 (n=3082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2968 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5667` → IC=+0.184 (n=8625)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5667 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.648` → IC=+0.195 (n=6534)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.648 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.199 (n=19439)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 90.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.255 (n=1122)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.266 (n=1122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=2275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9421` → IC=+0.289 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9421 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.453` → IC=+0.326 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.453 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.284 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.8322` → IC=+0.225 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8322 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.228 (n=3226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=3442)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.252 (n=2856)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.249)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.251 (n=1902)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.1018` → IC=+0.306 (n=1256)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1018 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=2949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.253 (n=2603)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.0081` → IC=+0.307 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0081 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.944` → IC=+0.255 (n=2833)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.944 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.253 (n=2527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.3017` → IC=+0.267 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3017 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` < `1.554` → IC=+0.264 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.554 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.679` → IC=+0.254 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.679 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=3034)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.249)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.191 (n=1048)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0683` → IC=+0.172 (n=1048)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0683 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=3280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2415` → IC=+0.200 (n=3143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2415 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1993` → IC=+0.210 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1993 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.488` → IC=+0.196 (n=564)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.488 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8508` → IC=+0.134 (n=2096)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8508 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.1914` → IC=+0.129 (n=1048)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.1914 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2761` → IC=+0.168 (n=480)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2761 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.4114` → IC=+0.130 (n=1032)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4114 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.4618` → IC=+0.138 (n=1032)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4618 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `380.0` → IC=+0.129 (n=3065)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 380.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.180 (n=3001)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0061 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2617` → IC=+0.175 (n=3000)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2617 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=1274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.617` → IC=+0.209 (n=3409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.617 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.857` → IC=+0.182 (n=633)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.857 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.023` → IC=+0.154 (n=2998)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.023 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.163 (n=3409)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2065 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.0971` → IC=+0.153 (n=3001)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0971 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.1519` → IC=+0.157 (n=2887)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1519 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.195 (n=1419)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 201.0 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.232 (n=1566)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2614` → IC=+0.233 (n=2303)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2614 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=3616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.284 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.304 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.233 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.1733` → IC=+0.218 (n=2254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1733 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2004.561` → IC=+0.224 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.561 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.243 (n=3123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.2561` → IC=+0.266 (n=2082)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2561 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.272 (n=1175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=1463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0465` → IC=+0.291 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0465 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.655` → IC=+0.283 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.655 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.277 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7655` → IC=+0.239 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7655 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1827` → IC=+0.249 (n=2019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1827 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1876.0604` → IC=+0.248 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.0604 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.188 (n=1131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.004 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0821` → IC=+0.169 (n=1128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0821 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2382` → IC=+0.187 (n=3381)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2382 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1528` → IC=+0.189 (n=1877)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1528 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.182` → IC=+0.201 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.182 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8337` → IC=+0.139 (n=2254)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8337 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.175 (n=505)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5166` → IC=+0.124 (n=1458)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.5166 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5053` → IC=+0.137 (n=1104)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5053 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6908.9474` → IC=+0.195 (n=1533)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6908.9474 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.126 (n=3316)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 124.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.173 (n=2413)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4365` → IC=+0.150 (n=3619)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4365 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6697` → IC=+0.189 (n=3619)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6697 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.186` → IC=+0.145 (n=859)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 9.186 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.151 (n=2414)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8521 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.169 (n=547)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1959` → IC=+0.133 (n=3037)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1959 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4125` → IC=+0.135 (n=3450)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4125 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6662.7463` → IC=+0.191 (n=1641)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6662.7463 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.147 (n=2318)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 79.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.176 (n=1256)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0131 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=3871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4731` → IC=+0.206 (n=3763)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4731 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.211` → IC=+0.188 (n=2009)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.211 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.849` → IC=+0.280 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.849 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1668` → IC=+0.132 (n=3764)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1668 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6222` → IC=+0.126 (n=3763)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6222 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1636` → IC=+0.124 (n=3842)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1636 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.135 (n=521)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.8021` → IC=+0.127 (n=2438)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8021 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2703.627` → IC=+0.199 (n=1706)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2703.627 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.128 (n=2436)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 26.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.153 (n=3483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0112 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.172 (n=1319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=4042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6471` → IC=+0.221 (n=3956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6471 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2325` → IC=+0.146 (n=3940)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2325 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.231` → IC=+0.145 (n=3500)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.231 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1834` → IC=+0.130 (n=3955)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1834 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.7008` → IC=+0.124 (n=3533)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7008 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.158 (n=562)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4437` → IC=+0.141 (n=1257)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4437 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.4855` → IC=+0.136 (n=1255)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4855 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2595.5143` → IC=+0.195 (n=1793)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2595.5143 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.130 (n=2557)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 25.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.244 (n=3379)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1705` → IC=+0.237 (n=1486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1705 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=3511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=3043)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.253 (n=3377)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1881` → IC=+0.233 (n=2060)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1881 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.8482` → IC=+0.227 (n=3501)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8482 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.366` → IC=+0.274 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.366 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6164` → IC=+0.233 (n=3377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6164 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2382` → IC=+0.267 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2382 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.5155` → IC=+0.232 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5155 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=4264)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2629.3094` → IC=+0.229 (n=2251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2629.3094 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.241 (n=3507)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6185` → IC=+0.247 (n=3509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6185 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1563)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0392` → IC=+0.296 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0392 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `1.1945` → IC=+0.254 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1945 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.959` → IC=+0.274 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.959 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.243 (n=2339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8641 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.296 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `2.5712` → IC=+0.235 (n=3333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5712 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.5632` → IC=+0.237 (n=2977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5632 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=4393)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.199 (n=1778)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0044 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1455` → IC=+0.167 (n=2339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1455 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=5557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.2959` → IC=+0.189 (n=5316)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2959 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.9188` → IC=+0.179 (n=798)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.9188 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.479` → IC=+0.207 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.479 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8527` → IC=+0.162 (n=3241)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8527 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.1856` → IC=+0.158 (n=1620)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1856 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1551` → IC=+0.171 (n=1368)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1551 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.5264` → IC=+0.156 (n=2286)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5264 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.8084` → IC=+0.155 (n=3462)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8084 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.154 (n=5851)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7310.8676` → IC=+0.185 (n=2410)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7310.8676 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.7108` → IC=+0.141 (n=5857)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.7108 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.135 (n=2582)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 22.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.204 (n=879)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.220 (n=581)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=1333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.2116` → IC=+0.221 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2116 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.3371` → IC=+0.234 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3371 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.822` → IC=+0.222 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.822 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6237` → IC=+0.210 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6237 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0887` → IC=+0.209 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0887 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1564` → IC=+0.200 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1564 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.4006` → IC=+0.190 (n=1295)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4006 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `15532.4609` → IC=+0.203 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15532.4609 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.150 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0033 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.2123` → IC=+0.196 (n=726)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.2123 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.165 (n=712)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 166.0 (IC base=+0.076)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.242 (n=545)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.157 (n=721)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=1698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.7624` → IC=+0.258 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7624 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1596` → IC=+0.162 (n=768)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1596 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.976` → IC=+0.182 (n=231)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.976 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8285` → IC=+0.153 (n=1089)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8285 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.269` → IC=+0.186 (n=221)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.269 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7736` → IC=+0.157 (n=1074)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7736 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `7746.9858` → IC=+0.174 (n=741)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7746.9858 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.147 (n=554)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 31.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.123 (n=1636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0082 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.1814` → IC=+0.209 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1814 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.6736` → IC=+0.134 (n=719)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6736 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.0763` → IC=+0.123 (n=603)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0763 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `7689.5058` → IC=+0.157 (n=741)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 7689.5058 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.145 (n=714)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 41.0 (IC base=+0.107)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.155 (n=479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0073 (IC base=+0.123)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.135 (n=478)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0129 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.159 (n=1008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.7273` → IC=+0.226 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7273 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0555` → IC=+0.150 (n=252)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 1.0555 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.856` → IC=+0.232 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.856 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.0388` → IC=+0.133 (n=1258)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.0388 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6994` → IC=+0.129 (n=1278)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6994 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.148 (n=245)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4196` → IC=+0.154 (n=463)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4196 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=1440)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3041.9067` → IC=+0.149 (n=477)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3041.9067 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.141 (n=460)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 9.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6957` → IC=+0.144 (n=1600)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6957 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `2736.0261` → IC=+0.160 (n=725)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2736.0261 (IC base=+0.076)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0146` → IC=+0.237 (n=321)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0146 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.312` → IC=+0.178 (n=321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.312 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.8462` → IC=+0.174 (n=424)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.8462 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.3805` → IC=+0.187 (n=481)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.3805 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.2422` → IC=+0.188 (n=229)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2422 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.53` → IC=+0.189 (n=483)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 5.53 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `1.1939` → IC=+0.248 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1939 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` < `0.2469` → IC=+0.192 (n=517)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.2469 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `2.5077` → IC=+0.193 (n=451)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.5077 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.190 (n=485)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `2676.4564` → IC=+0.200 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2676.4564 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.178 (n=538)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0105 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.5762` → IC=+0.170 (n=473)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.5762 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.174 (n=474)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.5 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.186` → IC=+0.168 (n=480)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.186 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `1.2297` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2297 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.882` → IC=+0.164 (n=582)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 4.882 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.8755` → IC=+0.201 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8755 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.1149` → IC=+0.179 (n=503)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.1149 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.242` → IC=+0.201 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.242 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4975` → IC=+0.214 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4975 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.6713` → IC=+0.180 (n=173)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.6713 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `2230.8308` → IC=+0.166 (n=480)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2230.8308 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.178 (n=461)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 15.0 (IC base=+0.163)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.226 (n=9034)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=28338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9656` → IC=+0.299 (n=9031)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9656 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9601` → IC=+0.215 (n=3090)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9601 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.848` → IC=+0.260 (n=6633)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.848 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8642` → IC=+0.163 (n=12187)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8642 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2934` → IC=+0.217 (n=3540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2934 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6444` → IC=+0.195 (n=8837)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6444 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1768.94` → IC=+0.182 (n=27093)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1768.94 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.200 (n=25732)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.199 (n=8431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0056 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.206 (n=8412)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.402` → IC=+0.201 (n=22213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.402 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=9424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.4901` → IC=+0.251 (n=22208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4901 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1974` → IC=+0.182 (n=16230)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1974 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.486` → IC=+0.205 (n=23569)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.486 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.6246` → IC=+0.182 (n=5640)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6246 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2945` → IC=+0.254 (n=3485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2945 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.6377` → IC=+0.211 (n=8107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6377 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=24153)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.199)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.266 (n=1440)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3095` → IC=+0.234 (n=3798)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3095 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=4543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.236 (n=2893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.314 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.026` → IC=+0.299 (n=2833)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.026 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2321` → IC=+0.287 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2321 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2896` → IC=+0.241 (n=1897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2896 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=4384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2065.02` → IC=+0.238 (n=1439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2065.02 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.268 (n=1325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.263 (n=2646)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1297` → IC=+0.291 (n=1746)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1297 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.270 (n=1478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.264 (n=3579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.4721` → IC=+0.284 (n=3491)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4721 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.264 (n=3632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2914` → IC=+0.287 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2914 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5674` → IC=+0.263 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5674 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6411` → IC=+0.272 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6411 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=4188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.263 (n=1428)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.170 (n=1968)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.145 (n=1489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=4658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2901` → IC=+0.201 (n=3988)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2901 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.745` → IC=+0.211 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.745 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.003` → IC=+0.170 (n=695)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.003 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6316` → IC=+0.157 (n=1488)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6316 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0625` → IC=+0.144 (n=2023)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0625 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.186 (n=620)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1761` → IC=+0.144 (n=3866)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1761 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.5219` → IC=+0.144 (n=3925)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5219 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `209.0` → IC=+0.158 (n=1455)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 209.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.169 (n=3475)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0062 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.175 (n=1316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=1454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.3224` → IC=+0.232 (n=2629)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3224 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.998` → IC=+0.147 (n=1855)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 2.998 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.173` → IC=+0.150 (n=4029)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.173 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0385` → IC=+0.157 (n=3470)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0385 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.222` → IC=+0.200 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.222 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4389` → IC=+0.150 (n=3831)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4389 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.1355` → IC=+0.155 (n=1737)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1355 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=5114)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.183 (n=1260)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 211.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.242 (n=2043)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=4735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.224 (n=4013)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1676)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.858` → IC=+0.310 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.858 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1298` → IC=+0.223 (n=4279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1298 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.204` → IC=+0.233 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.204 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.6125` → IC=+0.230 (n=4413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6125 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=5188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2009.7484` → IC=+0.238 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2009.7484 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.250 (n=1917)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.1864` → IC=+0.260 (n=1916)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1864 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1985)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.294 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.837` → IC=+0.304 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.837 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.3458` → IC=+0.298 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3458 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.1748` → IC=+0.255 (n=2813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1748 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1988.1984` → IC=+0.254 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1988.1984 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.243 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.244)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.189 (n=1565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3597` → IC=+0.148 (n=4125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3597 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8742` → IC=+0.263 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8742 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1545` → IC=+0.170 (n=2268)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1545 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.381` → IC=+0.166 (n=1350)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.381 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8533` → IC=+0.154 (n=3125)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8533 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.200 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.153 (n=2018)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.156` → IC=+0.145 (n=2080)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.156 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5902.637` → IC=+0.228 (n=2125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5902.637 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.144 (n=3070)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 86.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.170 (n=3994)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0083 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.4629` → IC=+0.163 (n=3990)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4629 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=1472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.7057` → IC=+0.201 (n=3990)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7057 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1732` → IC=+0.161 (n=3832)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1732 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.033` → IC=+0.159 (n=801)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.033 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.028` → IC=+0.155 (n=3481)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.028 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6816` → IC=+0.164 (n=1756)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6816 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.205 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4935` → IC=+0.155 (n=3871)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4935 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5276` → IC=+0.159 (n=3458)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5276 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `6725.1528` → IC=+0.218 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6725.1528 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.166 (n=2648)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 89.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.144 (n=3181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.01 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=3381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.256 (n=3183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.818` → IC=+0.195 (n=1042)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.818 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.192` → IC=+0.271 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.192 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2091` → IC=+0.128 (n=4771)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.2091 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1019` → IC=+0.124 (n=4547)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1019 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.148 (n=595)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.8288` → IC=+0.131 (n=3110)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8288 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2462.5472` → IC=+0.225 (n=2163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2462.5472 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.160 (n=3930)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0113 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1426` → IC=+0.152 (n=1489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1426 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=4606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.247 (n=3938)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5455 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.2311` → IC=+0.152 (n=4138)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2311 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.023` → IC=+0.162 (n=4339)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 3.023 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1941` → IC=+0.144 (n=4466)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1941 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.201 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4436` → IC=+0.166 (n=1424)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4436 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.5121` → IC=+0.145 (n=1424)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.5121 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2637.8463` → IC=+0.224 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2637.8463 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.161 (n=1463)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 17.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.254 (n=4356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=4564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=3897)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `0.99` → IC=+0.302 (n=1452)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.99 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.2063` → IC=+0.250 (n=2190)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2063 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.903` → IC=+0.300 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.903 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` < `1.2162` → IC=+0.236 (n=4357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2162 (IC base=+0.236)

- **PATRÓN** `volumen_regimen` > `0.6388` → IC=+0.242 (n=4356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6388 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2433` → IC=+0.263 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2433 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.5428` → IC=+0.256 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5428 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=5477)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2644.8146` → IC=+0.239 (n=2905)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2644.8146 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0244` → IC=+0.269 (n=1511)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0244 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=4744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1406` → IC=+0.304 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1406 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `1.199` → IC=+0.252 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.199 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.2342` → IC=+0.249 (n=4373)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2342 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.833` → IC=+0.283 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.833 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.6346` → IC=+0.248 (n=1508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6346 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2188` → IC=+0.264 (n=1508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2188 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.311 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.551` → IC=+0.248 (n=3846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.551 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.234 (n=6665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.5392` → IC=+0.235 (n=7573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5392 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=7602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.260 (n=2526)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` < `0.464` → IC=+0.231 (n=5412)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.464 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.427` → IC=+0.238 (n=2527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.427 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` < `0.7046` → IC=+0.233 (n=2381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7046 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.8773` → IC=+0.229 (n=3606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8773 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.237 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.4503` → IC=+0.238 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4503 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.232 (n=5405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `3772.7748` → IC=+0.236 (n=5049)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3772.7748 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.229 (n=1816)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.211 (n=2467)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.5326` → IC=+0.218 (n=5437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5326 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=1821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=2466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.7282` → IC=+0.216 (n=5438)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7282 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.7183` → IC=+0.218 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7183 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.677` → IC=+0.223 (n=4956)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.677 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2546` → IC=+0.209 (n=4942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2546 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.7274` → IC=+0.203 (n=4414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7274 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.212 (n=5031)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.5364` → IC=+0.216 (n=2357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5364 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.8218` → IC=+0.218 (n=3570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8218 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.236 (n=3599)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.211)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.281 (n=851)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.306 (n=323)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.284 (n=968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.274 (n=972)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` < `0.8328` → IC=+0.282 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.8328 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` < `0.2002` → IC=+0.287 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2002 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.302 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` < `1.2271` → IC=+0.280 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2271 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` > `0.8769` → IC=+0.291 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8769 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.337 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.283 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `1.4184` → IC=+0.276 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4184 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `12950.5411` → IC=+0.288 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12950.5411 (IC base=+0.274)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.260 (n=519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3904` → IC=+0.183 (n=1558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3904 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.173 (n=585)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.191 (n=685)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1382 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.3617` → IC=+0.173 (n=334)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3617 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.338` → IC=+0.188 (n=1532)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 6.338 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.0921` → IC=+0.183 (n=1370)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.0921 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1523` → IC=+0.185 (n=474)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1523 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `2.5027` → IC=+0.176 (n=1549)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.5027 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.8103` → IC=+0.169 (n=1032)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8103 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `14616.0048` → IC=+0.168 (n=706)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 14616.0048 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `703.0` → IC=+0.184 (n=1512)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 703.0 (IC base=+0.168)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.244 (n=362)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.6134` → IC=+0.217 (n=1087)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6134 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.711` → IC=+0.217 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.711 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9885` → IC=+0.253 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9885 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.268` → IC=+0.248 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.268 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2052` → IC=+0.248 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2052 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.7957` → IC=+0.218 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7957 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.222 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.343 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.312 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.6336` → IC=+0.316 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6336 (IC base=+0.288)

- **PATRÓN** `ibs_20min` > `0.1912` → IC=+0.300 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1912 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.025` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.025 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` < `0.1188` → IC=+0.327 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1188 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `1.8484` → IC=+0.296 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8484 (IC base=+0.288)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 5.0 (IC base=+0.288)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.224 (n=1844)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.4737` → IC=+0.223 (n=2094)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4737 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.4661` → IC=+0.232 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4661 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.8315` → IC=+0.217 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8315 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.43` → IC=+0.226 (n=2109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.43 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.938` → IC=+0.223 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.938 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.8615` → IC=+0.217 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8615 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `1.0645` → IC=+0.221 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0645 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.217 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1586` → IC=+0.217 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1586 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4017` → IC=+0.234 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4017 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.4937` → IC=+0.216 (n=1827)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4937 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.249 (n=568)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.5091` → IC=+0.219 (n=1691)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5091 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.215 (n=626)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.217 (n=1133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.0853` → IC=+0.212 (n=1691)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0853 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.7287` → IC=+0.221 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7287 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.201` → IC=+0.209 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.201 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2534` → IC=+0.211 (n=1691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2534 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.717` → IC=+0.209 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.717 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.228 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.1612` → IC=+0.207 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1612 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.7689` → IC=+0.209 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7689 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=2186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.209 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.205)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.234 (n=891)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.232 (n=446)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.253 (n=1201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.223 (n=1221)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9919` → IC=+0.303 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9919 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `1.094` → IC=+0.244 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.094 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.023` → IC=+0.275 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.023 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.6422` → IC=+0.252 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6422 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `1.2446` → IC=+0.225 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2446 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.226 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.250 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.5098` → IC=+0.232 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5098 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.229 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3376.162` → IC=+0.246 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3376.162 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.254 (n=908)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.246)

- **PATRÓN** `drift_60min` |x|≤ `0.5459` → IC=+0.253 (n=892)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5459 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.267 (n=702)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` < `0.6463` → IC=+0.271 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6463 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.5673` → IC=+0.246 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5673 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.03` → IC=+0.264 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.03 (IC base=+0.246)

- **PATRÓN** `volumen_regimen` < `0.7544` → IC=+0.255 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7544 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.104` → IC=+0.255 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.104 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `2.214` → IC=+0.272 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.214 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.250 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `4038.512` → IC=+0.267 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4038.512 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.271 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.246)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.144 (n=1014)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0044 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.425` → IC=+0.144 (n=2938)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.425 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1628` → IC=+0.160 (n=1327)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1628 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.148 (n=640)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.082)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.120 (n=1629)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` > 0.0071 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.5758` → IC=+0.182 (n=2365)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.5758 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.521` → IC=+0.135 (n=1055)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.521 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.1527` → IC=+0.192 (n=669)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1527 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.1796` → IC=+0.125 (n=2008)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.1796 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` > `2.5503` → IC=+0.124 (n=761)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.5503 (IC base=+0.103)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5656` → IC=-0.121 (n=354)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5656
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=719)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.122 (n=737)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0057 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5656` → IC=+0.159 (n=719)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.5656 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.3158` → IC=+0.183 (n=247)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.3158 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.243 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0588 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.139 (n=333)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.057)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.161 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0044 (IC base=+0.069)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.5241` → IC=+0.164 (n=751)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5241 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1367` → IC=+0.157 (n=395)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1367 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.066` → IC=+0.177 (n=184)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 12.066 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.3108` → IC=+0.223 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3108 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2025` → IC=+0.131 (n=120)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2025 (IC base=+0.048)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.981` → IC=+0.195 (n=323)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.981 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7705` → IC=+0.165 (n=231)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.7705 (IC base=+0.041)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.177 (n=444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0103 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.195 (n=634)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` < `0.2265` → IC=+0.149 (n=633)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2265 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.01` → IC=+0.248 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.01 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `1.1136` → IC=+0.185 (n=211)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.1136 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.1626` → IC=+0.179 (n=163)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1626 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `2.5569` → IC=+0.145 (n=201)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.5569 (IC base=+0.099)

### GBM_LATE_60M#XRP#60min
- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.400 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.386 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.297)

- **PATRÓN** `ibs_20min` < `0.9231` → IC=+0.312 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9231 (IC base=+0.297)

- **PATRÓN** `ibs_20min` > `0.5654` → IC=+0.333 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5654 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.4847` → IC=+0.381 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4847 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.737` → IC=+0.300 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.737 (IC base=+0.297)

- **PATRÓN** `volumen_regimen` < `0.8379` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8379 (IC base=+0.297)

- **PATRÓN** `volumen_regimen` > `1.1698` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1698 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` > `0.193` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.193 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` < `2.8946` → IC=+0.340 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.8946 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.310 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1582.85` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1582.85 (IC base=+0.297)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.330 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.324)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.325 (n=118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.324)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.361 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.324)

- **PATRÓN** `ibs_20min` < `0.0507` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0507 (IC base=+0.324)

- **PATRÓN** `ibs_20min` > `0.3665` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3665 (IC base=+0.324)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.665` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.665 (IC base=+0.324)

- **PATRÓN** `volumen_regimen` > `0.7932` → IC=+0.389 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7932 (IC base=+0.324)

- **PATRÓN** `volumen_pendiente_norm` > `0.1729` → IC=+0.421 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1729 (IC base=+0.324)

- **PATRÓN** `volumen_spike_ratio` < `1.547` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.547 (IC base=+0.324)

- **PATRÓN** `volumen_spike_ratio` > `3.2376` → IC=+0.329 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2376 (IC base=+0.324)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.352 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.324)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.248 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=214)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.310 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=328)

- **FILTRO** `volumen_regimen` < `0.8808` → IC=-0.307 (n=138)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8808
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=284)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.292 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=284)

- **FILTRO** `dist_vwap_pct` > `0.4617` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4617
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=366)

- **FILTRO** `sigma_ewma_delta_pct` > `9.288` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.288
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=372)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=277)

- **FILTRO** `volumen_spike_ratio` > `2.2757` → IC=-0.269 (n=76)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2757
  - _Potencial_: sin este filtro IC_bueno=-0.251 (n=231)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=104)

- **FILTRO** `ibs_20min` < `0.0328` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0328
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=101)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.329 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=120)

- **FILTRO** `volumen_spike_ratio` > `1.817` → IC=-0.318 (n=42)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.817
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=84)

- **FILTRO** `libro_liquidez` < `5581.9927` → IC=-0.260 (n=119)

  - _Acción_: SKIP cuando `libro_liquidez` < 5581.9927
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=40)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.003` → IC=-0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.003
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=104)

- **FILTRO** `hora_utc` < `2.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=112)

- **FILTRO** `ibs_20min` < `0.6002` → IC=-0.472 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6002
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=104)

- **FILTRO** `volumen_regimen` > `1.0898` → IC=-0.188 (n=46)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0898
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=92)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.372 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=106)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.342 (n=36)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.297 (n=72)

- **FILTRO** `volumen_spike_ratio` < `1.4507` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4507
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=81)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=128)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.346 (n=37)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=112)

- **FILTRO** `volumen_spike_ratio` < `1.5734` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5734
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=93)

- **FILTRO** `dist_vwap_pct` > `0.2836` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2836
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=61)

- **FILTRO** `volumen_regimen` < `0.9756` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9756
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=53)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.270 (n=324)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.191 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 16.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.203 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6818 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9043` → IC=+0.311 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9043 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.107` → IC=+0.187 (n=231)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 10.107 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.190 (n=317)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6195 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.179 (n=316)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.1915 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` < `0.2119` → IC=+0.183 (n=970)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2119 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5136` → IC=+0.204 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5136 (IC base=+0.167)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.148 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0067 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.7234` → IC=+0.131 (n=258)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.7234 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.3381` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3381 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.2543` → IC=+0.133 (n=469)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.2543 (IC base=+0.074)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.151 (n=270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0029 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.136 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1124 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.145 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 5.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.7994` → IC=+0.178 (n=243)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7994 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.8305` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.8305 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1156` → IC=+0.153 (n=217)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1156 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.063` → IC=+0.151 (n=279)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 9.063 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6195` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6195 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.1834` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1834 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` < `0.0508` → IC=+0.184 (n=223)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.0508 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.7116` → IC=+0.177 (n=162)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.7116 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=224)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1706.9595` → IC=+0.176 (n=270)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1706.9595 (IC base=+0.133)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2308` → IC=-0.274 (n=60)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2308
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=181)

- **FILTRO** `volumen_spike_ratio` > `2.2708` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2708
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=153)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.357 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` > `0.6119` → IC=+0.296 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6119 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.7916` → IC=+0.397 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7916 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.360 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.277)

- **PATRÓN** `volumen_regimen` < `0.8033` → IC=+0.297 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8033 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.312 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` < `1.4958` → IC=+0.333 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4958 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `2.4024` → IC=+0.320 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4024 (IC base=+0.277)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=218)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.322)

- **PATRÓN** `elapsed_s` > `231.9` → IC=+0.397 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 231.9 (IC base=+0.322)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.322)

- **PATRÓN** `drift_60min` |x|≤ `0.6903` → IC=+0.392 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6903 (IC base=+0.322)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.376 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.322)

- **PATRÓN** `ballena_activa_n` < `1043.0` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1043.0 (IC base=+0.322)

- **PATRÓN** `drift_ventana_pct` |x|> `0.453` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.453 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `225.0` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 225.0 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `2.8622` → IC=+0.299 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.8622 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.7139` → IC=+0.308 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7139 (IC base=+0.281)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1283.0` → IC=+0.358 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1283.0 (IC base=+0.281)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=218)

- **PATRÓN** `drift_ventana_pct` |x|> `0.5455` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.5455 (IC base=+0.322)

- **PATRÓN** `elapsed_s` > `231.9` → IC=+0.397 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 231.9 (IC base=+0.322)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.322)

- **PATRÓN** `drift_60min` |x|≤ `0.6903` → IC=+0.392 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6903 (IC base=+0.322)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.376 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.322)

- **PATRÓN** `ballena_activa_n` < `1043.0` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1043.0 (IC base=+0.322)

- **PATRÓN** `drift_ventana_pct` |x|> `0.453` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.453 (IC base=+0.281)

- **PATRÓN** `elapsed_s` > `225.0` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 225.0 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `2.8622` → IC=+0.299 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.8622 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.7139` → IC=+0.308 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7139 (IC base=+0.281)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `1283.0` → IC=+0.358 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1283.0 (IC base=+0.281)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=298)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=299)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=1821)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.176 (n=100)

  - _Acción_: Kelly boost +0.88€ cuando `liq_n` > 2.0 (IC base=+0.079)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.154 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 6.0 (IC base=+0.079)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.03 (IC base=+0.079)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11686.6395` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `libro_liquidez` < 11686.6395
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=129)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=177)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `1211.34` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_usd_total` < 1211.34
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=46)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=291)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=4372)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=285)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=242)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.156 (n=91)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=181)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.161 (n=181)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 30.0 (IC base=+0.023)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.139 (n=308)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=+0.027)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.160)

- **PATRÓN** `liq_usd_total` > `750.26` → IC=+0.223 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 750.26 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.207 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.169 (n=167)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.04 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `3293.329` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3293.329 (IC base=+0.160)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1743)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1697)

- **FILTRO** `liq_n` < `3.0` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `liq_n` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `liq_usd_total` < `6520.36` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 6520.36
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `ballena_activa_n` > `133.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 133.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=779)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=788)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=591)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=572)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.138 (n=241)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=-0.001)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=1222)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=1222)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1686)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1686)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=382)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=382)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.129 (n=173)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=224)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.132 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=442)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=493)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=355)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=470)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=470)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=458)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=3915)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=10075)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.153 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=156)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=59)

- **FILTRO** `restante_min` < `3.79` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `restante_min` < 3.79
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=55)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.194 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=75)

- **FILTRO** `lag_apertura_s` > `72.79` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `lag_apertura_s` > 72.79
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=55)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.162 (n=471)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1144)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.147 (n=372)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=1006)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.139 (n=472)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.51 (IC base=-0.009)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.130 (n=217)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=498)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=349)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=370)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.130 (n=376)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.51 (IC base=-0.020)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=399)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=838)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.125 (n=684)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=691)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.127 (n=644)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=669)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.162 (n=489)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=994)

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

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.178 (n=9458)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=29251)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.171 (n=9726)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=30395)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.199 (n=1732)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=5388)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.145 (n=2372)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=4627)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1823)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=3292)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.175 (n=1426)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4486)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=1749)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=5429)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=2186)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.032)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=1466)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=4444)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.156 (n=1781)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=5358)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2452)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2376)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3528)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4480)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.257 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=430)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.164 (n=409)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1248)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `ibs_20min` > `0.7714` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7714
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=58)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=382)

- **FILTRO** `drift_20min_pct` |x|> `0.1997` → IC=-0.124 (n=123)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1997
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=372)

- **FILTRO** `libro_liquidez` < `3260.3832` → IC=-0.185 (n=163)

  - _Acción_: SKIP cuando `libro_liquidez` < 3260.3832
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=332)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=983)

- **FILTRO** `ibs_20min` > `0.8553` → IC=-0.125 (n=665)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8553
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=666)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.175 (n=438)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=884)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.141 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=235)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=68)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.137 (n=26286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=59519)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=20900)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=64905)

- **FILTRO** `ibs_7min` < `0.2105` → IC=-0.237 (n=21449)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2105
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=64356)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.247 (n=26482)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=80467)

- **FILTRO** `ibs_7min` > `0.2778` → IC=-0.182 (n=26735)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2778
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=80214)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=3627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=11593)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.327 (n=3601)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=11619)

- **FILTRO** `ibs_7min` < `0.7087` → IC=-0.257 (n=5022)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7087
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=10198)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.280 (n=4447)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=13823)

- **FILTRO** `ibs_7min` > `0.7692` → IC=-0.212 (n=4564)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=13706)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.126 (n=3531)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=11109)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=3596)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=11044)

- **FILTRO** `ibs_7min` < `0.7101` → IC=-0.211 (n=3660)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7101
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10980)

- **FILTRO** `ballena_activa_n` > `157.0` → IC=-0.203 (n=3638)

  - _Acción_: SKIP cuando `ballena_activa_n` > 157.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=11002)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.265 (n=3419)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=11560)

- **FILTRO** `ibs_7min` > `0.2642` → IC=-0.188 (n=3744)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2642
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=11235)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.177 (n=3741)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=11238)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.169 (n=3485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=11100)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.329 (n=3483)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=11102)

- **FILTRO** `ibs_7min` < `0.291` → IC=-0.255 (n=4813)

  - _Acción_: SKIP cuando `ibs_7min` < 0.291
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9772)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.174 (n=3482)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=11103)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=4625)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=14684)

- **FILTRO** `ibs_7min` > `0.7222` → IC=-0.185 (n=4827)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7222
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=14482)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.276 (n=3296)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=11043)

- **FILTRO** `ibs_7min` < `0.7108` → IC=-0.202 (n=3584)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7108
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=10755)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.197 (n=3510)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10829)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.261 (n=3456)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=11379)

- **FILTRO** `ibs_7min` > `0.2715` → IC=-0.178 (n=3707)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2715
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=11128)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.170 (n=3678)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=11157)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=3271)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=10131)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.234 (n=4408)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8994)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.203 (n=4847)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=15553)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=4401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=9218)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=3332)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=10287)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.232 (n=4483)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=9136)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.231 (n=4655)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=14501)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=122)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1044)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1333)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.157 (n=196)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=719)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=940)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=251)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.141 (n=129)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=400)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=480)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=602)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=255)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=511)

- **FILTRO** `libro_liquidez` < `3309.2037` → IC=-0.140 (n=198)

  - _Acción_: SKIP cuando `libro_liquidez` < 3309.2037
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=596)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=571)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.142 (n=799)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.132 (n=636)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `458.564` → IC=+0.164 (n=588)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 458.564 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4217.5939` → IC=+0.128 (n=587)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 4217.5939 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.176 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 14.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.142 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 5.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `285.7` → IC=+0.173 (n=270)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 285.7 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.145 (n=364)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.04 (IC base=+0.141)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3984` → IC=+0.136 (n=369)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3984 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=345)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.120 (n=446)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.04 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4156` → IC=+0.162 (n=214)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4156 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `706.5888` → IC=+0.176 (n=282)

  - _Acción_: Kelly boost +0.88€ cuando `total_vol_5m` < 706.5888 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 59.0 (IC base=+0.129)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4315` → IC=+0.210 (n=136)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4315 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.133 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.161 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 5.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `4761.643` → IC=+0.180 (n=201)

  - _Acción_: Kelly boost +0.90€ cuando `total_vol_5m` < 4761.643 (IC base=+0.132)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=224)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.090)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `4.4525` → IC=-0.197 (n=130)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4525
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=132)

- **FILTRO** `sigma_h` > `0.0104` → IC=-0.174 (n=271)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0104
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=816)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.166 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0044 (IC base=-0.029)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.130 (n=163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=167)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.277 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.006)

- **PATRÓN** `pct_vs_K` |x|≤ `2.1117` → IC=+0.223 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 2.1117 (IC base=+0.006)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `7.5593` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.5593
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=72)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0078` → IC=-0.124 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=53)

- **FILTRO** `T_h` < `64.4744` → IC=-0.185 (n=52)

  - _Acción_: SKIP cuando `T_h` < 64.4744
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=156)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0147` → IC=-0.167 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0147
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.272 (n=616)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=304)

- **FILTRO** `T_h` > `66.9347` → IC=-0.264 (n=616)

  - _Acción_: SKIP cuando `T_h` > 66.9347
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=304)

- **FILTRO** `sigma_h` < `0.0067` → IC=-0.175 (n=290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=591)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.01` → IC=-0.239 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=78)

- **FILTRO** `T_h` > `49.268` → IC=-0.258 (n=229)

  - _Acción_: SKIP cuando `T_h` > 49.268
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **FILTRO** `sigma_h` < `0.0086` → IC=-0.143 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=83)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `pct_vs_K` |x|> `2.8122` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.273 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `T_h` > `139.1329` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `T_h` > 139.1329
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.325 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.296 (n=135)

- **FILTRO** `T_h` > `135.7558` → IC=-0.341 (n=67)

  - _Acción_: SKIP cuando `T_h` > 135.7558
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=203)

- **FILTRO** `sigma_h` < `0.0058` → IC=-0.147 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=200)

- **PATRÓN** `pct_vs_K` |x|≤ `1.9843` → IC=+0.176 (n=134)

  - _Acción_: Kelly boost +0.88€ cuando `pct_vs_K` |x|≤ 1.9843 (IC base=-0.090)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.239 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0147` → IC=-0.234 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0147
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=188)

- **FILTRO** `T_h` > `61.9454` → IC=-0.235 (n=187)

  - _Acción_: SKIP cuando `T_h` > 61.9454
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=63)

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.309 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=129)

- **FILTRO** `T_h` > `49.2646` → IC=-0.144 (n=130)

  - _Acción_: SKIP cuando `T_h` > 49.2646
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=65)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.106` → IC=+0.452 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.106 (IC base=+0.330)

- **PATRÓN** `sigma_h` < `0.0151` → IC=+0.349 (n=137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0151 (IC base=+0.330)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.372 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.330)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.330)

- **PATRÓN** `dist_50` > `0.4594` → IC=+0.485 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4594 (IC base=+0.330)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.347 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.330)

- **PATRÓN** `edge` > `0.098` → IC=+0.423 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.098 (IC base=+0.390)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.413 (n=206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.390)

- **PATRÓN** `T_h` < `0.7285` → IC=+0.420 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7285 (IC base=+0.390)

- **PATRÓN** `dist_50` > `0.366` → IC=+0.439 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.366 (IC base=+0.390)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.473 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.390)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.0972` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0972 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.284 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.208)

- **PATRÓN** `T_h` < `0.7026` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7026 (IC base=+0.208)

- **PATRÓN** `T_h` > `1.4764` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4764 (IC base=+0.208)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.240 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.208)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1295` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1295 (IC base=+0.280)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.340 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.280)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.280)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.280)

- **PATRÓN** `edge` > `0.0997` → IC=+0.468 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.439 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.417)

- **PATRÓN** `T_h` < `1.178` → IC=+0.444 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.178 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.4134` → IC=+0.484 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4134 (IC base=+0.417)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.407 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1324` → IC=+0.488 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1324 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.472 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.418)

- **PATRÓN** `T_h` < `1.0409` → IC=+0.417 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0409 (IC base=+0.418)

- **PATRÓN** `T_h` > `1.268` → IC=+0.466 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.268 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.3288` → IC=+0.476 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3288 (IC base=+0.418)

- **PATRÓN** `edge` > `0.177` → IC=+0.473 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.177 (IC base=+0.461)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.470 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.461)

- **PATRÓN** `T_h` < `0.8072` → IC=+0.460 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8072 (IC base=+0.461)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.461)

- **PATRÓN** `dist_50` > `0.4469` → IC=+0.486 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4469 (IC base=+0.461)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.468 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.461)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=507)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=547)

- **PATRÓN** `streak_estiramiento` < `0.3787` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.3787 (IC base=+0.023)

- **PATRÓN** `streak_estiramiento` < `0.8333` → IC=+0.126 (n=380)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.8333 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.139 (n=189)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 18.0 (IC base=+0.063)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.085)

- **PATRÓN** `streak_estiramiento` < `0.5551` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.5551 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 68.0 (IC base=+0.085)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=27)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.495 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 26.0 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `2474.7486` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2474.7486 (IC base=+0.068)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.2738` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.2738 (IC base=+0.042)

- **PATRÓN** `streak_estiramiento` < `0.3856` → IC=+0.209 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3856 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.141 (n=210)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 34.0 (IC base=+0.083)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=108)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.144 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=46)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=73)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=868)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=40)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.515 (IC base=+0.025)

- **PATRÓN** `streak_estiramiento` < `0.5336` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.5336 (IC base=+0.000)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `streak_len` > `4.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### STREAK_FADE_60M#SOL#60min
- **FILTRO** `py_entrada` < `0.525` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.525
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **PATRÓN** `streak_estiramiento` < `0.6279` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.6279 (IC base=+0.030)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=1132)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1366)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1341)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5815)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3440)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.183 (n=2272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0059 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2334` → IC=+0.158 (n=6814)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2334 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1239` → IC=+0.133 (n=6814)

  - _Acción_: Kelly boost +0.66€ cuando `drift_15min` |x|≤ 1.1239 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0643` → IC=+0.133 (n=6813)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0643 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.099` → IC=+0.144 (n=2150)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.099 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=6320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.5517` → IC=+0.206 (n=6090)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5517 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.969` → IC=+0.224 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.969 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3560)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4341.9356` → IC=+0.172 (n=2272)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4341.9356 (IC base=+0.132)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2686)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.248 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.245 (n=410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.208)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2648` → IC=+0.228 (n=310)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2648 (IC base=+0.208)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2221` → IC=+0.221 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2221 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_15` > `0.702` → IC=+0.275 (n=930)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.702 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.4048` → IC=+0.237 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4048 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.559` → IC=+0.210 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.559 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.088` → IC=+0.294 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.088 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `11825.4597` → IC=+0.222 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11825.4597 (IC base=+0.208)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.141 (n=1194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0075 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0667` → IC=+0.151 (n=526)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0667 (IC base=+0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0831` → IC=+0.136 (n=1066)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.0831 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.146 (n=478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 16.0 (IC base=+0.130)

- **PATRÓN** `ibs_15` > `0.4761` → IC=+0.216 (n=1194)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4761 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.143 (n=732)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.6657` → IC=+0.132 (n=1355)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6657 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.997` → IC=+0.282 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.997 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6126.0702` → IC=+0.172 (n=541)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6126.0702 (IC base=+0.130)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8333` → IC=+0.146 (n=708)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` > 0.8333 (IC base=+0.047)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.144 (n=1705)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0118 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2399` → IC=+0.175 (n=1705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2399 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0586` → IC=+0.139 (n=1705)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0586 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.185 (n=534)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.144 (n=1558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.142 (n=1504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.6957` → IC=+0.231 (n=1137)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6957 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2151` → IC=+0.141 (n=778)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2151 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.625` → IC=+0.140 (n=1866)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.625 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.866` → IC=+0.184 (n=394)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 16.866 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2938.7046` → IC=+0.179 (n=773)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2938.7046 (IC base=+0.137)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.381 (n=386)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.15` → IC=+0.363 (n=750)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.15 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.375 (n=568)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.383 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.373 (n=899)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7868` → IC=+0.390 (n=852)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7868 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.2713` → IC=+0.387 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2713 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.778` → IC=+0.387 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.778 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9875.3038` → IC=+0.374 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9875.3038 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.362 (n=273)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.1527` → IC=+0.365 (n=360)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1527 (IC base=+0.361)

- **PATRÓN** `drift_15min` |x|≤ `0.4181` → IC=+0.368 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4181 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2167` → IC=+0.372 (n=185)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2167 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.397 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.380 (n=380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.361)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.361 (n=416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.8042` → IC=+0.378 (n=409)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8042 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.397 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.506` → IC=+0.378 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.506 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `15106.6182` → IC=+0.388 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15106.6182 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `401.0` → IC=+0.385 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 401.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.367 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.379 (n=295)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.366 (n=297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1257` → IC=+0.379 (n=295)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1257 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1009` → IC=+0.386 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1009 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.370 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.370 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.397 (n=443)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4608` → IC=+0.382 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4608 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.857` → IC=+0.393 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.857 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.587` → IC=+0.365 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.587 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.363 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `4966.8384` → IC=+0.373 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4966.8384 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0079` → IC=-0.203 (n=3149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=3151)

- **FILTRO** `drift_15min` |x|> `0.9487` → IC=-0.156 (n=1573)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9487
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=4726)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.220 (n=2795)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=3505)

- **FILTRO** `libro_liquidez` < `4451.5462` → IC=-0.172 (n=4158)

  - _Acción_: SKIP cuando `libro_liquidez` < 4451.5462
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=2142)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.276 (n=1391)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1167` → IC=+0.208 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1167 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` < `0.6018` → IC=+0.200 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6018 (IC base=-0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.228` → IC=+0.268 (n=2083)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.228 (IC base=+0.001)

- **PATRÓN** `ibs_15` < `0.3781` → IC=+0.282 (n=6249)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3781 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` > `0.7109` → IC=+0.263 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7109 (IC base=+0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0342` → IC=-0.216 (n=3170)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0342
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=1060)

- **FILTRO** `sigma_ewma_delta_pct` > `22.121` → IC=-0.233 (n=594)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.121
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=3636)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1422` → IC=+0.286 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1422 (IC base=+0.067)

- **PATRÓN** `ibs_15` > `0.8098` → IC=+0.322 (n=452)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8098 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1068` → IC=+0.285 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1068 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.5549` → IC=+0.284 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5549 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.691` → IC=+0.135 (n=250)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 21.691 (IC base=+0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.230 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.180)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1432` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1432 (IC base=-0.180)

- **PATRÓN** `ibs_15` < `0.6353` → IC=+0.300 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6353 (IC base=-0.180)

- **PATRÓN** `dist_vwap_pct` < `0.052` → IC=+0.260 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.052 (IC base=-0.180)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.309 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 381.0 (IC base=-0.180)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=916)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.160 (n=700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0067 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.150 (n=467)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0053 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.177 (n=308)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.148)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.182 (n=555)

  - _Acción_: Kelly boost +0.91€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.174 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.5639` → IC=+0.239 (n=700)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5639 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6665` → IC=+0.164 (n=138)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.6665 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.148 (n=538)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.250 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=916)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5223.3427` → IC=+0.172 (n=467)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5223.3427 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.259 (n=1096)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.483` → IC=+0.243 (n=2491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.483 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.8354` → IC=+0.248 (n=2192)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8354 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1961` → IC=+0.256 (n=1131)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1961 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.242 (n=1097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.1947` → IC=+0.294 (n=1661)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1947 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.2433` → IC=+0.248 (n=832)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2433 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.527` → IC=+0.240 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.527 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.262` → IC=+0.239 (n=2614)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.262 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.199` → IC=-0.303 (n=378)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.199
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=1135)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.283 (n=514)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.166 (n=999)

- **FILTRO** `drift_15min` |x|> `1.0221` → IC=-0.302 (n=377)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0221
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=1136)

- **FILTRO** `sigma_ewma_delta_pct` > `6.094` → IC=-0.214 (n=330)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.094
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=1183)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.206)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.206)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.206)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2141` → IC=+0.251 (n=344)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2141 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.296 (n=1035)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.4776` → IC=+0.255 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4776 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1214` → IC=-0.273 (n=870)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1214
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=874)

- **FILTRO** `sigma_h` > `0.012` → IC=-0.244 (n=1307)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.012
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=437)

- **FILTRO** `drift_15min` |x|> `1.2903` → IC=-0.283 (n=435)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2903
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1309)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1720)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0705` → IC=+0.282 (n=1277)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0705 (IC base=-0.009)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0937` → IC=+0.287 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0937 (IC base=-0.009)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=1435)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.7901` → IC=+0.323 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7901 (IC base=-0.009)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.172 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.104)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.160 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.104)

- **PATRÓN** `drift_15min` |x|≤ `0.7469` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.7469 (IC base=+0.104)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2338` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2338 (IC base=+0.104)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.318 (n=31)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.341` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.341 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 52.0 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.136 (n=97)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.047)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.172 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0064 (IC base=+0.104)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.160 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.104)

- **PATRÓN** `drift_15min` |x|≤ `0.7469` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.7469 (IC base=+0.104)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2338` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2338 (IC base=+0.104)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.318 (n=31)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.341` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.341 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 52.0 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.136 (n=97)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.047)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.296 (n=518)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.292 (n=518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.305 (n=685)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0672` → IC=+0.286 (n=1552)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0672 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2158` → IC=+0.288 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2158 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.296 (n=1618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8354` → IC=+0.308 (n=1553)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8354 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2757` → IC=+0.318 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2757 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.592` → IC=+0.379 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.592 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13022.3239` → IC=+0.302 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13022.3239 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.305 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.282 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.076` → IC=+0.293 (n=360)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.076 (IC base=+0.279)

- **PATRÓN** `drift_15min` |x|≤ `0.3899` → IC=+0.282 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3899 (IC base=+0.279)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.279 (n=818)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.279)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2257` → IC=+0.293 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2257 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.302 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.8536` → IC=+0.305 (n=731)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8536 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2614` → IC=+0.313 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2614 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.43` → IC=+0.381 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.43 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `14354.3614` → IC=+0.312 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14354.3614 (IC base=+0.279)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.301 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.297 (n=491)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0502` → IC=+0.323 (n=246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0502 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0634` → IC=+0.292 (n=735)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0634 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1008` → IC=+0.306 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1008 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.297 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8444` → IC=+0.316 (n=736)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8444 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2913` → IC=+0.316 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2913 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.767` → IC=+0.372 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.767 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1066` → IC=-0.167 (n=241)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1066
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=119)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.144 (n=276)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=94)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1244` → IC=-0.220 (n=130)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1244
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=394)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.182 (n=130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=394)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `sigma_h` < `0.0065` → IC=-0.447 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.375 (n=6)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1431` → IC=-0.155 (n=56)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1431
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=171)

- **FILTRO** `drift_15min` |x|> `0.1893` → IC=-0.263 (n=36)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1893
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=37)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `drift_60min` |x|> `0.0858` → IC=-0.200 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0858
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1667` → IC=-0.167 (n=22)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1667
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

- **FILTRO** `drift_15min` |x|> `0.2372` → IC=-0.352 (n=25)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2372
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1551` → IC=-0.292 (n=22)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1551
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=44)

- **FILTRO** `sigma_h` > `0.0104` → IC=-0.250 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0104
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=44)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1457` → IC=-0.308 (n=24)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1457
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=47)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0549` → IC=-0.237 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9866` → IC=+0.252 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9866 (IC base=+0.122)

- **PATRÓN** `T_h` > `118.9798` → IC=+0.351 (n=3471)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 118.9798 (IC base=+0.330)

- **PATRÓN** `ratio` > `1.0009` → IC=+0.304 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0009 (IC base=+0.330)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9756` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `ratio` < 0.9756 (IC base=+0.064)

- **PATRÓN** `T_h` > `111.89` → IC=+0.320 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.89 (IC base=+0.300)

- **PATRÓN** `ratio` > `1.0002` → IC=+0.298 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0002 (IC base=+0.300)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9775` → IC=+0.361 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.185)

- **PATRÓN** `T_h` > `111.9977` → IC=+0.346 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9977 (IC base=+0.313)

- **PATRÓN** `ratio` > `1.0221` → IC=+0.409 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0221 (IC base=+0.313)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.409 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.396)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5517 sube el IC de +0.132 a +0.206 en UPDOWN_GBM#15min (n=6090). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.702 sube el IC de +0.208 a +0.275 en UPDOWN_GBM#BTC#15min (n=930). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4761 sube el IC de +0.130 a +0.216 en UPDOWN_GBM#ETH#15min (n=1194). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.6957 sube el IC de +0.137 a +0.231 en UPDOWN_GBM#XRP#15min (n=1137). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.086 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1391). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3781 sube el IC de +0.001 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=6249). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8098 sube el IC de +0.067 a +0.322 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=452). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6353 sube el IC de -0.180 a +0.300 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=88). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5639 sube el IC de +0.148 a +0.239 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=700). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.1947 sube el IC de +0.234 a +0.294 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1661). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.206 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.026 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=1035). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.009 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1435). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.104 a +0.318 en UPDOWN_GBM_ETH_15M_HORA7 (n=31). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.104 a +0.318 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=31). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8354 sube el IC de +0.284 a +0.308 en UPDOWN_GBM_IBS_ALTO (n=1553). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8536 sube el IC de +0.279 a +0.305 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=731). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8444 sube el IC de +0.289 a +0.316 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=736). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7868 sube el IC de +0.363 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=852). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8042 sube el IC de +0.361 a +0.378 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=409). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.363 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=443). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2393 | +0.084 | +266.17€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2393 | +0.084 | +266.17€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1981 | +0.085 | +226.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1981 | +0.085 | +226.68€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 96 | +0.122 | +29.03€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 96 | +0.122 | +29.03€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1529 | -0.028 | +50.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1529 | -0.028 | +50.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 1205 | -0.040 | +37.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 1205 | -0.040 | +37.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 224 | +0.035 | +20.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 93 | -0.037 | -10.65€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 52230 | -0.085 | -6679.12€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3495 | +0.086 | -324.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 48735 | -0.097 | -6355.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 5088 | -0.116 | -816.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 5088 | -0.116 | -816.49€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3495 | +0.086 | -324.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3495 | +0.086 | -324.09€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#DOGE | 5129 | -0.108 | -957.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5129 | -0.108 | -957.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 14946 | -0.040 | -1410.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 14946 | -0.040 | -1410.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 14135 | -0.121 | -1627.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 14135 | -0.121 | -1627.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9437 | -0.138 | -1543.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9437 | -0.138 | -1543.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 59773 | -0.012 | +2439.57€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 15400 | +0.004 | +1450.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 44373 | -0.017 | +988.61€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 59773 | -0.012 | +2439.57€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 15400 | +0.004 | +1450.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 44373 | -0.017 | +988.61€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 221099 | +0.112 | -9088.87€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#15min | 24040 | +0.178 | -785.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 1036 | +0.025 | -78.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 183493 | +0.105 | -7791.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 12530 | +0.095 | -432.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 30419 | +0.101 | -2210.10€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#15min | 92 | -0.202 | +7.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 30289 | +0.102 | -2226.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#60min | 23 | +0.140 | +20.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 41278 | +0.121 | -717.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5784 | +0.175 | -241.53€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 30369 | +0.118 | -273.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 5083 | +0.081 | -180.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 30477 | +0.099 | -2104.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 118 | -0.100 | +21.90€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 30326 | +0.100 | -2121.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#60min | 18 | -0.045 | +6.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 47391 | +0.123 | -1029.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 11790 | +0.176 | -350.14€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 30876 | +0.105 | -579.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4713 | +0.102 | -91.59€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 41107 | +0.111 | -1681.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 6155 | +0.199 | -240.96€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 939 | +0.048 | -24.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 31323 | +0.096 | -1226.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2690 | +0.108 | -189.61€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 30427 | +0.106 | -1345.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 101 | -0.131 | +17.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 30310 | +0.107 | -1365.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 36157 | +0.188 | -2798.35€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 36157 | +0.188 | -2798.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 8196 | +0.157 | -1023.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 8196 | +0.157 | -1023.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 5502 | +0.193 | -243.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 5502 | +0.193 | -243.51€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7969 | +0.171 | -751.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7969 | +0.171 | -751.67€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6609 | +0.251 | -239.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6609 | +0.251 | -239.04€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7802 | +0.183 | -554.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7802 | +0.183 | -554.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1376 | +0.424 | -56.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1376 | +0.424 | -56.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 588 | +0.437 | -7.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 588 | +0.437 | -7.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 528 | +0.421 | -23.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 528 | +0.421 | -23.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 246 | +0.399 | -20.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 246 | +0.399 | -20.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 127638 | +0.199 | -9370.84€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 127638 | +0.199 | -9370.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 22136 | +0.175 | -2633.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 22136 | +0.175 | -2633.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 20568 | +0.223 | -688.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 20568 | +0.223 | -688.12€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 21887 | +0.180 | -2299.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 21887 | +0.180 | -2299.73€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 20746 | +0.217 | -821.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 20746 | +0.217 | -821.34€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 21049 | +0.205 | -1236.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 21049 | +0.205 | -1236.49€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 21252 | +0.196 | -1691.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 21252 | +0.196 | -1691.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 49629 | +0.117 | +435.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 49629 | +0.117 | +435.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 24711 | +0.117 | +285.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 24711 | +0.117 | +285.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 24918 | +0.116 | +150.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 24918 | +0.116 | +150.16€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2717 | +0.294 | -7.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2717 | +0.294 | -7.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1243 | +0.283 | -25.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1243 | +0.283 | -25.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1332 | +0.297 | +10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1332 | +0.297 | +10.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1258 | +0.438 | -5.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1258 | +0.438 | -5.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 600 | +0.435 | -7.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 600 | +0.435 | -7.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 606 | +0.441 | +0.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 606 | +0.441 | +0.37€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 2090 | +0.064 | -108.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1365 | +0.073 | -44.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1656 | +0.069 | -63.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1365 | +0.073 | -44.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 101833 | +0.101 | -2142.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 8270 | +0.096 | +174.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 93563 | +0.101 | -2316.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 55542 | +0.105 | -480.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 8270 | +0.096 | +174.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 47272 | +0.106 | -654.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 21967 | +0.110 | -80.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 21967 | +0.110 | -80.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 24324 | +0.083 | -1580.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 24324 | +0.083 | -1580.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 961 | +0.167 | -109.84€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 961 | +0.167 | -109.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 961 | +0.167 | -109.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 961 | +0.167 | -109.84€ | 1 | 4 |
| ✅ GBM_LATE_15M | 69386 | +0.102 | +39070.40€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 69386 | +0.102 | +39070.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 11548 | +0.223 | +9838.10€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 11548 | +0.223 | +9838.10€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 10876 | +0.176 | +8769.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 10876 | +0.176 | +8769.12€ | 0 | 20 |
| ✅ GBM_LATE_15M#DOGE | 12400 | +0.207 | +9803.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 12400 | +0.207 | +9803.33€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 9201 | +0.064 | +3166.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 9201 | +0.064 | +3166.26€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 9603 | -0.025 | +2504.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 9603 | -0.025 | +2504.01€ | 3 | 14 |
| ✅ GBM_LATE_15M#XRP | 15758 | -0.019 | +4989.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 15758 | -0.019 | +4989.58€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 73766 | +0.088 | +43315.32€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 73766 | +0.088 | +43315.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 14330 | -0.002 | +7531.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 14330 | -0.002 | +7531.12€ | 3 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 15840 | +0.008 | +4410.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 15840 | +0.008 | +4410.52€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 9825 | +0.297 | +11297.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 9825 | +0.297 | +11297.45€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 14148 | +0.021 | +4571.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 14148 | +0.021 | +4571.63€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 11211 | +0.052 | +5284.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 11211 | +0.052 | +5284.43€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 8412 | +0.313 | +10220.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 8412 | +0.313 | +10220.18€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 54587 | +0.178 | +45276.93€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 54587 | +0.178 | +45276.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 8289 | +0.238 | +7643.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 8289 | +0.238 | +7643.37€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 8735 | +0.140 | +6566.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 8735 | +0.140 | +6566.23€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 8765 | +0.223 | +7576.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 8765 | +0.223 | +7576.25€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 9331 | +0.130 | +7312.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 9331 | +0.130 | +7312.57€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 10289 | +0.123 | +7952.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 10289 | +0.123 | +7952.94€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 9178 | +0.231 | +8225.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 9178 | +0.231 | +8225.55€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 14895 | +0.125 | +7553.57€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 14895 | +0.125 | +7553.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 680 | +0.161 | +443.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3956 | +0.125 | +2104.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3956 | +0.125 | +2104.22€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 510 | +0.154 | +284.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 510 | +0.154 | +284.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 4355 | +0.125 | +2196.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 4355 | +0.125 | +2196.56€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 4037 | +0.099 | +1655.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 4037 | +0.099 | +1655.81€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1357 | +0.168 | +868.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1357 | +0.168 | +868.50€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 69771 | +0.190 | +58135.23€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 69771 | +0.190 | +58135.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 11043 | +0.248 | +10560.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 11043 | +0.248 | +10560.35€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 11207 | +0.143 | +8191.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 11207 | +0.143 | +8191.21€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 11803 | +0.234 | +10629.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 11803 | +0.234 | +10629.66€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 11568 | +0.145 | +8735.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 11568 | +0.145 | +8735.56€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 12313 | +0.130 | +9043.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 12313 | +0.130 | +9043.04€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 11837 | +0.240 | +10975.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 11837 | +0.240 | +10975.41€ | 0 | 22 |
| ✅ GBM_LATE_5M | 17346 | +0.221 | +14718.58€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 17346 | +0.221 | +14718.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1953 | +0.254 | +1908.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1953 | +0.254 | +1908.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3363 | +0.209 | +2851.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3363 | +0.209 | +2851.83€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1592 | +0.218 | +1323.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1592 | +0.218 | +1323.49€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 5045 | +0.211 | +3987.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 5045 | +0.211 | +3987.13€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 3131 | +0.233 | +2819.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 3131 | +0.233 | +2819.38€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 2262 | +0.214 | +1828.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2262 | +0.214 | +1828.09€ | 0 | 0 |
| ✅ GBM_LATE_60M | 7294 | +0.092 | +2772.89€ | 0 | 10 |
| ✅ GBM_LATE_60M#60min | 7294 | +0.092 | +2772.89€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB | 302 | +0.276 | +332.15€ | 0 | 0 |
| ✅ GBM_LATE_60M#BNB#60min | 302 | +0.276 | +332.15€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 2166 | +0.062 | +653.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 2166 | +0.062 | +653.02€ | 1 | 5 |
| ✅ GBM_LATE_60M#DOGE | 294 | +0.307 | +352.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#DOGE#60min | 294 | +0.307 | +352.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 2020 | +0.060 | +647.52€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 2020 | +0.060 | +647.52€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 2214 | +0.065 | +434.89€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 2214 | +0.065 | +434.89€ | 0 | 9 |
| ✅ GBM_LATE_60M#XRP | 298 | +0.313 | +352.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#XRP#60min | 298 | +0.313 | +352.97€ | 0 | 23 |
| 🚫 GBM_LATE_60M_FADE | 828 | -0.246 | -36.30€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 828 | -0.246 | -36.30€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB | 12 | +0.000 | +4.05€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#BNB#60min | 12 | +0.000 | +4.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 293 | -0.256 | -19.27€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 293 | -0.256 | -19.27€ | 5 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE | 9 | -0.061 | +0.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_FADE#DOGE#60min | 9 | -0.061 | +0.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 281 | -0.246 | -9.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 281 | -0.246 | -9.46€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 229 | -0.245 | -11.34€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 229 | -0.245 | -11.34€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2751 | +0.094 | +764.64€ | 0 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2751 | +0.094 | +764.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 968 | +0.070 | +262.53€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 968 | +0.070 | +262.53€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE | 63 | +0.208 | +39.83€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#DOGE#60min | 63 | +0.208 | +39.83€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 834 | +0.054 | +160.87€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 834 | +0.054 | +160.87€ | 0 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 709 | +0.155 | +247.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 709 | +0.155 | +247.17€ | 2 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP | 177 | +0.120 | +54.24€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#XRP#60min | 177 | +0.120 | +54.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 452 | +0.302 | +534.70€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 452 | +0.302 | +534.70€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 452 | +0.302 | +534.70€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 452 | +0.302 | +534.70€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 5255 | +0.096 | +1143.17€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 5255 | +0.096 | +1143.17€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 5255 | +0.096 | +1143.17€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 5255 | +0.096 | +1143.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 2157 | +0.016 | +94.98€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 2157 | +0.016 | +94.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 277 | +0.077 | +42.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 277 | +0.077 | +42.56€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M#BTC | 389 | -0.017 | +6.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 389 | -0.017 | +6.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 202 | +0.025 | +16.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 202 | +0.025 | +16.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 463 | +0.031 | +26.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 463 | +0.031 | +26.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 365 | -0.023 | -0.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 365 | -0.023 | -0.14€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 461 | +0.018 | +3.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 461 | +0.018 | +3.76€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4763 | +0.020 | +221.16€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4763 | +0.020 | +221.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 241 | +0.002 | -6.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 893 | +0.020 | +57.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 893 | +0.020 | +57.99€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 380 | +0.065 | +94.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 380 | +0.065 | +94.36€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1795 | +0.024 | +41.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1795 | +0.024 | +41.17€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 829 | +0.011 | +3.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 829 | +0.011 | +3.42€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 625 | -0.002 | +30.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 625 | -0.002 | +30.37€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 3003 | -0.037 | -16.75€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 3003 | -0.037 | -16.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 905 | -0.040 | -20.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 905 | -0.040 | -20.80€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 1090 | -0.023 | +12.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 1090 | -0.023 | +12.10€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 973 | -0.053 | -8.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 973 | -0.053 | -8.99€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#XRP | 28 | +0.033 | +0.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#XRP#60min | 28 | +0.033 | +0.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 23008 | -0.032 | -231.59€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 11202 | -0.030 | -45.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 11806 | -0.035 | -185.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 794 | -0.051 | -38.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 407 | -0.035 | -2.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 387 | -0.068 | -35.80€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 6252 | -0.025 | -24.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2986 | -0.021 | +19.00€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 3266 | -0.030 | -43.39€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 2080 | -0.034 | -13.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 1075 | -0.035 | -12.87€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 1005 | -0.032 | -1.06€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 5307 | -0.029 | -18.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 2573 | -0.024 | +16.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2734 | -0.033 | -35.12€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 4366 | -0.028 | +13.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 2141 | -0.028 | +7.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 2225 | -0.028 | +5.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 4209 | -0.047 | -149.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 2020 | -0.048 | -73.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 2189 | -0.045 | -76.20€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 78830 | -0.001 | +4125.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 78830 | -0.001 | +4125.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 14119 | +0.027 | +1963.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 14119 | +0.027 | +1963.05€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 11395 | -0.038 | -164.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 11395 | -0.038 | -164.58€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14267 | +0.026 | +1578.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14267 | +0.026 | +1578.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 11301 | -0.055 | -331.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 11301 | -0.055 | -331.18€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 13237 | -0.004 | +377.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 14511 | +0.020 | +702.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 14511 | +0.020 | +702.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7650 | -0.052 | -112.91€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7650 | -0.052 | -112.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1271 | -0.002 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2229 | -0.059 | -21.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2229 | -0.059 | -21.98€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 107 | -0.032 | -1.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 107 | -0.032 | -1.71€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 829 | -0.117 | -34.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 829 | -0.117 | -34.58€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2338 | -0.064 | -10.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2338 | -0.064 | -10.01€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 876 | -0.021 | -29.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 876 | -0.021 | -29.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 4203 | -0.000 | -19.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 4203 | -0.000 | -19.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 1015 | -0.011 | -22.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 1015 | -0.011 | -22.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1327 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1327 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1392 | +0.006 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 197 | -0.013 | -0.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 192754 | -0.078 | +2088.33€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 192754 | -0.078 | +2088.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 33490 | -0.076 | +1909.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 33490 | -0.076 | +1909.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 29619 | -0.101 | -1408.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 29619 | -0.101 | -1408.89€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 33894 | -0.067 | +1650.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 33894 | -0.067 | +1650.49€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 29174 | -0.101 | -1061.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 29174 | -0.101 | -1061.91€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 33802 | -0.060 | +156.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 33802 | -0.060 | +156.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 32775 | -0.068 | +842.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 32775 | -0.068 | +842.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9497 | -0.035 | -175.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9497 | -0.035 | -175.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1014 | -0.017 | -18.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1014 | -0.017 | -18.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2263 | -0.046 | -28.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2263 | -0.046 | -28.65€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1013 | -0.021 | -30.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1013 | -0.021 | -30.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2691 | -0.023 | -29.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2691 | -0.023 | -29.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1324 | -0.062 | -29.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1324 | -0.062 | -29.11€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1192 | -0.036 | -39.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1192 | -0.036 | -39.19€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2484 | +0.119 | +991.42€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2348 | +0.123 | +978.82€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 539 | +0.141 | +279.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 539 | +0.141 | +279.46€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 491 | +0.119 | +176.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 491 | +0.119 | +176.30€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 427 | +0.129 | +200.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 427 | +0.129 | +200.22€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 400 | +0.132 | +191.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 400 | +0.132 | +191.83€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 491 | +0.090 | +131.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 491 | +0.090 | +131.01€ | 0 | 1 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2660 | -0.022 | -54.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2660 | -0.022 | -54.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 458 | +0.002 | +16.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 458 | +0.002 | +16.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 472 | -0.055 | -38.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 472 | -0.055 | -38.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 645 | -0.039 | -41.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 645 | -0.039 | -41.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 558 | -0.013 | -11.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 558 | -0.013 | -11.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 527 | -0.001 | +21.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 527 | -0.001 | +21.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1416 | -0.042 | +142.24€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 654 | -0.067 | +28.72€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 514 | -0.064 | +53.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 140 | -0.077 | -25.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 498 | -0.006 | +77.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 364 | +0.011 | +87.05€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 134 | -0.051 | -9.98€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 264 | -0.049 | +36.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 226 | -0.048 | +32.04€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 38 | -0.050 | +4.42€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 1104 | -0.036 | +172.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 312 | -0.064 | -30.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1801 | -0.186 | -37.88€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 716 | -0.174 | -9.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 636 | -0.172 | -5.62€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 80 | -0.183 | -3.68€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH | 606 | -0.197 | -32.04€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 536 | -0.203 | -36.64€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 70 | -0.153 | +4.60€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 479 | -0.188 | +3.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 445 | -0.185 | +0.32€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 34 | -0.222 | +3.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1617 | -0.186 | -41.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 184 | -0.183 | +4.06€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 627 | +0.373 | +555.50€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 147 | +0.185 | +120.72€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 147 | +0.185 | +120.72€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#ETH | 143 | +0.376 | +109.53€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 143 | +0.376 | +109.53€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#SOL | 337 | +0.450 | +325.25€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 337 | +0.450 | +325.25€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 627 | +0.373 | +555.50€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 1092 | +0.044 | +99.53€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 1092 | +0.044 | +99.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 361 | +0.018 | +4.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 361 | +0.018 | +4.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 83 | +0.029 | +3.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 83 | +0.029 | +3.15€ | 1 | 3 |
| ✅ STREAK_FADE_15M#SOL | 87 | +0.039 | +10.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 87 | +0.039 | +10.03€ | 2 | 3 |
| ✅ STREAK_FADE_15M#XRP | 561 | +0.063 | +81.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 561 | +0.063 | +81.61€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 3711 | -0.022 | -140.23€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3711 | -0.022 | -140.23€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1130 | -0.022 | -39.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 638 | -0.025 | -25.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 638 | -0.025 | -25.16€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 193 | -0.044 | -15.69€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 193 | -0.044 | -15.69€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1750 | -0.018 | -59.75€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1750 | -0.018 | -59.75€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 175 | +0.009 | -2.88€ | 1 | 2 |
| ✅ STREAK_FADE_60M#60min | 175 | +0.009 | -2.88€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB | 13 | +0.108 | +6.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#BNB#60min | 13 | +0.108 | +6.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#DOGE | 9 | -0.021 | -2.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#DOGE#60min | 9 | -0.021 | -2.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 52 | -0.018 | -1.12€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 52 | -0.018 | -1.12€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 92 | +0.000 | -5.57€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 92 | +0.000 | -5.57€ | 1 | 1 |
| ✅ STREAK_FADE_60M#XRP | 9 | +0.021 | -0.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#XRP#60min | 9 | +0.021 | -0.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 11817 | +0.013 | +60.94€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11817 | +0.013 | +60.94€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 3035 | +0.017 | +21.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 3035 | +0.017 | +21.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3175 | +0.011 | +22.02€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3175 | +0.011 | +22.02€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2980 | +0.008 | -1.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2980 | +0.008 | -1.87€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2627 | +0.014 | +19.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2627 | +0.014 | +19.40€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 14531 | +0.019 | +6.68€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 14531 | +0.019 | +6.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5834 | +0.021 | +5.42€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5834 | +0.021 | +5.42€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5223 | +0.020 | +5.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5223 | +0.020 | +5.09€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3474 | +0.014 | -3.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3474 | +0.014 | -3.84€ | 1 | 0 |
| ✅ UPDOWN_GBM | 131623 | +0.060 | +12605.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 32698 | +0.077 | +6380.14€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 3735 | -0.000 | +39.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 86799 | +0.062 | +6055.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 7938 | -0.002 | +135.23€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 11583 | +0.104 | +2173.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 2188 | +0.164 | +1024.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 9305 | +0.091 | +1150.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 30008 | +0.056 | +2622.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 4473 | +0.080 | +1000.23€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 1108 | +0.000 | +21.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 20682 | +0.065 | +1511.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3582 | -0.004 | +84.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 163 | -0.064 | +4.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14637 | +0.074 | +1604.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 2084 | +0.155 | +893.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 12467 | +0.061 | +712.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 31059 | +0.049 | +2206.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 7674 | +0.069 | +1179.07€ | 0 | 9 |
| ✅ UPDOWN_GBM#ETH#240min | 1070 | +0.006 | +15.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 19238 | +0.052 | +968.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2926 | -0.002 | +42.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 151 | -0.101 | +1.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 26949 | +0.042 | +1585.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 8792 | +0.034 | +509.78€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 984 | -0.011 | +6.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 15655 | +0.054 | +1071.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1381 | +0.003 | +6.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 137 | -0.140 | -8.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 17385 | +0.074 | +2414.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 7487 | +0.089 | +1772.94€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 9452 | +0.065 | +642.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#60min | 49 | +0.010 | +1.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 451 | -0.100 | -3.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1135 | +0.363 | +435.25€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1135 | +0.363 | +435.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 545 | +0.361 | +194.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 545 | +0.361 | +194.88€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 590 | +0.363 | +240.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 590 | +0.363 | +240.38€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 31052 | -0.017 | +7773.48€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 31052 | -0.017 | +7773.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 2485 | -0.046 | +651.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 2485 | -0.046 | +651.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5769 | -0.115 | +343.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5769 | -0.115 | +343.13€ | 2 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1294 | +0.218 | +1063.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 4254 | +0.215 | +2662.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 4254 | +0.215 | +2662.84€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 8701 | -0.057 | +1318.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 8701 | -0.057 | +1318.46€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 8549 | -0.052 | +1734.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 8549 | -0.052 | +1734.91€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 398 | +0.060 | +42.02€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 398 | +0.060 | +42.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 398 | +0.060 | +42.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 398 | +0.060 | +42.02€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 2070 | +0.284 | +1770.47€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 2070 | +0.284 | +1770.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 1090 | +0.279 | +880.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 1090 | +0.279 | +880.81€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 980 | +0.289 | +889.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 980 | +0.289 | +889.66€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 926 | -0.122 | -97.34€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 926 | -0.122 | -97.34€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 312 | -0.080 | -36.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 312 | -0.080 | -36.02€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 300 | -0.089 | -24.97€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 300 | -0.089 | -24.97€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 105 | -0.192 | -14.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 105 | -0.192 | -14.83€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 137 | -0.191 | -7.67€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 137 | -0.191 | -7.67€ | 6 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 5652 | +0.291 | +2427.86€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 2216 | +0.247 | +348.00€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 2187 | +0.283 | +886.89€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1249 | +0.382 | +1192.97€ | 0 | 1 |