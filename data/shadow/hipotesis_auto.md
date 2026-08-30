# Hipótesis automáticas — 2026-08-30 02:25 UTC
_Generado por shadow_postmortem.py sobre 208965 resoluciones (PNL=+16113.44€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.735` → IC=+0.268 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.166)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.185 (n=255)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 19.0 (IC base=+0.166)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.166)

- **PATRÓN** `banda_hit_calibrado` > `0.8194` → IC=+0.279 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8194 (IC base=+0.166)

- **PATRÓN** `banda_z` > `10.822` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.822 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.195 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 11.0 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=293)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `3000.2192` → IC=+0.223 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3000.2192 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.835` → IC=+0.123 (n=221)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.835 (IC base=-0.005)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.123 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=111)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.270 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.203)

- **PATRÓN** `n_ballena_banda` > `18.0` → IC=+0.225 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 18.0 (IC base=+0.203)

- **PATRÓN** `n_total_lado` > `55.0` → IC=+0.256 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 55.0 (IC base=+0.203)

- **PATRÓN** `banda_hit_calibrado` > `0.8294` → IC=+0.318 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8294 (IC base=+0.203)

- **PATRÓN** `banda_z` > `12.161` → IC=+0.264 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 12.161 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.223 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.203 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.218 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `4022.7675` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4022.7675 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=93)

- **FILTRO** `banda_hit_calibrado` < `0.6329` → IC=-0.232 (n=39)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6329
  - _Potencial_: sin este filtro IC_bueno=+0.238 (n=82)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=97)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=69)

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=52)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=71)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.335 (IC base=+0.085)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.085)

- **PATRÓN** `banda_z` > `8.441` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.441 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.085)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `147.7` → IC=-0.292 (n=2923)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.7
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=8773)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.82` → IC=-0.263 (n=377)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.82
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=1134)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `644.77` → IC=-0.189 (n=204)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 644.77
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=616)

- **FILTRO** `restante_s_al_confirmar` < `443.09` → IC=-0.191 (n=205)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 443.09
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=615)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.5` → IC=-0.382 (n=378)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.5
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1136)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `158.48` → IC=-0.165 (n=781)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.48
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2343)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `139.94` → IC=-0.323 (n=675)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.94
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2028)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.29` → IC=-0.359 (n=667)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.29
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=1357)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.192 (n=6248)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.7 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=1751)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2376.0723` → IC=+0.175 (n=1682)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2376.0723 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.143 (n=3791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 18.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=5041)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.256 (n=3948)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3252)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `1904.0199` → IC=+0.181 (n=2732)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1904.0199 (IC base=+0.142)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.208 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.383 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.190 (n=657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 7.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.259 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=935)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `13178.3279` → IC=+0.220 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13178.3279 (IC base=+0.188)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.127 (n=497)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.134 (n=575)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.555 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=263)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `4885.6012` → IC=+0.159 (n=209)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4885.6012 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.195 (n=195)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.184 (n=289)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.41 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4063.9233` → IC=+0.151 (n=302)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4063.9233 (IC base=+0.132)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=74)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=1382)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.129 (n=1161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.324 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.281 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.277 (n=546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.276)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.412 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `2165.7492` → IC=+0.282 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2165.7492 (IC base=+0.276)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.153 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.258 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=406)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2090.1554` → IC=+0.163 (n=298)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2090.1554 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.160 (n=142)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.079)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=1036)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.439 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.355 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `1967.759` → IC=+0.224 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1967.759 (IC base=+0.215)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.222 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.210 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=280)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.107)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.286 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `py_entrada` > `0.835` → IC=-0.364 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=133)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=5152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=4345)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.202 (n=2458)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2366.4457` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2366.4457 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=1118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.177 (n=1347)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.164)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=73)

- **FILTRO** `py_entrada` > `0.795` → IC=-0.403 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=67)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.409 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.328)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.328)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.175 (n=1246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=1095)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.169 (n=1239)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` < 0.73 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.179 (n=876)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.72 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=1173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.231 (n=989)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.231)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.309 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.231)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.185 (n=1075)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.199 (n=645)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.7 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.468 (n=91)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.445)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.448 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.456 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.445)

- **PATRÓN** `libro_liquidez` > `3351.8902` → IC=+0.460 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3351.8902 (IC base=+0.445)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.436 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `10024.8272` → IC=+0.457 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10024.8272 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.457 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.439 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.939` → IC=+0.441 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.939 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.435 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `3697.0572` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3697.0572 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.431 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.456 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.92` → IC=+0.443 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.92 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=4945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.218 (n=10840)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.141 (n=2673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.163 (n=1843)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.72 (IC base=+0.135)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=2328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.269 (n=1724)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.233)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.203 (n=848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.217 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.170)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.243 (n=1199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.227)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.231 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.244 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.209)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.199 (n=837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 18.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=1757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.232 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.206 (n=1963)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.133)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.139 (n=1800)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` < 3.95 (IC base=+0.133)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.155 (n=1927)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.93 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.153 (n=2648)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 8.0 (IC base=+0.133)

- **PATRÓN** `lag_apertura_s` < `4.2` → IC=+0.155 (n=1796)

  - _Acción_: Kelly boost +0.78€ cuando `lag_apertura_s` < 4.2 (IC base=+0.133)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.211 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.138)

- **PATRÓN** `restante_min` < `3.92` → IC=+0.144 (n=895)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` < 3.92 (IC base=+0.138)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.152 (n=1235)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` > 4.88 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.166 (n=1311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 8.0 (IC base=+0.138)

- **PATRÓN** `lag_apertura_s` < `7.04` → IC=+0.155 (n=1181)

  - _Acción_: Kelly boost +0.78€ cuando `lag_apertura_s` < 7.04 (IC base=+0.138)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.202 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.128)

- **PATRÓN** `restante_min` < `4.4` → IC=+0.130 (n=1190)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` < 4.4 (IC base=+0.128)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.162 (n=995)

  - _Acción_: Kelly boost +0.81€ cuando `restante_min` > 4.94 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=1190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `lag_apertura_s` < `3.41` → IC=+0.169 (n=901)

  - _Acción_: Kelly boost +0.84€ cuando `lag_apertura_s` < 3.41 (IC base=+0.128)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.312 (n=561)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=653)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.368 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `3824.2708` → IC=+0.298 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3824.2708 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.299 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `4160.4948` → IC=+0.295 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4160.4948 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.329 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.305 (n=300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.366 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `1733.724` → IC=+0.311 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1733.724 (IC base=+0.296)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.338 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.339)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.355 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.339)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.371 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.364 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.339)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.422 (n=269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.416)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.423 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.416)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.426 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.416)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.417 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.416)

- **PATRÓN** `libro_liquidez` > `2076.1143` → IC=+0.429 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.1143 (IC base=+0.416)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.426 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.413)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.413)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.416 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.413)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.421 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.413)

- **PATRÓN** `libro_liquidez` > `5531.9875` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5531.9875 (IC base=+0.413)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.431 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.421)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.421)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.423 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.421)

- **PATRÓN** `libro_liquidez` > `2076.021` → IC=+0.452 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.021 (IC base=+0.421)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.305 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.344 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.295 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `2113.8339` → IC=+0.324 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2113.8339 (IC base=+0.282)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.305 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.344 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.295 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `2113.8339` → IC=+0.324 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2113.8339 (IC base=+0.282)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9516` → IC=+0.211 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9516 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1852` → IC=+0.224 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1852 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.7196` → IC=+0.217 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7196 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.33` → IC=+0.161 (n=1059)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 5.33 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `0.6297` → IC=+0.224 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6297 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.0648` → IC=+0.237 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0648 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.153 (n=1464)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2464` → IC=+0.160 (n=310)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2464 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `2.4264` → IC=+0.159 (n=1342)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4264 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `1.9513` → IC=+0.154 (n=1016)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.9513 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.1163` → IC=+0.152 (n=1361)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1163 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1787` → IC=+0.142 (n=884)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1787 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `0.618` → IC=+0.158 (n=299)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.618 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `1.0417` → IC=+0.139 (n=405)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0417 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.3136` → IC=+0.257 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3136 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.9552` → IC=+0.221 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9552 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.211 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.028)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.180 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.007 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.186 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.963` → IC=+0.289 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.963 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2109` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2109 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.124 (n=509)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.175 (n=426)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.04 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.168 (n=221)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 48.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.260 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.290 (n=122)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.0689` → IC=+0.323 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0689 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.256 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.266 (n=370)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.0455` → IC=+0.339 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0455 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.917` → IC=+0.278 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.917 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.0707` → IC=+0.249 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0707 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.3107` → IC=+0.329 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3107 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.9274` → IC=+0.259 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9274 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.8655` → IC=+0.307 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8655 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.293 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1933.4502` → IC=+0.290 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.4502 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.244 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 63.0 (IC base=+0.256)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.247 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.234 (n=156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.211 (n=441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.399` → IC=+0.225 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.399 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.2097` → IC=+0.225 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2097 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.5452` → IC=+0.211 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5452 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.351` → IC=+0.231 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.351 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.221 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6892 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.0799` → IC=+0.234 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0799 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.215 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `2.109` → IC=+0.232 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.109 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `14064.4602` → IC=+0.216 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14064.4602 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `398.0` → IC=+0.206 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 398.0 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.165 (n=174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0023 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.150 (n=347)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0036 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.0735` → IC=+0.157 (n=173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0735 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.156 (n=547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 18.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.4461` → IC=+0.180 (n=455)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.4461 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.170 (n=452)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1366 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.938` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.938 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6183` → IC=+0.191 (n=173)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6183 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.9981` → IC=+0.146 (n=235)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.9981 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.197 (n=176)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.7479` → IC=+0.172 (n=275)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.7479 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4117` → IC=+0.172 (n=412)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.4117 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=669)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `14111.5146` → IC=+0.192 (n=235)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 14111.5146 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 214.0 (IC base=+0.144)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.222 (n=185)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.019` → IC=+0.277 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.019 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.1324` → IC=+0.148 (n=450)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.1324 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.4063` → IC=+0.157 (n=68)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.4063 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `3.3381` → IC=+0.143 (n=415)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 3.3381 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.6927` → IC=+0.158 (n=471)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.6927 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.182 (n=526)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.187 (n=244)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 43.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.259 (n=422)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.4476` → IC=+0.248 (n=422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4476 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.247 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.256 (n=436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.5185` → IC=+0.281 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5185 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.131` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.131 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.928` → IC=+0.252 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.928 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.4009` → IC=+0.340 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4009 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.6221` → IC=+0.243 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6221 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.274 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1876.5391` → IC=+0.255 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.5391 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.224 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.245)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `sigma_h` > `0.0094` → IC=-0.151 (n=130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=394)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.169 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=405)

- **FILTRO** `ibs_20min` < `0.2901` → IC=-0.132 (n=172)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2901
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=352)

- **FILTRO** `ibs_20min` > `0.8596` → IC=-0.175 (n=232)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8596
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=698)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.162 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=864)

- **PATRÓN** `dist_vwap_pct` > `0.124` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.124 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` < `0.6297` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6297 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` > `0.7026` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7026 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2199` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2199 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.435` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.435 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` > `1.9251` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9251 (IC base=-0.044)

- **PATRÓN** `ballena_activa_n` < `140.0` → IC=+0.243 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 140.0 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.2734` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2734 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.283 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` > `1.5804` → IC=+0.133 (n=107)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.5804 (IC base=-0.048)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.147 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=107)

- **FILTRO** `sigma_h` > `0.0104` → IC=-0.136 (n=363)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0104
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1092)

- **FILTRO** `sigma_ewma_delta_pct` > `5.019` → IC=-0.164 (n=313)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.019
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1142)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.176 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0056 (IC base=+0.039)

