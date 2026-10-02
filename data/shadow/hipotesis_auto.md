# Hipótesis automáticas — 2026-10-02 02:18 UTC
_Generado por shadow_postmortem.py sobre 706844 resoluciones (PNL=+84528.69€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=570)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.232 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.218 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.8035` → IC=+0.253 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8035 (IC base=+0.136)

- **PATRÓN** `banda_z` > `4.006` → IC=+0.153 (n=598)

  - _Acción_: Kelly boost +0.77€ cuando `banda_z` > 4.006 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=632)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3010.8456` → IC=+0.151 (n=399)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3010.8456 (IC base=+0.136)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=435)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.238 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.145)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.208 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.145)

- **PATRÓN** `banda_hit_calibrado` > `0.8017` → IC=+0.260 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8017 (IC base=+0.145)

- **PATRÓN** `banda_z` > `10.085` → IC=+0.216 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.085 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=540)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `6348.9626` → IC=+0.148 (n=160)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 6348.9626 (IC base=+0.145)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.214 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=+0.224 (n=103)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=92)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

- **PATRÓN** `py_entrada` > `0.35` → IC=+0.224 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.35 (IC base=+0.116)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.245 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.116)

- **PATRÓN** `banda_z` > `6.035` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 6.035 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.127 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `1196.2423` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1196.2423 (IC base=+0.116)

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
- **FILTRO** `restante_s_al_confirmar` < `145.2` → IC=-0.218 (n=7915)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.2
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=23748)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `135.17` → IC=-0.258 (n=1037)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 135.17
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3114)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.51` → IC=-0.311 (n=938)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.51
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=2816)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.68` → IC=-0.210 (n=1955)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.68
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=5868)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.5` → IC=-0.329 (n=1528)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.5
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=4584)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.211 (n=15465)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=3763)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5494.1585` → IC=+0.172 (n=2432)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5494.1585 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=13479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=16277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=12573)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=6165)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7716.0988` → IC=+0.168 (n=2353)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7716.0988 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1805)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=2273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `16028.2025` → IC=+0.230 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16028.2025 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.200 (n=1631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=1818)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2331)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `15958.35` → IC=+0.208 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15958.35 (IC base=+0.195)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.169 (n=363)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.615 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 4624.034 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=406)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.098)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=895)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.151 (n=230)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.098)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=3204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.356 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.232 (n=1442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.363 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.138 (n=761)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.250 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=867)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `1321.726` → IC=+0.147 (n=758)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1321.726 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.238 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.407 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.153 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 15.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.159 (n=641)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.150)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=792)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.150)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.226 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=13412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=12788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.231 (n=4250)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=3181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3010)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=3049)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=1216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.241 (n=1205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.342 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.238)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=2965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=2984)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=2521)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=2766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.330 (n=923)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=3056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.191 (n=2937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.194 (n=2313)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.194 (n=1114)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `11557.5115` → IC=+0.461 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11557.5115 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.447 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=250)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.455 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `17690.6554` → IC=+0.455 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 17690.6554 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.464 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `3371.5411` → IC=+0.448 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3371.5411 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.417 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.413)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.414 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.413)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.427 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.413)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.414 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.413)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=40015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.238 (n=17560)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=6883)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.183 (n=5509)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=7526)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=3580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.265 (n=4074)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=7277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=7277)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=3618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2444)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2615)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=2873)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=3059)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=6107)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=5827)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.52` → IC=+0.136 (n=5662)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.52 (IC base=+0.115)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=3073)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.139 (n=2889)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=3704)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.23` → IC=+0.139 (n=2819)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 3.23 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.183 (n=3034)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.129 (n=3211)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.134 (n=2862)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.25 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.315 (n=890)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.288 (n=1241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1549.9598` → IC=+0.295 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1549.9598 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.332 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5195.0219` → IC=+0.303 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5195.0219 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=625)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1448.4724` → IC=+0.304 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1448.4724 (IC base=+0.287)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.437 (n=488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.439 (n=244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.437 (n=269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.456 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.925` → IC=+0.455 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `1965.9066` → IC=+0.457 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1965.9066 (IC base=+0.441)

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
- **FILTRO** `py_entrada` > `0.74` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.74
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
- **FILTRO** `py_entrada` > `0.74` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.74
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
- **PATRÓN** `drift_60min` |x|≤ `0.4933` → IC=+0.130 (n=9529)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4933 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.244 (n=3180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.258 (n=2124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2197 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.366` → IC=+0.190 (n=2502)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 8.366 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.254 (n=2649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6158` → IC=+0.254 (n=2648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6158 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.231 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.321` → IC=+0.220 (n=3005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.321 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.136 (n=11568)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5667 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.5966` → IC=+0.199 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5966 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.1557` → IC=+0.176 (n=3839)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1557 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.183 (n=1838)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6971 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.8683` → IC=+0.177 (n=2786)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8683 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.1663` → IC=+0.224 (n=2003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1663 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.5599` → IC=+0.200 (n=6376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5599 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.213 (n=6939)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 122.0 (IC base=+0.068)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.207 (n=709)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.186 (n=709)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0081 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3537` → IC=+0.180 (n=2125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3537 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=1031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.180 (n=1423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 11.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.277 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.704` → IC=+0.294 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.704 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.217 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.4332` → IC=+0.178 (n=2003)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4332 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.192 (n=2166)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `2031.19` → IC=+0.176 (n=708)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2031.19 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.234 (n=1120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.241 (n=1501)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1259` → IC=+0.267 (n=740)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1259 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=1525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.0583` → IC=+0.286 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0583 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.479` → IC=+0.241 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.479 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.408` → IC=+0.240 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.408 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.265 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.5634` → IC=+0.241 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5634 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=1836)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1576.15` → IC=+0.245 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1576.15 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.238 (n=741)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3565` → IC=+0.228 (n=1684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3565 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.236 (n=1687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.220 (n=1713)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8947` → IC=+0.262 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8947 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.347` → IC=+0.222 (n=1563)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.347 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.672` → IC=+0.255 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.672 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2518` → IC=+0.223 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2518 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.0844` → IC=+0.223 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0844 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.239 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.4005` → IC=+0.223 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4005 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3804` → IC=+0.240 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3804 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11109.7462` → IC=+0.223 (n=1683)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11109.7462 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.169 (n=1139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2557` → IC=+0.149 (n=1498)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.2557 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=769)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.7169` → IC=+0.170 (n=1702)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7169 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1308` → IC=+0.154 (n=1537)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1308 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.145 (n=271)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.284` → IC=+0.144 (n=1568)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.284 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.148 (n=1702)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2085 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.8575` → IC=+0.138 (n=1135)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8575 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.178 (n=454)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4394` → IC=+0.149 (n=1592)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4394 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.145 (n=1061)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `14103.7518` → IC=+0.140 (n=1135)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 14103.7518 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.172 (n=665)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 230.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.202 (n=1906)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=2133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.299` → IC=+0.258 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.299 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.196 (n=1868)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.205 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.1669` → IC=+0.207 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1669 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=2540)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2005.405` → IC=+0.196 (n=711)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2005.405 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.220 (n=1650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.6292` → IC=+0.215 (n=1875)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6292 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=876)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.238 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.678` → IC=+0.235 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.678 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.569` → IC=+0.212 (n=2031)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.569 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3464` → IC=+0.250 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3464 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.72` → IC=+0.213 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.72 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.220 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.218 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1994.3897` → IC=+0.213 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1994.3897 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.211 (n=1674)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.211)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.170 (n=116)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=2557)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.148 (n=410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0037 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9581` → IC=+0.228 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9581 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1949` → IC=+0.332 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1949 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.846` → IC=+0.171 (n=844)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.846 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.343 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.326 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.357 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.358 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.1835` → IC=+0.334 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1835 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.331 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 155.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.1014` → IC=+0.154 (n=669)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1014 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6573` → IC=+0.196 (n=166)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6573 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.8497` → IC=+0.148 (n=685)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8497 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.1666` → IC=+0.143 (n=343)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1666 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2286` → IC=+0.197 (n=173)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2286 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.518` → IC=+0.164 (n=870)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.518 (IC base=+0.021)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=391)

- **FILTRO** `ibs_20min` < `0.3103` → IC=-0.192 (n=115)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3103
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=346)

- **FILTRO** `ibs_20min` > `0.24` → IC=-0.126 (n=2575)

  - _Acción_: SKIP cuando `ibs_20min` > 0.24
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=1271)

- **FILTRO** `sigma_ewma_delta_pct` > `8.728` → IC=-0.205 (n=405)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.728
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=3441)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.174 (n=231)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.6364 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.9817` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9817 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.332` → IC=+0.130 (n=163)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.332 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.320 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.292 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4963 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `1.4704` → IC=+0.278 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4704 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.303 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.24` → IC=+0.129 (n=1271)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.24 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7042` → IC=+0.253 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7042 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.4441` → IC=+0.241 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4441 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `0.6807` → IC=+0.270 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6807 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1591` → IC=+0.298 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1591 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.3831` → IC=+0.286 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3831 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.181 (n=666)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2021)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.210 (n=632)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=2055)

- **FILTRO** `ibs_20min` > `0.7669` → IC=-0.209 (n=997)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7669
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=2997)

- **PATRÓN** `dist_vwap_pct` > `0.7895` → IC=+0.330 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7895 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2116` → IC=+0.318 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2116 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` < `0.9837` → IC=+0.296 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9837 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6271` → IC=+0.311 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6271 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.304 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.4513` → IC=+0.304 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4513 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8125` → IC=+0.308 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8125 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5572` → IC=+0.276 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5572 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` < `0.7241` → IC=+0.258 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7241 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` > `1.0783` → IC=+0.269 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0783 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.265 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.167 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.1378` → IC=+0.261 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1378 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.4219` → IC=+0.252 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4219 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.201 (n=4110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.4721` → IC=+0.189 (n=11007)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4721 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.7125` → IC=+0.284 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7125 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.644` → IC=+0.158 (n=5650)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.644 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `1.1783` → IC=+0.246 (n=4469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1783 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `0.692` → IC=+0.254 (n=3992)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.692 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` < `0.0803` → IC=+0.241 (n=6605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0803 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.275 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `1.4628` → IC=+0.242 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4628 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `2.2634` → IC=+0.255 (n=3267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2634 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.276 (n=6737)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.101)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.167 (n=3988)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0092 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.156 (n=10528)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5455 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7043` → IC=+0.248 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7043 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2488` → IC=+0.248 (n=3461)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2488 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7077` → IC=+0.248 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7077 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1975` → IC=+0.259 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1975 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2394` → IC=+0.303 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2394 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5865` → IC=+0.274 (n=2170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5865 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.278 (n=4815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2567` → IC=-0.156 (n=853)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2567
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=2560)

- **FILTRO** `ibs_20min` > `0.7575` → IC=-0.163 (n=696)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7575
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2091)

- **FILTRO** `sigma_ewma_delta_pct` > `4.541` → IC=-0.173 (n=634)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.541
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2153)

- **PATRÓN** `ibs_20min` > `0.8991` → IC=+0.277 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8991 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.85` → IC=+0.213 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.85 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.276 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.205 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1741` → IC=+0.232 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1741 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.220 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.0951` → IC=+0.437 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0951 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1442` → IC=+0.447 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1442 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4485` → IC=+0.451 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4485 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.464 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8645` → IC=+0.168 (n=826)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8645 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.3011` → IC=+0.195 (n=444)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3011 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.176 (n=1027)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6754 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.233 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.199 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4058` → IC=+0.180 (n=376)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.4058 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.219 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 233.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.226 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.6881` → IC=+0.228 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6881 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.0717` → IC=+0.220 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0717 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.267` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.267 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5537` → IC=+0.223 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5537 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.241 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `456.0` → IC=+0.220 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 456.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.286 (n=1258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.260 (n=1696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.253 (n=1900)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.282 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.267 (n=1608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `2.1834` → IC=+0.266 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1834 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1995.0584` → IC=+0.272 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1995.0584 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.318 (n=708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.1855` → IC=+0.296 (n=686)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1855 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.321 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.3563` → IC=+0.292 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3563 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.291 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.1191` → IC=+0.292 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1191 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.571` → IC=+0.300 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.571 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.6427` → IC=+0.289 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6427 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1914.9372` → IC=+0.304 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.9372 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.289 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.286)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7729` → IC=-0.190 (n=711)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7729
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=2137)

- **PATRÓN** `ibs_20min` > `0.9046` → IC=+0.183 (n=633)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.9046 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.1819` → IC=+0.235 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1819 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `1.0035` → IC=+0.253 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0035 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.0813` → IC=+0.262 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0813 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4024` → IC=+0.278 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4024 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.261 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1443` → IC=+0.221 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1443 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.176` → IC=+0.215 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.176 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.281 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.262 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.808 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.257 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7561` → IC=-0.185 (n=1305)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7561
  - _Potencial_: sin este filtro IC_bueno=+0.284 (n=1306)

- **FILTRO** `ibs_20min` > `0.675` → IC=-0.238 (n=652)

  - _Acción_: SKIP cuando `ibs_20min` > 0.675
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=1962)

- **FILTRO** `sigma_ewma_delta_pct` > `4.739` → IC=-0.191 (n=561)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.739
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=2053)

- **PATRÓN** `ibs_20min` > `0.7561` → IC=+0.284 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7561 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.2146` → IC=+0.318 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2146 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.692` → IC=+0.168 (n=414)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.692 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8618` → IC=+0.308 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8618 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.302 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.0985` → IC=+0.301 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0985 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2733` → IC=+0.297 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2733 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4182` → IC=+0.323 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4182 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.3597` → IC=+0.295 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3597 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.325 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.131 (n=1730)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.5714 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.2196` → IC=+0.239 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2196 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.266 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.226 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.242 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.245 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.254 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.020)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.326 (n=1384)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.282)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.301 (n=725)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.282)

