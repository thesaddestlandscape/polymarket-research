# Plan Live Trading — Polymarket Bot
**Última actualización: 2026-06-25**

---

## Estado actual

El bot está en **shadow mode** — predice y registra resultados sin dinero real.
Objetivo para activar live: **IC ≥ 0.10 con n ≥ 50** en alguna estrategia confirmada.

| Estrategia | IC actual | n | ¿Lista? |
|---|---|---|---|
| UPDOWN_GBM #BTC#15min | +0.106 | 31 | ⚠️ IC sí, n casi |
| UPDOWN_GBM #15min global | +0.070 | 98 | ⚠️ n suficiente, IC bajo |
| ORDER_FLOW_5M | +0.033 | 585 | ❌ IC insuficiente |

---

## Circuito completo del dinero

```
════════════════════════════════════════════════════════
                   CIRCUITO COMPLETO
════════════════════════════════════════════════════════

        TU DINERO FIAT
    Coinbase (€ → USDC)
              │
              ▼
   ┌─────────────────────┐
   │   WALLET TRADING    │  20€ operativos
   │   (bot tiene clave) │  Polygon / MetaMask
   └─────────────────────┘
              │
              ▼
         POLYMARKET
      (bot opera aquí)
              │
         ganancias
              │
              ▼
   ┌─────────────────────┐
   │   WALLET AHORRO     │  Solo tú accedes
   │   (bot NO accede)   │  Polygon / MetaMask
   └─────────────────────┘
              │
              ▼
       USDC → BITCOIN
    (Coinbase o swap directo
     sin KYC via Uniswap)
              │
              ▼
   ┌─────────────────────┐
   │    RESERVA BTC      │  Reserva de valor
   │    (wallet fría)    │  No tocar salvo necesidad
   └─────────────────────┘
              │
              │  cuando necesitas liquidez
              ▼
    Vender BTC en Coinbase
    al cambio del momento
              │
              ▼
        € a cuenta bancaria
              │
              ▼
    Gastas con tarjeta normal

════════════════════════════════════════════════════════
  ⚠️  FISCAL: cada venta de BTC → declarar ganancia
      en IRPF (precio venta - precio compra)
════════════════════════════════════════════════════════
```

---

## Checklist de setup — pasos pendientes

```
[ ] 1. Instalar MetaMask (metamask.io — verificar URL oficial)
[ ] 2. Guardar seed phrase (12 palabras) en papel físico, NUNCA digital
[ ] 3. Añadir red Polygon en MetaMask
        - RPC: https://polygon-rpc.com
        - Chain ID: 137
[ ] 4. Crear DOS wallets en MetaMask
        - Wallet 1: TRADING  (el bot tendrá la clave privada)
        - Wallet 2: AHORRO   (solo tú, nunca en el bot)
[ ] 5. Comprar 30€ de USDC en Coinbase
[ ] 6. Retirar USDC a Wallet TRADING — red Polygon (NO Ethereum)
[ ] 7. Conectar al VPS via SSH para crear cuenta Polymarket
        - Abrir cmd en Windows
        - Comando: ssh root@2a01:4f9:c014:df39::1
        - Contraseña: la de Hetzner
[ ] 8. Crear cuenta Polymarket desde IP finlandesa (VPS Helsinki)
[ ] 9. Completar KYC en Polymarket
[ ] 10. Depositar USDC desde Wallet TRADING a Polymarket
[ ] 11. Añadir credenciales al bot
        - POLYMARKET_PRIVATE_KEY en data/live/.env (nunca en git)
[ ] 12. Activar live mode cuando IC esté confirmado
        - Comando: bash live_switch.sh on
```

---

## Infraestructura técnica

### VPS
- **Proveedor**: Hetzner Online GmbH
- **Ubicación**: Helsinki, Finlandia
- **IP**: 2a01:4f9:c014:df39::1
- **Relevancia**: IP finlandesa — Polymarket accesible (España bloqueada desde mayo 2026)