- **PATRÓN** `ibs_20min` > `0.5263` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.5263 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.5947` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5947 (IC base=+0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5168` → IC=-0.162 (n=264)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5168
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=515)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.201 (n=182)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=597)

- **FILTRO** `ibs_20min` > `0.7937` → IC=-0.183 (n=329)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7937
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=991)

- **FILTRO** `sigma_ewma_delta_pct` > `6.782` → IC=-0.156 (n=216)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.782
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1104)

- **PATRÓN** `dist_vwap_pct` < `0.3758` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.3758 (IC base=-0.104)

- **PATRÓN** `volumen_regimen` > `1.0562` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0562 (IC base=-0.104)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.220 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1309 (IC base=-0.054)

- **PATRÓN** `volumen_regimen` > `1.3639` → IC=+0.260 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3639 (IC base=-0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.088` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.088 (IC base=-0.054)

- **PATRÓN** `volumen_spike_ratio` < `2.4934` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4934 (IC base=-0.054)

- **PATRÓN** `volumen_spike_ratio` > `1.717` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.717 (IC base=-0.054)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 20.0 (IC base=-0.054)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.136 (n=1554)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0076 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.2759` → IC=+0.122 (n=3425)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.2759 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `1.2538` → IC=+0.295 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2538 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `1.0201` → IC=+0.216 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0201 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.1153` → IC=+0.186 (n=1542)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1153 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.251` → IC=+0.203 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.251 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.4951` → IC=+0.211 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4951 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.8672` → IC=+0.188 (n=527)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.8672 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.279 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.0909` → IC=+0.194 (n=1344)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.0909 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7758` → IC=+0.227 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7758 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` < `0.223` → IC=+0.215 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.223 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.8624` → IC=+0.220 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8624 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.233 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2623` → IC=+0.331 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2623 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `2.9138` → IC=+0.288 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9138 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.266 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.039)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2584` → IC=-0.152 (n=257)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2584
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=524)

- **FILTRO** `sigma_ewma_delta_pct` > `2.143` → IC=-0.172 (n=248)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.143
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=564)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.055` → IC=+0.131 (n=196)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 4.055 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.211` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.211 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.7557` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7557 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8811` → IC=-0.158 (n=308)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8811
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=928)

- **PATRÓN** `dist_vwap_pct` > `0.5723` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.5723 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.2669` → IC=+0.132 (n=104)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2669 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` < `0.5591` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5591 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` > `0.9911` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.9911 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.6908` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6908 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` > `2.1913` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.1913 (IC base=-0.044)

- **PATRÓN** `ballena_activa_n` < `265.0` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 265.0 (IC base=-0.044)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.288 (n=182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.224 (n=183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.206 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.258 (n=196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.126` → IC=+0.297 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.126 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.1431` → IC=+0.211 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1431 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.546` → IC=+0.208 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.546 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `3.34` → IC=+0.214 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.34 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `1925.7032` → IC=+0.212 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1925.7032 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.330 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.320)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.327 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.320)

- **PATRÓN** `drift_60min` |x|≤ `0.2352` → IC=+0.331 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2352 (IC base=+0.320)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.345 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.320)

- **PATRÓN** `ibs_20min` < `0.3415` → IC=+0.341 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3415 (IC base=+0.320)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.607` → IC=+0.335 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.607 (IC base=+0.320)

- **PATRÓN** `volumen_pendiente_norm` < `0.143` → IC=+0.313 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.143 (IC base=+0.320)

- **PATRÓN** `volumen_pendiente_norm` > `0.3643` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3643 (IC base=+0.320)

- **PATRÓN** `volumen_spike_ratio` < `1.6966` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6966 (IC base=+0.320)

- **PATRÓN** `volumen_spike_ratio` > `2.4671` → IC=+0.328 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4671 (IC base=+0.320)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.323 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.320)

- **PATRÓN** `libro_liquidez` > `1860.9977` → IC=+0.354 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1860.9977 (IC base=+0.320)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.320)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `sigma_h` > `0.0065` → IC=-0.147 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=406)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.167 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=365)

- **FILTRO** `dist_vwap_pct` < `0.2886` → IC=-0.225 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2886
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=38)

- **FILTRO** `volumen_regimen` > `0.9969` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9969
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=58)

- **FILTRO** `ibs_20min` > `0.7397` → IC=-0.136 (n=363)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7397
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=710)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `volumen_regimen` > `0.8819` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8819
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **FILTRO** `volumen_pendiente_norm` < `0.1167` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1167
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=5)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.176 (n=69)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1004)

- **PATRÓN** `dist_vwap_pct` > `0.2886` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2886 (IC base=-0.083)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=-0.083)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7576` → IC=-0.133 (n=499)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7576
  - _Potencial_: sin este filtro IC_bueno=+0.231 (n=258)

- **FILTRO** `ibs_20min` > `0.7647` → IC=-0.224 (n=237)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7647
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=713)

