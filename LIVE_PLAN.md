# Plan Live Trading — Polymarket Bot
**Última actualización: 2026-06-25 ~12:30 UTC**

---

## Estado del bot (ahora mismo)

Shadow mode activo. Candidatas a live más cercanas:

| Estrategia | IC | n | Faltan |
|---|---|---|---|
| UPDOWN_GBM #60min (global) | +0.105 | 36 | **4 ops** |
| UPDOWN_GBM #BTC#15min | +0.083 | 34 | **6 ops** |
| UPDOWN_GBM #ETH#60min | +0.110 | 15 | 25 ops |

A ritmo actual (~4-6 ops/día en #60min) podría estar lista **mañana o pasado**.
Cuando cruce el umbral, recibirás un aviso por Telegram.

---

## Circuito completo del dinero

```
          ENTRADA
    Coinbase (€ → USDC)
            │
            ▼
   ┌─────────────────────┐
   │  WALLET TRADING     │  ← dirección A (bot tiene la clave)
   │  20€ operativos     │     Polygon / MetaMask
   └─────────────────────┘
            │
       ganancias
            │
            ▼
   ┌─────────────────────┐
   │  WALLET AHORRO      │  ← dirección B (solo tú, bot NO accede)
   │  (nunca en el bot)  │     Polygon / MetaMask, dirección nueva
   └─────────────────────┘
            │
            ▼
     USDC → BITCOIN
   (Coinbase o swap directo
    sin KYC via Uniswap)
            │
            ▼
   ┌─────────────────────┐
   │   RESERVA BTC       │  Reserva de valor, no tocar
   └─────────────────────┘
            │  cuando necesites liquidez
            ▼
    Vender en Coinbase → €
    a tu cuenta bancaria normal

════════════════════════════════
  ⚠️  FISCAL: cada venta de BTC
  = hecho imponible en IRPF
════════════════════════════════
```

---

## Checklist esta tarde — paso a paso

```
[ ] 1. Instalar MetaMask
        → metamask.io (verificar URL oficial)
        → "Crear nueva cartera"
        → Guardar seed phrase (12 palabras) en PAPEL FÍSICO
          NUNCA en digital, nunca en foto, nunca en nube

[ ] 2. Añadir red Polygon en MetaMask
        → Redes → Añadir red → Añadir manualmente:
          Nombre:   Polygon
          RPC:      https://polygon-rpc.com
          Chain ID: 137
          Símbolo:  MATIC
          Explorer: https://polygonscan.com

[ ] 3. Crear DOS cuentas en MetaMask
        → Cuenta 1: "Trading" (usará el bot)
        → Cuenta 2: "Ahorro"  (solo tú, dirección diferente)
        → Copiar la dirección 0x... de "Trading"

[ ] 4. Abrir cmd en Windows y conectar al VPS
        → Escribir: ssh root@2a01:4f9:c014:df39::1
        → Contraseña: la de Hetzner
        → Aparece: root@servidor:~#

[ ] 5. Abrir Firefox con proxy Helsinki para crear cuenta Polymarket
        → Abrir otra ventana de cmd:
          ssh -D 1080 -N root@2a01:4f9:c014:df39::1
        → Firefox → Ajustes → Configuración de red
          → Configuración manual → SOCKS v5
          → localhost  puerto: 1080
        → Ir a polymarket.com → Crear cuenta → Conectar MetaMask
        → Verificar IP en whatismyip.com (debe ser Finlandia)

[ ] 6. Comprar 30 USDC en Coinbase
        → Coinbase → Comprar → USDC → 30€

[ ] 7. Retirar USDC a MetaMask wallet "Trading"
        → Coinbase → Enviar → USDC
        → RED: Polygon  ← CRÍTICO (no Ethereum)
        → Dirección: tu 0x... de MetaMask Trading
        → Cantidad: 30 USDC

[ ] 8. Verificar que llegan los fondos
        → MetaMask → Red Polygon → ver saldo USDC
        → O en polygonscan.com buscando tu dirección

[ ] 9. Depositar en Polymarket
        → polymarket.com → Depositar → conectar MetaMask
        → 20 USDC al capital operativo
        → 10 USDC quedan en MetaMask como reserva
```

---

## Acceso SSH — recordatorio

```bash
# Conectar al VPS (ventana 1 — para gestionar el bot)
ssh root@2a01:4f9:c014:df39::1

# Proxy para navegar con IP finlandesa (ventana 2 — dejar abierta)
ssh -D 1080 -N root@2a01:4f9:c014:df39::1

# Ver estado del bot
bash live_switch.sh

# Activar live trading cuando esté listo
bash live_switch.sh on
```

---

## Privacidad — plan mínimo razonable

**Principio**: cada propósito, una dirección distinta.

| Dirección | Uso | Vinculada a ti |
|---|---|---|
| Trading (A) | Bot opera aquí, fondeable desde Coinbase | Sí (via Coinbase KYC) |
| Ahorro (B) | Recibe ganancias, compra BTC | No directamente |

- Nunca mezcles Trading y Ahorro en la misma dirección
- Cuando haya beneficios reales, usar ruta sin KYC para Ahorro (cajero BTC efectivo o P2P)
- Para esta fase inicial (30€) Coinbase → Trading es suficiente y legal

---

## Control live trading

**Ventanas horarias L-V (hora Madrid):**
08:30-09:30 | 10:30-11:30 | 12:30-13:30 | 16:30-17:30 | 18:30-19:30 | 20:30-21:30

**Fines de semana:** solo switch manual

**Comandos Telegram** (desde el móvil, directo al bot):
```
/on      → activa el bot
/off     → para el bot
/status  → estado completo
```

**Circuit breakers automáticos:**
- Bankroll < 5€ → se apaga solo
- Pérdida diaria > 15% → para el día
- Pérdida en una ventana > 20% → para esa ventana

---

## Lo que falta para el primer trade real

```
[✅] Bot shadow funcionando y acumulando datos
[✅] Sistema live completo (ventanas, stake, circuit breakers)
[✅] Control Telegram (/on /off /status)
[✅] Notificaciones automáticas
[ ] MetaMask instalado con 2 wallets         ← esta tarde
[ ] 30 USDC en wallet Trading vía Polygon    ← esta tarde
[ ] Cuenta Polymarket creada desde Helsinki  ← esta tarde
[ ] Credenciales CLOB API en data/live/.env  ← tras crear cuenta
[ ] Primera estrategia cruzando umbral live  ← muy próximo (#60min)
```
