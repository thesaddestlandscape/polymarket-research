# PREREG E1D-FORWARD-R1 (24-Oct-2026 ~11:28Z) — forward pasivo de «no operar en ventanas tranquilas» (R1), única regla que pasó E1D
Regla congelada: para cada mercado 5m ETH/SOL/XRP, en su apertura t0 = fin−300 s, R1 = desviación típica (bps) de los retornos logarítmicos de 10 s del último
aggTrade Binance de su moneda (recepción c[7]) en [t0−900 s, t0]. Corte c1 = tercil 1/3 de R1 sobre TODAS las ventanas de los días anteriores (expansivo desde
el 05-Oct, como en E1D). Si R1 ≤ c1 → NO operar esa ventana (ni pujar). Código: e1d_pob.py (R1) + e1d_eval.py (walk-forward), sin cambiar nada.
Datos forward: días ≥ 24-Oct del archivo VOL/m5_registro (extractor diario 03:45) con desenlace oficial gamma closed=true (cobertura ≈100 %, reportarla),
rellenos de bid poblacionales banda 0,10-0,30 (convención E1D). Si hay rellenos propios (B, dry-run H47 seco o similar) se aplica igual, descriptivo hasta n≥150.
Gate (una hipótesis, alfa 0,05 una cola), TODO a la vez, con ≥10 días nuevos (≈ 03-Nov-2026):
1. EXCESO (vs saltar al azar la misma fracción de ventanas dentro del día, 2000) > 0 con p < 0,05 e IC90 por cierre > 0.
2. ΔPnL vs «operar siempre» > 0; EXCESO > 0 sin los 2 mejores días; ≥ 60 % de días con EXCESO > 0; INVERSIÓN (saltar el tercil alto) < 0.
3. Control de huecos: mismo signo excluyendo ventanas con >5 % de puntos Binance de más de 10 s.
4. Por moneda: ETH y SOL con EV del tercil saltado < EV del resto (XRP no se exige: en E1D sin gradiente).
Pasar NO autoriza dinero real: con propios n≥150 y ΔPnL>0 → propuesta con /code-review + OK Javi para aplicarla como filtro de ventana en B.