- **FILTRO** `dist_vwap_pct` > `0.1326` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1326
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `volumen_regimen` > `1.3339` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.3339
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **FILTRO** `volumen_spike_ratio` > `1.334` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.334
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `volumen_spike_ratio` < `2.5701` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.5701
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `ballena_activa_n` > `35.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 35.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **PATRÓN** `ibs_20min` > `0.8824` → IC=+0.286 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8824 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.3274` → IC=+0.288 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3274 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` < `0.8541` → IC=+0.200 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8541 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `1.1437` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1437 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` < `0.1127` → IC=+0.204 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1127 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2642` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2642 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4599` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4599 (IC base=-0.009)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.271 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0203` → IC=+0.315 (n=285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0203 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=552)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.8915` → IC=+0.309 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8915 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `1.381` → IC=+0.346 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.381 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.219` → IC=+0.280 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.219 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.8361` → IC=+0.267 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8361 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.259 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.4345` → IC=+0.250 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4345 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.238 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `2481.5612` → IC=+0.237 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2481.5612 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.280 (n=284)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.274)

- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.288 (n=215)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.2895` → IC=+0.280 (n=430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2895 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.280 (n=603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.275 (n=437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` < `0.2788` → IC=+0.330 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2788 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` < `0.2706` → IC=+0.286 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2706 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.963` → IC=+0.317 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.963 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` < `0.8883` → IC=+0.276 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8883 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` > `1.2535` → IC=+0.311 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2535 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.2435` → IC=+0.374 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2435 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `2.1847` → IC=+0.290 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1847 (IC base=+0.274)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.161 (n=978)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0049 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.197 (n=976)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0102 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0852` → IC=+0.168 (n=977)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0852 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=2961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.283 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `1.1448` → IC=+0.257 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1448 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.458` → IC=+0.245 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.458 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `0.6232` → IC=+0.172 (n=2022)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.6232 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.194 (n=563)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `2.3185` → IC=+0.163 (n=2347)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.3185 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8684` → IC=+0.156 (n=1778)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8684 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=2318)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3972.7896` → IC=+0.188 (n=975)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3972.7896 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.180 (n=1834)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 162.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.194 (n=1762)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.006 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.213 (n=881)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=1243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.183 (n=991)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 5.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.414` → IC=+0.237 (n=2641)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.414 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2215` → IC=+0.179 (n=2113)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2215 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.929` → IC=+0.208 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.929 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1669` → IC=+0.168 (n=2060)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1669 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.8484` → IC=+0.168 (n=1373)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.8484 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.238 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.9113` → IC=+0.174 (n=1349)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.9113 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.7073` → IC=+0.206 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7073 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.182 (n=1412)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 110.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.206 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.2631` → IC=+0.165 (n=475)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2631 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=426)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.306 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.486` → IC=+0.286 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.486 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2534` → IC=+0.230 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2534 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.4412` → IC=+0.154 (n=394)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4412 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.190 (n=346)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.274 (n=268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.246)

- **PATRÓN** `drift_60min` |x|≤ `0.3173` → IC=+0.270 (n=268)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3173 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.266 (n=276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` < `0.3143` → IC=+0.277 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3143 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.434` → IC=+0.267 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.434 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.0876` → IC=+0.227 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0876 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` > `0.3103` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3103 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` < `1.9498` → IC=+0.259 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9498 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `2.8655` → IC=+0.271 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8655 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.302 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1926.44` → IC=+0.315 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.44 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.228 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.246)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.241 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.4159` → IC=+0.191 (n=422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4159 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.207 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.4893` → IC=+0.219 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4893 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.2069` → IC=+0.234 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2069 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.678` → IC=+0.253 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.678 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.2821` → IC=+0.184 (n=422)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.2821 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `1.0648` → IC=+0.196 (n=192)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.0648 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.209 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.3655` → IC=+0.244 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3655 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `13192.0581` → IC=+0.207 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13192.0581 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=514)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2236` → IC=+0.178 (n=452)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2236 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.171 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.4297` → IC=+0.196 (n=514)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.4297 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1571` → IC=+0.179 (n=512)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1571 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.321` → IC=+0.235 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.321 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6864` → IC=+0.219 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6864 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.226 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.5679` → IC=+0.169 (n=406)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.5679 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.4083` → IC=+0.151 (n=405)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4083 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `15075.0467` → IC=+0.182 (n=171)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 15075.0467 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.247 (n=144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.1532` → IC=+0.175 (n=287)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1532 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.142` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.142 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` < `0.2288` → IC=+0.160 (n=374)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.2288 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `2.5706` → IC=+0.179 (n=247)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.5706 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `3.4171` → IC=+0.153 (n=168)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 3.4171 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.193 (n=399)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.259 (n=313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.2179` → IC=+0.287 (n=209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2179 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.274 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.3889` → IC=+0.284 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3889 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.143` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.143 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.278` → IC=+0.251 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.278 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3746` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3746 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `3.139` → IC=+0.266 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.139 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1878.3084` → IC=+0.266 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1878.3084 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.203 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.245)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.218 (n=371)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.4818` → IC=+0.184 (n=422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4818 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.191 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.4339` → IC=+0.224 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4339 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.8958` → IC=+0.235 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8958 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.198` → IC=+0.312 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.198 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.7015` → IC=+0.194 (n=377)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.7015 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.215 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.4363` → IC=+0.174 (n=136)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4363 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5992` → IC=+0.217 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5992 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=481)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `12317.4897` → IC=+0.234 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12317.4897 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.160 (n=239)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 142.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.236 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3741` → IC=+0.158 (n=495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3741 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.152 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.3721` → IC=+0.214 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3721 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.227` → IC=+0.189 (n=149)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 10.227 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.1652` → IC=+0.154 (n=495)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1652 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.604` → IC=+0.148 (n=495)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.604 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.162 (n=155)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.9175` → IC=+0.178 (n=259)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.9175 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.581` → IC=+0.149 (n=129)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 2.581 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `11127.6873` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 11127.6873 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.150 (n=135)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 112.0 (IC base=+0.141)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.188 (n=261)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0105 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5455` → IC=+0.188 (n=575)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5455 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.9146` → IC=+0.266 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9146 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.275 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.137 (n=574)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6201 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.134 (n=567)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.128 (n=181)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `1.7832` → IC=+0.130 (n=360)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.7832 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=454)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `3239.7916` → IC=+0.211 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3239.7916 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.136 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0051 (IC base=+0.127)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.208 (n=159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.185 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 14.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.413` → IC=+0.230 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.413 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.9641` → IC=+0.141 (n=62)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.9641 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.2402` → IC=+0.142 (n=453)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2402 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.296` → IC=+0.192 (n=183)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.296 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1545` → IC=+0.137 (n=475)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1545 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.8432` → IC=+0.161 (n=317)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.8432 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4538` → IC=+0.141 (n=115)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4538 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.285` → IC=+0.192 (n=115)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.285 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2174.6171` → IC=+0.174 (n=317)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2174.6171 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0244` → IC=+0.204 (n=275)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0244 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.1619` → IC=+0.205 (n=266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1619 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.8971` → IC=+0.265 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8971 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `1.5067` → IC=+0.243 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.5067 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.154` → IC=+0.238 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.154 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.8245` → IC=+0.204 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8245 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.269 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `2.5276` → IC=+0.197 (n=565)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.5276 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.181 (n=723)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.263 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.6622` → IC=+0.229 (n=578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6622 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.220 (n=287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.258 (n=271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.3832` → IC=+0.262 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3832 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.2494` → IC=+0.230 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2494 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.445` → IC=+0.267 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.445 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6915` → IC=+0.243 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6915 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.331 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.7624` → IC=+0.270 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7624 (IC base=+0.220)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.157 (n=386)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.006 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.158 (n=547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 8.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.6207` → IC=+0.178 (n=513)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6207 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8432` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8432 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.104` → IC=+0.192 (n=157)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.104 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8898` → IC=+0.136 (n=306)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8898 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `1.1727` → IC=+0.145 (n=153)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1727 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.194 (n=83)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `1.5926` → IC=+0.130 (n=465)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.5926 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=591)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `3038.9827` → IC=+0.139 (n=261)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3038.9827 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 13.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.3158` → IC=+0.127 (n=376)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.3158 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.154 (n=180)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 19.0 (IC base=+0.051)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=91)

- **FILTRO** `ibs_20min` < `0.5377` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5377
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=90)

- **FILTRO** `libro_liquidez` < `8533.3968` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `libro_liquidez` < 8533.3968
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=80)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.124 (n=91)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 9.0 (IC base=+0.045)

- **PATRÓN** `ibs_20min` > `0.9398` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9398 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.7932` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7932 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.003` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.003 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `12350.4009` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 12350.4009 (IC base=+0.045)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.176 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0027 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.6684` → IC=+0.153 (n=171)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.6684 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.164` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 7.164 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.0817` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0817 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `271.0` → IC=+0.145 (n=108)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 271.0 (IC base=+0.069)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.214 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=82)

- **FILTRO** `ibs_20min` > `0.6468` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6468
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=82)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.296 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.299)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.331 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.299)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.332 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.299)

- **PATRÓN** `ibs_20min` > `0.7004` → IC=+0.319 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7004 (IC base=+0.299)

- **PATRÓN** `dist_vwap_pct` > `0.1582` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1582 (IC base=+0.299)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.561` → IC=+0.381 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.561 (IC base=+0.299)

- **PATRÓN** `volumen_regimen` < `0.7015` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7015 (IC base=+0.299)

- **PATRÓN** `volumen_regimen` > `1.0786` → IC=+0.316 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0786 (IC base=+0.299)

- **PATRÓN** `volumen_pendiente_norm` > `0.1782` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1782 (IC base=+0.299)

- **PATRÓN** `volumen_spike_ratio` < `2.3129` → IC=+0.309 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3129 (IC base=+0.299)

- **PATRÓN** `volumen_spike_ratio` > `1.5284` → IC=+0.322 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5284 (IC base=+0.299)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.267 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.000)

- **PATRÓN** `drift_60min` |x|≤ `0.1265` → IC=+0.132 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.1265 (IC base=+0.000)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5714` → IC=-0.179 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5714
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=156)

- **FILTRO** `ibs_20min` > `0.4762` → IC=-0.250 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4762
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=82)

- **FILTRO** `dist_vwap_pct` > `0.1911` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1911
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.4994` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4994 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.935` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.935 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.041)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.211 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.2958` → IC=+0.150 (n=98)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.2958 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.433` → IC=+0.155 (n=111)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.433 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.718` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.718 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.6592` → IC=+0.183 (n=99)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6592 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` < `0.093` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.093 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.9259` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.9259 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.516` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.516 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=121)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.3128` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.3128 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.081)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.197 (n=1547)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0081 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.164 (n=3461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `1.0671` → IC=+0.239 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0671 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.535` → IC=+0.228 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.535 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6983` → IC=+0.158 (n=1057)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6983 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.0776` → IC=+0.151 (n=1088)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0776 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.177 (n=1180)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.3229` → IC=+0.156 (n=2720)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.3229 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.8757` → IC=+0.164 (n=2061)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8757 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=2712)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `3954.1559` → IC=+0.190 (n=1137)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3954.1559 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.206 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.210 (n=2085)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4726` → IC=+0.195 (n=3127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4726 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.203 (n=1121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5597` → IC=+0.240 (n=3127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5597 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.4293` → IC=+0.178 (n=2284)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.4293 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.474` → IC=+0.199 (n=453)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.474 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.539` → IC=+0.192 (n=3063)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 3.539 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6189` → IC=+0.180 (n=764)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6189 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `1.1954` → IC=+0.172 (n=763)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.1954 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2395` → IC=+0.253 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2395 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.3404` → IC=+0.199 (n=1099)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.3404 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.173 (n=886)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 37.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.163 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0053 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.218 (n=253)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.161 (n=562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 6.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.526` → IC=+0.309 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.526 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2129` → IC=+0.247 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2129 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8937` → IC=+0.166 (n=315)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8937 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.268 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.261)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.267 (n=376)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.261)

- **PATRÓN** `drift_60min` |x|≤ `0.1034` → IC=+0.292 (n=166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1034 (IC base=+0.261)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.266 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.261)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.270 (n=381)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` < `0.425` → IC=+0.308 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.425 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.14` → IC=+0.281 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.14 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.1758` → IC=+0.314 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1758 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` > `2.4166` → IC=+0.303 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4166 (IC base=+0.261)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.261)

- **PATRÓN** `libro_liquidez` > `1938.8398` → IC=+0.289 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1938.8398 (IC base=+0.261)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.243 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.261)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.195 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0028 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0032` → IC=+0.165 (n=490)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0032 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.3282` → IC=+0.214 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3282 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.252` → IC=+0.227 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.252 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.696` → IC=+0.205 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.696 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.417` → IC=+0.160 (n=469)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 4.417 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.170 (n=547)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2653 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.172 (n=248)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.0851 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.0734` → IC=+0.179 (n=447)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.0734 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2083` → IC=+0.176 (n=106)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2083 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.4168` → IC=+0.193 (n=499)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.4168 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.3798` → IC=+0.174 (n=498)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.3798 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `12688.6765` → IC=+0.189 (n=365)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 12688.6765 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.170 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.166 (n=342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0036 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.2658` → IC=+0.178 (n=451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2658 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.171 (n=478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 7.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.182 (n=532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.3939` → IC=+0.215 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3939 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` < `0.1412` → IC=+0.181 (n=459)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1412 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.842` → IC=+0.214 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.842 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6183` → IC=+0.246 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6183 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2159` → IC=+0.277 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2159 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.7531` → IC=+0.200 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7531 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `13571.5921` → IC=+0.177 (n=233)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 13571.5921 (IC base=+0.166)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.263 (n=209)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.245 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.7044` → IC=+0.264 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7044 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.287` → IC=+0.339 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.287 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.1416` → IC=+0.194 (n=361)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1416 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `1.9531` → IC=+0.192 (n=170)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.9531 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `4.1999` → IC=+0.195 (n=129)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 4.1999 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `1802.6286` → IC=+0.197 (n=305)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1802.6286 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.243 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.296 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.1268` → IC=+0.241 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1268 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.279 (n=179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.5364` → IC=+0.297 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5364 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.234` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.234 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3681` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3681 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.230 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.408` → IC=+0.215 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.408 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.266 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.197 (n=229)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 54.0 (IC base=+0.236)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.152 (n=547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0086 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.145 (n=488)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0039 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2375` → IC=+0.141 (n=366)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.2375 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.165 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.3335` → IC=+0.195 (n=546)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3335 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.798` → IC=+0.217 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.798 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.431` → IC=+0.191 (n=260)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 4.431 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.9021` → IC=+0.168 (n=365)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.9021 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `1.2022` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.2022 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1034` → IC=+0.233 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1034 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4113` → IC=+0.185 (n=510)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4113 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4668.2669` → IC=+0.221 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4668.2669 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.158 (n=279)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 152.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.172 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0073 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4721` → IC=+0.161 (n=473)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4721 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.180 (n=220)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.1065` → IC=+0.238 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1065 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.2215` → IC=+0.158 (n=200)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.2215 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.52` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.52 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.5844` → IC=+0.156 (n=158)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.5844 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.15` → IC=+0.175 (n=158)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.15 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5826` → IC=+0.163 (n=182)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5826 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5255` → IC=+0.179 (n=138)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.5255 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `11746.7684` → IC=+0.200 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11746.7684 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `192.0` → IC=+0.171 (n=347)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 192.0 (IC base=+0.146)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.149 (n=403)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0078 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.138 (n=415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 12.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4805` → IC=+0.180 (n=604)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4805 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.8895` → IC=+0.221 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8895 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.554` → IC=+0.224 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.554 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `3011.4132` → IC=+0.255 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3011.4132 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.153 (n=381)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 66.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.161 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0056 (IC base=+0.106)

- **PATRÓN** `drift_60min` |x|≤ `0.1236` → IC=+0.145 (n=187)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1236 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.146 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 15.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.189 (n=561)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.5076` → IC=+0.132 (n=525)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.5076 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.124` → IC=+0.131 (n=546)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.124 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `0.7076` → IC=+0.141 (n=246)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.7076 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.2064` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2064 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `2.4926` → IC=+0.127 (n=411)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.4926 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2729.7668` → IC=+0.152 (n=254)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2729.7668 (IC base=+0.106)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0273` → IC=+0.226 (n=235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0273 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.197 (n=705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `0.949` → IC=+0.291 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.949 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `1.4081` → IC=+0.287 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.4081 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.12` → IC=+0.249 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.12 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` > `0.8376` → IC=+0.209 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8376 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2373` → IC=+0.259 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2373 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `2.6647` → IC=+0.186 (n=655)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.6647 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.4456` → IC=+0.189 (n=654)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4456 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.194 (n=838)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `3031.8812` → IC=+0.192 (n=235)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3031.8812 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.298 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0244` → IC=+0.221 (n=249)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0244 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.4823` → IC=+0.227 (n=657)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4823 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.218 (n=697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.223 (n=791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.493` → IC=+0.277 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.493 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.4569` → IC=+0.227 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4569 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.652` → IC=+0.284 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.652 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.081` → IC=+0.217 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.081 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.245 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.320 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `1.465` → IC=+0.203 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.465 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.183 (n=458)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 36.0 (IC base=+0.217)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=1330)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.140 (n=651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0078 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.4477` → IC=+0.133 (n=857)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.4477 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.2678` → IC=+0.137 (n=974)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.2678 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.559` → IC=+0.125 (n=895)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.559 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2496` → IC=+0.154 (n=180)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2496 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4563` → IC=+0.169 (n=321)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4563 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.692` → IC=+0.146 (n=320)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.692 (IC base=+0.116)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.199 (n=337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3644` → IC=+0.165 (n=888)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3644 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.190 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 4.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.164 (n=444)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.2 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1828` → IC=+0.153 (n=381)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1828 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.095` → IC=+0.155 (n=1011)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.095 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2164` → IC=+0.154 (n=982)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2164 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.1463` → IC=+0.146 (n=1005)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.1463 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0692` → IC=+0.142 (n=490)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.0692 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.5268` → IC=+0.156 (n=1001)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5268 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4255` → IC=+0.147 (n=1001)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4255 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=1330)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `10602.7113` → IC=+0.146 (n=673)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 10602.7113 (IC base=+0.141)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `3.674` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.674
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=159)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.134 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.674` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 3.674 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `0.9341` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.9341 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `1.5188` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.5188 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `12550.0528` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 12550.0528 (IC base=+0.080)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.195 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0035 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.170 (n=183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.181 (n=202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1706` → IC=+0.180 (n=242)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1706 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6648` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.6648 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.164 (n=548)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1906` → IC=+0.157 (n=549)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1906 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.168 (n=260)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.5675` → IC=+0.152 (n=547)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.5675 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.8071` → IC=+0.145 (n=364)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8071 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `12033.4703` → IC=+0.140 (n=490)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 12033.4703 (IC base=+0.137)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.211 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.185 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0104 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.5715` → IC=+0.165 (n=240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.5715 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.196 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.244 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9524 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.656` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.656 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.111` → IC=+0.168 (n=215)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 3.111 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` < `0.096` → IC=+0.165 (n=219)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.096 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2193` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2193 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.6449` → IC=+0.195 (n=80)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.6449 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `3.0387` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 3.0387 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `1793.9526` → IC=+0.176 (n=214)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1793.9526 (IC base=+0.157)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.152 (n=326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0092 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.5172` → IC=+0.142 (n=325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.5172 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.2849` → IC=+0.142 (n=291)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.2849 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.8008` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.8008 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.2134` → IC=+0.133 (n=273)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2134 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.953` → IC=+0.138 (n=324)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.953 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.7231` → IC=+0.155 (n=143)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.7231 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.1811` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1811 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4422` → IC=+0.176 (n=106)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4422 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.8714` → IC=+0.129 (n=211)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.8714 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8938.0512` → IC=+0.148 (n=291)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 8938.0512 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.233 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.4997` → IC=+0.187 (n=295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.4997 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.165 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 10.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.1212` → IC=+0.167 (n=295)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.1212 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1394` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1394 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.3536` → IC=+0.146 (n=309)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3536 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.138` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.138 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.476` → IC=+0.141 (n=302)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.476 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.1919` → IC=+0.167 (n=295)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1919 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.1393` → IC=+0.161 (n=299)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.1393 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.1791` → IC=+0.174 (n=256)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.1791 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4522` → IC=+0.166 (n=291)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4522 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `8807.8238` → IC=+0.147 (n=264)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8807.8238 (IC base=+0.141)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=64)

- **FILTRO** `libro_liquidez` < `2949.8034` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 2949.8034
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=63)

- **FILTRO** `sigma_h` < `0.011` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `sigma_ewma_delta_pct` < `3.941` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.941
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6842` → IC=-0.196 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6842
  - _Potencial_: sin este filtro IC_bueno=+0.248 (n=165)

- **FILTRO** `sigma_h` > `0.011` → IC=-0.286 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=164)

- **FILTRO** `dist_vwap_pct` > `0.1153` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1153
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=59)

- **FILTRO** `volumen_regimen` > `1.2318` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.2318
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=88)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.205 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.248 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1234` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1234 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.6` → IC=+0.252 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.6 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.64` → IC=+0.153 (n=73)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.64 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `1.1984` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1984 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` < `0.0665` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0665 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2582` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2582 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `1.4494` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4494 (IC base=+0.089)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=150)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `1591.3597` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1591.3597 (IC base=+0.089)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.230 (n=61)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.348 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.7342` → IC=+0.230 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7342 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.354` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 15.354 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.9418` → IC=+0.128 (n=41)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.9418 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.0651` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0651 (IC base=+0.097)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=45)

- **FILTRO** `ibs_20min` > `0.2768` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2768
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=13)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.153 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.6789` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6789 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.457` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.457 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1234` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1234 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.891` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.891 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6023` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6023 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0919 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `2204.6678` → IC=+0.245 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2204.6678 (IC base=+0.133)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.125 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=44)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.000)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1243` → IC=-0.382 (n=32)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1243
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=63)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.462 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=73)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.380 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=76)

- **FILTRO** `ibs_20min` < `0.3707` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3707
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=75)

- **FILTRO** `dist_vwap_pct` > `0.3683` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3683
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=80)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.6047` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6047
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `sigma_h` < `0.0031` → IC=-0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0031
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.326 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `dist_vwap_pct` > `0.0802` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0802
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `volumen_regimen` > `0.6161` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.6161
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0064` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `ibs_20min` < `0.5833` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `dist_vwap_pct` < `0.3782` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3782
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.5882` → IC=-0.260 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5882
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=145)

- **FILTRO** `ibs_20min` > `0.4538` → IC=-0.211 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4538
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=133)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.133 (n=145)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.5882 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.4538` → IC=+0.130 (n=133)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.4538 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.945` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.945 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `3300.924` → IC=+0.122 (n=88)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 3300.924 (IC base=+0.045)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `sigma_h` < `0.0017` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0017
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=51)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=50)

- **FILTRO** `ibs_20min` < `0.5084` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5084
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=45)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.167 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0035 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.2185` → IC=+0.138 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.2185 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.2693` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.2693 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.84` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.84 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.1471` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1471 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `2.4144` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.4144 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `3958.8019` → IC=+0.129 (n=60)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3958.8019 (IC base=+0.115)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=30)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.077)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.139 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.077)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.250 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.077)

