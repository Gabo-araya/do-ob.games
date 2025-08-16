# Frogger Game - Plan de Implementación

## Objetivo
Crear el juego clásico Frogger en un solo archivo HTML con JavaScript vanilla, compatible con desktop y mobile.

## Características del juego
- Rana que debe cruzar calles y ríos peligrosos
- Múltiples carriles con vehículos en movimiento
- Sección de río con troncos y tortugas flotantes
- Objetivos en la parte superior para completar nivel
- Sistema de vidas y tiempo límite
- Niveles progresivos con mayor dificultad

## Estructura técnica

### Canvas y Grid
- Tamaño: 600x700px (responsive)
- Grid de 13 filas x 15 columnas
- Cada celda: 40x40px
- Movimiento discreto por celdas

### Controles
- **Desktop**: 
  - Flechas del teclado (↑↓←→)
  - WASD alternativo
- **Mobile**: 
  - Botones direccionales virtuales
  - Gestos de swipe

### Lógica del juego
1. **Rana (Jugador)**
   - Posición inicial en la parte inferior
   - Movimiento en grid discreto
   - Colisión con vehículos = muerte
   - Debe mantenerse en troncos/tortugas en el río

2. **Secciones del juego**
   - **Zona segura inferior**: Punto de inicio
   - **Carretera**: 5 carriles con vehículos
   - **Zona segura media**: Descanso entre carretera y río
   - **Río**: 5 carriles con troncos y tortugas
   - **Zona objetivo**: 5 espacios para completar

3. **Obstáculos y plataformas**
   - **Vehículos**: Coches, camiones, motos (diferentes velocidades)
   - **Troncos**: Plataformas flotantes en el río
   - **Tortugas**: Plataformas que se sumergen ocasionalmente

### Mecánicas del juego
- **Objetivo**: Llevar 5 ranas a los espacios objetivo
- **Tiempo límite**: Cada rana tiene tiempo limitado
- **Vidas**: 3-5 vidas iniciales
- **Puntuación**: Por avance, tiempo restante, y bonus

## Implementación por pasos

### Paso 1: Estructura base
- Canvas y sistema de grid
- Clase Frog, Vehicle, Log, Turtle
- Renderizado del campo de juego

### Paso 2: Movimiento de la rana
- Input del jugador
- Movimiento discreto en grid
- Animación de salto
- Límites del campo

### Paso 3: Sistema de tráfico
- Carriles de vehículos con diferentes velocidades
- Tipos de vehículos (coche, camión, moto)
- Spawn y reciclaje de vehículos
- Detección de colisiones

### Paso 4: Sistema de río
- Troncos flotantes
- Tortugas que se sumergen
- Lógica de "llevar" a la rana
- Detección de caída al agua

### Paso 5: Objetivos y progresión
- Espacios objetivo en la parte superior
- Detección de llegada
- Sistema de niveles
- Aumento de dificultad

### Paso 6: Timer y puntuación
- Countdown timer por rana
- Sistema de puntuación
- Bonus por tiempo restante
- Vidas y game over

### Paso 7: Efectos y polish
- Animaciones de muerte
- Efectos visuales
- Sonidos (opcional)
- Responsive design

## Layout del campo de juego

```javascript
const FIELD_LAYOUT = [
    'GOAL', 'GOAL', 'GOAL', 'GOAL', 'GOAL',     // Fila 0: Objetivos
    'SAFE',                                      // Fila 1: Zona segura
    'RIVER', 'RIVER', 'RIVER', 'RIVER', 'RIVER', // Filas 2-6: Río
    'SAFE',                                      // Fila 7: Zona segura media
    'ROAD', 'ROAD', 'ROAD', 'ROAD', 'ROAD',     // Filas 8-12: Carretera
    'SAFE'                                       // Fila 13: Zona segura inicial
];
```

## Tipos de vehículos

### Configuración de carriles
```javascript
const TRAFFIC_LANES = [
    { type: 'car', speed: 2, direction: 1, color: '#ff0000' },
    { type: 'truck', speed: 1, direction: -1, color: '#0000ff' },
    { type: 'car', speed: 3, direction: 1, color: '#ffff00' },
    { type: 'motorcycle', speed: 4, direction: -1, color: '#ff00ff' },
    { type: 'truck', speed: 1.5, direction: 1, color: '#00ff00' }
];
```

### Tipos de plataformas de río
```javascript
const RIVER_LANES = [
    { type: 'log', speed: 1, direction: 1, length: 3 },
    { type: 'turtle', speed: 2, direction: -1, length: 2, submerge: true },
    { type: 'log', speed: 1.5, direction: 1, length: 4 },
    { type: 'turtle', speed: 1, direction: -1, length: 3, submerge: false },
    { type: 'log', speed: 2, direction: 1, length: 2 }
];
```

## Sistema de puntuación
- Avanzar una fila: 10 puntos
- Llegar a objetivo: 50 puntos
- Bonus de tiempo: 1 punto por segundo restante
- Completar nivel: 1000 puntos
- Vida extra cada 10,000 puntos

## Algoritmo de colisiones

### En carretera
```javascript
function checkRoadCollision(frog) {
    const frogLane = Math.floor(frog.y / CELL_SIZE);
    if (frogLane >= ROAD_START && frogLane <= ROAD_END) {
        vehicles.forEach(vehicle => {
            if (vehicle.lane === frogLane && 
                isColliding(frog, vehicle)) {
                frogDeath();
            }
        });
    }
}
```

### En río
```javascript
function checkRiverLogic(frog) {
    const frogLane = Math.floor(frog.y / CELL_SIZE);
    if (frogLane >= RIVER_START && frogLane <= RIVER_END) {
        let onPlatform = false;
        
        platforms.forEach(platform => {
            if (platform.lane === frogLane && 
                isOnPlatform(frog, platform)) {
                onPlatform = true;
                frog.x += platform.speed * platform.direction;
            }
        });
        
        if (!onPlatform) {
            frogDeath(); // Fell in water
        }
    }
}
```

## Estados del juego
- **MENU**: Pantalla de inicio
- **PLAYING**: Juego activo
- **PAUSED**: Juego pausado
- **FROG_DEATH**: Animación de muerte
- **LEVEL_COMPLETE**: Completar nivel
- **GAME_OVER**: Sin vidas

## Animaciones
- Salto de rana con arco
- Muerte por aplastamiento
- Muerte por ahogamiento
- Tortugas sumergiéndose
- Splash al caer al agua

## Parámetros de juego
```javascript
const GAME_CONFIG = {
    frog: {
        startX: 7,
        startY: 12,
        moveDistance: 40
    },
    timer: {
        initial: 60, // seconds
        warning: 10  // red warning
    },
    lives: 3,
    scoring: {
        forward: 10,
        goal: 50,
        timeBonus: 1,
        levelComplete: 1000
    },
    difficulty: {
        speedIncrease: 0.2, // per level
        spawnIncrease: 0.1  // per level
    }
};
```

## Archivos a crear
- `frogger/index.html` - Juego completo
- `frogger/instrucciones.md` - Manual del juego

## Criterios de éxito
- Movimiento preciso en grid
- Colisiones justas y predecibles
- Física de río realista (llevar rana en troncos)
- Progresión de dificultad balanceada
- Controles responsivos
- Animaciones fluidas
- Timer y puntuación precisos