- **PATRÓN** `ibs_20min` > `0.7419` → IC=+0.322 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7419 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2129` → IC=+0.315 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2129 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.753` → IC=+0.307 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.753 (IC base=+0.282)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.295 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.282)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.333 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.282)

- **PATRÓN** `volumen_spike_ratio` > `1.4333` → IC=+0.294 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4333 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.286 (n=1542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `2468.9246` → IC=+0.291 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2468.9246 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.321 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.311 (n=1096)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.1967` → IC=+0.286 (n=724)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1967 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.290 (n=827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` < `0.377` → IC=+0.307 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.377 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.3173` → IC=+0.291 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3173 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.516` → IC=+0.298 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.516 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` < `0.6418` → IC=+0.284 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6418 (IC base=+0.281)

- **PATRÓN** `volumen_regimen` > `1.2365` → IC=+0.315 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2365 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.2334` → IC=+0.339 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2334 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.290 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `2.1363` → IC=+0.277 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1363 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `2421.8142` → IC=+0.285 (n=1469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2421.8142 (IC base=+0.281)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.176 (n=3102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0048 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.206 (n=3106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.3638` → IC=+0.180 (n=8189)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3638 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=9722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.225 (n=9308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1742` → IC=+0.197 (n=4002)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1742 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.38` → IC=+0.254 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.38 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.207` → IC=+0.165 (n=6196)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.207 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.160 (n=6197)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6297 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2927` → IC=+0.202 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2927 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.5582` → IC=+0.170 (n=3940)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5582 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5988` → IC=+0.180 (n=2986)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.5988 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `1963.62` → IC=+0.175 (n=8311)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1963.62 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.186 (n=8223)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 108.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.187 (n=5955)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0819` → IC=+0.214 (n=2978)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0819 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=3436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4855` → IC=+0.228 (n=8926)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4855 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.237` → IC=+0.164 (n=6472)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.237 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.319` → IC=+0.196 (n=1502)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.319 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1777` → IC=+0.158 (n=6411)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1777 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.214 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5543` → IC=+0.172 (n=3622)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5543 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.5913` → IC=+0.172 (n=2744)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5913 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.179 (n=7890)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 108.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.233 (n=523)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.205 (n=521)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.3425` → IC=+0.217 (n=1558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3425 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=1646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=1046)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.9081` → IC=+0.286 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9081 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.239` → IC=+0.331 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.239 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.247 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.4308` → IC=+0.194 (n=1453)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4308 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1595)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.247 (n=1045)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.250 (n=1061)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.286 (n=791)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.246 (n=1203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=590)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.3514` → IC=+0.259 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3514 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.213` → IC=+0.248 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.213 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.262 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4163` → IC=+0.266 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4163 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1573.1624` → IC=+0.253 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1573.1624 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.236 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0717` → IC=+0.193 (n=467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0717 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=1405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.3933` → IC=+0.223 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3933 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2016` → IC=+0.207 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2016 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.228 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.175 (n=616)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6892 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.200 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.503` → IC=+0.179 (n=600)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.503 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.160 (n=454)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `11929.0923` → IC=+0.162 (n=1251)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11929.0923 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.163 (n=583)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 235.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.160 (n=1482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.2935` → IC=+0.167 (n=1480)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2935 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.180 (n=495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 18.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.583` → IC=+0.192 (n=1480)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.583 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.924` → IC=+0.203 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.924 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.159 (n=1480)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2129 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.157` → IC=+0.149 (n=448)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.157 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4531` → IC=+0.147 (n=1369)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4531 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4221` → IC=+0.139 (n=1368)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4221 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `208.0` → IC=+0.174 (n=431)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 208.0 (IC base=+0.140)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.225 (n=703)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2509` → IC=+0.222 (n=1034)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2509 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.435` → IC=+0.276 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.435 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2002` → IC=+0.213 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2002 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.7854` → IC=+0.204 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7854 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.7283` → IC=+0.216 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7283 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=1835)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `1995.9484` → IC=+0.215 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1995.9484 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.234 (n=1173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1015` → IC=+0.256 (n=444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1015 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.246 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.624` → IC=+0.252 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.624 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.252 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7377` → IC=+0.232 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7377 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.1662` → IC=+0.224 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1662 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1988.6161` → IC=+0.227 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1988.6161 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.214 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.220)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.181 (n=1326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0065 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.4267` → IC=+0.163 (n=1501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4267 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=1567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.3498` → IC=+0.203 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3498 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1491` → IC=+0.183 (n=974)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1491 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.223 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.162 (n=1001)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.856 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.183 (n=630)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4275` → IC=+0.163 (n=490)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4275 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.165 (n=490)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `5255.5941` → IC=+0.193 (n=1000)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 5255.5941 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.152 (n=1441)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 155.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.156 (n=1569)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3873` → IC=+0.146 (n=1569)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3873 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.66` → IC=+0.175 (n=1569)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.66 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.1561` → IC=+0.141 (n=1539)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1561 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.904` → IC=+0.163 (n=547)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.904 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8571` → IC=+0.150 (n=1046)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8571 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.177 (n=233)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8013` → IC=+0.138 (n=963)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8013 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.5127` → IC=+0.129 (n=481)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5127 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `9285.5183` → IC=+0.165 (n=711)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 9285.5183 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.125 (n=1217)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 127.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.165 (n=769)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0101 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.5066` → IC=+0.213 (n=1696)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5066 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.0784` → IC=+0.216 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0784 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.821` → IC=+0.256 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.821 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.134 (n=1696)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2036 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6455` → IC=+0.128 (n=1696)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6455 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.129 (n=1705)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.127 (n=706)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.5373` → IC=+0.140 (n=721)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5373 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=1774)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2892.276` → IC=+0.206 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2892.276 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.142 (n=1331)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 47.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.163 (n=755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0062 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1064` → IC=+0.169 (n=572)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1064 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5778` → IC=+0.217 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5778 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2097` → IC=+0.147 (n=1587)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2097 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.609` → IC=+0.135 (n=357)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 7.609 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6383` → IC=+0.150 (n=572)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6383 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.226` → IC=+0.159 (n=300)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.226 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4463` → IC=+0.144 (n=521)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4463 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4154` → IC=+0.129 (n=521)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4154 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2744.6466` → IC=+0.179 (n=777)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2744.6466 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.126 (n=1509)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 52.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.227 (n=1601)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.2933` → IC=+0.209 (n=1068)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2933 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.209 (n=722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.245 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.209` → IC=+0.212 (n=1084)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.209 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.245 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.1937` → IC=+0.209 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1937 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.214 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.273 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.4668` → IC=+0.211 (n=1550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4668 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.213 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.208 (n=1582)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2839.1078` → IC=+0.205 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2839.1078 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.224 (n=727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.213 (n=748)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.232 (n=551)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.243 (n=1650)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `1.2084` → IC=+0.223 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2084 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.425` → IC=+0.249 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.425 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.7031` → IC=+0.220 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7031 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.285 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `2.1921` → IC=+0.203 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1921 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4348` → IC=+0.207 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4348 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2393.0118` → IC=+0.216 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2393.0118 (IC base=+0.210)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.190 (n=1074)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0043 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.172 (n=813)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0085 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.346` → IC=+0.174 (n=2140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.346 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=1221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.5074` → IC=+0.202 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5074 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.7962` → IC=+0.187 (n=394)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.7962 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.709` → IC=+0.192 (n=1068)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.709 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8717` → IC=+0.188 (n=1442)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8717 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `1.2057` → IC=+0.175 (n=721)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.2057 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.1625` → IC=+0.181 (n=656)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1625 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.4352` → IC=+0.178 (n=786)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4352 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.173 (n=1570)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=2753)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2674.4599` → IC=+0.170 (n=2172)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2674.4599 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.182 (n=2212)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 143.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.141 (n=1671)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0056 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=2348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.0657` → IC=+0.191 (n=834)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0657 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6992` → IC=+0.128 (n=994)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.6992 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.1642` → IC=+0.131 (n=615)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.1642 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.441` → IC=+0.146 (n=808)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.441 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2761.3271` → IC=+0.124 (n=2234)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2761.3271 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.130 (n=1033)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 27.0 (IC base=+0.110)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.178 (n=281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0029 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3311` → IC=+0.159 (n=637)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3311 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.185 (n=592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.6458` → IC=+0.208 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6458 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.2886` → IC=+0.168 (n=224)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.2886 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.162 (n=282)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.847` → IC=+0.144 (n=667)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.847 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8986` → IC=+0.177 (n=425)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8986 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.1548` → IC=+0.145 (n=662)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1548 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.0916` → IC=+0.156 (n=225)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0916 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.2005` → IC=+0.155 (n=546)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.2005 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.5048` → IC=+0.146 (n=555)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5048 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=824)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `10885.9044` → IC=+0.154 (n=637)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10885.9044 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.185 (n=268)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 155.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.210 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3396` → IC=+0.159 (n=784)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3396 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.148 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.140 (n=795)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6151` → IC=+0.179 (n=690)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6151 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1832` → IC=+0.156 (n=774)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1832 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.074` → IC=+0.145 (n=717)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.074 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.148 (n=784)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2216 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.7034` → IC=+0.153 (n=701)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.7034 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.206 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1106` → IC=+0.158 (n=682)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1106 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4106` → IC=+0.147 (n=774)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4106 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11980.3002` → IC=+0.141 (n=701)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11980.3002 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `357.0` → IC=+0.152 (n=753)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 357.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.264 (n=337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4066` → IC=+0.221 (n=765)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4066 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.6787` → IC=+0.258 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6787 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.3803` → IC=+0.218 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3803 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.2186` → IC=+0.212 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2186 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.231 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `0.8358` → IC=+0.221 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8358 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `1.1649` → IC=+0.232 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1649 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.1546` → IC=+0.252 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1546 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4105` → IC=+0.236 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4105 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.4173` → IC=+0.248 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4173 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.143 (n=239)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.087 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.6872` → IC=+0.143 (n=315)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6872 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `8078.9503` → IC=+0.128 (n=477)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 8078.9503 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.162 (n=518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0059 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.5423` → IC=+0.145 (n=579)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.5423 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.183 (n=534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.9873` → IC=+0.236 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9873 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.329` → IC=+0.198 (n=243)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 5.329 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.069` → IC=+0.161 (n=509)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.069 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.646` → IC=+0.151 (n=579)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.646 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.173` → IC=+0.169 (n=161)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.173 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.2007` → IC=+0.167 (n=253)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.2007 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=611)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2944.1737` → IC=+0.179 (n=263)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2944.1737 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.4545` → IC=+0.158 (n=486)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4545 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.8278` → IC=+0.135 (n=349)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8278 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `2503.5226` → IC=+0.134 (n=367)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2503.5226 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.128 (n=498)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 41.0 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.170 (n=183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0238 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.181 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0068 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.2345` → IC=+0.177 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2345 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.206 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.188 (n=184)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.2393` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.2393 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `1.0637` → IC=+0.159 (n=206)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 1.0637 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.301` → IC=+0.171 (n=156)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 3.301 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.6087` → IC=+0.165 (n=183)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6087 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.2547` → IC=+0.172 (n=178)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.2547 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4437` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4437 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.179 (n=185)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2499.5335` → IC=+0.153 (n=122)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2499.5335 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.149 (n=209)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0093 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.135 (n=209)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.6 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.1471` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1471 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.576` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.576 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.6508` → IC=+0.130 (n=209)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6508 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.8174` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.8174 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 17.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.211 (n=4013)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=12593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.46` → IC=+0.222 (n=12040)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.46 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.2389` → IC=+0.189 (n=4095)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.2389 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.363` → IC=+0.247 (n=2983)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.363 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `0.8807` → IC=+0.172 (n=5383)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8807 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2879` → IC=+0.202 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2879 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.5733` → IC=+0.196 (n=3874)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5733 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `1798.4772` → IC=+0.179 (n=12033)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1798.4772 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.202 (n=9394)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 81.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.193 (n=7229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.191 (n=4768)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=4105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.4509` → IC=+0.246 (n=9535)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4509 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2505` → IC=+0.163 (n=6772)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2505 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.045` → IC=+0.202 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.045 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.734` → IC=+0.183 (n=10463)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.734 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7061` → IC=+0.162 (n=3243)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7061 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.242 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.5918` → IC=+0.192 (n=3357)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5918 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.201 (n=6526)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.231 (n=668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.220 (n=1335)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.3613` → IC=+0.206 (n=1998)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3613 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.206 (n=1347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.331 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.358 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2269` → IC=+0.258 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2269 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.2349` → IC=+0.211 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2349 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=2021)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2031.19` → IC=+0.207 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.19 (IC base=+0.204)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.221 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.261 (n=1086)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.261 (n=1629)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.1259` → IC=+0.281 (n=716)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1259 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.3594` → IC=+0.282 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3594 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.511` → IC=+0.258 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.511 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.466` → IC=+0.258 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.466 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.291 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.5452` → IC=+0.258 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5452 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.602` → IC=+0.275 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.602 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=1779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1576.15` → IC=+0.268 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1576.15 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.205 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.157 (n=853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1124 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2898` → IC=+0.204 (n=1938)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2898 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.185 (n=1091)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.174 (n=425)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.169` → IC=+0.154 (n=1766)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.169 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6276` → IC=+0.179 (n=646)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6276 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0731` → IC=+0.155 (n=1714)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0731 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2681` → IC=+0.189 (n=278)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2681 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1166` → IC=+0.161 (n=1656)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1166 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `11387.0581` → IC=+0.155 (n=1731)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 11387.0581 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.173 (n=806)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 278.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.166 (n=1631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.26` → IC=+0.166 (n=1433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.26 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=740)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.2908` → IC=+0.236 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2908 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.164 (n=1487)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.523` → IC=+0.159 (n=274)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.523 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.303` → IC=+0.149 (n=1484)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.303 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.161 (n=1629)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1967 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.202 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.408` → IC=+0.156 (n=1531)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.408 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7569` → IC=+0.161 (n=1020)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7569 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `259.0` → IC=+0.158 (n=480)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 259.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.258 (n=655)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2062)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=1986)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.349` → IC=+0.302 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.349 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.223 (n=1800)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.231 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2005.4352` → IC=+0.233 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2005.4352 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.240 (n=1619)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.6121` → IC=+0.236 (n=1840)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6121 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.260 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0148` → IC=+0.302 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0148 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.844` → IC=+0.280 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.844 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3404` → IC=+0.294 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3404 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7265` → IC=+0.233 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7265 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.1457` → IC=+0.239 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1457 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1988.6686` → IC=+0.248 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1988.6686 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.249 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.193 (n=689)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0034 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4358` → IC=+0.151 (n=2063)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4358 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=2155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.2746` → IC=+0.190 (n=2063)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.2746 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3636` → IC=+0.165 (n=799)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.3636 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.528` → IC=+0.165 (n=332)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.528 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.872` → IC=+0.163 (n=1376)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.872 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.208 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.154 (n=882)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1577` → IC=+0.158 (n=909)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1577 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7612.6539` → IC=+0.235 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7612.6539 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.172 (n=651)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 72.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.171 (n=1104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0052 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3594` → IC=+0.140 (n=1456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3594 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.5901` → IC=+0.196 (n=1456)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5901 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1587` → IC=+0.132 (n=1450)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1587 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.273` → IC=+0.161 (n=249)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.273 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6225` → IC=+0.141 (n=552)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6225 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.221 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.141 (n=1581)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `9534.8435` → IC=+0.204 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9534.8435 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.129 (n=1390)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 145.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.149 (n=1367)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0082 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.5758` → IC=+0.127 (n=2050)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.5758 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.463` → IC=+0.200 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.463 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.0669` → IC=+0.209 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0669 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.546` → IC=+0.240 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.546 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8919` → IC=+0.146 (n=1367)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8919 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.128 (n=2107)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8314` → IC=+0.124 (n=1331)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.8314 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.4546` → IC=+0.134 (n=665)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4546 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=2085)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2536.8901` → IC=+0.238 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2536.8901 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.143 (n=1629)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 52.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.181 (n=653)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0058 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1368` → IC=+0.158 (n=652)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1368 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.208 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.2212` → IC=+0.136 (n=1629)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2212 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.128 (n=1881)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.6464` → IC=+0.162 (n=652)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6464 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2207` → IC=+0.181 (n=308)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2207 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `2.1519` → IC=+0.131 (n=1575)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.1519 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2799.1755` → IC=+0.186 (n=652)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2799.1755 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.131 (n=1585)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 51.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.229 (n=2026)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=894)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.262 (n=1818)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.2144` → IC=+0.234 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2144 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.596` → IC=+0.256 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.596 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.0607` → IC=+0.216 (n=1782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0607 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.221 (n=2025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2856` → IC=+0.246 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2856 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.4788` → IC=+0.236 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4788 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2622.2574` → IC=+0.219 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2622.2574 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.217 (n=711)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.231 (n=711)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.223 (n=1508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.262 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `1.2224` → IC=+0.215 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2224 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2187` → IC=+0.214 (n=1892)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2187 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.258 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.232` → IC=+0.238 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.232 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.279 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `2.1732` → IC=+0.204 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1732 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4297` → IC=+0.207 (n=1942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4297 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2402.9744` → IC=+0.211 (n=1904)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2402.9744 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.199 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.209)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=3669)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.218 (n=1215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.5106` → IC=+0.190 (n=3637)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.5106 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=1365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.182 (n=1663)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9428` → IC=+0.238 (n=1212)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9428 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1728` → IC=+0.189 (n=1335)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1728 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.2` → IC=+0.208 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.2 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7092` → IC=+0.185 (n=1095)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.7092 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.8941` → IC=+0.183 (n=1659)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.8941 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1682` → IC=+0.208 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1682 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.189 (n=1197)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.186 (n=2393)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=2699)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `2516.9882` → IC=+0.186 (n=3636)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2516.9882 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.218 (n=924)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.4894` → IC=+0.177 (n=2764)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.4894 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=1251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.1827` → IC=+0.187 (n=1217)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1827 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.6663` → IC=+0.184 (n=514)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6663 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.22` → IC=+0.171 (n=2758)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.22 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2562` → IC=+0.166 (n=2599)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2562 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.168 (n=2526)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5345` → IC=+0.169 (n=1201)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5345 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8235` → IC=+0.172 (n=1819)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8235 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=3669)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `5320.6072` → IC=+0.167 (n=2469)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5320.6072 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.167 (n=1796)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 85.0 (IC base=+0.162)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.223 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.202)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.212 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1526` → IC=+0.204 (n=511)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1526 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.190 (n=530)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5327` → IC=+0.200 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5327 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.8859` → IC=+0.192 (n=387)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.8859 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.207` → IC=+0.198 (n=975)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.207 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.152` → IC=+0.197 (n=1047)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 4.152 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `1.0851` → IC=+0.192 (n=1021)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.0851 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `1.2448` → IC=+0.190 (n=388)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.2448 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.200 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.4736` → IC=+0.194 (n=1138)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.4736 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=1165)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.223 (n=316)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3841` → IC=+0.197 (n=827)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3841 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.178 (n=628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 10.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.7559` → IC=+0.171 (n=940)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.7559 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.0908` → IC=+0.173 (n=939)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.0908 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.6077` → IC=+0.188 (n=203)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6077 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.74` → IC=+0.171 (n=962)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.74 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6432` → IC=+0.203 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6432 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `0.7257` → IC=+0.167 (n=839)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.7257 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.0726` → IC=+0.182 (n=398)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0726 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.181 (n=810)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.7855` → IC=+0.167 (n=614)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.7855 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `7781.8228` → IC=+0.181 (n=839)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 7781.8228 (IC base=+0.166)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.178 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0089 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.171 (n=357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 3.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.144 (n=369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 14.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.9326` → IC=+0.242 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9326 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.2235` → IC=+0.197 (n=242)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2235 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.224 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.7117` → IC=+0.193 (n=161)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.7117 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.2654` → IC=+0.145 (n=122)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.2654 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.4173` → IC=+0.200 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4173 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=430)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2997.549` → IC=+0.167 (n=364)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2997.549 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.165 (n=305)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 51.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.191 (n=299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0067 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.6689` → IC=+0.178 (n=299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.6689 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.164 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 16.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` < `0.6765` → IC=+0.191 (n=263)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6765 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.6343` → IC=+0.225 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6343 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.639` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.639 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.3` → IC=+0.163 (n=289)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 5.3 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `1.3839` → IC=+0.168 (n=299)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.3839 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `1.1845` → IC=+0.159 (n=136)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.1845 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.219 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.6095` → IC=+0.179 (n=129)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.6095 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `3188.7067` → IC=+0.198 (n=299)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3188.7067 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.215 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.160)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.165 (n=503)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0039 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.6459` → IC=+0.181 (n=936)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6459 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1469` → IC=+0.147 (n=564)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1469 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.194 (n=246)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.190 (n=143)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.081)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.124 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0045 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.0406` → IC=+0.298 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0406 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.1925` → IC=+0.132 (n=444)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1925 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.074` → IC=+0.145 (n=333)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.074 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.1389` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1389 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.5091` → IC=+0.142 (n=339)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.5091 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `1.4436` → IC=+0.143 (n=303)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4436 (IC base=+0.043)

- **PATRÓN** `libro_liquidez` > `3269.2861` → IC=+0.142 (n=163)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3269.2861 (IC base=+0.043)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.135 (n=392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0058 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.426` → IC=+0.161 (n=361)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.426 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.156 (n=190)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `2.0809` → IC=+0.134 (n=282)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.0809 (IC base=+0.088)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.131 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0052 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.194 (n=60)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.2748` → IC=+0.258 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2748 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.3046` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.3046 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.0689` → IC=+0.144 (n=192)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.0689 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.069` → IC=+0.190 (n=182)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 7.069 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `1.1635` → IC=+0.137 (n=188)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1635 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `0.6903` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6903 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `1.437` → IC=+0.140 (n=148)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.437 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `3329.7378` → IC=+0.146 (n=159)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3329.7378 (IC base=+0.088)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.7001` → IC=-0.123 (n=152)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7001
  - _Potencial_: sin este filtro IC_bueno=+0.220 (n=309)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=154)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.138 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0049 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.7001` → IC=+0.220 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7001 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.3353` → IC=+0.201 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3353 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.652` → IC=+0.282 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.652 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.8` → IC=+0.135 (n=231)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.7617` → IC=+0.151 (n=196)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.7617 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `1135.9488` → IC=+0.155 (n=305)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1135.9488 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2423` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2423 (IC base=+0.003)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0118` → IC=-0.262 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0118
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=122)

- **FILTRO** `ibs_20min` > `0.15` → IC=-0.291 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.281 (n=80)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.180 (n=229)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.7778 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.7761` → IC=+0.139 (n=95)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.7761 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.104` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 8.104 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.055)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.133 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0092 (IC base=+0.012)

- **PATRÓN** `ibs_20min` < `0.15` → IC=+0.281 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.15 (IC base=+0.012)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.0734` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0734 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `1.7331` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7331 (IC base=+0.012)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1705` → IC=-0.300 (n=58)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1705
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=175)