- **PATRÓN** `ibs_20min` > `0.7289` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7289 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.413` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 7.413 (IC base=+0.077)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.7231` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.7231 (IC base=+0.056)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_regimen` < `0.8893` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8893
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.095)

- **PATRÓN** `drift_60min` |x|≤ `0.1849` → IC=+0.159 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1849 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.03 (IC base=+0.095)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2502.1452` → IC=+0.164 (n=114)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2502.1452 (IC base=+0.097)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2497.7868` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2497.7868 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2502.1452` → IC=+0.164 (n=114)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2502.1452 (IC base=+0.097)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2497.7868` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2497.7868 (IC base=+0.103)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=101)

- **FILTRO** `libro_liquidez` < `2114.4748` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 2114.4748
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=124)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

- **FILTRO** `libro_liquidez` < `15120.4031` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 15120.4031
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_15M#SOL#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.132 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.011)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=659)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9444` → IC=-0.289 (n=36)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9444
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.5 (IC base=+0.065)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_n` < `2.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=70)

- **FILTRO** `liq_usd_total` < `26874.22` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `liq_usd_total` < 26874.22
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=63)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `libro_liquidez` < `15381.0964` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 15381.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `ballena_activa_n` > `630.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 630.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.495 (IC base=-0.005)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.8749` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.8749
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=49)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=196)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **PATRÓN** `liq_usd_total` > `14137.9` → IC=+0.191 (n=53)

  - _Acción_: Kelly boost +0.95€ cuando `liq_usd_total` > 14137.9 (IC base=+0.061)

### LIQUIDACIONES_5M#SOL#5min
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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=30)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=30)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` > `0.56` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=111)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=59)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=31)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=81)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=31)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.6408` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.6408
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=551)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1771` → IC=-0.132 (n=112)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1771
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=220)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.176 (n=1025)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=3147)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.215 (n=1015)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=3307)

- **FILTRO** `ibs_20min` > `0.2734` → IC=-0.174 (n=1080)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2734
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=3242)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.260 (n=144)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=458)

- **FILTRO** `ibs_20min` < `0.7279` → IC=-0.197 (n=150)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7279
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=452)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.161 (n=187)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=568)

- **FILTRO** `ibs_20min` > `0.1818` → IC=-0.128 (n=377)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1818
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=378)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.218 (n=168)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=533)

- **FILTRO** `ballena_activa_n` > `72.0` → IC=-0.147 (n=171)

  - _Acción_: SKIP cuando `ballena_activa_n` > 72.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=530)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=452)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.206 (n=209)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=433)

- **FILTRO** `ibs_20min` < `0.7244` → IC=-0.177 (n=159)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7244
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=483)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.233 (n=174)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=551)

- **FILTRO** `ibs_20min` > `0.7315` → IC=-0.216 (n=181)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7315
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=544)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.145 (n=184)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=553)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.186 (n=183)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=561)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.156 (n=184)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=560)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.218 (n=168)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=526)

- **FILTRO** `ibs_20min` > `0.2778` → IC=-0.178 (n=172)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2778
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=522)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.169 (n=170)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=524)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.202 (n=166)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=522)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=673)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.256 (n=166)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=537)

- **FILTRO** `ibs_20min` > `0.2733` → IC=-0.189 (n=175)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2733
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=528)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.306 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=375)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=381)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `libro_liquidez` < `2063.3848` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 2063.3848
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `ibs_20min` < `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `drift_20min_pct` |x|> `0.0299` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.0299
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `ibs_20min` < `0.0752` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0752
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=16)

- **FILTRO** `libro_liquidez` < `15251.0076` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 15251.0076
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `drift_20min_pct` |x|> `0.1906` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1906
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `ibs_20min` > `0.8837` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8837
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

- **FILTRO** `drift_7min_pct` |x|> `0.0331` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0331
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=630)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.144 (n=3046)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=7508)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.278 (n=2628)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=7926)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.231 (n=2637)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7917)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.173 (n=3567)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=6987)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.229 (n=3005)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=9999)

