# Hipótesis automáticas — 2026-09-02 06:19 UTC
_Generado por shadow_postmortem.py sobre 248275 resoluciones (PNL=+22055.59€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.835` → IC=-0.395 (n=74)

  - _Acción_: SKIP cuando `py_entrada` > 0.835
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=234)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.269 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.163)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.182 (n=278)

  - _Acción_: Kelly boost +0.91€ cuando `n_ballena_banda` > 19.0 (IC base=+0.163)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.255 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 74.0 (IC base=+0.163)

- **PATRÓN** `banda_hit_calibrado` > `0.8038` → IC=+0.258 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8038 (IC base=+0.163)

- **PATRÓN** `banda_z` > `11.871` → IC=+0.271 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.871 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.175 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.164 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 11.0 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=322)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `3036.1004` → IC=+0.218 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3036.1004 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `242.0` → IC=+0.258 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 242.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` < `0.835` → IC=+0.131 (n=234)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.835 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 116.0 (IC base=+0.003)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=118)

- **FILTRO** `n_ballena_banda` < `34.0` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `n_ballena_banda` < 34.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=116)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.123 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=119)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.279 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.199)

- **PATRÓN** `n_ballena_banda` > `18.0` → IC=+0.216 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 18.0 (IC base=+0.199)

- **PATRÓN** `n_total_lado` > `55.0` → IC=+0.244 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 55.0 (IC base=+0.199)

- **PATRÓN** `banda_hit_calibrado` > `0.8067` → IC=+0.280 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8067 (IC base=+0.199)

- **PATRÓN** `banda_z` > `11.967` → IC=+0.280 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.967 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.211 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.210 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2935.919` → IC=+0.219 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2935.919 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `226.0` → IC=+0.260 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 226.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.133 (n=118)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.023)

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

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.269 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.085)

- **PATRÓN** `banda_hit_calibrado` > `0.8113` → IC=+0.230 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8113 (IC base=+0.085)

- **PATRÓN** `banda_z` > `8.441` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.441 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.085)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `146.35` → IC=-0.294 (n=3398)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.35
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=10199)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `151.0` → IC=-0.246 (n=439)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1318)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `111.95` → IC=-0.407 (n=438)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 111.95
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=1315)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `157.05` → IC=-0.157 (n=928)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.05
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2787)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `136.94` → IC=-0.325 (n=752)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 136.94
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=2258)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.04` → IC=-0.372 (n=809)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.04
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=1645)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.189 (n=7411)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.7 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=1900)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2385.1288` → IC=+0.171 (n=1823)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2385.1288 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.147 (n=4426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=5847)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.258 (n=4508)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=3572)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `1919.6059` → IC=+0.184 (n=3038)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1919.6059 (IC base=+0.142)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.215 (n=741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.209 (n=812)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.378 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `12999.7032` → IC=+0.216 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12999.7032 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=837)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.265 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=1076)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `12461.8732` → IC=+0.213 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12461.8732 (IC base=+0.194)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.129 (n=534)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` > `0.595` → IC=+0.161 (n=284)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.595 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=268)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `4800.0243` → IC=+0.153 (n=214)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4800.0243 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.385` → IC=+0.182 (n=212)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.385 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4013.5945` → IC=+0.155 (n=326)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4013.5945 (IC base=+0.132)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=85)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=1537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=1292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` > `0.695` → IC=+0.325 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.695 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.278 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.273 (n=627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.269)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.413 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.269 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `2212.3731` → IC=+0.275 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2212.3731 (IC base=+0.269)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.159 (n=312)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.273 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=427)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2022.4564` → IC=+0.163 (n=315)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2022.4564 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=143)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.217 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.432 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` < `0.215` → IC=+0.349 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.215 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2120.4177` → IC=+0.231 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2120.4177 (IC base=+0.209)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.332 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=167)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `3436.329` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3436.329 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.124 (n=509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.109)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.216 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=286)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.109)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.344 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=124)

- **FILTRO** `libro_liquidez` < `10760.7327` → IC=-0.259 (n=139)

  - _Acción_: SKIP cuando `libro_liquidez` < 10760.7327
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=47)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=5743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=4875)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.203 (n=2771)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3916.0714` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3916.0714 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.165 (n=1007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.174 (n=1420)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=1492)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.164)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=84)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=85)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.330)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.330)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=1468)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=1232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.173 (n=1493)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.74 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.182 (n=995)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.72 (IC base=+0.170)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=1309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.236 (n=1108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.235)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.313 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.235)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=1204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.191 (n=725)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.7 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.452 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.444)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.446 (n=257)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.479 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.444)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.442 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `3363.9486` → IC=+0.457 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3363.9486 (IC base=+0.444)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `10601.0016` → IC=+0.459 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10601.0016 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.451 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.450 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `2309.2972` → IC=+0.448 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2309.2972 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.457 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.439 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `1927.8949` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.8949 (IC base=+0.444)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=18304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.207 (n=15851)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.189)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=3255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.171 (n=2286)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.72 (IC base=+0.141)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=2733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=1304)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.260 (n=2047)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.226)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=1174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=2709)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.164)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.236 (n=1404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.224 (n=1337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.280 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.238 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=1132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=2078)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.202 (n=2642)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.210 (n=2292)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.134)

- **PATRÓN** `restante_min` < `3.98` → IC=+0.145 (n=2123)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` < 3.98 (IC base=+0.134)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.155 (n=2244)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.93 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.149 (n=3108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.134)

- **PATRÓN** `lag_apertura_s` < `4.25` → IC=+0.158 (n=2112)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 4.25 (IC base=+0.134)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.213 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.137)

- **PATRÓN** `restante_min` < `3.94` → IC=+0.151 (n=1057)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` < 3.94 (IC base=+0.137)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.150 (n=1444)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.88 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.161 (n=1538)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 8.0 (IC base=+0.137)

- **PATRÓN** `lag_apertura_s` < `7.07` → IC=+0.151 (n=1387)

  - _Acción_: Kelly boost +0.76€ cuando `lag_apertura_s` < 7.07 (IC base=+0.137)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.206 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.130)

- **PATRÓN** `restante_min` < `4.42` → IC=+0.138 (n=1405)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 4.42 (IC base=+0.130)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.164 (n=1173)

  - _Acción_: Kelly boost +0.82€ cuando `restante_min` > 4.94 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=3338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=1404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `lag_apertura_s` < `3.38` → IC=+0.172 (n=1061)

  - _Acción_: Kelly boost +0.86€ cuando `lag_apertura_s` < 3.38 (IC base=+0.130)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.298 (n=613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.383 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5555.6091` → IC=+0.320 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5555.6091 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.320 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.305)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.303 (n=283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.305)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.377 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.305)

- **PATRÓN** `libro_liquidez` > `1700.1685` → IC=+0.319 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1700.1685 (IC base=+0.305)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.327 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.328)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.346 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.328)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.400 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.328)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `662.0852` → IC=+0.359 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 662.0852 (IC base=+0.328)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.436 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.427 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.420)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.426 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.420)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.431 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.420)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.421 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.420)

- **PATRÓN** `libro_liquidez` > `2076.021` → IC=+0.431 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.021 (IC base=+0.420)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.429 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.425 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.415)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.417 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.415)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.426 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.415)

- **PATRÓN** `libro_liquidez` > `5506.0634` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5506.0634 (IC base=+0.415)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.439 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.430 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.427 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `2031.364` → IC=+0.456 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.364 (IC base=+0.427)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.269)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.422 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.287 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1319.6978` → IC=+0.288 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1319.6978 (IC base=+0.269)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.269)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.422 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.287 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1319.6978` → IC=+0.288 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1319.6978 (IC base=+0.269)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.351` → IC=+0.124 (n=3282)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.351 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.223 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.452` → IC=+0.146 (n=1257)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 5.452 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.238 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.1711` → IC=+0.173 (n=549)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1711 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `2.4264` → IC=+0.166 (n=1690)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.4264 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `1.4785` → IC=+0.166 (n=1920)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4785 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.197 (n=913)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 54.0 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.4065` → IC=+0.122 (n=3212)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.4065 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.6747` → IC=+0.162 (n=483)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6747 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.3055` → IC=+0.262 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3055 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` > `2.8846` → IC=+0.212 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8846 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.222 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.036)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.178 (n=330)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.007 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.269` → IC=+0.149 (n=727)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.269 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.182 (n=357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 8.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.453` → IC=+0.302 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.453 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2285` → IC=+0.209 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2285 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.8937` → IC=+0.127 (n=421)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8937 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4564` → IC=+0.144 (n=631)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4564 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.191 (n=564)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.182 (n=376)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 60.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.257 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.291 (n=161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.1064` → IC=+0.336 (n=211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1064 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.264 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.264 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.4014` → IC=+0.280 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4014 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.158` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.158 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.14` → IC=+0.276 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.14 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.0697` → IC=+0.265 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0697 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.8031` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8031 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1698.3448` → IC=+0.273 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1698.3448 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.255 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=+0.257)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.247 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.220 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.231 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.206 (n=577)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.9292` → IC=+0.248 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9292 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.1784` → IC=+0.220 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1784 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.332` → IC=+0.220 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.332 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.135` → IC=+0.211 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.135 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.2518` → IC=+0.207 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2518 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.229 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.208 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.207 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1027` → IC=+0.227 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1027 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `11047.9956` → IC=+0.227 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11047.9956 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `383.0` → IC=+0.205 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 383.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.148 (n=632)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.006 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1746` → IC=+0.155 (n=421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1746 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.148 (n=566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.147 (n=664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 18.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6376` → IC=+0.170 (n=631)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6376 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.857` → IC=+0.227 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.857 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.613` → IC=+0.195 (n=211)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.613 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.151` → IC=+0.205 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.151 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4183` → IC=+0.165 (n=524)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.4183 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.491` → IC=+0.162 (n=468)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.491 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=817)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `12561.7266` → IC=+0.169 (n=421)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 12561.7266 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 233.0 (IC base=+0.145)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.205 (n=310)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.203 (n=261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.171` → IC=+0.256 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.171 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.1321` → IC=+0.162 (n=575)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.1321 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.3169` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.3169 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `3.2535` → IC=+0.154 (n=527)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 3.2535 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.6876` → IC=+0.174 (n=599)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.6876 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.188 (n=681)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.201 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.248 (n=541)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0101 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4694` → IC=+0.242 (n=541)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4694 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.242 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.242 (n=560)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0441` → IC=+0.303 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0441 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.545` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.545 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3816` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3816 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.9639` → IC=+0.227 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9639 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.219 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.234)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.156 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=467)

- **FILTRO** `ibs_20min` < `0.2901` → IC=-0.141 (n=204)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2901
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=415)

- **FILTRO** `ibs_20min` > `0.8413` → IC=-0.181 (n=268)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8413
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=808)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.153 (n=70)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1006)

- **PATRÓN** `dist_vwap_pct` > `0.3391` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3391 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` < `0.6297` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6297 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1929 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2199` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2199 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.435` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.435 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` > `1.9251` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9251 (IC base=-0.044)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.250 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.2864` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.2864 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.0926` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0926 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` > `1.573` → IC=+0.125 (n=158)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.573 (IC base=-0.044)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.134 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=127)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.179 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=112)

- **FILTRO** `sigma_ewma_delta_pct` > `8.208` → IC=-0.186 (n=189)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.208
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=1460)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `volumen_spike_ratio` > `1.441` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.441
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.182 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0058 (IC base=+0.036)

- **PATRÓN** `ibs_20min` > `0.2759` → IC=+0.140 (n=112)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.2759 (IC base=+0.036)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5207` → IC=-0.165 (n=323)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5207
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=628)

- **FILTRO** `ibs_20min` < `0.4286` → IC=-0.192 (n=475)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4286
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=476)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.200 (n=208)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=743)

- **FILTRO** `sigma_h` > `0.0205` → IC=-0.128 (n=509)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0205
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=989)

- **FILTRO** `ibs_20min` > `0.8` → IC=-0.190 (n=369)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1129)

- **FILTRO** `sigma_ewma_delta_pct` > `8.662` → IC=-0.147 (n=182)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.662
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1316)

- **PATRÓN** `dist_vwap_pct` > `0.5071` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5071 (IC base=-0.104)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.229 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=-0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.0665` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0665 (IC base=-0.104)

- **PATRÓN** `volumen_spike_ratio` < `1.6001` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6001 (IC base=-0.104)

- **PATRÓN** `volumen_spike_ratio` > `1.8487` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8487 (IC base=-0.104)

- **PATRÓN** `volumen_regimen` > `1.2726` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2726 (IC base=-0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.0889` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0889 (IC base=-0.053)

- **PATRÓN** `volumen_spike_ratio` > `1.6969` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.6969 (IC base=-0.053)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.149 (n=1854)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0077 (IC base=+0.061)

- **PATRÓN** `ibs_20min` > `0.2722` → IC=+0.129 (n=4085)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.2722 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `1.2123` → IC=+0.289 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2123 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` > `0.6802` → IC=+0.207 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6802 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` < `0.1149` → IC=+0.204 (n=1852)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1149 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.253` → IC=+0.217 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.253 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` < `1.4968` → IC=+0.220 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4968 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` > `2.8554` → IC=+0.215 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8554 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.294 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.5882` → IC=+0.126 (n=4016)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.5882 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.7953` → IC=+0.261 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7953 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.7018` → IC=+0.229 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7018 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.2272` → IC=+0.245 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2272 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2598` → IC=+0.346 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2598 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.273 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.275 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.049)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2584` → IC=-0.152 (n=334)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2584
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=683)

- **FILTRO** `sigma_ewma_delta_pct` > `2.237` → IC=-0.166 (n=285)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.237
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=622)

- **PATRÓN** `ibs_20min` > `0.7885` → IC=+0.189 (n=255)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7885 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.7645` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7645 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.391 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8717` → IC=-0.155 (n=352)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8717
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1059)