- **FILTRO** `volumen_regimen` < `0.7296` → IC=-0.350 (n=58)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7296
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=177)

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
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=51)

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

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=-0.201)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=65)

- **FILTRO** `ibs_20min` < `0.125` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.125
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

- **FILTRO** `volumen_spike_ratio` < `1.6212` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.6212
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=38)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.180 (n=148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0059 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.6616` → IC=+0.149 (n=326)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6616 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.4967` → IC=+0.192 (n=76)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.4967 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `1.4188` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4188 (IC base=+0.092)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.123 (n=335)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.006 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.149 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.190 (n=295)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.156 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.13` → IC=+0.186 (n=135)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 6.13 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` < `0.1746` → IC=+0.125 (n=254)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1746 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `2.5919` → IC=+0.144 (n=259)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.5919 (IC base=+0.091)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=355)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `3965.7979` → IC=+0.208 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3965.7979 (IC base=+0.091)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6292` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6292
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=99)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.186 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0033 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.237 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.173 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.1613` → IC=+0.230 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1613 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.1046` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1046 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.62` → IC=+0.179 (n=135)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.62 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.1644` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.1644 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `0.8617` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8617 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.233 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `2.5892` → IC=+0.233 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5892 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.4576` → IC=+0.192 (n=118)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4576 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `4542.5709` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4542.5709 (IC base=+0.162)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.2505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2505
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=90)

