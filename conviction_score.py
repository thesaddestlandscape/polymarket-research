"""
conviction_score.py — agrega señales de todas las estrategias por mercado.

Para cada mercado con al menos una predicción operable (BUY_YES/BUY_NO),
calcula cuántas estrategias coinciden en la misma dirección y genera un
score de convicción. Los mercados con mayor convicción son los candidatos
prioritarios para el bot real.

Física aplicada:
- Entropía de Shannon: mide desorden entre votos. Entropía baja = consenso = señal fiable.
- Kelly soft switching ya implementado (HMM): conviction × 0.25-Kelly base.

Salida: data/shadow/conviction_YYYY-MM-DD.csv
"""
import csv
import math
import glob
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DIR_SHADOW = Path("data/shadow")
DIR_SHADOW.mkdir(parents=True, exist_ok=True)

N_ESTRATEGIAS = 15  # 14 base + CONSENSUS_TURBO
ACCURACY_PATH = DIR_SHADOW / "strategy_accuracy.csv"
IC_MINIMO_OBSERVACIONES = 10


def cargar_ic_por_estrategia() -> dict:
    """
    IC Bayesiano con Laplace smoothing — activo desde la primera observación.
    No espera N mínimo; la confianza escala con el número de datos.
    """
    if not ACCURACY_PATH.exists():
        return {}
    ic_map = {}
    with open(ACCURACY_PATH, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                n = int(row.get("n_total", 0))
                if n == 0:
                    continue
                aciertos = int(row.get("n_aciertos", 0))
                # IC Bayesiano: prior neutro (50%), actualizado con cada dato
                ic_bayes = (aciertos + 1) / (n + 2) - 0.5
                # Confianza: 0 con n=0, sube a 1.0 en n=20
                confianza = min(1.0, n / 20)
                ic_efectivo = ic_bayes * confianza
                # Peso = 0.5 + IC_efectivo, mínimo 0.05 para no eliminar nunca del todo
                ic_map[row["strategy"]] = max(0.05, round(0.5 + ic_efectivo, 4))
            except (ValueError, TypeError):
                pass
    if not ic_map:
        return {}
    media = sum(ic_map.values()) / len(ic_map)
    return {s: round(v / media, 4) for s, v in ic_map.items()}


def cargar_predicciones_hoy() -> list:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    archivo = DIR_SHADOW / f"predictions_{fecha}.csv"
    if not archivo.exists():
        from datetime import timedelta
        fecha = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
        archivo = DIR_SHADOW / f"predictions_{fecha}.csv"
    if not archivo.exists():
        return []
    with open(archivo, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def calcular_conviction(predicciones: list, ic_pesos: dict | None = None) -> list:
    ultimas = {}
    for p in predicciones:
        clave = (p.get("strategy", ""), p.get("market_id", ""))
        ts = p.get("timestamp_utc", "")
        if clave not in ultimas or ts > ultimas[clave].get("timestamp_utc", ""):
            ultimas[clave] = p
    predicciones = list(ultimas.values())

    por_mercado = defaultdict(lambda: {
        "question": "",
        "end_date": "",
        "horas": None,
        "precio_yes": None,
        "volatilidad": 0.0,
        "votos_yes": [],
        "votos_no": [],
    })

    for p in predicciones:
        dec = p.get("decision", "SKIP")
        if dec not in ("BUY_YES", "BUY_NO"):
            continue
        mid = p.get("market_id", "")
        if not mid:
            continue
        m = por_mercado[mid]
        m["question"] = p.get("question", "")
        m["end_date"] = p.get("end_date", "")
        try:
            m["horas"] = float(p.get("horas_a_vencimiento", 0))
        except (ValueError, TypeError):
            pass
        try:
            m["precio_yes"] = float(p.get("precio_yes_mercado", 0))
        except (ValueError, TypeError):
            pass
        try:
            v = float(p.get("volatilidad", 0) or 0)
            if v > m["volatilidad"]:
                m["volatilidad"] = v
        except (ValueError, TypeError):
            pass

        estrategia = p.get("strategy", "")
        try:
            edge = float(p.get("edge_direccional", 0))
        except (ValueError, TypeError):
            edge = 0.0

        ic_w = (ic_pesos or {}).get(estrategia, 1.0)

        if dec == "BUY_YES":
            m["votos_yes"].append((estrategia, edge, ic_w))
        else:
            m["votos_no"].append((estrategia, edge, ic_w))

    resultados = []
    for mid, m in por_mercado.items():
        n_yes = len(m["votos_yes"])
        n_no = len(m["votos_no"])
        total_votos = n_yes + n_no
        if total_votos == 0:
            continue

        peso_yes = sum(w for _, _, w in m["votos_yes"])
        peso_no  = sum(w for _, _, w in m["votos_no"])

        if peso_yes >= peso_no:
            direccion = "BUY_YES"
            votos_favor = n_yes
            votos_contra = n_no
            peso_favor = peso_yes
            peso_contra = peso_no
            edge_medio = sum(e * w for _, e, w in m["votos_yes"]) / peso_yes if peso_yes else 0
            estrategias_favor = "|".join(s for s, _, _ in m["votos_yes"])
        else:
            direccion = "BUY_NO"
            votos_favor = n_no
            votos_contra = n_yes
            peso_favor = peso_no
            peso_contra = peso_yes
            edge_medio = sum(e * w for _, e, w in m["votos_no"]) / peso_no if peso_no else 0
            estrategias_favor = "|".join(s for s, _, _ in m["votos_no"])

        estable = peso_contra < peso_favor

        total_peso = peso_favor + peso_contra
        p_yes = peso_favor / total_peso if total_peso > 0 else 1.0
        p_no  = peso_contra / total_peso if peso_contra > 0 else 0.0
        entropia = 0.0
        if p_yes > 0: entropia -= p_yes * math.log2(p_yes)
        if p_no  > 0: entropia -= p_no  * math.log2(p_no)
        factor_consenso = round(1.0 - entropia, 4)

        score_votos = peso_favor / N_ESTRATEGIAS
        score_edge = min(1.0, edge_medio / 0.20)
        conviction = round(0.60 * score_votos + 0.25 * score_edge + 0.15 * factor_consenso, 4)

        vol = m["volatilidad"]
        if vol < 0.02:
            factor_vol = 0.8
        elif vol < 0.05:
            factor_vol = 1.0
        elif vol < 0.10:
            factor_vol = 1.3
        else:
            factor_vol = 1.5

        kelly_base = 0.25
        kelly_soft = round(
            kelly_base * conviction * factor_vol * (1.0 if estable else 0.25),
            4
        )
        turbo_activo = "CONSENSUS_TURBO" in estrategias_favor
        kelly_cap = 0.60 if turbo_activo else 0.40
        kelly_soft = min(kelly_soft, kelly_cap)

        resultados.append({
            "market_id": mid,
            "question": m["question"],
            "end_date": m["end_date"],
            "horas_a_vencimiento": round(m["horas"], 1) if m["horas"] else "",
            "precio_yes": round(m["precio_yes"], 4) if m["precio_yes"] else "",
            "direccion": direccion,
            "votos_favor": votos_favor,
            "votos_contra": votos_contra,
            "total_votos": total_votos,
            "edge_medio": round(edge_medio, 4),
            "entropia": round(entropia, 4),
            "factor_consenso": factor_consenso,
            "volatilidad": round(vol, 4),
            "factor_vol": round(factor_vol, 2),
            "conviction_score": conviction,
            "estable": estable,
            "kelly_recomendado": kelly_soft,
            "estrategias": estrategias_favor,
        })

    resultados.sort(key=lambda x: (x["conviction_score"], x["votos_favor"]), reverse=True)
    return resultados


def guardar(resultados: list, ts: str) -> Path:
    fecha = ts[:10]
    archivo = DIR_SHADOW / f"conviction_{fecha}.csv"
    columnas = [
        "timestamp_utc", "market_id", "question", "end_date",
        "horas_a_vencimiento", "precio_yes", "direccion",
        "votos_favor", "votos_contra", "total_votos",
        "edge_medio", "entropia", "factor_consenso",
        "volatilidad", "factor_vol", "conviction_score",
        "estable", "kelly_recomendado", "estrategias",
    ]
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        w.writeheader()
        for r in resultados:
            r["timestamp_utc"] = ts
            w.writerow(r)
    return archivo


def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] === Conviction score ===")

    predicciones = cargar_predicciones_hoy()
    print(f"  Predicciones cargadas: {len(predicciones)}")

    operables = [p for p in predicciones if p.get("decision") in ("BUY_YES", "BUY_NO")]
    print(f"  Operables (BUY_YES/BUY_NO): {len(operables)}")

    ic_pesos = cargar_ic_por_estrategia()
    if ic_pesos:
        print(f"  Pesos IC cargados para {len(ic_pesos)} estrategias:")
        for s, w in sorted(ic_pesos.items(), key=lambda x: -x[1]):
            print(f"    {s:30s}  IC_peso={w:.3f}")
    else:
        print(f"  Sin datos IC suficientes — todos los pesos = 1.0 (modo inicial)")

    resultados = calcular_conviction(predicciones, ic_pesos)
    print(f"  Mercados con ≥1 voto: {len(resultados)}")

    alta = [r for r in resultados if r["votos_favor"] >= 3]
    media = [r for r in resultados if r["votos_favor"] == 2]
    baja = [r for r in resultados if r["votos_favor"] == 1]
    print(f"  Alta convicción (≥3 estrategias): {len(alta)}")
    print(f"  Media convicción (2 estrategias):  {len(media)}")
    print(f"  Baja convicción  (1 estrategia):   {len(baja)}")

    inestables = [r for r in resultados if not r["estable"]]
    print(f"  Inestables (votos_contra >= votos_favor): {len(inestables)}")

    if alta:
        print(f"\n  TOP mercados alta convicción:")
        for r in alta[:5]:
            flag = "" if r["estable"] else " ⚠INEST"
            print(f"    [{r['votos_favor']}/{N_ESTRATEGIAS}] {r['direccion']:8s} "
                  f"score={r['conviction_score']:.3f} "
                  f"H={r['entropia']:.3f} "
                  f"vol={r['volatilidad']:.3f}×{r['factor_vol']} "
                  f"kelly={r['kelly_recomendado']:.4f} "
                  f"edge={r['edge_medio']:.3f} "
                  f"h={r['horas_a_vencimiento']}"
                  f"{flag}  {r['question'][:45]}")

    if resultados:
        archivo = guardar(resultados, ts)
        print(f"\n  Guardado: {archivo} ({len(resultados)} mercados)")

    print(f"[{ts}] === Fin conviction score ===")


if __name__ == "__main__":
    main()
