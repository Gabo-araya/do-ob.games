# Breakout Game - Plan de Implementación

## Objetivo
Crear el juego clásico Breakout en un solo archivo HTML con JavaScript vanilla, compatible con desktop y mobile.

## Características del juego
- Paleta controlada por el jugador en la parte inferior
- Pelota que rebota destruyendo bloques
- Grid de bloques de colores con diferentes puntuaciones
- Física de rebote realista con ángulos variables
- Power-ups que caen de bloques especiales
- Múltiples niveles con patrones de bloques únicos

## Estructura técnica

### Canvas
- Tamaño: 800x600px (responsive)
- Paleta en la parte inferior
- Grid de bloques en la parte superior
- Área de juego en el medio

### Controles
- **Desktop**: 
  - Flechas izquierda/derecha o A/D
  - Mouse para movimiento preciso
  - Espacio para lanzar pelota
- **Mobile**: 
  - Botones virtuales izquierda/derecha
  - Deslizar dedo para mover paleta
  - Tap para lanzar

### Lógica del juego
1. **Paleta**
   - Movimiento horizontal suave
   - Rebote de pelota con ángulo variable
   - Diferentes zonas de rebote (centro vs extremos)

2. **Pelota**
   - Física de rebote en paredes y objetos
   - Velocidad constante con aceleración opcional
   - Ángulo de rebote basado en punto de impacto

3. **Bloques**
   - Grid configurable (típicamente 8x10)
   - Diferentes tipos con resistencia variable
   - Algunos bloques requieren múltiples golpes
   - Bloques especiales con power-ups

### Mecánicas del juego
- **Objetivo**: Destruir todos los bloques destructibles
- **Vidas**: 3 pelotas iniciales
- **Power-ups**: Mejoras temporales que caen de bloques
- **Niveles**: Patrones de bloques progresivamente más difíciles

## Implementación por pasos

### Paso 1: Estructura base
- Canvas y sistema de renderizado
- Clases Paddle, Ball, Block, PowerUp
- Loop principal del juego

### Paso 2: Paleta y controles
- Movimiento de paleta
- Input de mouse y teclado
- Controles táctiles para mobile

### Paso 3: Física de la pelota
- Movimiento y rebotes básicos
- Colisión con paredes
- Lanzamiento desde paleta

### Paso 4: Sistema de bloques
- Grid de bloques
- Detección de colisiones pelota-bloque
- Destrucción y puntuación

### Paso 5: Física avanzada
- Ángulos de rebote variables
- Rebote en paleta con efecto
- Prevención de bucles infinitos

### Paso 6: Power-ups
- Sistema de power-ups que caen
- Diferentes tipos de mejoras
- Efectos temporales

### Paso 7: Niveles y progresión
- Múltiples patrones de bloques
- Aumento de dificultad
- Transiciones entre niveles

## Tipos de bloques

### Bloques básicos
```javascript
const BLOCK_TYPES = {
    red: { hits: 1, points: 7, color: '#ff0000' },
    orange: { hits: 1, points: 5, color: '#ffa500' },
    yellow: { hits: 1, points: 3, color: '#ffff00' },
    green: { hits: 1, points: 1, color: '#00ff00' },
    blue: { hits: 2, points: 10, color: '#0000ff' },
    purple: { hits: 2, points: 15, color: '#800080' },
    silver: { hits: 3, points: 25, color: '#c0c0c0', indestructible: false },
    gold: { hits: 0, points: 50, color: '#ffd700', indestructible: true }
};
```

### Power-ups
```javascript
const POWERUPS = {
    expand: { 
        effect: 'expandPaddle', 
        duration: 10000, 
        color: '#00ff00',
        symbol: '↔️'
    },
    shrink: { 
        effect: 'shrinkPaddle', 
        duration: 10000, 
        color: '#ff0000',
        symbol: '↔️'
    },
    multiball: { 
        effect: 'addBalls', 
        duration: 0, 
        color: '#ffff00',
        symbol: '⚪'
    },
    slowball: { 
        effect: 'slowBall', 
        duration: 8000, 
        color: '#0000ff',
        symbol: '🐌'
    },
    fastball: { 
        effect: 'fastBall', 
        duration: 8000, 
        color: '#ff00ff',
        symbol: '⚡'
    },
    extralife: { 
        effect: 'addLife', 
        duration: 0, 
        color: '#ffd700',
        symbol: '❤️'
    }
};
```