- **PATRÓN** `ballena_activa_n` < `287.0` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 287.0 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.5424` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5424 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` < `0.5727` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5727 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` > `1.1078` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.1078 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.1467` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.1467 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.3623` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3623 (IC base=-0.030)

- **PATRÓN** `ballena_activa_n` < `337.0` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 337.0 (IC base=-0.030)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.272 (n=301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.0827` → IC=+0.222 (n=221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0827 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.247 (n=251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.7091` → IC=+0.250 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7091 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.142` → IC=+0.279 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.142 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.1067` → IC=+0.229 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1067 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `2.4776` → IC=+0.216 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4776 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.7308` → IC=+0.215 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7308 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.258 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.333 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.338 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` < `0.325` → IC=+0.324 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.325 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.729` → IC=+0.316 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.729 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.749` → IC=+0.308 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.749 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3643` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3643 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` < `3.5266` → IC=+0.303 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.5266 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `2.4058` → IC=+0.321 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4058 (IC base=+0.308)

- **PATRÓN** `libro_liquidez` > `1836.8021` → IC=+0.339 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1836.8021 (IC base=+0.308)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.290 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.308)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.157 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=500)

- **FILTRO** `ibs_20min` < `0.7257` → IC=-0.155 (n=421)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7257
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=217)

- **FILTRO** `volumen_regimen` > `0.9213` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9213
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=64)

- **FILTRO** `ibs_20min` > `0.8719` → IC=-0.159 (n=291)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8719
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=877)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `volumen_regimen` > `0.8624` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8624
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **FILTRO** `volumen_pendiente_norm` < `0.1167` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1167
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=5)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.146 (n=77)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1091)

- **PATRÓN** `dist_vwap_pct` > `0.4471` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4471 (IC base=-0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.0567` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0567 (IC base=-0.080)

- **PATRÓN** `volumen_spike_ratio` < `1.3975` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.3975 (IC base=-0.080)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.78` → IC=-0.146 (n=583)

  - _Acción_: SKIP cuando `ibs_20min` < 0.78
  - _Potencial_: sin este filtro IC_bueno=+0.266 (n=301)

- **FILTRO** `ibs_20min` > `0.7667` → IC=-0.230 (n=257)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7667
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=773)

- **FILTRO** `dist_vwap_pct` > `0.1234` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1234
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=69)

- **FILTRO** `volumen_regimen` > `1.0409` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0409
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=57)

- **FILTRO** `volumen_pendiente_norm` < `0.1798` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1798
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

- **PATRÓN** `ibs_20min` > `0.78` → IC=+0.266 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.78 (IC base=-0.006)

- **PATRÓN** `dist_vwap_pct` > `0.5648` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5648 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.228 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.1463` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1463 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` < `0.1169` → IC=+0.238 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1169 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2303` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2303 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.4566` → IC=+0.270 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4566 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.282 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0214` → IC=+0.322 (n=313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0214 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.254 (n=608)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` > `0.8982` → IC=+0.316 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8982 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `1.3482` → IC=+0.345 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3482 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.169` → IC=+0.284 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.169 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `0.8427` → IC=+0.283 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8427 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2403` → IC=+0.286 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2403 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` < `2.5913` → IC=+0.252 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5913 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.2494` → IC=+0.250 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2494 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.255 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `2469.502` → IC=+0.248 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2469.502 (IC base=+0.245)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.281 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.024` → IC=+0.309 (n=244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.024 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.288 (n=688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.3654` → IC=+0.319 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3654 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.5389` → IC=+0.279 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5389 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` < `0.2087` → IC=+0.283 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2087 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.239` → IC=+0.313 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.239 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.914` → IC=+0.280 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.914 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` < `0.6376` → IC=+0.285 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6376 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `1.2624` → IC=+0.309 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2624 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.243` → IC=+0.379 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.243 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.1844` → IC=+0.302 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1844 (IC base=+0.280)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.206 (n=1146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.332` → IC=+0.169 (n=3023)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.332 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=3605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `1.111` → IC=+0.244 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.111 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.843` → IC=+0.251 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.843 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.170 (n=2339)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6279 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1049` → IC=+0.186 (n=1264)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1049 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.324` → IC=+0.166 (n=2792)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.324 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=2662)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3946.0946` → IC=+0.181 (n=1145)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3946.0946 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.183 (n=2064)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 89.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.193 (n=2162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0063 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.212 (n=1079)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.179 (n=1499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 7.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.4225` → IC=+0.230 (n=3237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4225 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.921` → IC=+0.220 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.921 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1693` → IC=+0.168 (n=2464)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1693 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.256 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.5763` → IC=+0.170 (n=1150)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5763 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6688` → IC=+0.195 (n=871)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6688 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.174 (n=2196)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 158.0 (IC base=+0.177)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.184 (n=254)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0057 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.195 (n=260)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0071 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.2758` → IC=+0.190 (n=569)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.2758 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=257)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.54` → IC=+0.323 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.54 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.250 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.7061` → IC=+0.154 (n=487)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.7061 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.4596` → IC=+0.167 (n=487)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4596 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.208 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.186 (n=294)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 65.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.262 (n=322)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.2479` → IC=+0.284 (n=317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2479 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.242 (n=389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.258 (n=383)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.2708` → IC=+0.265 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2708 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.687` → IC=+0.253 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.687 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0905` → IC=+0.234 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0905 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2483` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2483 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.9129` → IC=+0.251 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9129 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.791` → IC=+0.250 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.791 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.281 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1698.1076` → IC=+0.277 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1698.1076 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.247 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.228 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.4064` → IC=+0.179 (n=500)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.4064 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.4579` → IC=+0.221 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4579 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1847` → IC=+0.231 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1847 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.986` → IC=+0.239 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.986 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.52` → IC=+0.174 (n=477)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 7.52 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.176 (n=220)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6973 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `1.0613` → IC=+0.190 (n=227)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.0613 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.195 (n=149)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `2.1261` → IC=+0.192 (n=414)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.1261 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `11354.3179` → IC=+0.193 (n=447)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 11354.3179 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.176 (n=603)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.006 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2979` → IC=+0.173 (n=603)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2979 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.4506` → IC=+0.193 (n=603)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.4506 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.387` → IC=+0.233 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.387 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6305` → IC=+0.229 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6305 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1598` → IC=+0.226 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1598 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4667` → IC=+0.166 (n=495)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.4667 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.3943` → IC=+0.156 (n=495)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.3943 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `15529.4655` → IC=+0.175 (n=201)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 15529.4655 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.159 (n=136)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 231.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.219 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.2701` → IC=+0.190 (n=465)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.2701 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.193 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 5.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.331` → IC=+0.287 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.331 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` < `0.1052` → IC=+0.160 (n=416)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.1052 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1318` → IC=+0.165 (n=192)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1318 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.171 (n=156)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `4.1198` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 4.1198 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=516)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.223 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.247 (n=413)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.2226` → IC=+0.263 (n=276)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2226 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.254 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.229 (n=374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.3724` → IC=+0.271 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3724 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.556` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.556 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.3645` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3645 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.9412` → IC=+0.215 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9412 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `3.1577` → IC=+0.224 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1577 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `1854.821` → IC=+0.229 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1854.821 (IC base=+0.228)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.204 (n=441)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.3561` → IC=+0.186 (n=441)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.3561 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.4362` → IC=+0.216 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4362 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1443` → IC=+0.202 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1443 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.292 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6402` → IC=+0.186 (n=501)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6402 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1049` → IC=+0.213 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1049 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6221` → IC=+0.207 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6221 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=564)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `12394.6216` → IC=+0.222 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12394.6216 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.159 (n=385)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 169.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.163 (n=520)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3801` → IC=+0.151 (n=591)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3801 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.148 (n=268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.3886` → IC=+0.199 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3886 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.301` → IC=+0.192 (n=128)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 12.301 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.1598` → IC=+0.139 (n=591)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1598 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.6089` → IC=+0.136 (n=591)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6089 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.1073` → IC=+0.180 (n=192)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1073 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8875` → IC=+0.145 (n=322)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.8875 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.5391` → IC=+0.169 (n=161)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5391 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `11512.1645` → IC=+0.158 (n=197)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 11512.1645 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.188 (n=299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0106 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=685)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5455` → IC=+0.190 (n=657)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5455 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.1462` → IC=+0.257 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1462 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.067` → IC=+0.264 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.067 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6257` → IC=+0.131 (n=657)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6257 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1661` → IC=+0.137 (n=653)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1661 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.148 (n=208)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.123 (n=508)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `3232.1195` → IC=+0.224 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3232.1195 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.156 (n=312)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 40.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.131 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0059 (IC base=+0.130)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.170 (n=265)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0094 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1005` → IC=+0.135 (n=195)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1005 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.4394` → IC=+0.231 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4394 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `1.0076` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 1.0076 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.22` → IC=+0.187 (n=228)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.22 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.1545` → IC=+0.145 (n=586)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1545 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.8419` → IC=+0.145 (n=390)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.8419 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2647` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2647 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.5471` → IC=+0.142 (n=199)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5471 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.3191` → IC=+0.186 (n=151)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.3191 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `1421.8863` → IC=+0.155 (n=522)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1421.8863 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0171` → IC=+0.213 (n=455)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0171 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1678` → IC=+0.213 (n=301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1678 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.8919` → IC=+0.260 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8919 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.1517` → IC=+0.219 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1517 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.279` → IC=+0.246 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.279 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `0.6788` → IC=+0.204 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6788 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.254 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `2.5276` → IC=+0.202 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5276 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=820)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.267 (n=230)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.0924` → IC=+0.250 (n=230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0924 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.222 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=318)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.258 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.482` → IC=+0.266 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.482 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6252` → IC=+0.230 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6252 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.317 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.7091` → IC=+0.243 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7091 (IC base=+0.213)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.176 (n=239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0097 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3305` → IC=+0.132 (n=631)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.3305 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.160 (n=681)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 8.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.181 (n=644)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.8823` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8823 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.273` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.273 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8772` → IC=+0.143 (n=379)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8772 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.168` → IC=+0.156 (n=190)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.168 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.1823` → IC=+0.199 (n=194)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1823 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.3099` → IC=+0.143 (n=583)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.3099 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.894` → IC=+0.139 (n=441)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.894 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=530)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4681.5356` → IC=+0.147 (n=239)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4681.5356 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.188 (n=174)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 12.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.3112` → IC=+0.129 (n=481)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.3112 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.164 (n=248)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 17.0 (IC base=+0.059)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.186 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=108)

- **FILTRO** `ibs_20min` > `0.6298` → IC=-0.126 (n=105)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6298
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=204)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.145 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 10.0 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5377` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.5377 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.7947` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7947 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.972` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.972 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `16864.0568` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16864.0568 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.6298` → IC=+0.146 (n=204)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.6298 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.1521` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1521 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `274.0` → IC=+0.147 (n=134)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 274.0 (IC base=+0.053)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.259 (n=110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.277 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0039 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1004` → IC=+0.272 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1004 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.291 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` > `0.7838` → IC=+0.329 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7838 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` > `0.1626` → IC=+0.316 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1626 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.535` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.535 (IC base=+0.258)

- **PATRÓN** `volumen_regimen` < `0.6827` → IC=+0.270 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6827 (IC base=+0.258)

- **PATRÓN** `volumen_regimen` > `1.1837` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1837 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.0936` → IC=+0.389 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0936 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.3667` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3667 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.5338` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5338 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.098` → IC=+0.200 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.098 (IC base=+0.027)

- **PATRÓN** `libro_liquidez` > `9336.2451` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9336.2451 (IC base=+0.027)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4524` → IC=-0.240 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4524
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=98)

- **FILTRO** `dist_vwap_pct` > `0.2318` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2318
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=125)

- **FILTRO** `volumen_pendiente_norm` > `0.2195` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2195
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=108)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.178 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 14.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.123 (n=173)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.5714 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.7416` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7416 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.979` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.979 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.1727` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1727 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.2214` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.2214 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 22.0 (IC base=-0.068)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0159` → IC=+0.205 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0159 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2982` → IC=+0.172 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2982 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.56 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1962` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1962 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.275` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.275 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6571` → IC=+0.178 (n=116)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6571 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.2201` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.2201 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.9259` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.9259 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4996` → IC=+0.157 (n=106)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4996 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.196 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0135 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `1.0608` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0608 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.481` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 8.481 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `0.6173` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6173 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.136 (n=116)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 18.0 (IC base=+0.102)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.202 (n=1858)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=4293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `1.0541` → IC=+0.224 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0541 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.396` → IC=+0.229 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.396 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.156 (n=1900)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8812 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.083` → IC=+0.153 (n=1292)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.083 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.193 (n=1098)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.8815` → IC=+0.172 (n=2514)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8815 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.165 (n=3958)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `3888.0428` → IC=+0.186 (n=1364)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3888.0428 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.213 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.204 (n=2546)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4748` → IC=+0.194 (n=3818)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4748 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=1739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.56` → IC=+0.240 (n=3819)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.56 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.2431` → IC=+0.173 (n=2439)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2431 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.576` → IC=+0.214 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.576 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.68` → IC=+0.189 (n=3579)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.68 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.62` → IC=+0.177 (n=915)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.62 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2374` → IC=+0.248 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2374 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.3234` → IC=+0.195 (n=1411)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.3234 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.173 (n=2691)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 142.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.187 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0052 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.221 (n=303)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.332 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.701` → IC=+0.307 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.701 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2176` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2176 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.5922` → IC=+0.169 (n=258)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5922 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.8937` → IC=+0.179 (n=391)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8937 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.237 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.275 (n=495)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.273 (n=492)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.11` → IC=+0.308 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.11 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.280 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.276 (n=497)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.4058` → IC=+0.305 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4058 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.268` → IC=+0.285 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.268 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `1.5024` → IC=+0.290 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5024 (IC base=+0.271)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.280 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `1899.0172` → IC=+0.277 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1899.0172 (IC base=+0.271)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.263 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 67.0 (IC base=+0.271)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.192 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0029 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.176 (n=223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0068 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.0927` → IC=+0.165 (n=222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0927 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.3257` → IC=+0.209 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3257 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.2354` → IC=+0.212 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2354 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.201 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.384` → IC=+0.168 (n=577)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 4.384 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.2659` → IC=+0.166 (n=665)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2659 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.0975` → IC=+0.171 (n=302)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.0975 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.074` → IC=+0.176 (n=554)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.074 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2078` → IC=+0.192 (n=131)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2078 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.1056` → IC=+0.178 (n=542)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.1056 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.7153` → IC=+0.180 (n=411)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.7153 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `10716.3301` → IC=+0.188 (n=594)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 10716.3301 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `499.0` → IC=+0.174 (n=541)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 499.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.172 (n=622)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0061 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3456` → IC=+0.178 (n=622)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3456 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.175 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.4364` → IC=+0.216 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4364 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.013` → IC=+0.213 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.013 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.6154` → IC=+0.248 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6154 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1411` → IC=+0.241 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1411 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `2.4236` → IC=+0.189 (n=526)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.4236 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.084` → IC=+0.179 (n=238)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.084 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=805)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `11565.2208` → IC=+0.168 (n=414)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 11565.2208 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `285.0` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 285.0 (IC base=+0.168)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.269 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.243 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.6907` → IC=+0.264 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6907 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.364` → IC=+0.336 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.364 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.219` → IC=+0.214 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.219 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.9299` → IC=+0.214 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9299 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.265 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.282 (n=195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.242 (n=265)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.239 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.245 (n=610)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.4138` → IC=+0.298 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4138 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.578` → IC=+0.284 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.578 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2275` → IC=+0.261 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2275 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7067` → IC=+0.276 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7067 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.92` → IC=+0.212 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.92 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.204 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.237)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.155 (n=587)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.007 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.145 (n=596)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.004 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1399` → IC=+0.152 (n=294)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1399 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.161 (n=597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 8.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.7469` → IC=+0.238 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7469 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.377` → IC=+0.180 (n=267)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.377 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.692` → IC=+0.206 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.692 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.9021` → IC=+0.169 (n=445)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.9021 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.2078` → IC=+0.144 (n=223)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.2078 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1047` → IC=+0.230 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1047 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.1579` → IC=+0.208 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1579 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `9611.138` → IC=+0.234 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9611.138 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.155 (n=494)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.4486` → IC=+0.152 (n=561)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4486 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.176 (n=251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6744` → IC=+0.175 (n=561)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6744 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.219` → IC=+0.136 (n=240)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.219 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.341` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.341 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.299` → IC=+0.135 (n=527)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.299 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.0096` → IC=+0.133 (n=494)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.0096 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.1365` → IC=+0.156 (n=187)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.1365 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `2.5341` → IC=+0.169 (n=167)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5341 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `11732.317` → IC=+0.214 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11732.317 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `186.0` → IC=+0.148 (n=424)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 186.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_20min` < `0.4868` → IC=-0.182 (n=237)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4868
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=712)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.146 (n=475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0084 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.136 (n=479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 12.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4868` → IC=+0.186 (n=712)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4868 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.8812` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.8812 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.463` → IC=+0.194 (n=354)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.463 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2968.0664` → IC=+0.254 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.0664 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.155 (n=166)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 33.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.178 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0058 (IC base=+0.107)

- **PATRÓN** `drift_60min` |x|≤ `0.1314` → IC=+0.161 (n=228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1314 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.191 (n=684)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` < `0.2907` → IC=+0.130 (n=565)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.2907 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.187` → IC=+0.128 (n=668)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.187 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.7076` → IC=+0.136 (n=300)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.7076 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.147 (n=219)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `1.4441` → IC=+0.139 (n=178)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4441 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2648.2907` → IC=+0.166 (n=309)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2648.2907 (IC base=+0.107)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.028` → IC=+0.249 (n=269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.028 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.9389` → IC=+0.291 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9389 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `1.3244` → IC=+0.278 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3244 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.12` → IC=+0.246 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.12 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` > `0.6868` → IC=+0.206 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6868 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.268 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `1.4495` → IC=+0.197 (n=756)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4495 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.201 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.287 (n=294)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.231 (n=295)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.658` → IC=+0.218 (n=880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.658 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.217 (n=826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.222 (n=926)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.493` → IC=+0.268 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.493 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.1798` → IC=+0.225 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1798 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.98` → IC=+0.298 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.98 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `1.2298` → IC=+0.243 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2298 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.302 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.4651` → IC=+0.207 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4651 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.194 (n=605)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 35.0 (IC base=+0.216)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=1612)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.135 (n=1148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0102 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.4418` → IC=+0.137 (n=1148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4418 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.139 (n=447)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 4.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.9237` → IC=+0.193 (n=435)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.9237 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.514` → IC=+0.163 (n=200)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 10.514 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.04` → IC=+0.129 (n=1331)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 6.04 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.8876` → IC=+0.130 (n=611)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.8876 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.1742` → IC=+0.164 (n=352)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1742 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4629` → IC=+0.157 (n=430)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4629 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.3856` → IC=+0.152 (n=585)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.3856 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `9099.4108` → IC=+0.132 (n=591)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 9099.4108 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.188 (n=408)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0037 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.497` → IC=+0.151 (n=1221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.497 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.161 (n=417)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 4.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.2027` → IC=+0.159 (n=537)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.2027 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.7395` → IC=+0.135 (n=217)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.7395 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.261` → IC=+0.142 (n=1220)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.261 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.2234` → IC=+0.139 (n=1189)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2234 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.147` → IC=+0.133 (n=1215)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.147 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0688` → IC=+0.146 (n=586)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0688 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.4869` → IC=+0.142 (n=1209)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4869 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.7932` → IC=+0.136 (n=806)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.7932 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=1612)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `5356.8505` → IC=+0.140 (n=1221)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 5356.8505 (IC base=+0.130)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.471` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.471
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.129 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 15.0 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.6469` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.6469 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.471` → IC=+0.141 (n=179)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.471 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.8077` → IC=+0.129 (n=103)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.8077 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.2086` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.2086 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `12680.3815` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 12680.3815 (IC base=+0.089)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.185 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0035 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.0862` → IC=+0.157 (n=202)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0862 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.156 (n=213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.1706` → IC=+0.172 (n=266)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1706 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.6484` → IC=+0.179 (n=82)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6484 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.34` → IC=+0.148 (n=603)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.34 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1904` → IC=+0.140 (n=604)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1904 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.0643` → IC=+0.164 (n=284)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0643 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.155 (n=201)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.794` → IC=+0.130 (n=401)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.794 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `11193.0875` → IC=+0.129 (n=604)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 11193.0875 (IC base=+0.123)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.225 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.187 (n=132)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0104 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.5484` → IC=+0.163 (n=286)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.5484 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.260 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.9565` → IC=+0.276 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9565 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.706` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.706 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.232` → IC=+0.160 (n=257)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.232 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.163 (n=262)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.6484` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.6484 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `3.5724` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 3.5724 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `1844.889` → IC=+0.167 (n=256)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1844.889 (IC base=+0.155)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.161 (n=213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0052 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.4835` → IC=+0.147 (n=482)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4835 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.176 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.147 (n=168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 4.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.7912` → IC=+0.170 (n=219)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.7912 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.9851` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.9851 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.2362` → IC=+0.141 (n=410)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2362 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.953` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 9.953 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.008` → IC=+0.143 (n=485)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 7.008 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.7271` → IC=+0.154 (n=212)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7271 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.175` → IC=+0.160 (n=145)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.175 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.424` → IC=+0.169 (n=158)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.424 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.8309` → IC=+0.145 (n=316)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8309 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `8385.7236` → IC=+0.143 (n=482)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 8385.7236 (IC base=+0.132)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.161 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0088 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.5091` → IC=+0.188 (n=370)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.5091 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.161 (n=249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 11.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.1164` → IC=+0.158 (n=369)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.1164 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.412` → IC=+0.153 (n=381)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.412 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.012` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.012 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.164 (n=370)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2227 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.7262` → IC=+0.148 (n=330)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7262 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.147` → IC=+0.154 (n=374)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.147 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.183` → IC=+0.176 (n=319)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.183 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.5267` → IC=+0.163 (n=324)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5267 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `8160.4392` → IC=+0.155 (n=369)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8160.4392 (IC base=+0.142)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=67)

- **FILTRO** `dist_vwap_pct` < `0.7269` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7269
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=27)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.341` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 2.341 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.1303` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1303 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` > `0.7269` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.7269 (IC base=+0.016)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0108` → IC=-0.293 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0108
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=171)

- **FILTRO** `ibs_20min` > `0.113` → IC=-0.174 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` > 0.113
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=32)

- **FILTRO** `dist_vwap_pct` > `0.1153` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1153
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=68)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.218 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.6869` → IC=+0.258 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6869 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.3638` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3638 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.1959` → IC=+0.169 (n=158)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1959 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.902` → IC=+0.260 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.902 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6313` → IC=+0.174 (n=87)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6313 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `0.5769` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.5769 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.0856` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0856 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.3826` → IC=+0.298 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3826 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2340.5972` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2340.5972 (IC base=+0.105)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7892` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7892
  - _Potencial_: sin este filtro IC_bueno=+0.243 (n=72)

- **FILTRO** `sigma_h` > `0.0047` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.231 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.1037` → IC=+0.237 (n=17)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1037 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.134 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 17.0 (IC base=+0.112)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.150 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` > `0.7892` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7892 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.232` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.232 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.5947` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.5947 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` < `0.0779` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0779 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.1451` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1451 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.9335` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9335 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `1.6307` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6307 (IC base=+0.112)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=47)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.199 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.157 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 7.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.6789` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6789 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.4736` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4736 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1383` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1383 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8141` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8141 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.5463` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5463 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.0998` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0998 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.5019` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5019 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2520.3298` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2520.3298 (IC base=+0.143)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=64)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=43)

- **FILTRO** `volumen_regimen` > `0.8778` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8778
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.230 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.75 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.492` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.492 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.36` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.36 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `0.8458` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.8458 (IC base=+0.031)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0032` → IC=-0.308 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0032
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=50)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.443 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=67)

- **FILTRO** `libro_liquidez` < `2177.7794` → IC=-0.308 (n=50)

  - _Acción_: SKIP cuando `libro_liquidez` < 2177.7794
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=50)

- **FILTRO** `dist_vwap_pct` > `0.3683` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3683
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=84)

- **FILTRO** `volumen_spike_ratio` > `1.4137` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4137
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=6)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.233 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=23)

- **FILTRO** `sigma_h` < `0.0031` → IC=-0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0031
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `dist_vwap_pct` > `0.0802` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0802
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=18)

- **FILTRO** `volumen_regimen` > `0.6161` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.6161
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0064` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ibs_20min` < `0.5833` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `ibs_20min` < `0.7391` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.6119` → IC=-0.236 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6119
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=153)

- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.173 (n=47)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=143)

- **PATRÓN** `ibs_20min` > `0.6119` → IC=+0.132 (n=153)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.6119 (IC base=+0.039)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.4444` → IC=+0.128 (n=143)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.4444 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.753` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 5.753 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `3314.3277` → IC=+0.129 (n=95)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3314.3277 (IC base=+0.052)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `sigma_h` < `0.0017` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0017
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **FILTRO** `ibs_20min` < `0.5739` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5739
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=47)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0035 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.259 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.2693` → IC=+0.175 (n=75)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.2693 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.924` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.924 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.5657` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5657 (IC base=+0.114)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=31)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.085)

- **PATRÓN** `drift_60min` |x|≤ `0.1478` → IC=+0.139 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1478 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6645` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6645 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.413` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 7.413 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8554 (IC base=+0.065)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1333` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1333
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `dist_vwap_pct` > `0.1937` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1937
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=32)

- **FILTRO** `volumen_regimen` < `0.9057` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9057
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=24)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0046 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.1849` → IC=+0.136 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1849 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.7895` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7895 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.201` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 4.201 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.088)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.088)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2499.3327` → IC=+0.138 (n=139)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2499.3327 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.136 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 18.0 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2469.9192` → IC=+0.146 (n=156)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2469.9192 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2499.3327` → IC=+0.138 (n=139)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2499.3327 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.136 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 18.0 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2469.9192` → IC=+0.146 (n=156)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2469.9192 (IC base=+0.107)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `12.0` → IC=-0.210 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=106)

