# Polymarket Research

Captura de datos en bruto del mercado de predicción Polymarket en la categoría
cripto, con vistas a un análisis exploratorio posterior y eventual modelado.

## Diseño

Proyecto de investigación observacional. El sistema **no opera, no predice, no
toma decisiones**. Solo registra el estado del mercado a intervalos regulares.

- **`capture_markets.py`** se ejecuta cada 20 minutos. Captura todos los
  eventos activos de Polymarket con el tag oficial `crypto` y sus mercados,
  junto con los precios spot de 18 tickers en Binance.
- **`capture_wallets.py`** se ejecuta cada 2 horas. Captura el top 50 de
  traders mensuales en la categoría CRYPTO (combinación de PNL y volumen,
  pesos 0.6 / 0.4) y sus posiciones actuales en mercados abiertos.

## Endpoints consultados

Todos son endpoints públicos oficiales documentados en
[docs.polymarket.com](https://docs.polymarket.com/api-reference/introduction.md):

- `GET https://gamma-api.polymarket.com/events?tag_slug=crypto&active=true&closed=false&related_tags=true`
  — eventos activos en cripto, incluyendo sub-categorías relacionadas
  (Bitcoin, Ethereum, Solana, etc.). De cada evento extraemos sus mercados.
- `GET https://data-api.polymarket.com/v1/leaderboard?category=CRYPTO&timePeriod=MONTH&orderBy=PNL`
  — ranking mensual por P&L.
- `GET https://data-api.polymarket.com/v1/leaderboard?category=CRYPTO&timePeriod=MONTH&orderBy=VOL`
  — ranking mensual por volumen.
- `GET https://data-api.polymarket.com/positions?user=<address>`
  — posiciones actuales de cada wallet.
- `GET https://api.binance.com/api/v3/ticker/price` — precios spot.

## Estructura de salida

```
data/
├── markets/
│   ├── 2026-06-16.csv      # 1 fila por mercado × captura
│   └── ...
├── prices/
│   ├── 2026-06-16.csv      # precios spot Binance
│   └── ...
└── wallets/
    ├── leaderboard_2026-06-16.csv   # ranking de wallets
    ├── positions_2026-06-16.csv     # posiciones detalladas
    └── ...
```

## Decisiones metodológicas

1. **Identificación de mercados cripto**: usamos el tag oficial `crypto` con
   `related_tags=true`. Esto garantiza paridad con la página
   https://polymarket.com/es/crypto (~318 mercados) sin depender de listas de
   *keywords* hardcodeadas (que perdían tokens nuevos como Hyperliquid,
   MegaETH, Printr, Tea, MicroStrategy, etc.).
2. **Win rate no disponible**: la API pública no expone esta métrica. La
   definición original de "top wallet" (PNL + win rate + volumen) se
   sustituye por una combinación de PNL (peso 0.6) y volumen (peso 0.4)
   sobre el ranking mensual.
3. **Frecuencia**: 20 min para mercados, 2 h para wallets. Combinación
   compatible con el límite de 2000 min/mes de GitHub Actions Free Tier
   en repos privados (consumo estimado ~1440 min/mes, margen del 28%).
4. **Jitter**: GitHub Actions no garantiza ejecución puntual exacta. Cada fila
   incluye `timestamp_utc` con el momento real de la captura, no el programado.
5. **Tolerancia a fallos**: si una API responde con error, el ciclo se
   continúa con las demás. Los huecos se registran en stdout y son visibles
   en la pestaña "Actions" de GitHub.

## Análisis posterior

Tras 3 semanas de captura ininterrumpida (objetivo del estudio), los CSV se
descargan en local y se analizan con scripts separados (no incluidos
todavía en este repo).

## Licencia y citación

Datos públicos. Si reutilizas este dataset, agradezco mención al repositorio.