## Física de rebote

### Rebote en paleta
```javascript
function calculatePaddleBounce(ball, paddle) {
    const paddleCenter = paddle.x + paddle.width / 2;
    const ballCenter = ball.x + ball.radius;
    const relativePosition = (ballCenter - paddleCenter) / (paddle.width / 2);
    
    // Angle ranges from -60° to +60°
    const maxAngle = Math.PI / 3; // 60 degrees
    const bounceAngle = relativePosition * maxAngle;
    
    const speed = Math.sqrt(ball.dx * ball.dx + ball.dy * ball.dy);
    ball.dx = Math.sin(bounceAngle) * speed;
    ball.dy = -Math.abs(Math.cos(bounceAngle) * speed);
}
```

### Rebote en bloques
```javascript
function calculateBlockBounce(ball, block) {
    const ballCenterX = ball.x + ball.radius;
    const ballCenterY = ball.y + ball.radius;
    const blockCenterX = block.x + block.width / 2;
    const blockCenterY = block.y + block.height / 2;
    
    const deltaX = Math.abs(ballCenterX - blockCenterX);
    const deltaY = Math.abs(ballCenterY - blockCenterY);
    
    if (deltaX > deltaY) {
        ball.dx = -ball.dx; // Horizontal bounce
    } else {
        ball.dy = -ball.dy; // Vertical bounce
    }
}
```

## Patrones de niveles

### Nivel 1 - Básico
```javascript
const LEVEL_1 = [
    'RRRRRRRRR',
    'OOOOOOOOO',
    'YYYYYYYYY',
    'GGGGGGGGG',
    '         ',
    '         '
];
```

### Nivel 2 - Pirámide
```javascript
const LEVEL_2 = [
    '    R    ',
    '   OOO   ',
    '  YYYYY  ',
    ' GGGGGGG ',
    'BBBBBBBBB',
    '         '
];
```

### Nivel 3 - Fortaleza
```javascript
const LEVEL_3 = [
    'SSSSSSSSS',
    'S       S',
    'S RRRRR S',
    'S R   R S',
    'S R G R S',
    'S RRRRR S'
];
```

## Sistema de puntuación
- Bloque destruido: Puntos según tipo
- Combo multiplier: x2, x3, x4 por golpes consecutivos
- Nivel completado: 1000 puntos bonus
- Vida restante: 500 puntos bonus
- Power-up recogido: 100 puntos

## Parámetros de juego
```javascript
const GAME_CONFIG = {
    paddle: {
        width: 100,
        height: 15,
        speed: 8,
        minWidth: 50,
        maxWidth: 150
    },
    ball: {
        radius: 8,
        speed: 5,
        maxSpeed: 8,
        minSpeed: 3
    },
    blocks: {
        width: 75,
        height: 25,
        rows: 6,
        cols: 10,
        padding: 5
    },
    powerup: {
        width: 20,
        height: 20,
        fallSpeed: 3,
        spawnChance: 0.15
    }
};
```

## Estados del juego
- **MENU**: Pantalla de inicio
- **READY**: Pelota en paleta, esperando lanzamiento
- **PLAYING**: Juego activo
- **PAUSED**: Juego pausado
- **BALL_LOST**: Animación de pérdida de pelota
- **LEVEL_COMPLETE**: Completar nivel
- **GAME_OVER**: Sin vidas

## Efectos visuales
- Partículas al destruir bloques
- Trail de la pelota
- Efectos de power-ups
- Animaciones de transición
- Shake de pantalla en impactos

## Archivos a crear
- `breakout/index.html` - Juego completo
- `breakout/instrucciones.md` - Manual del juego

## Criterios de éxito
- Física de rebote precisa y predecible
- Controles responsivos y suaves
- Variedad de power-ups balanceados
- Progresión de niveles desafiante
- Efectos visuales atractivos
- Performance estable con múltiples pelotas
- Detección de colisiones precisa