- **FILTRO** `ibs_7min` > `0.7273` → IC=-0.168 (n=3242)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=9762)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.3` → IC=-0.322 (n=346)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=1111)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=1017)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=440)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.243 (n=348)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=1109)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.231 (n=544)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=1719)

- **FILTRO** `drift_7min_pct` |x|> `0.122` → IC=-0.144 (n=768)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.122
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1495)

- **FILTRO** `ibs_7min` > `0.298` → IC=-0.168 (n=769)

  - _Acción_: SKIP cuando `ibs_7min` > 0.298
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1494)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.148 (n=441)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=1586)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.248 (n=502)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1525)

- **FILTRO** `ibs_7min` < `0.7899` → IC=-0.192 (n=504)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7899
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1523)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.189 (n=502)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1525)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.225 (n=489)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=1532)

- **FILTRO** `ballena_activa_n` > `98.0` → IC=-0.175 (n=687)

  - _Acción_: SKIP cuando `ballena_activa_n` > 98.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1334)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.200 (n=374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=1178)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.308 (n=488)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=1064)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.282 (n=384)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1168)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.240 (n=382)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=1170)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.244 (n=502)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1775)

- **FILTRO** `ibs_7min` > `0.8105` → IC=-0.176 (n=569)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8105
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1708)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.157 (n=403)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=1378)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.259 (n=430)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=1351)

- **FILTRO** `ibs_7min` < `0.7608` → IC=-0.182 (n=445)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7608
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=1336)

- **FILTRO** `ballena_activa_n` > `39.0` → IC=-0.192 (n=440)

  - _Acción_: SKIP cuando `ballena_activa_n` > 39.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=1341)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=438)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1348)

- **FILTRO** `ibs_7min` > `0.1905` → IC=-0.173 (n=607)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1905
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1179)

- **FILTRO** `ballena_activa_n` > `35.0` → IC=-0.189 (n=438)

  - _Acción_: SKIP cuando `ballena_activa_n` > 35.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=1348)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.236 (n=494)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1531)

- **FILTRO** `ibs_7min` < `0.7619` → IC=-0.204 (n=501)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1524)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.186 (n=491)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1534)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.180 (n=598)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1808)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.128 (n=557)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=1155)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.298 (n=419)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1293)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.228 (n=425)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1287)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.225 (n=423)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1289)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.268 (n=464)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=1787)

- **FILTRO** `ibs_7min` > `0.8` → IC=-0.162 (n=560)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1691)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.132 (n=739)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1512)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=149)

- **FILTRO** `drift_7min_pct` |x|> `0.106` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.106
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

- **FILTRO** `ibs_7min` > `0.0606` → IC=-0.133 (n=58)

  - _Acción_: SKIP cuando `ibs_7min` > 0.0606
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=117)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=412)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=248)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=435)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3984` → IC=+0.139 (n=388)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3984 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.136 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `447.889` → IC=+0.177 (n=122)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 447.889 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `3738.4224` → IC=+0.164 (n=105)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3738.4224 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.130 (n=187)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 47.0 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.224 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.102)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3984` → IC=+0.145 (n=60)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.3984 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 4.0 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2025.6726` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2025.6726 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 31.0 (IC base=+0.105)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.413` → IC=+0.225 (n=38)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.413 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.159 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 10.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `471.727` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 471.727 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `8937.6986` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8937.6986 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 157.0 (IC base=+0.128)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3997` → IC=+0.209 (n=53)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.3997 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.153)

- **PATRÓN** `total_vol_5m` < `11104.393` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 11104.393 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2945.8122` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2945.8122 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 77.0 (IC base=+0.153)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.156 (n=59)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.089)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.129 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 18.0 (IC base=+0.089)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `3338.8044` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3338.8044 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 44.0 (IC base=+0.089)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=71)

- **FILTRO** `T_h` > `63.9853` → IC=-0.346 (n=102)

  - _Acción_: SKIP cuando `T_h` > 63.9853
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=36)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `63.9853` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `T_h` > 63.9853
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.292 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=-0.136)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.008` → IC=-0.132 (n=93)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=34)

- **FILTRO** `T_h` > `143.1632` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=97)

- **FILTRO** `pct_vs_K` |x|> `4.0608` → IC=-0.471 (n=32)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.0608
  - _Potencial_: sin este filtro IC_bueno=-0.291 (n=65)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3968` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3968 (IC base=-0.074)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **PATRÓN** `T_h` < `111.9773` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `T_h` < 111.9773 (IC base=+0.047)

- **PATRÓN** `pct_vs_K` |x|≤ `2.84` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `pct_vs_K` |x|≤ 2.84 (IC base=+0.047)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `87.9947` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `T_h` > 87.9947
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `4.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=46)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=100)

- **PATRÓN** `streak_estiramiento` < `0.4411` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4411 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 44.0 (IC base=+0.052)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 32.0 (IC base=+0.069)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=58)

- **FILTRO** `streak_estiramiento` > `0.4326` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4326
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=16)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` < `2.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=103)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=97)

- **FILTRO** `streak_estiramiento` > `0.6079` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6079
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=61)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=107)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=108)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=188)

- **PATRÓN** `streak_estiramiento` < `0.3153` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.3153 (IC base=+0.011)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=372)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=191)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=262)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1319)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=750)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=758)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.150 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1873` → IC=+0.128 (n=404)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1873 (IC base=+0.120)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.128 (n=404)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.125 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 4.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.160 (n=183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 6.0 (IC base=+0.120)

- **PATRÓN** `ibs_15` > `0.5319` → IC=+0.212 (n=404)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5319 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.398` → IC=+0.182 (n=108)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.398 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.094` → IC=+0.239 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.094 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=422)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `8015.433` → IC=+0.179 (n=135)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 8015.433 (IC base=+0.120)

### UPDOWN_GBM#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.0796` → IC=-0.129 (n=141)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0796
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=426)

- **FILTRO** `ibs_15` < `0.2727` → IC=-0.171 (n=141)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=426)

- **FILTRO** `sigma_ewma_delta_pct` > `6.683` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.683
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=515)

### UPDOWN_GBM#60min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0347` → IC=-0.192 (n=24)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0347
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=49)

- **FILTRO** `ibs_15` < `0.2105` → IC=-0.214 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2105
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=40)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0041` → IC=-0.260 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=69)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.239 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=71)

- **FILTRO** `ibs_15` > `0.7088` → IC=-0.167 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.7088
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=70)

- **FILTRO** `ibs_15` < `0.2983` → IC=-0.180 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2983
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=69)

- **FILTRO** `libro_liquidez` < `13630.9549` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 13630.9549
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=69)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.173 (n=105)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0036 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.191 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0046 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.193` → IC=+0.189 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.193 (IC base=+0.165)

- **PATRÓN** `drift_15min` |x|≤ `0.4558` → IC=+0.195 (n=80)

  - _Acción_: Kelly boost +0.98€ cuando `drift_15min` |x|≤ 0.4558 (IC base=+0.165)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2389` → IC=+0.191 (n=40)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio_macro` |x|> 0.2389 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.191 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 4.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.169 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_15` > `0.9483` → IC=+0.289 (n=55)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9483 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.3217` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3217 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` < `0.1189` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1189 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.165)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=49)

- **FILTRO** `ibs_15` < `0.1461` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1461
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **FILTRO** `libro_liquidez` < `13135.9064` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 13135.9064
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **FILTRO** `hora_utc` > `19.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=88)

- **FILTRO** `ibs_15` < `0.675` → IC=-0.214 (n=26)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.675
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=79)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.622` → IC=-0.244 (n=37)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.622
  - _Potencial_: sin este filtro IC_bueno=+0.225 (n=78)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.210 (n=29)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.073)

- **PATRÓN** `ibs_15` > `0.622` → IC=+0.225 (n=78)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.622 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.0774` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.0774 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.073)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=81)

- **FILTRO** `dist_vwap_pct` > `0.1505` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1505
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=83)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `drift_15min` |x|> `0.5033` → IC=-0.150 (n=138)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5033
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=415)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6111` → IC=-0.167 (n=31)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6111
  - _Potencial_: sin este filtro IC_bueno=+0.294 (n=32)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.294 (n=32)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.477` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.477 (IC base=+0.069)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0088` → IC=-0.204 (n=42)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=44)

- **FILTRO** `ibs_15` < `0.225` → IC=-0.370 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.225
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=65)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0131` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0131
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=47)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` < `0.3754` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.3754 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0597` → IC=+0.139 (n=106)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.0597 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.160 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 6.0 (IC base=+0.101)

- **PATRÓN** `ibs_15` > `0.5556` → IC=+0.180 (n=95)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` > 0.5556 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.3587` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3587 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.773` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.773 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=106)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2489.2422` → IC=+0.149 (n=95)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2489.2422 (IC base=+0.101)

- **PATRÓN** `ibs_15` < `0.1282` → IC=+0.201 (n=115)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1282 (IC base=+0.041)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.383 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.315)

- **PATRÓN** `drift_60min` |x|≤ `0.1155` → IC=+0.339 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1155 (IC base=+0.315)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.317 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.347 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `ibs_15` > `0.9115` → IC=+0.380 (n=115)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9115 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.2982` → IC=+0.357 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2982 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.649` → IC=+0.319 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.649 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.293` → IC=+0.316 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 18.293 (IC base=+0.315)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.319 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `11026.1015` → IC=+0.350 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11026.1015 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `528.0` → IC=+0.363 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 528.0 (IC base=+0.315)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.313 (n=89)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.300)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.306 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.300)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.333 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.300)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.333 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.300)

- **PATRÓN** `drift_15min` |x|≤ `0.4083` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4083 (IC base=+0.300)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1021` → IC=+0.304 (n=90)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1021 (IC base=+0.300)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.300)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.335 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.300)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.348 (n=90)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.300)

- **PATRÓN** `dist_vwap_pct` > `0.4531` → IC=+0.397 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4531 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.991` → IC=+0.311 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.991 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `11026.1015` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11026.1015 (IC base=+0.300)

- **PATRÓN** `ballena_activa_n` < `581.0` → IC=+0.415 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 581.0 (IC base=+0.300)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.327 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.328)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.357 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.328)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.363 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.328)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.363 (n=49)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.328)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2065` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2065 (IC base=+0.328)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.329 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.328)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.329 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.328)

- **PATRÓN** `ibs_15` > `0.8893` → IC=+0.402 (n=49)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8893 (IC base=+0.328)

- **PATRÓN** `dist_vwap_pct` < `0.4534` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4534 (IC base=+0.328)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `3288.4647` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3288.4647 (IC base=+0.328)

- **PATRÓN** `ballena_activa_n` < `174.0` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 174.0 (IC base=+0.328)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0101` → IC=-0.191 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=832)

- **FILTRO** `ibs_15` < `0.7` → IC=-0.146 (n=207)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=209)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=291)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=817)

- **FILTRO** `sigma_ewma_delta_pct` > `17.696` → IC=-0.175 (n=380)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.696
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=2932)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.357` → IC=+0.145 (n=150)

  - _Acción_: Kelly boost +0.72€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.357 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.7` → IC=+0.258 (n=209)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1405` → IC=+0.241 (n=160)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1405 (IC base=-0.078)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3008` → IC=+0.267 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3008 (IC base=-0.078)

- **PATRÓN** `ibs_15` < `0.3676` → IC=+0.315 (n=241)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3676 (IC base=-0.078)

- **PATRÓN** `dist_vwap_pct` < `0.1453` → IC=+0.250 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1453 (IC base=-0.078)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.246 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=-0.078)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.247 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=532)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.215 (n=233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=475)

- **FILTRO** `drift_15min` |x|> `0.7597` → IC=-0.219 (n=176)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7597
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=532)

- **FILTRO** `hora_utc` > `17.0` → IC=-0.258 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=557)

- **FILTRO** `sigma_ewma_delta_pct` > `19.398` → IC=-0.267 (n=131)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.398
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=577)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1422` → IC=+0.140 (n=23)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.1422 (IC base=+0.016)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.300 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.016)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4704` → IC=-0.354 (n=46)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4704
  - _Potencial_: sin este filtro IC_bueno=+0.185 (n=141)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=170)

- **PATRÓN** `drift_60min` |x|≤ `0.0608` → IC=+0.194 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0608 (IC base=+0.050)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3719` → IC=+0.209 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3719 (IC base=+0.050)

- **PATRÓN** `ibs_15` > `0.4704` → IC=+0.185 (n=141)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.4704 (IC base=+0.050)