- **FILTRO** `libro_liquidez` < `1419.7314` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 1419.7314
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=105)

- **PATRÓN** `libro_liquidez` > `1545.7265` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1545.7265 (IC base=+0.039)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.191 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0027 (IC base=+0.078)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.124 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 8.0 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.3115` → IC=+0.147 (n=120)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.3115 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.734` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.734 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `0.8247` → IC=+0.134 (n=80)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8247 (IC base=+0.078)

- **PATRÓN** `libro_liquidez` > `1586.0507` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1586.0507 (IC base=+0.078)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=67)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.314 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.265 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.244 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.9583` → IC=+0.262 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9583 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.267 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.309 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.1671` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1671 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.423 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `591.0149` → IC=+0.241 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 591.0149 (IC base=+0.239)

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
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.123 (n=1062)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.495 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2925.3906` → IC=+0.158 (n=302)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2925.3906 (IC base=+0.112)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.495` → IC=+0.123 (n=1062)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.495 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2925.3906` → IC=+0.158 (n=302)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2925.3906 (IC base=+0.112)

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
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=230)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=216)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=46)

- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=50)

- **FILTRO** `liq_n` < `5.0` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `liq_n` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=23)

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
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=2325)

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
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=93)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.121 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 15.0 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 16.0 (IC base=+0.044)

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

- **PATRÓN** `liq_usd_total` > `136034.58` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `liq_usd_total` > 136034.58 (IC base=+0.044)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.164 (n=138)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.495 (IC base=+0.044)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=948)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=902)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=548)

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
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=246)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.495 (IC base=+0.030)

- **PATRÓN** `libro_liquidez` > `4102.5152` → IC=+0.162 (n=66)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4102.5152 (IC base=+0.030)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=723)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=723)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=456)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=456)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=196)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=196)

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
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=277)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=277)

- **FILTRO** `libro_liquidez` < `537.9862` → IC=-0.121 (n=101)

  - _Acción_: SKIP cuando `libro_liquidez` < 537.9862
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=206)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=163)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.121 (n=951)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=965)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.131 (n=82)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=93)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.134 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=156)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.52 (IC base=-0.014)

- **PATRÓN** `py_entrada` < `0.48` → IC=+0.130 (n=79)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.48 (IC base=+0.004)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.56 (IC base=+0.044)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` < `8.11` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `restante_min` < 8.11
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=95)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.200 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=88)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.150 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 9.0 (IC base=+0.086)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.127 (n=116)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=42)

