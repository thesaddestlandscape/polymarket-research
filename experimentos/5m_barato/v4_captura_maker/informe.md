# V4/V3 captura MAKER y TOMADOR con colchón — 20-Oct-2026 (alpha-researcher). EXPLORATORY
Universo y reloj: vigía V4 OOS desde el 06-Oct a las 12Z hasta el 19-Oct (6 monedas) y extracto BTC del 06 al 18-Oct (H23). Desenlace oficial (`maker_ms_desenlaces_cache`, cobertura 230/230). Hora de RECEPCIÓN. EV ponderado por € y con IC90 por días (bootstrap de días). Intermedios en `/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_captura_maker/`; scripts m1_h23_reloj.py, m1_analisis.py, m2_tomador.py y m3_profundidad.py (copiar del scratchpad del alpha-researcher).

## 1. Tomador V4: dónde se pierde
- 62 señales 1.ª (acierto 0,58 frente a un ask de 0,42). A +215 ms se ejecutan 27, con EV +0,170, IC90 por días (−0,44;+0,92) y −0,344 sin los 2 mejores días. Las ejecutadas aciertan 10/27 (37 %, con un precio de ≈0,45). Las no ejecutadas aciertan 72-76 % (B, repreciadas: 18; C, consumidas: 17). Es selección adversa pura.
- A L150 (suelo físico): n=33, EV +0,32, sin los 2 mejores días −0,16. A L250: −0,05. Por moneda, solo BTC es positiva (n=13, +0,93, sin los 2 mejores días −0,16). Las altcoins dan n 1-5 y son negativas salvo DOGE.
- **Colchón de límite (límite FOK = p_limite + k, mismo disparo).** En 10/35 de las perdidas el ask a +215 ms solo subió 1-2c. En BTC, con el tamaño REAL del nivel 1 (m3, filas q del extracto; chequeo de la clase A 11/11): k=0 da n=12, EV +0,98, sin los 2 mejores días −0,10. **k=+0,02 da n=20 en 10 días, EV +1,17, IC90 por días (+0,37;+2,30) y +0,575 sin los 2 mejores días**. Las 8 operaciones añadidas ganan 7. Con las 6 monedas (vigía, profundidad supuesta): +0,52, IC90 (−0,08;+1,21). Se probaron 5 valores de k: exploratorio y sin corrección por multiplicidad. El tamaño de q se registra en cada cambio de precio y puede sobrestimar el disponible (2 casos con exactamente 5 acciones).

## 2. Maker H23: auditoría del reloj (M1, 13 días, BTC)
- delta = rx(print tomador) − rx(caída del bid5): P50 entre −35 y −169 ms por día; el libro llega antes en el 27-39 % de los casos y en el 10-17 % con más de 150 ms.
- Re-simulación adelantando S ms todos los rellenos. S=0 reproduce exactamente el resultado anterior (A join base: n=16, +0,992).
  - **A join base:** de S=50 a S=250 da entre +0,77 y +1,44; IC90 por días >0 en todos; sin los 2 mejores días entre +0,49 y +0,98.
  - B join base: de +0,30 a +0,74; a S=250 el IC cruza 0.
  - **El edge de H23 no es un artefacto del orden libro/print.**
- Control sin cancelar: A +0,061 (n=31) y B +0,303 (sin los 2 mejores días −0,105). Lo que aporta el edge es la cancelación.
- Arnés real actual, join_r (debe esperar 1,5 s antes de volver a pujar): A n=10, +0,595, sin los 2 mejores días −0,035. **La palanca de ingeniería es re-pujar al instante (cancel/replace) en el arnés real.**
- Bucket 0,05: A [0,20-0,30) n=7, +1,75/+2,29; el resto tiene n≤3.
- Capacidad simulada: A 1,23 rellenos/día (+3,4 €/día a 2 €); B 2,0 rellenos/día.

## 3. V3 (bin_ret_5s)
- Como filtro tomador, el corte b5≥−1 sube el acierto de las señales (0,58→0,72) pero baja el relleno (44 %→33 %):
  - V4: n_ejec 13, +0,42, −0,37 sin los 2 mejores días.
  - V2 por mercado: n 34→19, EV +0,43→+0,82, IC90 (−0,05;+1,95), +0,07 sin los 2 mejores días.
- No puede subir n. No tocar V3, que está congelado.
- Aplicado al MAKER (retorno Binance en el segundo previo al relleno, observable):
  - A con ret≥0: +1,81 (n=6); con ret<0: +0,32 (n=10).
  - B: +1,18 (n=12) frente a +0,33 (n=14).
  - Se mantiene con S=100.
  - Es un mecanismo de vendedor informado. Corte post hoc: solo como regla de cancelación a re-simular.

## 4. Preregistro propuesto (ids libres H56-H58; el chief lo copia a REGISTRO)
- **H56 V4-COLCHÓN-2c (tomador)**
  - Regla:
    - Disparo V4 idéntico (margen ≥0,05, lado s, 1.ª señal, recepción).
    - FOK con límite p_limite(0,05)+0,02, enviada a t+215 ms.
    - Acciones max(5, 2/p).
    - BTC; las altcoins con gate propio.
  - Gate:
    - n≥40 ejecutables, ≥10 días y EV ≥+0,10.
    - IC90 por cierre >0 y >0 sin los 2 mejores días.
    - En el subconjunto INCREMENTAL frente a V4 emparejada: n≥15 y EV >0 con IC90 por días >0.
  - Kill: incremental < −0,15 con n≥10.
  - OOS a partir del 21-Oct a las 00Z.
  - Ritmo de ~1,5 eventos/día, por lo que harán falta 25-30 días.
  - Canibaliza parcialmente a H53, que dispara antes con el límite = ask(t).
- **H57 H23-ALTS:** misma regla H23 (join, margen ≥−0,05, cancelación a 60 ms) en ETH/SOL/XRP/DOGE/BNB, con la cola base y el rango [opt, cons] (c 0,97 en las altcoins). DATA_BLOCKED: falta el extracto de altcoins del 06 al 18-Oct (trabajo pesado). Primero replay de descubrimiento y después OOS en h23shadow ampliado. Gate por moneda igual al de H23.
- **H58 H23-CANCEL-BIN1s:** H23 join, cancelando además mientras el retorno Binance a 1 s (rx) orientado a s sea <0, y re-pujando cuando sea ≥0. Antes del OOS: re-simulación 06-18 como REGLA, con la frecuencia del disparo medida y reteniendo ≥60 % de los rellenos H23 (trampa de cancelar siempre = no operar). Gate H23.

## 5. Plan sombra F2 (sin órdenes)
- H56: en el mismo disparo V4, registrar los límites k=0 y k=0,02 y el libro L completo a +215 ms; dos rellenos virtuales emparejados.
- H58: brazo nuevo de h23shadow con Binance aggTrade por recepción.
- H23 real: cancel/replace inmediato en el arnés H47 antes de cualquier micro-orden (/code-review + OK de Javi).

## Viable / no viable
- Viable para probar: el maker H23 join (robusto al reloj) y el tomador con colchón de 2c.
- No viable:
  - el tomador V4 a la latencia actual sin colchón;
  - V3 como filtro tomador para subir n;
  - el join_r actual.
- Contribución a 2 €: H23 A ≈1,2 k€/año simulados y H56 ≈+0,6 k€/año incrementales. Ninguna validada; escalar depende de stake/capital (decisión de Javi).