- **PATRÓN** `libro_liquidez` > `10452.9608` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 10452.9608 (IC base=+0.050)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1041` → IC=+0.239 (n=86)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1041 (IC base=+0.238)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.254 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.247 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.238)

- **PATRÓN** `drift_15min` |x|≤ `0.4275` → IC=+0.256 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4275 (IC base=+0.238)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1569` → IC=+0.247 (n=85)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1569 (IC base=+0.238)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2601` → IC=+0.250 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2601 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.250 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.337 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.238)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.331 (n=128)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` < `0.2166` → IC=+0.243 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2166 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.416` → IC=+0.266 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.416 (IC base=+0.238)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0108` → IC=-0.235 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0108
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=202)

- **FILTRO** `drift_60min` |x|> `0.1589` → IC=-0.167 (n=91)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1589
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=177)

- **FILTRO** `drift_15min` |x|> `0.7897` → IC=-0.235 (n=66)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7897
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=202)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.111)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1944` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1944 (IC base=-0.060)

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.167 (n=52)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.38 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` < `0.3035` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.3035 (IC base=-0.060)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_15min` |x|> `1.1396` → IC=-0.257 (n=72)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.1396
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=220)

- **FILTRO** `sigma_ewma_delta_pct` > `14.966` → IC=-0.225 (n=38)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.966
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=254)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.293 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=265)

- **FILTRO** `libro_liquidez` < `2530.6025` → IC=-0.214 (n=96)

  - _Acción_: SKIP cuando `libro_liquidez` < 2530.6025
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=196)

- **FILTRO** `sigma_ewma_delta_pct` > `16.69` → IC=-0.152 (n=113)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.69
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=947)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1618` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1618 (IC base=-0.072)

- **PATRÓN** `ibs_15` < `0.05` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.05 (IC base=-0.072)

- **PATRÓN** `ibs_15` > `0.119` → IC=+0.357 (n=33)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.119 (IC base=-0.072)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.284 (n=183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.287 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.330 (n=92)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0567` → IC=+0.293 (n=274)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0567 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.313 (n=255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.9673` → IC=+0.358 (n=125)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9673 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.3217` → IC=+0.352 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3217 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.294 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.285 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13449.5003` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13449.5003 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.285 (n=105)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.300 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.307 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.277)

- **PATRÓN** `drift_15min` |x|≤ `0.7222` → IC=+0.280 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7222 (IC base=+0.277)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2427` → IC=+0.318 (n=53)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2427 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.311 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.8332` → IC=+0.299 (n=157)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8332 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.3523` → IC=+0.364 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3523 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.592` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.592 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.533` → IC=+0.296 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.533 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `13595.2872` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13595.2872 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.292 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.286 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0608` → IC=+0.333 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0608 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0682` → IC=+0.304 (n=105)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0682 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.315 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.307 (n=117)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.0921` → IC=+0.319 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0921 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.851` → IC=+0.291 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.851 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.299 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `10076.1613` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10076.1613 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.285)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0887` → IC=-0.280 (n=57)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0887
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=112)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.250 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=127)

- **FILTRO** `drift_60min` |x|> `0.2669` → IC=-0.159 (n=42)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2669
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=127)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1211` → IC=-0.163 (n=99)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1211
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=300)

- **FILTRO** `drift_15min` |x|> `0.4352` → IC=-0.120 (n=135)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4352
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=264)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.154 (n=53)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2228` → IC=-0.220 (n=23)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2228
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `79.3918` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 79.3918 (IC base=+0.096)

- **PATRÓN** `ratio` < `0.9709` → IC=+0.463 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9709 (IC base=+0.096)

- **PATRÓN** `T_h` < `103.3918` → IC=+0.346 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 103.3918 (IC base=+0.344)

- **PATRÓN** `T_h` > `146.0788` → IC=+0.430 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.344)

- **PATRÓN** `ratio` < `1.0189` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0189 (IC base=+0.344)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.344)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `63.9918` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9918 (IC base=+0.083)

- **PATRÓN** `T_h` < `87.9882` → IC=+0.353 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9882 (IC base=+0.272)

- **PATRÓN** `pct_dist` |x|≤ `0.6381` → IC=+0.286 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6381 (IC base=+0.272)

- **PATRÓN** `ratio` < `1.0189` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0189 (IC base=+0.272)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `57.6124` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 57.6124 (IC base=+0.139)