- **FILTRO** `profundidad_ratio` < `54.9` → IC=-0.222 (n=52)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.9
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=106)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=143)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.53 (IC base=-0.044)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=171)

- **FILTRO** `restante_min` < `3.4` → IC=-0.257 (n=68)

  - _Acción_: SKIP cuando `restante_min` < 3.4
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=142)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.167 (n=61)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=149)

- **FILTRO** `lag_apertura_s` > `92.29` → IC=-0.253 (n=71)

  - _Acción_: SKIP cuando `lag_apertura_s` > 92.29
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=139)

- **FILTRO** `profundidad_ratio` < `81.1` → IC=-0.173 (n=105)

  - _Acción_: SKIP cuando `profundidad_ratio` < 81.1
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=105)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.162 (n=140)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=78)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` > 0.5 (IC base=-0.050)

- **PATRÓN** `profundidad_ratio` > `14.4` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `profundidad_ratio` > 14.4 (IC base=+0.023)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.226 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=194)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.164 (n=4255)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=12825)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.166 (n=4274)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=13374)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.198 (n=744)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=2260)

- **PATRÓN** `libro_liquidez` > `1798.16` → IC=+0.127 (n=1022)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1798.16 (IC base=+0.032)

- **PATRÓN** `libro_liquidez` > `1565.4334` → IC=+0.142 (n=1075)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1565.4334 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.180 (n=744)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2314)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=754)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=2443)

- **PATRÓN** `libro_liquidez` > `1792.72` → IC=+0.128 (n=1040)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 1792.72 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.166 (n=735)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2264)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2383)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3123)

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
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=655)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=11914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=26673)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=8998)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=29589)

- **FILTRO** `ibs_7min` < `0.2656` → IC=-0.235 (n=9646)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=28941)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.157 (n=12747)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=25840)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.234 (n=11938)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=36907)

- **FILTRO** `ibs_7min` > `0.2909` → IC=-0.181 (n=12205)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2909
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=36640)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.139 (n=1936)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4570)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.307 (n=1564)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=4942)

- **FILTRO** `ibs_7min` < `0.7077` → IC=-0.252 (n=2145)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7077
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=4361)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.181 (n=1512)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=4994)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.263 (n=2082)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6346)

- **FILTRO** `ibs_7min` > `0.7917` → IC=-0.211 (n=2106)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7917
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6322)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=5047)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=1621)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4992)

- **FILTRO** `ibs_7min` < `0.7438` → IC=-0.197 (n=1653)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7438
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4960)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.180 (n=1647)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=4966)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=1569)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5156)

- **FILTRO** `ibs_7min` > `0.2621` → IC=-0.186 (n=1679)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2621
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5046)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.187 (n=1671)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=5054)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.161 (n=1525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4670)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=1458)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=4737)

- **FILTRO** `ibs_7min` < `0.7042` → IC=-0.247 (n=2043)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7042
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=4152)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.212 (n=1466)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4729)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.246 (n=2066)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=6942)

- **FILTRO** `ibs_7min` > `0.7436` → IC=-0.177 (n=2249)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7436
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=6759)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.233 (n=1881)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=4474)

- **FILTRO** `ibs_7min` < `0.7407` → IC=-0.184 (n=1588)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4767)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.173 (n=1565)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4790)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=1617)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=4900)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.180 (n=1628)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4889)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.179 (n=1628)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4889)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.263 (n=1612)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4973)

- **FILTRO** `ibs_7min` < `0.2558` → IC=-0.230 (n=1645)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2558
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4940)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.183 (n=2215)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=7127)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.273 (n=1484)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=4849)

- **FILTRO** `ibs_7min` < `0.2692` → IC=-0.223 (n=1583)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2692
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4750)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1471)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=4862)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.207 (n=2070)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=6755)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1181)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=585)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

- **FILTRO** `libro_liquidez` < `7904.1448` → IC=-0.131 (n=345)

  - _Acción_: SKIP cuando `libro_liquidez` < 7904.1448
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=701)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=333)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.150 (n=158)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=477)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4167` → IC=+0.145 (n=573)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4167 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `447.889` → IC=+0.154 (n=287)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 447.889 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=284)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 16.0 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4377` → IC=+0.167 (n=67)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4377 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.226 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.140)

- **PATRÓN** `total_vol_5m` < `421.686` → IC=+0.144 (n=175)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 421.686 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2571.3862` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2571.3862 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 13.0 (IC base=+0.140)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 11.0 (IC base=+0.108)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4137` → IC=+0.183 (n=118)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.4137 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.189 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 16.0 (IC base=+0.105)

- **PATRÓN** `total_vol_5m` < `385.7846` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 385.7846 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 73.0 (IC base=+0.105)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.165 (n=150)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.179 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 11.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.154 (n=151)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 8043.774 (IC base=+0.129)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.141 (n=151)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.093)

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
- **FILTRO** `sigma_h` > `0.0081` → IC=-0.227 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=44)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.8` → IC=-0.250 (n=110)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=335)

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
- **FILTRO** `T_h` > `135.9851` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=95)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=228)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=325)

- **PATRÓN** `streak_estiramiento` < `0.4493` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `streak_estiramiento` < 0.4493 (IC base=+0.034)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=46)

- **FILTRO** `streak_estiramiento` > `0.4382` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4382
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=40)