- **FILTRO** `libro_liquidez` < `2136.6655` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 2136.6655
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=157)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `libro_liquidez` < `11811.9773` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 11811.9773
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=937)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=47)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35093.65` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `liq_usd_total` < 35093.65
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **PATRÓN** `liq_usd_total` > `55522.43` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `liq_usd_total` > 55522.43 (IC base=+0.004)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.004)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9215` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9215
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=67)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=299)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=369)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=52)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.7335` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.7335
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=51)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=52)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` > `0.56` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=124)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.141 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=82)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=27)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=90)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=35)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=40)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=308)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=654)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=711)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1713` → IC=-0.130 (n=117)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1713
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=235)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.184 (n=1274)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=3870)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.189 (n=1345)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=4041)

- **FILTRO** `ibs_20min` > `0.27` → IC=-0.155 (n=1341)

  - _Acción_: SKIP cuando `ibs_20min` > 0.27
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=4045)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.261 (n=178)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=577)

- **FILTRO** `ibs_20min` < `0.722` → IC=-0.247 (n=188)

  - _Acción_: SKIP cuando `ibs_20min` < 0.722
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=567)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.200 (n=211)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=672)

- **FILTRO** `ballena_activa_n` > `64.0` → IC=-0.147 (n=219)

  - _Acción_: SKIP cuando `ballena_activa_n` > 64.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=664)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=848)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.205 (n=266)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=544)

- **FILTRO** `ibs_20min` < `0.7196` → IC=-0.186 (n=202)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7196
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=608)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.232 (n=222)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=675)

- **FILTRO** `ibs_20min` > `0.7304` → IC=-0.203 (n=224)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7304
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=673)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.176 (n=220)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=674)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.185 (n=220)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=676)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.148 (n=234)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=636)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.193 (n=210)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=681)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.203 (n=200)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=632)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=817)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.225 (n=205)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=679)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `15.0` → IC=-0.357 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=139)

- **FILTRO** `hora_utc` > `19.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=147)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=150)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=414)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=420)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.259 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `libro_liquidez` < `15251.0076` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 15251.0076
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `ibs_20min` < `0.7743` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7743
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=66)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=3696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=8988)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.286 (n=3135)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=9549)