- **PATRÓN** `T_h` < `111.9836` → IC=+0.330 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9836 (IC base=+0.311)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.316 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.311)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `113.2461` → IC=+0.431 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 113.2461 (IC base=+0.412)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0059 (IC=+0.222 n=16). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5319 sube el IC de +0.120 a +0.212 en UPDOWN_GBM#15min (n=404). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9483 sube el IC de +0.165 a +0.289 en UPDOWN_GBM#BTC#15min (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.622 sube el IC de +0.073 a +0.225 en UPDOWN_GBM#ETH#15min (n=78). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.069 a +0.294 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5556 sube el IC de +0.101 a +0.180 en UPDOWN_GBM#XRP#15min (n=95). Ya aplicado como kelly_boost=+0.90€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1282 sube el IC de +0.041 a +0.201 en UPDOWN_GBM#XRP#15min (n=115). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.7 sube el IC de -0.067 a +0.258 en UPDOWN_GBM_15M_TARDIO (n=209). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3676 sube el IC de -0.078 a +0.315 en UPDOWN_GBM_15M_TARDIO (n=241). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.016 a +0.300 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4704 sube el IC de +0.050 a +0.185 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=141). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.238 a +0.331 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=128). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.111 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.060 a +0.167 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=52). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.05 sube el IC de -0.072 a +0.342 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS > 0.119 sube el IC de -0.072 a +0.357 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=33). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9673 sube el IC de +0.282 a +0.358 en UPDOWN_GBM_IBS_ALTO (n=125). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8332 sube el IC de +0.277 a +0.299 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=157). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.285 a +0.307 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=117). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.9115 sube el IC de +0.315 a +0.380 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=115). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.300 a +0.348 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=90). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8893 sube el IC de +0.328 a +0.402 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=49). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.357 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.357 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min` — IC=+0.149 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 668 | +0.091 | +38.80€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 668 | +0.091 | +38.80€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 416 | +0.115 | +29.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 416 | +0.115 | +29.18€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 11696 | -0.102 | -1950.89€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 820 | -0.032 | -130.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 10876 | -0.107 | -1820.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1511 | -0.055 | -296.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1511 | -0.055 | -296.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 820 | -0.032 | -130.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 820 | -0.032 | -130.34€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1514 | -0.141 | -447.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1514 | -0.141 | -447.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 3124 | -0.070 | -315.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 3124 | -0.070 | -315.20€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2703 | -0.109 | -271.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2703 | -0.109 | -271.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2024 | -0.173 | -489.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2024 | -0.173 | -489.62€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 1467 | -0.060 | +736.33€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 414 | -0.002 | +276.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 1053 | -0.082 | +460.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 1467 | -0.060 | +736.33€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 414 | -0.002 | +276.27€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 1053 | -0.082 | +460.06€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 35 | -0.122 | -10.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 35 | -0.122 | -10.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 35 | -0.122 | -10.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 35 | -0.122 | -10.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 37807 | +0.115 | -2346.75€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 6723 | +0.186 | -245.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 117 | -0.088 | -49.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 27585 | +0.098 | -2006.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3382 | +0.119 | -44.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 4626 | +0.071 | -710.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 22 | -0.083 | +0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 4599 | +0.073 | -705.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 7711 | +0.134 | -161.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1915 | +0.198 | -92.38€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 4590 | +0.110 | -101.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1164 | +0.128 | +54.56€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 4638 | +0.084 | -540.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 24 | +0.077 | +2.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 4613 | +0.084 | -540.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 8275 | +0.127 | -131.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2451 | +0.168 | -18.25€ | 1 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 4593 | +0.112 | -78.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1219 | +0.100 | -25.52€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 7934 | +0.131 | -506.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2294 | +0.199 | -137.94€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 55 | +0.009 | -9.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 4586 | +0.098 | -285.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 999 | +0.132 | -73.85€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 4623 | +0.108 | -296.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 17 | -0.022 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 4604 | +0.109 | -295.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 6660 | +0.175 | -516.58€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 6660 | +0.175 | -516.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1684 | +0.164 | -187.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1684 | +0.164 | -187.17€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 132 | -0.112 | +2.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 132 | -0.112 | +2.21€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1655 | +0.168 | -177.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1655 | +0.168 | -177.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1492 | +0.231 | -46.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1492 | +0.231 | -46.16€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1618 | +0.185 | -122.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1618 | +0.185 | -122.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 345 | +0.445 | +3.18€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 345 | +0.445 | +3.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 133 | +0.441 | +1.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 133 | +0.441 | +1.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 126 | +0.438 | +0.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 126 | +0.438 | +0.44€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 82 | +0.441 | +1.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 82 | +0.441 | +1.34€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 19667 | +0.191 | -1723.01€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 19667 | +0.191 | -1723.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 3558 | +0.135 | -614.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 3558 | +0.135 | -614.25€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 3084 | +0.233 | -75.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 3084 | +0.233 | -75.10€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 3359 | +0.170 | -399.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 3359 | +0.170 | -399.70€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 3127 | +0.227 | -106.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 3127 | +0.227 | -106.16€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 3223 | +0.209 | -191.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 3223 | +0.209 | -191.97€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 3316 | +0.184 | -335.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 3316 | +0.184 | -335.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 7175 | +0.133 | +257.05€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 7175 | +0.133 | +257.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 3575 | +0.138 | +158.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 3575 | +0.138 | +158.23€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 3600 | +0.128 | +98.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 3600 | +0.128 | +98.82€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 837 | +0.294 | -6.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 837 | +0.294 | -6.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 361 | +0.277 | -11.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 361 | +0.277 | -11.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 391 | +0.296 | +4.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 391 | +0.296 | +4.06€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 85 | +0.339 | +1.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 85 | +0.339 | +1.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 355 | +0.416 | -14.08€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 355 | +0.416 | -14.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 159 | +0.413 | -7.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 159 | +0.413 | -7.23€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 163 | +0.421 | -5.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 163 | +0.421 | -5.87€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 33 | +0.357 | -0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 33 | +0.357 | -0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 309 | +0.092 | -4.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 94 | +0.104 | -0.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 215 | +0.085 | -3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 14 | +0.131 | +3.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 14 | +0.131 | +3.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 250 | +0.095 | -0.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 35 | +0.149 | +3.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 215 | +0.085 | -3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 45 | +0.032 | -7.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 45 | +0.032 | -7.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 9146 | +0.096 | -326.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 870 | +0.067 | -29.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 8276 | +0.099 | -296.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 5855 | +0.097 | -128.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 870 | +0.067 | -29.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 4985 | +0.103 | -98.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 659 | +0.119 | +10.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 659 | +0.119 | +10.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 2632 | +0.086 | -209.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 2632 | +0.086 | -209.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 490 | +0.282 | -34.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 490 | +0.282 | -34.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 490 | +0.282 | -34.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 490 | +0.282 | -34.89€ | 0 | 4 |
| ✅ GBM_LATE_15M | 9045 | +0.045 | +3030.27€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 9045 | +0.045 | +3030.27€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1288 | +0.183 | +862.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1288 | +0.183 | +862.33€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 1311 | +0.175 | +792.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1311 | +0.175 | +792.52€ | 0 | 30 |
| ✅ GBM_LATE_15M#DOGE | 1299 | +0.193 | +921.10€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1299 | +0.193 | +921.10€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 1454 | -0.047 | +46.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1454 | -0.047 | +46.42€ | 5 | 11 |
| ✅ GBM_LATE_15M#SOL | 1594 | -0.054 | +153.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1594 | -0.054 | +153.89€ | 5 | 3 |
| ✅ GBM_LATE_15M#XRP | 2099 | -0.073 | +254.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2099 | -0.073 | +254.02€ | 4 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 9928 | +0.047 | +3926.91€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 9928 | +0.047 | +3926.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1593 | -0.014 | +665.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1593 | -0.014 | +665.11€ | 2 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2160 | -0.039 | +187.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2160 | -0.039 | +187.61€ | 1 | 7 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1160 | +0.245 | +1084.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1160 | +0.245 | +1084.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1613 | -0.057 | -32.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1613 | -0.057 | -32.09€ | 10 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1707 | -0.028 | +379.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1707 | -0.028 | +379.23€ | 7 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1695 | +0.252 | +1642.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1695 | +0.252 | +1642.43€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 7420 | +0.171 | +5173.29€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 7420 | +0.171 | +5173.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 989 | +0.191 | +718.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 989 | +0.191 | +718.90€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1246 | +0.165 | +848.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1246 | +0.165 | +848.63€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 990 | +0.200 | +756.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 990 | +0.200 | +756.79€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1221 | +0.156 | +774.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1221 | +0.156 | +774.14€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1398 | +0.123 | +853.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1398 | +0.123 | +853.36€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1576 | +0.198 | +1221.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1576 | +0.198 | +1221.47€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1516 | +0.087 | +388.12€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1516 | +0.087 | +388.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 377 | +0.062 | +88.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 377 | +0.062 | +88.89€ | 3 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 238 | +0.154 | +119.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 238 | +0.154 | +119.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 245 | +0.168 | +82.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 245 | +0.168 | +82.30€ | 2 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 331 | -0.017 | +4.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 331 | -0.017 | +4.59€ | 3 | 5 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 269 | +0.113 | +78.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 269 | +0.113 | +78.42€ | 0 | 16 |
| ✅ GBM_LATE_15M_TARDIO | 8715 | +0.170 | +5932.99€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#15min | 8715 | +0.170 | +5932.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1238 | +0.202 | +946.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1238 | +0.202 | +946.96€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1412 | +0.163 | +932.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1412 | +0.163 | +932.43€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1225 | +0.214 | +994.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1225 | +0.214 | +994.25€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1358 | +0.143 | +799.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1358 | +0.143 | +799.49€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1550 | +0.100 | +767.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1550 | +0.100 | +767.86€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1932 | +0.202 | +1492.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1932 | +0.202 | +1492.01€ | 0 | 24 |
| ✅ GBM_LATE_5M | 2643 | +0.129 | +1208.39€ | 1 | 22 |
| ✅ GBM_LATE_5M#5min | 2643 | +0.129 | +1208.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 95 | +0.222 | +72.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 95 | +0.222 | +72.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 910 | +0.126 | +448.31€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 910 | +0.126 | +448.31€ | 1 | 17 |
| ✅ GBM_LATE_5M#DOGE | 333 | +0.169 | +199.02€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 333 | +0.169 | +199.02€ | 0 | 12 |
| ✅ GBM_LATE_5M#ETH | 826 | +0.133 | +361.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 826 | +0.133 | +361.95€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 126 | -0.023 | -1.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 126 | -0.023 | -1.19€ | 4 | 0 |
| ✅ GBM_LATE_5M#XRP | 353 | +0.114 | +128.05€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 353 | +0.114 | +128.05€ | 0 | 0 |
| ✅ GBM_LATE_60M | 559 | -0.010 | +125.26€ | 4 | 12 |
| ✅ GBM_LATE_60M#60min | 559 | -0.010 | +125.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 193 | +0.028 | +18.37€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 193 | +0.028 | +18.37€ | 2 | 6 |
| ✅ GBM_LATE_60M#ETH | 205 | +0.027 | +78.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 205 | +0.027 | +78.94€ | 2 | 9 |
| ✅ GBM_LATE_60M#SOL | 161 | -0.101 | +27.95€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 161 | -0.101 | +27.95€ | 2 | 1 |
| 🚫 GBM_LATE_60M_FADE | 196 | -0.303 | -33.79€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 196 | -0.303 | -33.79€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 78 | -0.263 | -8.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 78 | -0.263 | -8.38€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 53 | -0.282 | -6.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 53 | -0.282 | -6.35€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 369 | +0.039 | +4.20€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 369 | +0.039 | +4.20€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 155 | +0.035 | +11.12€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 155 | +0.035 | +11.12€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 93 | +0.068 | -3.50€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 93 | +0.068 | -3.50€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 121 | +0.020 | -3.43€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 121 | +0.020 | -3.43€ | 1 | 5 |
| ✅ LATE_WINDOW_5MIN | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 25 | +0.278 | +10.54€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 356 | +0.101 | +90.27€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 356 | +0.101 | +90.27€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 356 | +0.101 | +90.27€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 356 | +0.101 | +90.27€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M | 262 | -0.091 | -31.21€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 262 | -0.091 | -31.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 64 | -0.076 | -6.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 64 | -0.076 | -6.54€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 55 | -0.061 | -5.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 55 | -0.061 | -5.52€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 66 | +0.000 | -2.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 66 | +0.000 | -2.24€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M#XRP | 48 | -0.180 | -9.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 48 | -0.180 | -9.97€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 854 | -0.015 | -18.06€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 854 | -0.015 | -18.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 50 | +0.019 | -1.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 50 | +0.019 | -1.14€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 125 | -0.051 | -8.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 125 | -0.051 | -8.06€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 69 | -0.091 | -7.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 69 | -0.091 | -7.38€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 242 | +0.021 | +9.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 242 | +0.021 | +9.54€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#SOL | 309 | +0.002 | -3.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 309 | +0.002 | -3.90€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 59 | -0.107 | -7.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 59 | -0.107 | -7.11€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 486 | -0.006 | -1.07€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 486 | -0.006 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 154 | -0.038 | -10.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 154 | -0.038 | -10.57€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 148 | +0.007 | +2.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 148 | +0.007 | +2.71€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 184 | +0.011 | +6.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 184 | +0.011 | +6.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 5156 | -0.002 | -80.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 5156 | -0.002 | -80.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 528 | -0.006 | +1.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 528 | -0.006 | +1.43€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 599 | +0.004 | -9.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 599 | +0.004 | -9.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1017 | +0.001 | -21.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1017 | +0.001 | -21.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1165 | +0.007 | +11.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1165 | +0.007 | +11.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 932 | -0.009 | -32.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 932 | -0.009 | -32.39€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 915 | -0.014 | -30.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 915 | -0.014 | -30.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 8494 | -0.036 | +183.19€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 8494 | -0.036 | +183.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1357 | -0.035 | +140.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1357 | -0.035 | +140.31€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1484 | -0.028 | -22.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1484 | -0.028 | -22.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1367 | -0.044 | +82.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1367 | -0.044 | +82.34€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1481 | -0.035 | -31.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1481 | -0.035 | -31.03€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1414 | -0.040 | +25.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1414 | -0.040 | +25.85€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1391 | -0.034 | -11.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1391 | -0.034 | -11.79€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 556 | -0.061 | -42.52€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 556 | -0.061 | -42.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 67 | -0.065 | -5.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 67 | -0.065 | -5.01€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3170 | +0.004 | -5.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3170 | +0.004 | -5.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1160 | +0.008 | +7.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1160 | +0.008 | +7.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1385 | +0.006 | -2.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1385 | +0.006 | -2.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 23558 | -0.078 | +363.28€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 23558 | -0.078 | +363.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 3720 | -0.090 | +399.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 3720 | -0.090 | +399.14€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 4048 | -0.073 | -88.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 4048 | -0.073 | -88.41€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 3829 | -0.082 | +83.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 3829 | -0.082 | +83.23€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 3567 | -0.099 | -198.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 3567 | -0.099 | -198.28€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 4431 | -0.051 | +55.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 4431 | -0.051 | +55.14€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 3963 | -0.078 | +112.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 3963 | -0.078 | +112.45€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1204 | +0.000 | -15.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1204 | +0.000 | -15.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1001 | -0.019 | -30.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1001 | -0.019 | -30.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1310 | -0.002 | -14.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1310 | -0.002 | -14.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 555 | +0.101 | +151.83€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 419 | +0.115 | +139.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 106 | +0.102 | +36.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 106 | +0.102 | +36.50€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 79 | +0.105 | +19.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 79 | +0.105 | +19.69€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 76 | +0.128 | +31.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 76 | +0.128 | +31.91€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 70 | +0.153 | +33.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 70 | +0.153 | +33.86€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 88 | +0.089 | +17.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 88 | +0.089 | +17.28€ | 0 | 5 |
| ✅ PRICE_TARGET_GBM | 270 | -0.158 | -23.63€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 121 | -0.240 | -35.60€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 106 | -0.269 | -34.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 15 | -0.022 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 102 | -0.125 | -3.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 83 | -0.135 | -6.04€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 19 | -0.068 | +2.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 47 | -0.010 | +15.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 40 | +0.000 | +14.48€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 7 | -0.019 | +0.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 229 | -0.175 | -26.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 41 | -0.058 | +2.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 224 | -0.199 | +7.76€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 93 | -0.121 | +9.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 91 | -0.113 | +10.18€ | 0 | 2 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 88 | -0.289 | -18.70€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 84 | -0.291 | -20.09€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 43 | -0.167 | +17.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 41 | -0.151 | +19.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 216 | -0.193 | +9.23€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 8 | -0.120 | -1.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 78 | +0.338 | +20.23€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 20 | +0.318 | +2.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 20 | +0.318 | +2.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 41 | +0.477 | +20.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 41 | +0.477 | +20.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 78 | +0.338 | +20.23€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 184 | +0.032 | +2.01€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 184 | +0.032 | +2.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 78 | +0.013 | -3.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 78 | +0.013 | -3.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 12 | +0.043 | +0.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 12 | +0.043 | +0.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 19 | +0.113 | +1.96€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 19 | +0.113 | +1.96€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 75 | +0.019 | +2.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 75 | +0.019 | +2.23€ | 1 | 1 |
| ✅ STREAK_FADE_5M | 1309 | -0.021 | -58.45€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1309 | -0.021 | -58.45€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 443 | -0.012 | -12.46€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 443 | -0.012 | -12.46€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 470 | -0.006 | -12.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 470 | -0.006 | -12.47€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 132 | -0.037 | -12.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 132 | -0.037 | -12.47€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 264 | -0.053 | -21.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 264 | -0.053 | -21.04€ | 5 | 0 |
| ✅ STREAK_FADE_60M | 34 | +0.000 | -0.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 34 | +0.000 | -0.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 20 | -0.091 | -2.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 20 | -0.091 | -2.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 14 | +0.087 | +1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 14 | +0.087 | +1.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 2734 | +0.028 | +56.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 2734 | +0.028 | +56.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 904 | +0.030 | +15.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 904 | +0.030 | +15.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 527 | +0.027 | +13.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 527 | +0.027 | +13.79€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 808 | +0.024 | +7.19€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 808 | +0.024 | +7.19€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 495 | +0.031 | +19.92€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 495 | +0.031 | +19.92€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 3480 | +0.009 | -27.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3480 | +0.009 | -27.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1338 | +0.009 | -12.89€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1338 | +0.009 | -12.89€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1360 | +0.018 | +1.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1360 | +0.018 | +1.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 782 | -0.005 | -16.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 782 | -0.005 | -16.07€ | 2 | 0 |
| ✅ UPDOWN_GBM | 7091 | +0.003 | +142.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2531 | +0.040 | +233.09€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 285 | +0.016 | +1.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 3802 | -0.018 | -83.95€ | 3 | 0 |
| ✅ UPDOWN_GBM#60min | 426 | -0.012 | -7.25€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 196 | +0.091 | +38.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 8 | -0.040 | -1.01€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1581 | +0.012 | +65.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 251 | +0.081 | +47.09€ | 5 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 84 | +0.058 | +5.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1093 | +0.001 | +18.02€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 135 | -0.033 | -6.60€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 829 | -0.004 | -0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 123 | +0.100 | +28.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 697 | -0.024 | -29.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1703 | -0.003 | -11.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 763 | +0.019 | +13.58€ | 1 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 82 | +0.059 | +4.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 652 | -0.034 | -28.90€ | 4 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 191 | +0.003 | -0.85€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1800 | -0.007 | -17.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 616 | -0.003 | -3.55€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 69 | +0.007 | -1.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1003 | -0.007 | -12.50€ | 2 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 100 | -0.010 | +0.19€ | 1 | 2 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 980 | +0.008 | +70.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 599 | +0.056 | +105.36€ | 0 | 8 |
| ✅ UPDOWN_GBM#XRP#240min | 33 | -0.157 | -6.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 348 | -0.057 | -28.37€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 230 | +0.315 | +46.75€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 230 | +0.315 | +46.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 133 | +0.300 | +18.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 133 | +0.300 | +18.46€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 97 | +0.328 | +28.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 97 | +0.328 | +28.30€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 4420 | -0.075 | +903.72€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 4420 | -0.075 | +903.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 898 | -0.164 | -95.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 898 | -0.164 | -95.15€ | 5 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 78 | +0.062 | +12.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 78 | +0.062 | +12.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 357 | +0.141 | +166.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 357 | +0.141 | +166.71€ | 2 | 15 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1432 | -0.070 | +276.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1432 | -0.070 | +276.63€ | 3 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1352 | -0.092 | +201.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1352 | -0.092 | +201.42€ | 5 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 34 | +0.000 | -1.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 34 | +0.000 | -1.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 34 | +0.000 | -1.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 34 | +0.000 | -1.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 365 | +0.282 | +272.65€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 365 | +0.282 | +272.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 209 | +0.277 | +151.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 209 | +0.277 | +151.06€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 156 | +0.285 | +121.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 156 | +0.285 | +121.58€ | 0 | 12 |
| ✅ UPDOWN_OU_5M | 568 | -0.089 | -60.76€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 568 | -0.089 | -60.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 287 | -0.068 | -30.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 287 | -0.068 | -30.31€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 135 | -0.033 | -5.05€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 135 | -0.033 | -5.05€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 30 | -0.188 | -6.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 30 | -0.188 | -6.21€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 46 | -0.125 | -5.08€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 46 | -0.125 | -5.08€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 39 | -0.207 | -7.30€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 39 | -0.207 | -7.30€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 31 | -0.197 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1171 | +0.291 | +503.57€ | 0 | 6 |
| ✅ WEEKLY_PRICE#BTC | 356 | +0.212 | +8.23€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 374 | +0.269 | +105.74€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 441 | +0.371 | +389.59€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.084) — sin ventaja clara. oversold(IBS<0.3): IC=+0.018 n=2523 | neutral: IC=-0.001 n=2696 | overbought(IBS>0.7): IC=+0.083 n=2830
  - _Datos_: n=8394 IC=+0.035 PNL=+746.77€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 187s) 32 celda(s) GATE OK de 2240 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.003 < 0.08 — monitorear
  - _Datos_: n=616 IC=-0.003 PNL=-3.55€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=374/15 IC=+0.269 PNL=+105.74€ | BTC: n=356/15 IC=+0.212 PNL=+8.23€ | SOL: n=441/15 IC=+0.371 PNL=+389.59€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.073 n=117005 | tras_1loss IC=+0.046 n=91659 | tras_2loss IC=+0.008 n=41585/40 | gap=+0.065 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 19 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC, UPDOWN_GBM#SOL
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
  - _Estado_: 7029 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.100 n=48/60 | contraria IC=+0.052 n=27 | gap=+0.048 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=101, boost estimado=+0.014. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 70 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=191/40 IC=+0.003 PNL=-0.85€ | BTC#60min: n=135/40 IC=-0.033 PNL=-6.60€ | SOL#60min: n=100/40 IC=-0.010 PNL=+0.19€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.012 n=762 | contrario_BTC IC=-0.021 n=579/40 | gap=-0.010 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.192 > 0.08 con n=76 PNL=+48.25€
  - _Datos_: n=76 IC=+0.192 PNL=+48.25€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.143 > 0.08 con n=96 PNL=+27.92€
  - _Datos_: n=96 IC=+0.143 PNL=+27.92€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 15/25 ops en el filtro definido (IC actual=+0.243 PNL=+14.93€)
  - _Datos_: n=15 IC=+0.243 PNL=+14.93€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=993 PNL=+507.89€
  - _Datos_: n=993 IC=+0.335 PNL=+507.89€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=62 IC=+0.031 PNL=+10.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=62 IC=+0.031 PNL=+10.83€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 20/30 ops en el filtro definido (IC actual=+0.182 PNL=+11.24€)
  - _Datos_: n=20 IC=+0.182 PNL=+11.24€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=6822 IC=-0.000 PNL=+91.52€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=6822 IC=-0.000 PNL=+91.52€

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
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=353 IC=+0.001 PNL=-1.08€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=353 IC=+0.001 PNL=-1.08€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=73 IC=-0.073 PNL=-6.17€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=73 IC=-0.073 PNL=-6.17€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=122 IC=-0.073 PNL=-8.21€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=122 IC=-0.073 PNL=-8.21€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.1 con n=538 PNL=+134.84€
  - _Datos_: n=538 IC=+0.120 PNL=+134.84€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=189 IC=+0.076 PNL=+40.74€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=189 IC=+0.076 PNL=+40.74€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=251 IC=+0.081 PNL=+47.09€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=251 IC=+0.081 PNL=+47.09€

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
  - _Estado_: n=1475 IC=+0.023 PNL=+86.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1475 IC=+0.023 PNL=+86.84€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 26/30 ops en el filtro definido (IC actual=-0.214 PNL=-5.03€)
  - _Datos_: n=26 IC=-0.214 PNL=-5.03€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=79 IC=-0.018 PNL=+8.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=79 IC=-0.018 PNL=+8.79€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=96 IC=+0.031 PNL=+8.08€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=96 IC=+0.031 PNL=+8.08€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 6/15 ops en el filtro definido (IC actual=+0.037 PNL=+1.09€)
  - _Datos_: n=6 IC=+0.037 PNL=+1.09€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2293 IC=-0.023 PNL=-61.16€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2293 IC=-0.023 PNL=-61.16€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=38 PNL=+9.28€
  - _Datos_: n=38 IC=+0.175 PNL=+9.28€

