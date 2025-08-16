# Pong Game - Plan de Implementación

## Objetivo
Crear el juego clásico Pong en un solo archivo HTML con JavaScript vanilla, compatible con desktop y mobile.

## Características del juego
- Dos paletas (jugador vs CPU o jugador vs jugador)
- Pelota que rebota con física realista
- Sistema de puntuación (primero en llegar a X puntos)
- Diferentes niveles de dificultad de CPU
- Efectos visuales y sonoros
- Modo multijugador local

## Estructura técnica

### Canvas
- Tamaño: 800x400px (responsive)
- Campo de juego con línea central punteada
- Paletas en los extremos izquierdo y derecho
- Marcador en la parte superior

### Controles
- **Desktop**: 
  - Jugador 1: W/S o flechas arriba/abajo
  - Jugador 2: I/K o mouse
- **Mobile**: 
  - Controles táctiles virtuales
  - Gestos de deslizamiento

### Física del juego
1. **Pelota**
   - Velocidad constante con aceleración gradual
   - Ángulo de rebote basado en punto de impacto
   - Rebote en paredes superior e inferior
   - Reset al centro después de punto

2. **Paletas**
   - Movimiento vertical limitado al campo
   - Velocidad constante de movimiento
   - Colisión precisa con la pelota

3. **CPU (Inteligencia Artificial)**
   - Seguimiento de pelota con delay realista
   - Diferentes niveles de dificultad
   - Errores ocasionales para jugabilidad

### Mecánicas del juego
1. **Modos de juego**
   - Jugador vs CPU
   - Jugador vs Jugador (local)
   - Práctica (pelota infinita)

2. **Puntuación**
   - Primer jugador en llegar a 5, 10 o 15 puntos
   - Puntos por pelota que pasa la paleta contraria

3. **Dificultad CPU**
   - Fácil: CPU lenta, muchos errores
   - Medio: CPU moderada, algunos errores
   - Difícil: CPU rápida, pocos errores
   - Imposible: CPU perfecta

## Implementación por pasos

### Paso 1: Estructura base
- Canvas y sistema de renderizado
- Clases Paddle, Ball, Game
- Loop principal del juego

### Paso 2: Física básica
- Movimiento de pelota
- Rebotes en paredes
- Colisión pelota-paleta

### Paso 3: Controles de jugador
- Input de teclado
- Movimiento de paletas
- Controles táctiles para mobile

### Paso 4: CPU/AI
- Algoritmo de seguimiento
- Niveles de dificultad
- Comportamiento realista

### Paso 5: Sistema de puntuación
- Detección de puntos
- Marcador visual
- Condiciones de victoria

### Paso 6: Modos de juego
- Selección de modo
- Configuración de partida
- Menús y navegación

### Paso 7: Polish y efectos
- Efectos visuales
- Animaciones
- Responsive design

## Elementos visuales

### Estilo clásico
- Fondo negro
- Elementos blancos
- Línea central punteada
- Fuente pixelada/retro

### Efectos visuales
- Trail de la pelota
- Partículas en colisiones
- Flash en puntuación
- Animaciones de entrada/salida

### Responsive design
- Escalado proporcional del canvas
- Controles adaptativos
- UI optimizada para mobile

## Parámetros de juego
```javascript
const GAME_CONFIG = {
    canvas: { width: 800, height: 400 },
    paddle: { width: 10, height: 80, speed: 5 },
    ball: { size: 10, baseSpeed: 4, maxSpeed: 8 },
    scoring: { winScore: 5 },
    cpu: {
        easy: { speed: 3, errorRate: 0.3 },
        medium: { speed: 4, errorRate: 0.15 },
        hard: { speed: 5, errorRate: 0.05 },
        impossible: { speed: 6, errorRate: 0 }
    }
};
```

## Algoritmo de CPU
```javascript
function updateCPU() {
    const targetY = ball.y - paddle.height / 2;
    const diff = targetY - cpu.paddle.y;
    
    // Add difficulty-based error
    if (Math.random() < difficulty.errorRate) {
        return; // Skip this frame
    }
    
    // Move towards target with speed limit
    if (Math.abs(diff) > difficulty.speed) {
        cpu.paddle.y += Math.sign(diff) * difficulty.speed;
    } else {
        cpu.paddle.y = targetY;
    }
}
```

## Física de rebote
```javascript
function calculateBounceAngle(paddle, ball) {
    const relativeIntersectY = (paddle.y + paddle.height/2) - ball.y;
    const normalizedIntersect = relativeIntersectY / (paddle.height/2);
    const bounceAngle = normalizedIntersect * Math.PI/4; // Max 45 degrees
    
    return {
        x: Math.cos(bounceAngle) * ball.speed,
        y: Math.sin(bounceAngle) * ball.speed
    };
}
```

## Estados del juego
- **MENU**: Selección de modo y configuración
- **PLAYING**: Juego activo
- **PAUSED**: Juego pausado
- **POINT_SCORED**: Animación de punto
- **GAME_OVER**: Fin de partida

## Archivos a crear
- `pong/index.html` - Juego completo
- `pong/instrucciones.md` - Manual del juego

## Criterios de éxito
- Física de rebote realista y predecible
- CPU con comportamiento natural
- Controles responsivos en desktop y mobile
- Diferentes niveles de dificultad balanceados
- Interfaz clara y retro
- Performance estable (60fps)
- Multijugador local funcional