### Situación regulatoria en España
- **DGOJ** (mayo 2026): bloqueó Polymarket via ISPs españoles (Vodafone, Telefónica, Orange)
- Clasificación: juego de azar sin licencia española
- **Finlandia**: no bloqueada — el VPS opera sin restricción
- Acceso a Polymarket: siempre desde el VPS, nunca desde IP española

### Acceso SSH desde Windows
```bash
# En cmd de Windows:
ssh root@2a01:4f9:c014:df39::1

# Para navegar por Polymarket desde IP finlandesa (SOCKS proxy):
ssh -D 1080 -N root@2a01:4f9:c014:df39::1
# Luego en Firefox: Preferencias → Red → SOCKS proxy → localhost:1080
```

---

## Sistema de ventanas horarias (live_guard.py)

El bot solo ejecuta trades reales cuando:
1. El switch manual está activado (`bash live_switch.sh on`)
2. **Y** la hora de Madrid está dentro de una ventana

### Ventanas L-V (hora Madrid)
| Ventana | Horario | UTC equivalente |
|---|---|---|
| Apertura europea | 08:30 – 09:30 | 06:30 – 07:30 |
| Media mañana | 10:30 – 11:30 | 08:30 – 09:30 |
| Mediodía | 12:30 – 13:30 | 10:30 – 11:30 |
| Tarde 1 | 16:30 – 17:30 | 14:30 – 15:30 |
| Tarde 2 | 18:30 – 19:30 | 16:30 – 17:30 |
| Cierre | 20:30 – 21:30 | 18:30 – 19:30 |

**Fines de semana**: solo switch manual, sin restricción horaria.

### Comandos de control
```bash
bash live_switch.sh on      # activar
bash live_switch.sh off     # parar inmediatamente
bash live_switch.sh         # ver estado actual
```

---

## Lógica de stake (live_stake.py)

| Parámetro | Valor | Razón |
|---|---|---|
| Capital operativo | 20€ | De los 30€ depositados |
| Reserva intocable | 10€ | Colchón de seguridad |
| Budget diario | 30% del bankroll | ~6€/día con bankroll inicial |
| Máx por trade | 10% del bankroll | Nunca más de 2€ con 20€ |
| Sizing | Half-Kelly | IC × bankroll × 0.5 |
| Mínimo por trade | 0.25€ | Por debajo no compensa fees |
| Máximo por trade | 2.00€ | Cap absoluto |

### Ejemplos con bankroll=20€
| IC confirmado | Stake calculado |
|---|---|
| 0.08 | 0.80€ |
| 0.10 | 1.00€ |
| 0.15 | 1.50€ |
| 0.22+ | 2.00€ (cap) |

---

## Estrategias permitidas en live

Solo operará en estrategias con edge confirmado:
- `UPDOWN_GBM` subtypes: `BTC#15min`, `ETH#15min`, `SOL#15min`, `BTC#60min`, `ETH#60min`
- IC histórico mínimo: **0.08**
- n mínimo: **40 resoluciones**

Configuración en: `data/live/config_live.json`

---

## Compra USDC — ruta desde España

```
Coinbase (cuenta existente)
    │
    ├─ Comprar: 30€ → USDC
    │
    └─ Retirar:
         Dirección: 0x... (Wallet TRADING de MetaMask)
         Red: Polygon  ← CRÍTICO, no Ethereum
         Importe: 30 USDC
```

**Gas fees**: Polymarket tiene trading gasless (no necesitas MATIC para operar).
Opcional: comprar 1€ de MATIC para movimientos manuales de fondos.

---

## Notas importantes

- La **seed phrase** (12 palabras de MetaMask) es lo más valioso. Papel físico, caja fuerte.
- La **clave privada** de la wallet TRADING va en `data/live/.env` (en el VPS, nunca en git).
- El bot tiene acceso **solo** a la wallet de trading, nunca a la de ahorro.
- Cada venta de BTC (incluido swap a euros) es un **hecho imponible** en IRPF España.
- El shadow mode continúa en paralelo aunque el live esté activo — comparación permanente.
