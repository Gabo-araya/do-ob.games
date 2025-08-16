# Pacman Game - Plan de Implementación

## Objetivo
Crear el juego clásico Pacman en un solo archivo HTML con JavaScript vanilla, compatible con desktop y mobile.

## Características del juego
- Laberinto clásico con puntos para comer
- Pacman controlado por el jugador
- 4 fantasmas con IA diferente cada uno
- Power pellets que permiten comer fantasmas
- Sistema de puntuación y vidas
- Niveles progresivos con mayor dificultad

## Estructura técnica

### Canvas y Grid
- Tamaño: 600x700px (responsive)
- Grid de 19x21 celdas (laberinto clásico)
- Cada celda: 25x25px
- Renderizado tile-based

### Controles
- **Desktop**: 
  - Flechas del teclado (↑↓←→)
  - WASD alternativo
- **Mobile**: 
  - Botones direccionales virtuales
  - Gestos de swipe

### Lógica del juego
1. **Pacman**
   - Movimiento en grid discreto
   - Animación de apertura/cierre de boca
   - Colisión con paredes, puntos y fantasmas
   - 3 vidas iniciales

2. **Fantasmas (4 tipos)**
   - **Blinky (Rojo)**: Persigue directamente a Pacman
   - **Pinky (Rosa)**: Intenta emboscar (4 celdas adelante)
   - **Inky (Cyan)**: Comportamiento complejo basado en Blinky
   - **Clyde (Naranja)**: Persigue hasta cierta distancia, luego huye

3. **Estados del juego**
   - READY: Pantalla de inicio
   - PLAYING: Juego activo
   - POWER_MODE: Fantasmas vulnerables
   - GAME_OVER: Sin vidas
   - LEVEL_COMPLETE: Todos los puntos comidos

### Sistema de puntuación
- Punto normal: 10 puntos
- Power pellet: 50 puntos
- Fantasma comido: 200, 400, 800, 1600 (secuencial)
- Bonus por fruta: 100-5000 puntos
- Vida extra cada 10,000 puntos

## Implementación por pasos

### Paso 1: Estructura base
- Canvas y sistema de grid
- Clase Game, Pacman, Ghost
- Renderizado básico del laberinto

### Paso 2: Laberinto y colisiones
- Mapa del laberinto (array 2D)
- Sistema de colisiones con paredes
- Puntos y power pellets

### Paso 3: Movimiento de Pacman
- Input del jugador
- Movimiento en grid
- Animación de sprite
- Colección de puntos

### Paso 4: IA de fantasmas
- Algoritmo de pathfinding básico
- Comportamientos únicos por fantasma
- Estados: Chase, Scatter, Frightened

### Paso 5: Mecánicas de juego
- Power mode y fantasmas vulnerables
- Sistema de vidas
- Detección de colisiones Pacman-fantasma

### Paso 6: Niveles y progresión
- Completar nivel
- Aumento de dificultad
- Frutas bonus

### Paso 7: UI y efectos
- Puntuación y vidas
- Efectos visuales
- Sonidos (opcional)

## Mapa del laberinto
```javascript
const MAZE = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,1],
    [1,3,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,3,1],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
    // ... resto del laberinto
];

// 0 = vacío, 1 = pared, 2 = punto, 3 = power pellet
// 4 = puerta fantasmas, 5 = túnel
```

## IA de fantasmas

### Algoritmo base
```javascript
class Ghost {
    constructor(color, homeCorner, scatterTarget) {
        this.mode = 'scatter'; // scatter, chase, frightened
        this.target = scatterTarget;
        this.direction = 'up';
    }
    
    update() {
        if (this.mode === 'chase') {
            this.target = this.getChaseTarget();
        } else if (this.mode === 'scatter') {
            this.target = this.scatterTarget;
        }
        
        this.move();
    }
    
    getChaseTarget() {
        // Implementación específica por fantasma
    }
}
```

### Comportamientos específicos
- **Blinky**: Target = posición actual de Pacman
- **Pinky**: Target = 4 celdas adelante de Pacman
- **Inky**: Target = vector desde Blinky a 2 celdas adelante de Pacman, duplicado
- **Clyde**: Target = Pacman si distancia > 8, sino esquina

## Estados de fantasmas
1. **Scatter**: Van a sus esquinas asignadas
2. **Chase**: Persiguen a Pacman con estrategia única
3. **Frightened**: Movimiento aleatorio, vulnerables
4. **Dead**: Regresan a casa después de ser comidos

## Sistema de timing
```javascript
const TIMING = {
    scatterTime: [7000, 7000, 5000, 5000], // ms por nivel
    chaseTime: [20000, 20000, 20000, 20000],
    frightenedTime: 6000,
    pacmanSpeed: 150, // ms por movimiento
    ghostSpeed: 160,
    frightenedGhostSpeed: 200
};
```

## Elementos visuales

### Sprites/Formas
- **Pacman**: Círculo amarillo con animación de boca
- **Fantasmas**: Formas redondeadas con colores únicos
- **Puntos**: Círculos pequeños blancos
- **Power pellets**: Círculos grandes parpadeantes
- **Frutas**: Sprites de bonus (cereza, fresa, etc.)

### Animaciones
- Pacman: Apertura/cierre de boca según dirección
- Fantasmas: Movimiento suave entre celdas
- Power pellets: Parpadeo
- Fantasmas asustados: Cambio de color azul

## Archivos a crear
- `pacman/index.html` - Juego completo
- `pacman/instrucciones.md` - Manual del juego

## Criterios de éxito
- IA de fantasmas desafiante pero justa
- Movimiento fluido en grid
- Mecánicas clásicas de Pacman
- Controles responsivos
- Progresión de dificultad balanceada
- Performance estable
- Interfaz fiel al original