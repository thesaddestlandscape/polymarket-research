# PREREG E-RE-CM-03 — ¿persiste el régimen diario del EV maker barato (H50 «operar solo si la población del día anterior gana»)? (ANTES de calcular; manda mtime+sha)
Datos: los de E-RE-CM-02 (cells 06-21 Oct, 5min, tb 1-2, banda 0,05-0,30), grupos BTC y ALT3. Serie diaria EV_d = Σpnl/Σcoste (población, sin rebate).
Prueba: r = Pearson(EV_{d−1}, EV_d) sobre 15 pares por grupo; p por permutación del orden de días (5.000). Política P: operar el día d solo si EV_{d−1} > 0; ΔEV = EV(días operados) − EV(todos), ponderado por €.
Decisión: régimen USABLE si r>0 con p<0,05 en AMBOS grupos y ΔEV>0 en ambos; si no, H50 se cierra con datos de población (16 días; declarado: poca n, 15 pares).