- **FILTRO** `ibs_7min` < `0.711` → IC=-0.248 (n=3169)

  - _Acción_: SKIP cuando `ibs_7min` < 0.711
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=9515)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.173 (n=4245)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=8439)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.222 (n=3726)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=12279)

- **FILTRO** `ibs_7min` > `0.7273` → IC=-0.169 (n=3990)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=12015)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.165 (n=550)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=1273)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.328 (n=441)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=1382)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.273 (n=601)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1222)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.238 (n=441)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=1382)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.140 (n=1824)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=967)

- **FILTRO** `drift_7min_pct` |x|> `0.115` → IC=-0.131 (n=948)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.115
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1843)

- **FILTRO** `ibs_7min` > `0.8367` → IC=-0.182 (n=697)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8367
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2094)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.147 (n=533)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=1862)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.266 (n=567)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=1828)

- **FILTRO** `ibs_7min` < `0.7717` → IC=-0.192 (n=598)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7717
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=1797)

- **FILTRO** `ballena_activa_n` > `164.0` → IC=-0.194 (n=596)

  - _Acción_: SKIP cuando `ballena_activa_n` > 164.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=1799)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.226 (n=601)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1833)

- **FILTRO** `ballena_activa_n` > `105.0` → IC=-0.180 (n=824)

  - _Acción_: SKIP cuando `ballena_activa_n` > 105.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1610)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.198 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=1407)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.313 (n=607)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1265)

- **FILTRO** `ibs_7min` < `0.7151` → IC=-0.269 (n=616)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7151
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1256)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.243 (n=457)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=1415)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.227 (n=669)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=2168)

- **FILTRO** `ibs_7min` > `0.8113` → IC=-0.173 (n=707)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8113
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2130)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.143 (n=659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=1509)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.261 (n=533)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1635)

- **FILTRO** `ibs_7min` < `0.7527` → IC=-0.195 (n=542)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7527
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=1626)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.188 (n=722)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=1446)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.233 (n=714)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1461)

- **FILTRO** `ibs_7min` > `0.2764` → IC=-0.186 (n=543)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2764
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=1632)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.184 (n=539)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=1636)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.243 (n=569)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1796)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.212 (n=591)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=1774)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.194 (n=567)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1798)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.176 (n=743)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2238)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.126 (n=666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=1395)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.299 (n=511)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1550)

- **FILTRO** `ibs_7min` < `0.7309` → IC=-0.247 (n=515)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7309
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1546)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.227 (n=499)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=1562)

- **FILTRO** `libro_liquidez` < `2671.2242` → IC=-0.138 (n=1360)

  - _Acción_: SKIP cuando `libro_liquidez` < 2671.2242
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=701)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.248 (n=566)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=2221)