- **PATRÓN** `volumen_racha` < `991078.0` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_racha` < 991078.0 (IC base=-0.015)

- **PATRÓN** `streak_estiramiento` < `0.4382` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.4382 (IC base=-0.015)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.143 (n=82)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 48.0 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `2479.8468` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2479.8468 (IC base=+0.063)

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
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=819)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=825)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=490)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=726)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1315)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=866)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=853)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3233)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1656)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.239 (n=673)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1594` → IC=+0.204 (n=1775)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1594 (IC base=+0.198)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2192` → IC=+0.207 (n=673)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2192 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.128` → IC=+0.238 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.128 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=1882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=2080)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.619` → IC=+0.278 (n=2017)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.619 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1189` → IC=+0.196 (n=1004)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1189 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.77` → IC=+0.290 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.77 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2957.7936` → IC=+0.204 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2957.7936 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.219 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.198)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=856)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.230 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.284 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `0.3831` → IC=+0.216 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3831 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2014` → IC=+0.244 (n=197)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2014 (IC base=+0.211)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4` → IC=+0.242 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.244 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` > `0.7176` → IC=+0.274 (n=435)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7176 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.275 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.385` → IC=+0.262 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.385 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `16193.642` → IC=+0.248 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16193.642 (IC base=+0.211)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.296` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.296
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=517)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.169 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0035 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.147 (n=310)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.005 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.162 (n=205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.175 (n=155)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1204` → IC=+0.169 (n=173)

  - _Acción_: Kelly boost +0.84€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1204 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.163 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.144 (n=484)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.6604` → IC=+0.263 (n=415)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6604 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.2911` → IC=+0.150 (n=429)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2911 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.389` → IC=+0.234 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.389 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3402.1385` → IC=+0.152 (n=415)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3402.1385 (IC base=+0.141)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.009` → IC=+0.298 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.1511` → IC=+0.224 (n=215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1511 (IC base=+0.191)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0615` → IC=+0.203 (n=244)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0615 (IC base=+0.191)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3271` → IC=+0.239 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3271 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.200 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_15` > `0.5926` → IC=+0.281 (n=244)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5926 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.206 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.190 (n=240)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.981` → IC=+0.404 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.981 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=266)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `3083.8765` → IC=+0.288 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3083.8765 (IC base=+0.191)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.191` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.191 (IC base=-0.011)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.243 (n=458)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.224 (n=226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.204)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0641` → IC=+0.204 (n=458)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0641 (IC base=+0.204)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0847` → IC=+0.266 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0847 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.230 (n=250)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.204)

- **PATRÓN** `ibs_15` > `0.5769` → IC=+0.290 (n=513)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5769 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.3546` → IC=+0.218 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3546 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.249` → IC=+0.248 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.249 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2923.757` → IC=+0.292 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2923.757 (IC base=+0.204)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.357 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.355)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.383 (n=160)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.355)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.358 (n=321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.355)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.379 (n=319)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.355)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1316` → IC=+0.392 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1316 (IC base=+0.355)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.373 (n=488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.355)

- **PATRÓN** `ibs_15` > `0.7863` → IC=+0.392 (n=480)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7863 (IC base=+0.355)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.390 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.355)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.363 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.355)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.354 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.355)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.359 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.355)

- **PATRÓN** `libro_liquidez` > `3823.0046` → IC=+0.372 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3823.0046 (IC base=+0.355)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.367 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.367 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.361)

- **PATRÓN** `drift_60min` |x|≤ `0.0537` → IC=+0.378 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0537 (IC base=+0.361)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.373 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.372 (n=263)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1241` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1241 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.384 (n=265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.391 (n=263)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.3935` → IC=+0.400 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3935 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.106` → IC=+0.361 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.106 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.763` → IC=+0.363 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.763 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `16049.8465` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.8465 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `504.0` → IC=+0.411 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 504.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.382 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.345)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.357 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.345)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.367 (n=194)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.345)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.375 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.345)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.406 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.345)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.395 (n=217)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.345)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.382 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.345)

- **PATRÓN** `dist_vwap_pct` < `0.2994` → IC=+0.344 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2994 (IC base=+0.345)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.361 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.345)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.346 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.345)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.352 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.345)

- **PATRÓN** `libro_liquidez` > `4305.62` → IC=+0.367 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4305.62 (IC base=+0.345)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.224 (n=774)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2324)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1095)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2003)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.243 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6423` → IC=+0.274 (n=749)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6423 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.193 (n=611)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1232` → IC=+0.249 (n=1530)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1232 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1804` → IC=+0.250 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1804 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.3499` → IC=+0.275 (n=2293)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3499 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.6676` → IC=+0.294 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6676 (IC base=-0.024)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.214 (n=467)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1402)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.216 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1402)

- **FILTRO** `sigma_ewma_delta_pct` > `23.61` → IC=-0.260 (n=265)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.61
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1604)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.165 (n=180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0028 (IC base=+0.083)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.286 (n=101)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.083)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.083)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.326 (n=222)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.288 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` < `0.2297` → IC=+0.280 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2297 (IC base=+0.083)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0841` → IC=+0.157 (n=33)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.0841 (IC base=-0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.193)

- **PATRÓN** `ibs_15` < `0.5472` → IC=+0.300 (n=33)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.5472 (IC base=-0.193)

- **PATRÓN** `ballena_activa_n` < `305.0` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 305.0 (IC base=-0.193)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=464)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.153 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0065 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.174 (n=323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0039 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.214 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.152)

- **PATRÓN** `drift_15min` |x|≤ `0.4133` → IC=+0.159 (n=121)

  - _Acción_: Kelly boost +0.79€ cuando `drift_15min` |x|≤ 0.4133 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.224 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.182 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 11.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.659` → IC=+0.258 (n=361)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.659 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.4686` → IC=+0.154 (n=102)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.4686 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1135` → IC=+0.176 (n=257)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1135 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=464)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `10043.6494` → IC=+0.187 (n=164)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 10043.6494 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.245 (n=874)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4431` → IC=+0.239 (n=874)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4431 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `0.778` → IC=+0.247 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.778 (IC base=+0.234)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2074` → IC=+0.261 (n=396)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2074 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.235 (n=334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.234)

- **PATRÓN** `ibs_15` < `0.2735` → IC=+0.280 (n=769)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2735 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.7445` → IC=+0.308 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7445 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.25` → IC=+0.271 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.25 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.472` → IC=+0.239 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.472 (IC base=+0.234)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1704` → IC=-0.231 (n=247)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1704
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=482)

- **FILTRO** `drift_15min` |x|> `0.9044` → IC=-0.272 (n=182)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9044
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=547)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.195 (n=362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=367)

- **FILTRO** `sigma_ewma_delta_pct` > `18.215` → IC=-0.139 (n=386)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.215
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3109)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.196 (n=54)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.5625 (IC base=-0.172)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 47.0 (IC base=-0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0785` → IC=+0.225 (n=340)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0785 (IC base=-0.042)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1843` → IC=+0.226 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1843 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.267 (n=380)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7023` → IC=+0.253 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7023 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1738` → IC=+0.229 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1738 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.264 (n=438)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=439)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=253)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=624)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0626` → IC=+0.270 (n=524)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0626 (IC base=-0.035)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1078` → IC=+0.324 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1078 (IC base=-0.035)

- **PATRÓN** `ibs_15` < `0.3284` → IC=+0.292 (n=586)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3284 (IC base=-0.035)

- **PATRÓN** `dist_vwap_pct` > `0.8735` → IC=+0.345 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8735 (IC base=-0.035)

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
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.296 (n=688)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.329 (n=261)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2388` → IC=+0.302 (n=261)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2388 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2191` → IC=+0.317 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2191 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8408` → IC=+0.327 (n=782)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8408 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.4391` → IC=+0.335 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4391 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.344 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `13020.8583` → IC=+0.298 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13020.8583 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.295 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0549` → IC=+0.335 (n=143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0549 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.314 (n=143)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.303 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8303` → IC=+0.316 (n=428)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8303 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.355 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.321 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.306 (n=312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.295 (n=354)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.318 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.295 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2883` → IC=+0.326 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2883 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.315 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.335 (n=355)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2911` → IC=+0.306 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2911 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.333 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.294 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2521` → IC=-0.153 (n=73)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2521
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=221)