**⏳ H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: 30
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: 25/30 ops en el filtro definido (IC actual=+0.278 PNL=+10.54€)
  - _Datos_: n=25 IC=+0.278 PNL=+10.54€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1838 IC=+0.017 PNL=+90.85€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1838 IC=+0.017 PNL=+90.85€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=478 IC=+0.035 PNL=+4.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=478 IC=+0.035 PNL=+4.84€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=145 PNL=+34.38€
  - _Datos_: n=145 IC=+0.105 PNL=+34.38€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.08 con n=135 PNL=+3.08€
  - _Datos_: n=135 IC=+0.120 PNL=+3.08€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.08 con n=123 PNL=+38.94€
  - _Datos_: n=123 IC=+0.132 PNL=+38.94€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=22995 IC=+0.102 PNL=+7078.66€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=22995 IC=+0.102 PNL=+7078.66€

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
  - _Estado_: n=918 IC=+0.025 PNL=+46.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=918 IC=+0.025 PNL=+46.59€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=302 PNL=+90.67€
  - _Datos_: n=302 IC=+0.118 PNL=+90.67€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=94 IC=-0.094 PNL=+19.83€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=94 IC=-0.094 PNL=+19.83€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.443 > 0.1 con n=630 PNL=+545.87€
  - _Datos_: n=630 IC=+0.443 PNL=+545.87€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1671 IC=+0.021 PNL=+88.86€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1671 IC=+0.021 PNL=+88.86€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=820 PNL=+302.97€
  - _Datos_: n=820 IC=+0.166 PNL=+302.97€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 36/40 ops en el filtro definido (IC actual=-0.263 PNL=-7.46€)
  - _Datos_: n=36 IC=-0.263 PNL=-7.46€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=458 IC=+0.041 PNL=+58.90€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=458 IC=+0.041 PNL=+58.90€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=74 IC=+0.079 PNL=+7.36€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=74 IC=+0.079 PNL=+7.36€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=5494 IC=-0.146 PNL=+184.69€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5494 IC=-0.146 PNL=+184.69€

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
  - _Estado_: n=689 IC=+0.144 PNL=+315.62€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=689 IC=+0.144 PNL=+315.62€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.08 con n=538 PNL=+134.84€
  - _Datos_: n=538 IC=+0.120 PNL=+134.84€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=725 IC=-0.001 PNL=-1.08€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=725 IC=-0.001 PNL=-1.08€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=697 PNL=+361.41€
  - _Datos_: n=697 IC=+0.084 PNL=+361.41€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.08 con n=159 PNL=+53.41€
  - _Datos_: n=159 IC=+0.165 PNL=+53.41€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.241 < -0.1 con n=601 PNL=-80.64€
  - _Datos_: n=601 IC=-0.241 PNL=-80.64€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1479 IC=+0.129 PNL=+766.83€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1479 IC=+0.129 PNL=+766.83€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 35/40 ops en el filtro definido (IC actual=+0.095 PNL=+9.61€)
  - _Datos_: n=35 IC=+0.095 PNL=+9.61€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=746 IC=-0.021 PNL=+63.48€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=746 IC=-0.021 PNL=+63.48€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=659 PNL=+409.25€
  - _Datos_: n=659 IC=+0.184 PNL=+409.25€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1101 IC=-0.065 PNL=+144.70€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1101 IC=-0.065 PNL=+144.70€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.08 con n=278 PNL=-36.57€
  - _Datos_: n=278 IC=+0.118 PNL=-36.57€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.235 > 0.08 con n=1637 PNL=-158.27€
  - _Datos_: n=1637 IC=+0.235 PNL=-158.27€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 11/40 ops en el filtro definido (IC actual=-0.021 PNL=+0.98€)
  - _Datos_: n=11 IC=-0.021 PNL=+0.98€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.103 n=187) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=187 IC=+0.103 PNL=+44.67€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.352 > 0.08 con n=79 PNL=+51.51€
  - _Datos_: n=79 IC=+0.352 PNL=+51.51€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.430 n=242) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=242 IC=+0.430 PNL=+330.53€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=3558 IC=+0.135 PNL=-614.25€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=3558 IC=+0.135 PNL=-614.25€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.208 > 0.1 con n=46 PNL=+28.21€
  - _Datos_: n=46 IC=+0.208 PNL=+28.21€