- **FILTRO** `ibs_7min` > `0.7907` → IC=-0.157 (n=695)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7907
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2092)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.106` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.106
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=414)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.418` → IC=+0.159 (n=326)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.418 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.145 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.177 (n=156)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 451.687 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=219)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3276.3563` → IC=+0.144 (n=189)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3276.3563 (IC base=+0.127)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.220 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `total_vol_5m` < `600.958` → IC=+0.128 (n=100)

  - _Acción_: Kelly boost +0.64€ cuando `total_vol_5m` < 600.958 (IC base=+0.119)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3977` → IC=+0.139 (n=81)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3977 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2091.1708` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2091.1708 (IC base=+0.100)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4115` → IC=+0.179 (n=54)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.4115 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.122 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 12.0 (IC base=+0.109)

- **PATRÓN** `total_vol_5m` < `707.9675` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `total_vol_5m` < 707.9675 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `7409.4986` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7409.4986 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 153.0 (IC base=+0.109)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4012` → IC=+0.212 (n=71)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4012 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.200 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.177)

- **PATRÓN** `total_vol_5m` < `6300.756` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `total_vol_5m` < 6300.756 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2684.6484` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2684.6484 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 73.0 (IC base=+0.177)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.133 (n=77)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.130 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 18.0 (IC base=+0.105)

- **PATRÓN** `total_vol_5m` < `356326.0` → IC=+0.145 (n=74)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 356326.0 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.148 (n=69)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 58.0 (IC base=+0.105)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `3.7615` → IC=-0.395 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7615
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=107)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0079` → IC=-0.329 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=35)

- **FILTRO** `T_h` > `87.9756` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `T_h` > 87.9756
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.300 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.129)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `291.9853` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `T_h` < 291.9853
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0097` → IC=-0.196 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `143.1616` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `T_h` > 143.1616
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=132)

- **FILTRO** `pct_vs_K` |x|> `4.5` → IC=-0.205 (n=59)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.5
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=116)

- **FILTRO** `T_h` > `145.7462` → IC=-0.392 (n=35)

  - _Acción_: SKIP cuando `T_h` > 145.7462
  - _Potencial_: sin este filtro IC_bueno=-0.332 (n=111)

- **FILTRO** `pct_vs_K` |x|> `4.3806` → IC=-0.461 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.3806
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=97)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `1.2216` → IC=-0.182 (n=42)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.2216
  - _Potencial_: sin este filtro IC_bueno=+0.283 (n=21)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.300 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **PATRÓN** `T_h` < `87.9853` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9853 (IC base=-0.023)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8662` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 0.8662 (IC base=-0.023)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.4552` → IC=-0.375 (n=22)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4552
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=25)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.2492` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2492 (IC base=+0.384)

- **PATRÓN** `T_h` > `1.4884` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4884 (IC base=+0.384)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.467 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.384)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `6.0` → IC=-0.227 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=60)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=118)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.145 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.049)

- **PATRÓN** `streak_estiramiento` < `0.4302` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4302 (IC base=+0.038)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=74)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=77)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` < `2.0` → IC=-0.214 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=121)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=121)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=156)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=236)

- **PATRÓN** `streak_estiramiento` < `0.291` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.291 (IC base=+0.043)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=484)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=237)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=326)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=1467)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=831)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=839)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.162 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0041 (IC base=+0.122)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.154 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0064 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1662` → IC=+0.128 (n=398)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1662 (IC base=+0.122)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0649` → IC=+0.132 (n=452)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0649 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.157 (n=202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `ibs_15` > `0.566` → IC=+0.211 (n=452)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.566 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.4139` → IC=+0.182 (n=108)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4139 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.353` → IC=+0.226 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.353 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=482)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `8988.4246` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8988.4246 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 51.0 (IC base=+0.122)

### UPDOWN_GBM#5min
- **FILTRO** `ibs_15` < `0.2963` → IC=-0.158 (n=159)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2963
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=477)

- **FILTRO** `sigma_ewma_delta_pct` > `6.623` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.623
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=583)

### UPDOWN_GBM#60min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0732` → IC=-0.250 (n=22)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0732
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=67)

- **FILTRO** `ibs_15` < `0.1725` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=57)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0047` → IC=-0.149 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=106)

- **FILTRO** `ibs_15` > `0.6105` → IC=-0.153 (n=47)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.6105
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=94)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.196 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0048 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.1916` → IC=+0.197 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1916 (IC base=+0.169)

- **PATRÓN** `drift_15min` |x|≤ `0.4558` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `drift_15min` |x|≤ 0.4558 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.201 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.174 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_15` > `0.8791` → IC=+0.275 (n=87)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8791 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.3217` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3217 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.118` → IC=+0.178 (n=88)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.118 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.220 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.21` → IC=+0.176 (n=140)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 23.21 (IC base=+0.169)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` > `0.0048` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `ibs_15` < `0.1461` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1461
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=55)

### UPDOWN_GBM#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `25.64` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 25.64 (IC base=+0.007)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5728` → IC=-0.257 (n=35)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5728
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=108)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2488` → IC=+0.158 (n=36)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.2488 (IC base=+0.072)

- **PATRÓN** `ibs_15` > `0.5728` → IC=+0.182 (n=108)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.5728 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.072)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `dist_vwap_pct` > `0.1505` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1505
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=84)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `drift_15min` |x|> `0.5033` → IC=-0.155 (n=140)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5033
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=421)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.4444` → IC=-0.237 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.196 (n=54)

- **PATRÓN** `ibs_15` > `0.4444` → IC=+0.196 (n=54)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.4444 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.141` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.141 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `2991.1392` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2991.1392 (IC base=+0.089)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0185` → IC=-0.214 (n=33)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0185
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=66)

- **FILTRO** `drift_60min` |x|> `0.6605` → IC=-0.157 (n=33)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6605
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=66)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=76)

- **FILTRO** `ibs_15` < `0.25` → IC=-0.300 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=76)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.027)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.176 (n=35)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.88€ cuando `ibs_15` > 0.6 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.3805` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.3805 (IC base=+0.027)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0571` → IC=+0.161 (n=116)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.0571 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.173 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.109)

- **PATRÓN** `ibs_15` > `0.5676` → IC=+0.189 (n=104)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.94€ cuando `ibs_15` > 0.5676 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.3587` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3587 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.845` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.845 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=118)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2479.6478` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2479.6478 (IC base=+0.109)

- **PATRÓN** `ibs_15` < `0.1304` → IC=+0.169 (n=140)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` < 0.1304 (IC base=+0.031)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.391 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.326)

- **PATRÓN** `drift_60min` |x|≤ `0.1141` → IC=+0.348 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1141 (IC base=+0.326)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.329 (n=185)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.326)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.354 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.326)

- **PATRÓN** `ibs_15` > `0.8299` → IC=+0.374 (n=165)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8299 (IC base=+0.326)

- **PATRÓN** `dist_vwap_pct` > `0.2982` → IC=+0.366 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2982 (IC base=+0.326)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.08` → IC=+0.332 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.08 (IC base=+0.326)

- **PATRÓN** `sigma_ewma_delta_pct` < `22.686` → IC=+0.328 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 22.686 (IC base=+0.326)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.329 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `8147.128` → IC=+0.360 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8147.128 (IC base=+0.326)

- **PATRÓN** `ballena_activa_n` < `528.0` → IC=+0.377 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 528.0 (IC base=+0.326)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.325 (n=95)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.312)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.316 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.368 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.312)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.344 (n=94)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.312)

- **PATRÓN** `drift_15min` |x|≤ `0.376` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.376 (IC base=+0.312)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1021` → IC=+0.316 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1021 (IC base=+0.312)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.109` → IC=+0.423 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.109 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.360 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.312)

- **PATRÓN** `ibs_15` > `0.8418` → IC=+0.357 (n=96)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8418 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.778` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.778 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.509` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.509 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `11204.8499` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11204.8499 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `625.0` → IC=+0.417 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 625.0 (IC base=+0.312)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.338 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.368 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.338)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.370 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.338)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1288` → IC=+0.370 (n=52)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1288 (IC base=+0.338)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2029` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2029 (IC base=+0.338)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.340 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.338)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.342 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.338)

- **PATRÓN** `ibs_15` > `0.743` → IC=+0.412 (n=78)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.743 (IC base=+0.338)

- **PATRÓN** `dist_vwap_pct` < `0.3157` → IC=+0.347 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3157 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.338)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.88` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.88 (IC base=+0.338)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.338)

- **PATRÓN** `libro_liquidez` > `3288.4647` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3288.4647 (IC base=+0.338)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 168.0 (IC base=+0.338)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0106` → IC=-0.200 (n=311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=934)

- **FILTRO** `ibs_15` < `0.4775` → IC=-0.241 (n=110)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4775
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=331)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.133 (n=317)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=928)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.297` → IC=+0.147 (n=148)

  - _Acción_: Kelly boost +0.73€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.297 (IC base=-0.069)

- **PATRÓN** `ibs_15` > `0.4775` → IC=+0.173 (n=331)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.86€ cuando `ibs_15` > 0.4775 (IC base=-0.069)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0853` → IC=+0.237 (n=321)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0853 (IC base=-0.068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0943` → IC=+0.250 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0943 (IC base=-0.068)

- **PATRÓN** `ibs_15` < `0.3519` → IC=+0.287 (n=360)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3519 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.7799` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7799 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2669` → IC=+0.224 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2669 (IC base=-0.068)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.223 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=-0.068)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.236 (n=206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=620)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.226 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=554)

- **FILTRO** `hora_utc` > `17.0` → IC=-0.225 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=650)

- **FILTRO** `sigma_ewma_delta_pct` > `19.475` → IC=-0.252 (n=155)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.475
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=671)

- **FILTRO** `libro_liquidez` < `15957.1513` → IC=-0.215 (n=545)

  - _Acción_: SKIP cuando `libro_liquidez` < 15957.1513
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=281)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.127 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.003 (IC base=+0.022)

- **PATRÓN** `ibs_15` > `0.5837` → IC=+0.250 (n=34)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5837 (IC base=+0.022)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.5006` → IC=-0.292 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5006
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=155)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=189)

- **PATRÓN** `drift_60min` |x|≤ `0.0629` → IC=+0.222 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0629 (IC base=+0.067)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.347` → IC=+0.210 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.347 (IC base=+0.067)

- **PATRÓN** `ibs_15` > `0.5006` → IC=+0.188 (n=155)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.94€ cuando `ibs_15` > 0.5006 (IC base=+0.067)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.067)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.266 (n=186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.4492` → IC=+0.239 (n=186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4492 (IC base=+0.223)

- **PATRÓN** `drift_15min` |x|≤ `0.594` → IC=+0.230 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.594 (IC base=+0.223)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0648` → IC=+0.234 (n=186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0648 (IC base=+0.223)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.095` → IC=+0.239 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.095 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.230 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.300 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_15` < `0.3707` → IC=+0.287 (n=186)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3707 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.8488` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8488 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.219` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.219 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.717` → IC=+0.251 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.717 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `13721.2442` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13721.2442 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `184.0` → IC=+0.230 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 184.0 (IC base=+0.223)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1657` → IC=-0.170 (n=104)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1657
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=204)

- **FILTRO** `drift_15min` |x|> `0.8298` → IC=-0.256 (n=76)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8298
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=232)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=114)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=194)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.222 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.119)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0746` → IC=+0.153 (n=70)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.0746 (IC base=-0.050)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1752` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1752 (IC base=-0.050)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.228 (n=79)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.050)