- **FILTRO** `ballena_activa_n` > `46.0` → IC=-0.136 (n=196)

  - _Acción_: SKIP cuando `ballena_activa_n` > 46.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=66)

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
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=116)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1259` → IC=-0.167 (n=43)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1259
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=132)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.619 sube el IC de +0.198 a +0.278 en UPDOWN_GBM#15min (n=2017). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7176 sube el IC de +0.211 a +0.274 en UPDOWN_GBM#BTC#15min (n=435). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6604 sube el IC de +0.141 a +0.263 en UPDOWN_GBM#ETH#15min (n=415). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5926 sube el IC de +0.191 a +0.281 en UPDOWN_GBM#SOL#15min (n=244). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5769 sube el IC de +0.204 a +0.290 en UPDOWN_GBM#XRP#15min (n=513). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6423 sube el IC de -0.066 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=749). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3499 sube el IC de -0.024 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=2293). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.083 a +0.326 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=222). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.5472 sube el IC de -0.193 a +0.300 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=33). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.659 sube el IC de +0.152 a +0.258 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=361). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2735 sube el IC de +0.234 a +0.280 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=769). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.172 a +0.196 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=54). Ya aplicado como kelly_boost=+0.98€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.042 a +0.267 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=380). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3284 sube el IC de -0.035 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=586). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8408 sube el IC de +0.289 a +0.327 en UPDOWN_GBM_IBS_ALTO (n=782). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8303 sube el IC de +0.283 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=428). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.295 a +0.335 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=355). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7863 sube el IC de +0.355 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=480). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.361 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=263). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.345 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=217). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1479 | +0.098 | +197.33€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1479 | +0.098 | +197.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1124 | +0.107 | +169.44€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1124 | +0.107 | +169.44€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 257 | +0.060 | +10.44€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 257 | +0.060 | +10.44€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 67 | +0.123 | +17.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 67 | +0.123 | +17.79€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 42 | +0.023 | -4.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 42 | +0.023 | -4.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 35 | +0.013 | -6.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 35 | +0.013 | -6.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 7 | +0.019 | +1.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 7 | +0.019 | +1.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 31663 | -0.088 | -4130.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1629 | -0.022 | -213.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 30034 | -0.091 | -3917.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4151 | -0.110 | -670.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4151 | -0.110 | -670.94€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1629 | -0.022 | -213.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1629 | -0.022 | -213.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3754 | -0.110 | -872.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3754 | -0.110 | -872.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8194 | -0.014 | -768.50€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8194 | -0.014 | -768.50€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7823 | -0.097 | -461.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7823 | -0.097 | -461.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6112 | -0.163 | -1143.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6112 | -0.163 | -1143.68€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 23037 | -0.022 | +3762.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5965 | +0.001 | +1759.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 17072 | -0.030 | +2002.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 23037 | -0.022 | +3762.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5965 | +0.001 | +1759.13€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 17072 | -0.030 | +2002.97€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 107793 | +0.113 | -5150.63€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15522 | +0.184 | -468.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 450 | -0.060 | -57.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 85032 | +0.101 | -4373.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6789 | +0.106 | -250.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 14126 | +0.100 | -1077.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 50 | -0.135 | +11.03€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 14061 | +0.102 | -1077.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 21537 | +0.130 | -397.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4751 | +0.199 | -142.04€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 14101 | +0.115 | -176.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2643 | +0.095 | -56.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 14172 | +0.092 | -1216.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 58 | -0.117 | -8.25€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 14099 | +0.093 | -1196.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 22888 | +0.124 | -435.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6160 | +0.177 | -86.27€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 14255 | +0.105 | -285.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2461 | +0.101 | -54.91€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 20925 | +0.114 | -1174.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4451 | +0.189 | -253.38€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 353 | -0.021 | -3.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 14436 | +0.093 | -777.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1685 | +0.131 | -139.17€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 14145 | +0.099 | -850.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 52 | -0.037 | +9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 14080 | +0.100 | -859.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 17151 | +0.195 | -1047.93€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 17151 | +0.195 | -1047.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4009 | +0.173 | -380.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4009 | +0.173 | -380.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1713 | +0.204 | -13.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1713 | +0.204 | -13.47€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3954 | +0.182 | -317.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3954 | +0.182 | -317.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3499 | +0.243 | -107.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3499 | +0.243 | -107.89€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3897 | +0.190 | -242.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3897 | +0.190 | -242.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 803 | +0.433 | -17.24€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 803 | +0.433 | -17.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 315 | +0.443 | +0.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 315 | +0.443 | +0.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 305 | +0.432 | -6.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 305 | +0.432 | -6.80€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 171 | +0.413 | -8.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 171 | +0.413 | -8.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 59492 | +0.198 | -4579.22€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 59492 | +0.198 | -4579.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10240 | +0.179 | -1140.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10240 | +0.179 | -1140.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9535 | +0.222 | -352.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9535 | +0.222 | -352.05€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10251 | +0.175 | -1180.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10251 | +0.175 | -1180.41€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9619 | +0.218 | -380.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9619 | +0.218 | -380.37€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9858 | +0.202 | -651.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9858 | +0.202 | -651.51€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9989 | +0.192 | -874.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9989 | +0.192 | -874.14€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 22609 | +0.115 | +110.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 22609 | +0.115 | +110.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11224 | +0.119 | +114.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11224 | +0.119 | +114.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11385 | +0.112 | -3.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11385 | +0.112 | -3.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1654 | +0.289 | -23.77€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1654 | +0.289 | -23.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 741 | +0.279 | -16.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 741 | +0.279 | -16.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 798 | +0.287 | -10.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 798 | +0.287 | -10.34€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 115 | +0.346 | +3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 115 | +0.346 | +3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 733 | +0.437 | -1.76€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 733 | +0.437 | -1.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 351 | +0.435 | -3.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 351 | +0.435 | -3.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 336 | +0.441 | +0.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 336 | +0.441 | +0.99€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1262 | +0.066 | -67.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 443 | +0.053 | -39.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 819 | +0.072 | -27.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 65 | +0.112 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 65 | +0.112 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 996 | +0.071 | -37.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 177 | +0.064 | -9.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 819 | +0.072 | -27.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 201 | +0.022 | -33.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 201 | +0.022 | -33.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 42896 | +0.098 | -1229.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3504 | +0.089 | +24.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 39392 | +0.099 | -1254.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 23873 | +0.102 | -345.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3504 | +0.089 | +24.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 20369 | +0.105 | -369.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8373 | +0.107 | -43.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8373 | +0.107 | -43.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10650 | +0.081 | -840.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10650 | +0.081 | -840.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 859 | +0.208 | -102.88€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 859 | +0.208 | -102.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 859 | +0.208 | -102.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 859 | +0.208 | -102.88€ | 1 | 4 |
| ✅ GBM_LATE_15M | 30225 | +0.087 | +14860.71€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 30225 | +0.087 | +14860.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 5071 | +0.201 | +3868.39€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 5071 | +0.201 | +3868.39€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4513 | +0.178 | +3224.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4513 | +0.178 | +3224.86€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 5341 | +0.200 | +4027.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5341 | +0.200 | +4027.17€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 4312 | +0.029 | +1057.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4312 | +0.029 | +1057.46€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4307 | -0.032 | +937.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4307 | -0.032 | +937.20€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6681 | -0.038 | +1745.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6681 | -0.038 | +1745.63€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 32379 | +0.088 | +17275.61€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 32379 | +0.088 | +17275.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6200 | +0.013 | +3237.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6200 | +0.013 | +3237.21€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6733 | +0.015 | +1421.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6733 | +0.015 | +1421.96€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4591 | +0.268 | +4727.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4591 | +0.268 | +4727.13€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5375 | +0.009 | +1165.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5375 | +0.009 | +1165.38€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5225 | +0.035 | +2093.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5225 | +0.035 | +2093.25€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4255 | +0.281 | +4630.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4255 | +0.281 | +4630.69€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 24305 | +0.172 | +18650.70€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 24305 | +0.172 | +18650.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3657 | +0.215 | +3033.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3657 | +0.215 | +3033.55€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3839 | +0.148 | +2772.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3839 | +0.148 | +2772.88€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3840 | +0.212 | +3115.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3840 | +0.212 | +3115.71€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4091 | +0.136 | +2988.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4091 | +0.136 | +2988.48€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4545 | +0.121 | +3268.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4545 | +0.121 | +3268.08€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4333 | +0.207 | +3471.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4333 | +0.207 | +3471.99€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6574 | +0.138 | +3082.56€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6574 | +0.138 | +3082.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 308 | +0.132 | +158.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 308 | +0.132 | +158.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1894 | +0.141 | +999.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1894 | +0.141 | +999.18€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1972 | +0.154 | +973.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1972 | +0.154 | +973.06€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1505 | +0.112 | +553.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1505 | +0.112 | +553.27€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 521 | +0.133 | +221.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 521 | +0.133 | +221.06€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 30490 | +0.178 | +23323.61€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 30490 | +0.178 | +23323.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4831 | +0.228 | +4242.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4831 | +0.228 | +4242.94€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4754 | +0.149 | +3113.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4754 | +0.149 | +3113.83€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 5069 | +0.227 | +4389.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 5069 | +0.227 | +4389.21€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4956 | +0.135 | +3499.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4956 | +0.135 | +3499.83€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5340 | +0.120 | +3599.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5340 | +0.120 | +3599.03€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5540 | +0.211 | +4478.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5540 | +0.211 | +4478.76€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8532 | +0.172 | +5656.14€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 8532 | +0.172 | +5656.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2054 | +0.167 | +1488.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2054 | +0.167 | +1488.35€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2798 | +0.178 | +1849.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2798 | +0.178 | +1849.50€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 883 | +0.151 | +506.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 883 | +0.151 | +506.33€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1049 | +0.139 | +510.94€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2152 | +0.070 | +780.94€ | 0 | 13 |
| ✅ GBM_LATE_60M#60min | 2152 | +0.070 | +780.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 804 | +0.088 | +277.85€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 804 | +0.088 | +277.85€ | 0 | 17 |
| ✅ GBM_LATE_60M#ETH | 691 | +0.071 | +316.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 691 | +0.071 | +316.01€ | 2 | 11 |
| ✅ GBM_LATE_60M#SOL | 657 | +0.045 | +187.08€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 657 | +0.045 | +187.08€ | 2 | 9 |
| 🚫 GBM_LATE_60M_FADE | 430 | -0.243 | -11.79€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 430 | -0.243 | -11.79€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 161 | -0.218 | -5.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 161 | -0.218 | -5.44€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 145 | -0.235 | -0.58€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 145 | -0.235 | -0.58€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 124 | -0.278 | -5.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 124 | -0.278 | -5.77€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 880 | +0.092 | +229.49€ | 0 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 880 | +0.092 | +229.49€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 331 | +0.083 | +76.26€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 331 | +0.083 | +76.26€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 298 | +0.060 | +38.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 298 | +0.060 | +38.52€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 251 | +0.140 | +114.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 251 | +0.140 | +114.70€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 117 | +0.248 | +95.63€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 117 | +0.248 | +95.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 117 | +0.248 | +95.63€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 117 | +0.248 | +95.63€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2469 | +0.107 | +686.10€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2469 | +0.107 | +686.10€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2469 | +0.107 | +686.10€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2469 | +0.107 | +686.10€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 414 | -0.072 | -32.72€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 414 | -0.072 | -32.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 111 | -0.040 | -2.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 111 | -0.040 | -2.85€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 154 | -0.026 | -5.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 154 | -0.026 | -5.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2525 | +0.020 | +63.45€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2525 | +0.020 | +63.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 129 | +0.027 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 129 | +0.027 | -1.60€ | 1 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 351 | +0.021 | +27.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 351 | +0.021 | +27.41€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 186 | -0.021 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 186 | -0.021 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 996 | +0.033 | +33.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 996 | +0.033 | +33.88€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 588 | +0.009 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 588 | +0.009 | -1.04€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 275 | +0.020 | +10.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 275 | +0.020 | +10.26€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1274 | -0.042 | -24.95€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1274 | -0.042 | -24.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 361 | -0.040 | -12.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 361 | -0.040 | -12.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 428 | -0.030 | -2.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 428 | -0.030 | -2.39€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 485 | -0.054 | -10.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 485 | -0.054 | -10.09€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 3666 | -0.020 | +56.29€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1715 | -0.026 | -2.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1951 | -0.014 | +58.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 100 | +0.020 | +9.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 51 | +0.066 | +10.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 49 | -0.029 | -1.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 887 | +0.003 | +48.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 411 | -0.004 | +12.54€ | 2 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 476 | +0.008 | +36.09€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 425 | -0.020 | +11.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 205 | -0.046 | -5.56€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 220 | +0.004 | +17.14€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 735 | -0.043 | -33.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 333 | -0.052 | -23.78€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 402 | -0.035 | -9.34€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 725 | -0.028 | +1.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 348 | -0.034 | -1.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 377 | -0.022 | +2.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 794 | -0.020 | +18.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 367 | -0.020 | +5.13€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 427 | -0.020 | +13.29€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 34728 | -0.005 | +1583.58€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 34728 | -0.005 | +1583.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6165 | +0.022 | +790.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6165 | +0.022 | +790.95€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5245 | -0.031 | -80.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5245 | -0.031 | -80.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6255 | +0.018 | +575.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6255 | +0.018 | +575.39€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 5025 | -0.053 | -166.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 5025 | -0.053 | -166.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5852 | -0.009 | +197.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5852 | -0.009 | +197.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6186 | +0.012 | +266.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6186 | +0.012 | +266.61€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6066 | -0.061 | -154.87€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6066 | -0.061 | -154.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1217 | +0.000 | -14.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1467 | -0.084 | -41.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1467 | -0.084 | -41.73€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 689 | -0.127 | -33.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 689 | -0.127 | -33.66€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1794 | -0.078 | -34.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1794 | -0.078 | -34.75€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 87432 | -0.073 | +1786.28€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 87432 | -0.073 | +1786.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 14934 | -0.075 | +902.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 14934 | -0.075 | +902.36€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 13338 | -0.096 | -716.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 13338 | -0.096 | -716.86€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 15203 | -0.067 | +795.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 15203 | -0.067 | +795.76€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 12872 | -0.093 | -273.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 12872 | -0.093 | -273.52€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 15927 | -0.050 | +357.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 15927 | -0.050 | +357.31€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 15158 | -0.063 | +721.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 15158 | -0.063 | +721.22€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7901 | -0.029 | -135.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7901 | -0.029 | -135.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1827 | -0.038 | -14.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1827 | -0.038 | -14.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1004 | -0.021 | -31.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1004 | -0.021 | -31.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2235 | -0.024 | -29.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2235 | -0.024 | -29.06€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1071 | -0.043 | -15.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1071 | -0.043 | -15.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 768 | -0.021 | -23.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 768 | -0.021 | -23.86€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1281 | +0.110 | +446.22€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1145 | +0.116 | +433.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 265 | +0.140 | +135.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 265 | +0.140 | +135.90€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 220 | +0.108 | +61.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 220 | +0.108 | +61.90€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 236 | +0.105 | +86.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 236 | +0.105 | +86.48€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 200 | +0.129 | +90.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 200 | +0.129 | +90.05€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 224 | +0.093 | +59.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 224 | +0.093 | +59.29€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 739 | -0.036 | -43.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 739 | -0.036 | -43.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 147 | +0.003 | +6.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 147 | +0.003 | +6.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 104 | -0.057 | -10.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 104 | -0.057 | -10.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 208 | -0.052 | -23.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 208 | -0.052 | -23.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 159 | -0.022 | -6.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 159 | -0.022 | -6.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 121 | -0.053 | -10.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 121 | -0.053 | -10.48€ | 0 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE | 833 | -0.201 | -40.70€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 345 | -0.195 | -30.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 295 | -0.197 | -30.77€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 50 | -0.173 | +0.17€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 284 | -0.217 | -26.27€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 243 | -0.227 | -32.11€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 204 | -0.184 | +16.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 186 | -0.181 | +12.51€ | 4 | 1 |
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
| ✅ STREAK_FADE_15M | 591 | +0.031 | +17.99€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 591 | +0.031 | +17.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 287 | +0.029 | +4.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 287 | +0.029 | +4.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 42 | +0.068 | +1.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 42 | +0.068 | +1.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 63 | -0.008 | -1.69€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 63 | -0.008 | -1.69€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 199 | +0.037 | +13.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 199 | +0.037 | +13.28€ | 2 | 5 |
| ✅ STREAK_FADE_5M | 3000 | -0.023 | -123.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3000 | -0.023 | -123.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 899 | -0.021 | -31.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 899 | -0.021 | -31.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 576 | -0.024 | -24.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 576 | -0.024 | -24.20€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1369 | -0.021 | -53.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1369 | -0.021 | -53.91€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 79 | -0.043 | -6.02€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 79 | -0.043 | -6.02€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 41 | +0.012 | -1.58€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 41 | +0.012 | -1.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9207 | +0.022 | +128.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9207 | +0.022 | +128.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2547 | +0.024 | +33.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2547 | +0.024 | +33.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2107 | +0.032 | +54.78€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2107 | +0.032 | +54.78€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2792 | +0.013 | +8.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2792 | +0.013 | +8.41€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1761 | +0.023 | +31.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1761 | +0.023 | +31.69€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8206 | +0.012 | -47.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8206 | +0.012 | -47.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3252 | +0.017 | -7.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3252 | +0.017 | -7.93€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3264 | +0.011 | -23.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3264 | +0.011 | -23.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1690 | +0.005 | -16.77€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1690 | +0.005 | -16.77€ | 1 | 0 |
| ✅ UPDOWN_GBM | 48741 | +0.038 | +3402.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 12584 | +0.074 | +2519.89€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1685 | +0.004 | +7.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 31378 | +0.030 | +843.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2912 | +0.004 | +32.23€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4932 | +0.076 | +634.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 928 | +0.161 | +417.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3971 | +0.057 | +218.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 9370 | +0.046 | +726.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1634 | +0.088 | +371.37€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 451 | +0.012 | +5.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5899 | +0.048 | +313.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1318 | +0.005 | +34.31€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 68 | -0.086 | +1.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5653 | +0.046 | +414.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 894 | +0.143 | +331.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4731 | +0.028 | +83.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 10717 | +0.028 | +531.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3139 | +0.051 | +405.04€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 444 | +0.007 | +8.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 6092 | +0.023 | +119.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 982 | +0.000 | -4.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 60 | -0.113 | +3.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 10947 | +0.018 | +341.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 3004 | +0.027 | +238.38€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 435 | -0.003 | -1.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6844 | +0.018 | +105.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 612 | +0.006 | +2.81€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 52 | -0.148 | -3.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 7120 | +0.042 | +756.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2985 | +0.089 | +755.96€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 294 | +0.000 | -3.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3841 | +0.009 | +3.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 180 | -0.115 | +0.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 639 | +0.355 | +221.05€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 639 | +0.355 | +221.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 350 | +0.361 | +119.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 350 | +0.361 | +119.59€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 289 | +0.345 | +101.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 289 | +0.345 | +101.47€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 14246 | -0.033 | +3173.61€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 14246 | -0.033 | +3173.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1024 | -0.053 | +381.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1024 | -0.053 | +381.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2588 | -0.116 | +56.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2588 | -0.116 | +56.18€ | 3 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 555 | +0.200 | +417.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 555 | +0.200 | +417.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1645 | +0.210 | +1040.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1645 | +0.210 | +1040.98€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4224 | -0.064 | +586.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4224 | -0.064 | +586.90€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4210 | -0.071 | +690.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4210 | -0.071 | +690.55€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 163 | +0.039 | +8.29€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 163 | +0.039 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 163 | +0.039 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 163 | +0.039 | +8.29€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1042 | +0.289 | +859.31€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1042 | +0.289 | +859.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 570 | +0.283 | +433.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 570 | +0.283 | +433.33€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 472 | +0.295 | +425.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 472 | +0.295 | +425.97€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 745 | -0.112 | -83.03€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 745 | -0.112 | -83.03€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 221 | -0.083 | -16.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 221 | -0.083 | -16.77€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 75 | -0.188 | -6.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 75 | -0.188 | -6.89€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2733 | +0.305 | +1353.40€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 958 | +0.257 | +142.14€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1043 | +0.296 | +460.38€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 732 | +0.377 | +750.88€ | 0 | 1 |