- **PATRÓN** `dist_vwap_pct` < `0.2889` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2889 (IC base=-0.050)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 38.0 (IC base=-0.050)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0225` → IC=-0.269 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0225
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=224)

- **FILTRO** `drift_15min` |x|> `1.1577` → IC=-0.244 (n=84)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.1577
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=255)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.241 (n=83)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=256)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0862` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0862 (IC base=-0.066)

- **PATRÓN** `ibs_15` < `0.1277` → IC=+0.289 (n=55)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1277 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.3273` → IC=+0.328 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.3273 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1973` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1973 (IC base=-0.066)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.066)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.291 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.287 (n=139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0543` → IC=+0.327 (n=102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0543 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1335` → IC=+0.300 (n=203)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1335 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1069` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1069 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.321 (n=277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8341` → IC=+0.314 (n=305)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8341 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.3131` → IC=+0.346 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3131 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.899` → IC=+0.289 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 18.899 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.290 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `13625.3561` → IC=+0.337 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13625.3561 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.288 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.290 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.300 (n=153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `0.4172` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4172 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1342` → IC=+0.305 (n=116)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1342 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.310 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.968` → IC=+0.342 (n=80)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.968 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.3306` → IC=+0.363 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3306 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.121` → IC=+0.289 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.121 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `15468.9258` → IC=+0.350 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15468.9258 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.298 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.292 (n=118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0041 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0655` → IC=+0.333 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0655 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0501` → IC=+0.298 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0501 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1043` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1043 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.337 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8661` → IC=+0.326 (n=119)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8661 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.0921` → IC=+0.323 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0921 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.157` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.157 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` < `25.276` → IC=+0.304 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 25.276 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `195.0` → IC=+0.311 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 195.0 (IC base=+0.291)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0825` → IC=-0.275 (n=69)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0825
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=136)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.170 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.174` → IC=-0.123 (n=59)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.174
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=60)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `63.9936` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9936 (IC base=+0.100)

- **PATRÓN** `ratio` < `0.9922` → IC=+0.348 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.100)

- **PATRÓN** `T_h` > `146.0287` → IC=+0.422 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0287 (IC base=+0.343)

- **PATRÓN** `ratio` > `1.0104` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0104 (IC base=+0.343)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `63.9997` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `T_h` < 63.9997 (IC base=+0.085)

- **PATRÓN** `ratio` < `0.973` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.085)

- **PATRÓN** `T_h` < `87.9882` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9882 (IC base=+0.276)

- **PATRÓN** `ratio` > `1.0104` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0104 (IC base=+0.276)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `63.9918` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9918 (IC base=+0.143)

- **PATRÓN** `ratio` < `0.9766` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9766 (IC base=+0.143)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.324 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.313)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.313)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `127.3918` → IC=+0.429 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 127.3918 (IC base=+0.411)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0061 (IC=+0.214 n=19). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.566 sube el IC de +0.122 a +0.211 en UPDOWN_GBM#15min (n=452). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8791 sube el IC de +0.169 a +0.275 en UPDOWN_GBM#BTC#15min (n=87). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5728 sube el IC de +0.072 a +0.182 en UPDOWN_GBM#ETH#15min (n=108). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.089 a +0.196 en UPDOWN_GBM#SOL#15min (n=54). Ya aplicado como kelly_boost=+0.98€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5676 sube el IC de +0.109 a +0.189 en UPDOWN_GBM#XRP#15min (n=104). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1304 sube el IC de +0.031 a +0.169 en UPDOWN_GBM#XRP#15min (n=140). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#60min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.027 a +0.176 en UPDOWN_GBM#SOL#60min (n=35). Ya aplicado como kelly_boost=+0.88€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.4775 sube el IC de -0.069 a +0.173 en UPDOWN_GBM_15M_TARDIO (n=331). Ya aplicado como kelly_boost=+0.86€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3519 sube el IC de -0.068 a +0.287 en UPDOWN_GBM_15M_TARDIO (n=360). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.5837 sube el IC de +0.022 a +0.250 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5006 sube el IC de +0.067 a +0.188 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=155). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3707 sube el IC de +0.223 a +0.287 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=186). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.119 a +0.222 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.050 a +0.228 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=79). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1277 sube el IC de -0.066 a +0.289 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS > 0.3273 sube el IC de -0.066 a +0.328 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=27). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8341 sube el IC de +0.287 a +0.314 en UPDOWN_GBM_IBS_ALTO (n=305). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.968 sube el IC de +0.281 a +0.342 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=80). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8661 sube el IC de +0.291 a +0.326 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=119). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8299 sube el IC de +0.326 a +0.374 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=165). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8418 sube el IC de +0.312 a +0.357 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=96). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.743 sube el IC de +0.338 a +0.412 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=78). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.361 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.361 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `BALLENAS_CONFIRMADAS_15M#XRP#15min` — IC=+0.147 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `BALLENAS_CONFIRMADAS_15M#XRP` — IC=+0.147 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN` — IC=+0.210 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC#5min` — IC=+0.210 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC` — IC=+0.210 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#5min` — IC=+0.210 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 718 | +0.094 | +38.15€ | 1 | 12 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 718 | +0.094 | +38.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 7 | +0.058 | +3.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 7 | +0.058 | +3.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 457 | +0.117 | +26.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 457 | +0.117 | +26.77€ | 3 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 32 | +0.147 | +9.06€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 32 | +0.147 | +9.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 13597 | -0.107 | -2302.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 908 | -0.003 | -129.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 12689 | -0.114 | -2172.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1757 | -0.073 | -333.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1757 | -0.073 | -333.06€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 908 | -0.003 | -129.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 908 | -0.003 | -129.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1753 | -0.156 | -526.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1753 | -0.156 | -526.89€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 3715 | -0.060 | -347.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 3715 | -0.060 | -347.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 3010 | -0.120 | -309.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 3010 | -0.120 | -309.36€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2454 | -0.187 | -656.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2454 | -0.187 | -656.37€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 3126 | -0.061 | +1358.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 884 | -0.006 | +449.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 2242 | -0.083 | +908.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 3126 | -0.061 | +1358.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 884 | -0.006 | +449.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 2242 | -0.083 | +908.41€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 72 | -0.122 | -20.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 72 | -0.122 | -20.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 72 | -0.122 | -20.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 72 | -0.122 | -20.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 43799 | +0.113 | -2853.75€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 7473 | +0.186 | -248.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 136 | -0.101 | -56.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 32599 | +0.097 | -2491.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3591 | +0.118 | -57.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 5480 | +0.076 | -795.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 24 | -0.115 | -1.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 9 | -0.143 | -7.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 5447 | +0.078 | -786.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 8825 | +0.131 | -213.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2169 | +0.200 | -81.86€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 5394 | +0.106 | -161.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1220 | +0.128 | +52.82€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 5489 | +0.081 | -706.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 26 | +0.036 | +0.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#240min | 6 | -0.075 | -4.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 5457 | +0.082 | -702.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 9495 | +0.127 | -136.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2753 | +0.172 | -10.11€ | 1 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 5423 | +0.111 | -88.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1307 | +0.097 | -29.25€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 9039 | +0.127 | -617.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2482 | +0.195 | -154.09€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 64 | +0.000 | -11.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 5429 | +0.097 | -369.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1064 | +0.131 | -81.33€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 5471 | +0.105 | -384.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 19 | -0.023 | -0.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 5449 | +0.105 | -382.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 7434 | +0.177 | -579.84€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 7434 | +0.177 | -579.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1887 | +0.164 | -211.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1887 | +0.164 | -211.19€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 144 | -0.130 | -0.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 144 | -0.130 | -0.72€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1854 | +0.170 | -195.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1854 | +0.170 | -195.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1662 | +0.236 | -42.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1662 | +0.236 | -42.36€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1808 | +0.183 | -143.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1808 | +0.183 | -143.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 372 | +0.444 | +1.82€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 372 | +0.444 | +1.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 141 | +0.437 | -0.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 141 | +0.437 | -0.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 139 | +0.436 | -0.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 139 | +0.436 | -0.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 88 | +0.444 | +2.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 88 | +0.444 | +2.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 23210 | +0.189 | -2179.81€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 23210 | +0.189 | -2179.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 4153 | +0.141 | -696.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 4153 | +0.141 | -696.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 3628 | +0.226 | -125.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 3628 | +0.226 | -125.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 4015 | +0.164 | -534.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 4015 | +0.164 | -534.83€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 3684 | +0.224 | -132.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 3684 | +0.224 | -132.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 3827 | +0.202 | -274.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 3827 | +0.202 | -274.71€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 3903 | +0.182 | -415.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 3903 | +0.182 | -415.45€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 8445 | +0.134 | +323.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 8445 | +0.134 | +323.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 4202 | +0.137 | +184.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 4202 | +0.137 | +184.97€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 4243 | +0.130 | +138.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 4243 | +0.130 | +138.44€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 905 | +0.297 | +0.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 905 | +0.297 | +0.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 391 | +0.279 | -10.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 391 | +0.279 | -10.80€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 423 | +0.305 | +12.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 423 | +0.305 | +12.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 91 | +0.328 | -1.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 91 | +0.328 | -1.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 386 | +0.420 | -12.27€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 386 | +0.420 | -12.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 175 | +0.415 | -7.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 175 | +0.415 | -7.26€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 177 | +0.427 | -4.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 177 | +0.427 | -4.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 34 | +0.361 | -0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 34 | +0.361 | -0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 400 | +0.102 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 129 | +0.080 | -7.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 271 | +0.112 | +7.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 21 | +0.109 | +1.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 21 | +0.109 | +1.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 319 | +0.117 | +10.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 48 | +0.140 | +3.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 271 | +0.112 | +7.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 60 | +0.016 | -11.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 60 | +0.016 | -11.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 12067 | +0.095 | -461.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1107 | +0.074 | -22.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 10960 | +0.097 | -439.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 7401 | +0.098 | -167.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1107 | +0.074 | -22.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 6294 | +0.102 | -144.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 1308 | +0.116 | +24.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 1308 | +0.116 | +24.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 3358 | +0.079 | -319.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 3358 | +0.079 | -319.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 543 | +0.269 | -55.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 543 | +0.269 | -55.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 543 | +0.269 | -55.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 543 | +0.269 | -55.30€ | 0 | 4 |
| ✅ GBM_LATE_15M | 10798 | +0.052 | +4317.80€ | 0 | 13 |
| ✅ GBM_LATE_15M#15min | 10798 | +0.052 | +4317.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1606 | +0.192 | +1140.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1606 | +0.192 | +1140.01€ | 0 | 24 |
| ✅ GBM_LATE_15M#BTC | 1603 | +0.175 | +1034.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1603 | +0.175 | +1034.07€ | 0 | 29 |
| ✅ GBM_LATE_15M#DOGE | 1630 | +0.194 | +1170.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1630 | +0.194 | +1170.51€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 1695 | -0.044 | +70.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1695 | -0.044 | +70.54€ | 4 | 11 |
| ✅ GBM_LATE_15M#SOL | 1815 | -0.051 | +408.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1815 | -0.051 | +408.21€ | 5 | 2 |
| ✅ GBM_LATE_15M#XRP | 2449 | -0.073 | +494.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2449 | -0.073 | +494.47€ | 6 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 11523 | +0.054 | +5271.93€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 11523 | +0.054 | +5271.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1924 | -0.012 | +1013.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1924 | -0.012 | +1013.04€ | 2 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2517 | -0.029 | +290.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2517 | -0.029 | +290.62€ | 1 | 7 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1468 | +0.252 | +1411.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1468 | +0.252 | +1411.87€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1806 | -0.054 | -3.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1806 | -0.054 | -3.62€ | 9 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1914 | -0.025 | +639.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1914 | -0.025 | +639.28€ | 5 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1894 | +0.263 | +1920.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1894 | +0.263 | +1920.73€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 8895 | +0.170 | +6259.60€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 8895 | +0.170 | +6259.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 1238 | +0.198 | +934.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 1238 | +0.198 | +934.01€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1469 | +0.162 | +1016.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1469 | +0.162 | +1016.45€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 1254 | +0.196 | +939.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 1254 | +0.196 | +939.73€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1455 | +0.149 | +907.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1455 | +0.149 | +907.69€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1654 | +0.123 | +1038.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1654 | +0.123 | +1038.88€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1825 | +0.200 | +1422.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1825 | +0.200 | +1422.83€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1915 | +0.096 | +561.00€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1915 | +0.096 | +561.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 58 | +0.083 | +12.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 58 | +0.083 | +12.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 450 | +0.058 | +101.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 450 | +0.058 | +101.91€ | 2 | 8 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 318 | +0.147 | +154.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 318 | +0.147 | +154.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 365 | +0.165 | +143.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 365 | +0.165 | +143.98€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 373 | +0.004 | +21.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 373 | +0.004 | +21.68€ | 3 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 351 | +0.123 | +125.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 351 | +0.123 | +125.65€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO | 10545 | +0.174 | +7479.99€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 10545 | +0.174 | +7479.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1546 | +0.219 | +1285.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1546 | +0.219 | +1285.00€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1714 | +0.163 | +1191.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1714 | +0.163 | +1191.61€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1545 | +0.221 | +1301.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1545 | +0.221 | +1301.70€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1636 | +0.139 | +981.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1636 | +0.139 | +981.56€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1857 | +0.100 | +954.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1857 | +0.100 | +954.73€ | 1 | 17 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2247 | +0.206 | +1765.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2247 | +0.206 | +1765.38€ | 0 | 21 |
| ✅ GBM_LATE_5M | 3365 | +0.128 | +1561.85€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 3365 | +0.128 | +1561.85€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 161 | +0.205 | +120.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 161 | +0.205 | +120.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1010 | +0.117 | +483.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1010 | +0.117 | +483.82€ | 1 | 19 |
| ✅ GBM_LATE_5M#DOGE | 398 | +0.165 | +236.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 398 | +0.165 | +236.83€ | 0 | 11 |
| ✅ GBM_LATE_5M#ETH | 1134 | +0.136 | +529.32€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1134 | +0.136 | +529.32€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 155 | +0.016 | +13.46€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 155 | +0.016 | +13.46€ | 2 | 3 |
| ✅ GBM_LATE_5M#XRP | 507 | +0.109 | +177.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 507 | +0.109 | +177.79€ | 0 | 0 |
| ✅ GBM_LATE_60M | 610 | +0.008 | +179.26€ | 3 | 13 |
| ✅ GBM_LATE_60M#60min | 610 | +0.008 | +179.26€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 211 | +0.045 | +48.24€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 211 | +0.045 | +48.24€ | 2 | 12 |
| ✅ GBM_LATE_60M#ETH | 222 | +0.040 | +87.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 222 | +0.040 | +87.81€ | 1 | 11 |
| ✅ GBM_LATE_60M#SOL | 177 | -0.075 | +43.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 177 | -0.075 | +43.21€ | 3 | 5 |
| 🚫 GBM_LATE_60M_FADE | 204 | -0.296 | -32.54€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 204 | -0.296 | -32.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 82 | -0.250 | -7.73€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 82 | -0.250 | -7.73€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 68 | -0.357 | -20.58€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 68 | -0.357 | -20.58€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 54 | -0.268 | -4.23€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 54 | -0.268 | -4.23€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 394 | +0.045 | +30.65€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 394 | +0.045 | +30.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 169 | +0.044 | +25.39€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 169 | +0.044 | +25.39€ | 3 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 95 | +0.077 | +2.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 95 | +0.077 | +2.03€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 130 | +0.023 | +3.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 130 | +0.023 | +3.22€ | 3 | 6 |
| ✅ LATE_WINDOW_5MIN | 36 | +0.210 | +12.46€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 36 | +0.210 | +12.46€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 36 | +0.210 | +12.46€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 36 | +0.210 | +12.46€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 438 | +0.100 | +110.77€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 438 | +0.100 | +110.77€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 438 | +0.100 | +110.77€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 438 | +0.100 | +110.77€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 300 | -0.086 | -32.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 300 | -0.086 | -32.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 71 | -0.103 | -9.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 71 | -0.103 | -9.18€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 62 | -0.047 | -4.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 62 | -0.047 | -4.85€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 88 | +0.000 | -1.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 88 | +0.000 | -1.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 50 | -0.173 | -9.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 50 | -0.173 | -9.93€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 1133 | -0.015 | -24.04€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1133 | -0.015 | -24.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 65 | -0.022 | -4.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 65 | -0.022 | -4.19€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 146 | -0.034 | -4.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 146 | -0.034 | -4.94€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 87 | -0.096 | -9.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 87 | -0.096 | -9.54€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 345 | +0.013 | +7.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 345 | +0.013 | +7.76€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 409 | -0.001 | -5.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 409 | -0.001 | -5.91€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 81 | -0.078 | -7.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 81 | -0.078 | -7.22€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M | 547 | -0.006 | +1.19€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 547 | -0.006 | +1.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 166 | -0.036 | -9.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 166 | -0.036 | -9.80€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 167 | +0.015 | +4.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 167 | +0.015 | +4.86€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 214 | +0.000 | +6.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 214 | +0.000 | +6.13€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 6240 | -0.003 | -79.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 6240 | -0.003 | -79.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 534 | -0.002 | +3.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 534 | -0.002 | +3.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 646 | -0.012 | -10.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 646 | -0.012 | -10.43€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1401 | +0.008 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1401 | +0.008 | -14.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1396 | +0.002 | +5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1396 | +0.002 | +5.40€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 987 | -0.016 | -33.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 987 | -0.016 | -33.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1276 | -0.006 | -29.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1276 | -0.006 | -29.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 10530 | -0.036 | +404.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 10530 | -0.036 | +404.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1690 | -0.030 | +179.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1690 | -0.030 | +179.62€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1866 | -0.033 | -22.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1866 | -0.033 | -22.92€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1707 | -0.043 | +150.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1707 | -0.043 | +150.03€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1790 | -0.040 | -21.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1790 | -0.040 | -21.63€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1761 | -0.036 | +70.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1761 | -0.036 | +70.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1716 | -0.032 | +48.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1716 | -0.032 | +48.82€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 614 | -0.081 | -54.34€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 614 | -0.081 | -54.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 96 | -0.143 | -13.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 96 | -0.143 | -13.40€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 118 | -0.133 | -15.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 118 | -0.133 | -15.59€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 159 | -0.047 | -7.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 159 | -0.047 | -7.96€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3174 | +0.004 | -4.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3174 | +0.004 | -4.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1163 | +0.008 | +8.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1163 | +0.008 | +8.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1386 | +0.006 | -1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1386 | +0.006 | -1.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 28689 | -0.079 | +561.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 28689 | -0.079 | +561.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 4614 | -0.090 | +401.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 4614 | -0.090 | +401.63€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 4829 | -0.076 | -81.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 4829 | -0.076 | -81.59€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 4709 | -0.084 | +154.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 4709 | -0.084 | +154.93€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 4343 | -0.100 | -231.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 4343 | -0.100 | -231.46€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 5346 | -0.055 | +81.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 5346 | -0.055 | +81.41€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 4848 | -0.071 | +237.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 4848 | -0.071 | +237.03€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6063 | -0.011 | -117.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6063 | -0.011 | -117.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1224 | +0.000 | -13.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1224 | +0.000 | -13.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1321 | -0.001 | -10.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1321 | -0.001 | -10.31€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 796 | -0.015 | -17.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 796 | -0.015 | -17.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 728 | -0.021 | -24.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 728 | -0.021 | -24.07€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 690 | +0.110 | +219.99€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 554 | +0.122 | +207.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 132 | +0.119 | +55.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 132 | +0.119 | +55.17€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 108 | +0.100 | +26.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 108 | +0.100 | +26.44€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 108 | +0.109 | +38.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 108 | +0.109 | +38.36€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 94 | +0.177 | +57.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 94 | +0.177 | +57.07€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 112 | +0.105 | +30.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 112 | +0.105 | +30.35€ | 0 | 5 |
| ✅ PRICE_TARGET_GBM | 327 | -0.126 | -14.43€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 142 | -0.201 | -34.46€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 112 | -0.263 | -36.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 30 | +0.031 | +1.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 124 | -0.103 | -0.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 87 | -0.129 | -7.25€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 37 | -0.038 | +7.13€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 61 | +0.008 | +20.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 44 | -0.022 | +13.06€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 17 | +0.067 | +7.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 243 | -0.173 | -30.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 84 | +0.012 | +15.98€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 321 | -0.218 | -8.08€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 137 | -0.169 | -7.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 113 | -0.152 | -6.07€ | 2 | 2 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 24 | -0.231 | -1.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 119 | -0.285 | -21.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 97 | -0.308 | -25.66€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 22 | -0.167 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 65 | -0.187 | +20.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 52 | -0.185 | +16.98€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 13 | -0.108 | +3.57€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 262 | -0.220 | -14.76€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 59 | -0.205 | +6.68€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 92 | +0.362 | +34.82€ | 0 | 3 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 23 | +0.340 | +5.79€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 23 | +0.340 | +5.79€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 52 | +0.481 | +31.97€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 52 | +0.481 | +31.97€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 92 | +0.362 | +34.82€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 221 | +0.043 | +4.50€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 221 | +0.043 | +4.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 95 | +0.057 | +3.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 95 | +0.057 | +3.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 17 | +0.067 | +2.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 17 | +0.067 | +2.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 23 | +0.060 | -0.57€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 23 | +0.060 | -0.57€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 86 | +0.011 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 86 | +0.011 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1691 | -0.027 | -81.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1691 | -0.027 | -81.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 661 | -0.013 | -18.18€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 661 | -0.013 | -18.18€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 553 | -0.026 | -25.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 553 | -0.026 | -25.13€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 141 | -0.038 | -12.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 141 | -0.038 | -12.96€ | 2 | 0 |
| ✅ STREAK_FADE_5M#XRP | 336 | -0.050 | -25.38€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 336 | -0.050 | -25.38€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 43 | -0.011 | -1.01€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 43 | -0.011 | -1.01€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 26 | -0.107 | -3.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 26 | -0.107 | -3.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 3442 | +0.029 | +75.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 3442 | +0.029 | +75.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1128 | +0.025 | +14.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1128 | +0.025 | +14.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 682 | +0.048 | +33.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 682 | +0.048 | +33.87€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 1027 | +0.018 | +4.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1027 | +0.018 | +4.88€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 605 | +0.030 | +22.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 605 | +0.030 | +22.37€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 3889 | +0.011 | -25.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3889 | +0.011 | -25.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1486 | +0.015 | -5.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1486 | +0.015 | -5.90€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1540 | +0.017 | -1.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1540 | +0.017 | -1.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 863 | -0.005 | -17.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 863 | -0.005 | -17.78€ | 2 | 0 |
| ✅ UPDOWN_GBM | 8425 | +0.006 | +194.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2990 | +0.036 | +266.21€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 341 | +0.007 | -0.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 4535 | -0.011 | -67.51€ | 2 | 0 |
| ✅ UPDOWN_GBM#60min | 512 | +0.000 | -2.80€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 196 | +0.091 | +38.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 8 | -0.040 | -1.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1726 | +0.017 | +89.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 314 | +0.085 | +64.73€ | 2 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 103 | +0.062 | +7.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1117 | +0.001 | +20.51€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 174 | -0.011 | -4.92€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 915 | -0.008 | -7.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 126 | +0.086 | +24.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 780 | -0.024 | -32.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1876 | -0.003 | -7.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 881 | +0.015 | +18.17€ | 1 | 3 |
| ✅ UPDOWN_GBM#ETH#240min | 96 | +0.041 | +2.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 661 | -0.032 | -27.66€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 223 | +0.007 | -0.84€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 2412 | +0.000 | -1.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 777 | -0.001 | +2.09€ | 1 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 88 | -0.011 | -3.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1420 | +0.003 | -3.54€ | 4 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 115 | +0.004 | +2.96€ | 0 | 3 |
| ✅ UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 1298 | +0.012 | +85.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 713 | +0.048 | +114.29€ | 0 | 8 |
| ✅ UPDOWN_GBM#XRP#240min | 37 | -0.167 | -7.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 548 | -0.022 | -21.39€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 245 | +0.326 | +59.80€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 245 | +0.326 | +59.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 142 | +0.312 | +25.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 142 | +0.312 | +25.25€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 103 | +0.338 | +34.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 103 | +0.338 | +34.55€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 5148 | -0.068 | +1143.04€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 5148 | -0.068 | +1143.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 305 | -0.051 | +341.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 305 | -0.051 | +341.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1046 | -0.155 | -89.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1046 | -0.155 | -89.80€ | 5 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 80 | +0.049 | +9.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 80 | +0.049 | +9.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 453 | +0.153 | +227.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 453 | +0.153 | +227.71€ | 2 | 17 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1684 | -0.063 | +333.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1684 | -0.063 | +333.01€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1580 | -0.088 | +321.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1580 | -0.088 | +321.14€ | 3 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 42 | +0.023 | -0.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 42 | +0.023 | -0.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 42 | +0.023 | -0.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 42 | +0.023 | -0.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 406 | +0.287 | +321.53€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 406 | +0.287 | +321.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 231 | +0.281 | +177.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 231 | +0.281 | +177.49€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 175 | +0.291 | +144.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 175 | +0.291 | +144.04€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 631 | -0.096 | -70.68€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 631 | -0.096 | -70.68€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 310 | -0.077 | -35.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 310 | -0.077 | -35.00€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 157 | -0.041 | -7.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 157 | -0.041 | -7.21€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 31 | -0.197 | -6.72€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 31 | -0.197 | -6.72€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 52 | -0.148 | -7.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 52 | -0.148 | -7.02€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 48 | -0.180 | -7.92€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 48 | -0.180 | -7.92€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1302 | +0.292 | +566.93€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 411 | +0.219 | +19.52€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 424 | +0.272 | +119.01€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 467 | +0.372 | +428.39€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.088) — sin ventaja clara. oversold(IBS<0.3): IC=+0.023 n=3021 | neutral: IC=-0.000 n=3279 | overbought(IBS>0.7): IC=+0.088 n=3288
  - _Datos_: n=9976 IC=+0.038 PNL=+971.99€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 326s) 98 celda(s) GATE OK de 2373 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.001 < 0.08 — monitorear
  - _Datos_: n=777 IC=-0.001 PNL=+2.09€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=424/15 IC=+0.272 PNL=+119.01€ | BTC: n=411/15 IC=+0.219 PNL=+19.52€ | SOL: n=467/15 IC=+0.372 PNL=+428.39€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.070 n=138823 | tras_1loss IC=+0.048 n=109146 | tras_2loss IC=+0.010 n=49334/40 | gap=+0.059 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 20 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC
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
  - _Estado_: 8363 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.082 n=53/60 | contraria IC=+0.062 n=30 | gap=+0.019 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=137, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 94 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=223/40 IC=+0.007 PNL=-0.84€ | BTC#60min: n=174/40 IC=-0.011 PNL=-4.92€ | SOL#60min: n=115/40 IC=+0.004 PNL=+2.96€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.001 n=841 | contrario_BTC IC=-0.016 n=680/40 | gap=-0.015 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.195 > 0.08 con n=80 PNL=+51.91€
  - _Datos_: n=80 IC=+0.195 PNL=+51.91€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.145 > 0.08 con n=108 PNL=+34.13€
  - _Datos_: n=108 IC=+0.145 PNL=+34.13€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 22/25 ops en el filtro definido (IC actual=+0.250 PNL=+16.04€)
  - _Datos_: n=22 IC=+0.250 PNL=+16.04€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=1105 PNL=+573.42€
  - _Datos_: n=1105 IC=+0.335 PNL=+573.42€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=74 IC=+0.053 PNL=+13.80€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=74 IC=+0.053 PNL=+13.80€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 26/30 ops en el filtro definido (IC actual=+0.214 PNL=+19.08€)
  - _Datos_: n=26 IC=+0.214 PNL=+19.08€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=8148 IC=+0.003 PNL=+141.23€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=8148 IC=+0.003 PNL=+141.23€

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
  - _Estado_: n=423 IC=+0.013 PNL=+2.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=423 IC=+0.013 PNL=+2.74€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=89 IC=-0.060 PNL=-5.54€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=89 IC=-0.060 PNL=-5.54€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=149 IC=-0.030 PNL=-1.68€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=149 IC=-0.030 PNL=-1.68€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.1 con n=602 PNL=+168.55€
  - _Datos_: n=602 IC=+0.122 PNL=+168.55€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=194 IC=+0.076 PNL=+41.53€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=194 IC=+0.076 PNL=+41.53€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=314 IC=+0.085 PNL=+64.73€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=314 IC=+0.085 PNL=+64.73€

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
  - _Estado_: n=1732 IC=+0.026 PNL=+123.06€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1732 IC=+0.026 PNL=+123.06€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=32 IC=-0.265 PNL=-8.09€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=32 IC=-0.265 PNL=-8.09€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=93 IC=-0.037 PNL=+6.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=93 IC=-0.037 PNL=+6.73€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=113 IC=+0.039 PNL=+9.48€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=113 IC=+0.039 PNL=+9.48€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 8/15 ops en el filtro definido (IC actual=+0.080 PNL=+2.13€)
  - _Datos_: n=8 IC=+0.080 PNL=+2.13€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2345 IC=-0.021 PNL=-58.71€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2345 IC=-0.021 PNL=-58.71€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=38 PNL=+9.28€
  - _Datos_: n=38 IC=+0.175 PNL=+9.28€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.210 n=36) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=36 IC=+0.210 PNL=+12.46€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=2217 IC=+0.015 PNL=+93.37€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2217 IC=+0.015 PNL=+93.37€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=579 IC=+0.037 PNL=+15.97€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=579 IC=+0.037 PNL=+15.97€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.08 con n=197 PNL=+52.53€
  - _Datos_: n=197 IC=+0.108 PNL=+52.53€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=141 PNL=+7.31€
  - _Datos_: n=141 IC=+0.115 PNL=+7.31€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.142 > 0.08 con n=135 PNL=+49.07€
  - _Datos_: n=135 IC=+0.142 PNL=+49.07€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=26986 IC=+0.102 PNL=+8484.48€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=26986 IC=+0.102 PNL=+8484.48€

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
  - _Estado_: n=1157 IC=+0.029 PNL=+66.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1157 IC=+0.029 PNL=+66.28€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=377 PNL=+135.80€
  - _Datos_: n=377 IC=+0.128 PNL=+135.80€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=127 IC=-0.043 PNL=+34.76€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=127 IC=-0.043 PNL=+34.76€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.445 > 0.1 con n=683 PNL=+602.86€
  - _Datos_: n=683 IC=+0.445 PNL=+602.86€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1908 IC=+0.023 PNL=+122.06€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1908 IC=+0.023 PNL=+122.06€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.1 con n=897 PNL=+341.24€
  - _Datos_: n=897 IC=+0.165 PNL=+341.24€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.211 < -0.1 con n=43 PNL=-2.82€
  - _Datos_: n=43 IC=-0.211 PNL=-2.82€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=559 IC=+0.031 PNL=+58.65€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=559 IC=+0.031 PNL=+58.65€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.1 con n=103 PNL=+18.94€
  - _Datos_: n=103 IC=+0.119 PNL=+18.94€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 2/20 ops en el filtro definido (IC actual=-0.025 PNL=-1.02€)
  - _Datos_: n=2 IC=-0.025 PNL=-1.02€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=6818 IC=-0.147 PNL=+219.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6818 IC=-0.147 PNL=+219.57€

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
  - _Estado_: n=841 IC=+0.145 PNL=+435.58€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=841 IC=+0.145 PNL=+435.58€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.08 con n=583 PNL=+163.69€
  - _Datos_: n=583 IC=+0.124 PNL=+163.69€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=870 IC=-0.003 PNL=-0.06€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=870 IC=-0.003 PNL=-0.06€

**〰️ H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: n=868 IC=+0.079 PNL=+513.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=868 IC=+0.079 PNL=+513.99€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.169 > 0.08 con n=173 PNL=+64.29€
  - _Datos_: n=173 IC=+0.169 PNL=+64.29€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.247 < -0.1 con n=756 PNL=-117.93€
  - _Datos_: n=756 IC=-0.247 PNL=-117.93€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1920 IC=+0.125 PNL=+1014.17€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1920 IC=+0.125 PNL=+1014.17€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.096 > 0.08 con n=45 PNL=+13.21€
  - _Datos_: n=45 IC=+0.096 PNL=+13.21€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=863 IC=-0.019 PNL=+75.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=863 IC=-0.019 PNL=+75.02€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.08 con n=771 PNL=+473.64€
  - _Datos_: n=771 IC=+0.177 PNL=+473.64€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1291 IC=-0.066 PNL=+263.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1291 IC=-0.066 PNL=+263.13€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.08 con n=295 PNL=-37.93€
  - _Datos_: n=295 IC=+0.116 PNL=-37.93€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.230 > 0.08 con n=1901 PNL=-194.26€
  - _Datos_: n=1901 IC=+0.230 PNL=-194.26€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 15/40 ops en el filtro definido (IC actual=-0.022 PNL=+2.89€)
  - _Datos_: n=15 IC=-0.022 PNL=+2.89€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.107 n=232) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=232 IC=+0.107 PNL=+60.71€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.321 > 0.08 con n=93 PNL=+53.19€
  - _Datos_: n=93 IC=+0.321 PNL=+53.19€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.426 n=268) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=268 IC=+0.426 PNL=+369.33€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=4153 IC=+0.141 PNL=-696.63€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=4153 IC=+0.141 PNL=-696.63€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.241 > 0.1 con n=56 PNL=+38.56€
  - _Datos_: n=56 IC=+0.241 PNL=+38.56€
