# Space Invaders Game - Plan de Implementación

## Objetivo
Crear el juego clásico Space Invaders en un solo archivo HTML con JavaScript vanilla, compatible con desktop y mobile.

## Características del juego
- Nave espacial controlada por el jugador
- Oleadas de invasores alienígenas que se mueven en formación
- Sistema de disparos bidireccional (jugador y aliens)
- Barreras destructibles para protección
- Niveles progresivos con mayor dificultad
- Nave nodriza ocasional para puntos bonus

## Estructura técnica

### Canvas
- Tamaño: 800x600px (responsive)
- Fondo estrellado animado
- HUD con puntuación, vidas y nivel

### Controles
- **Desktop**: 
  - Flechas izquierda/derecha para mover
  - Barra espaciadora para disparar
  - A/D alternativos
- **Mobile**: 
  - Botones virtuales de movimiento
  - Botón de disparo
  - Auto-disparo opcional

### Lógica del juego
1. **Jugador**
   - Nave que se mueve horizontalmente
   - Un disparo activo a la vez (clásico)
   - 3 vidas iniciales
   - Colisión con aliens o proyectiles enemigos

2. **Invasores**
   - Grid de 5x11 aliens (55 total)
   - 3 tipos diferentes con puntuaciones distintas
   - Movimiento lateral con descenso periódico
   - Velocidad aumenta conforme quedan menos

3. **Sistema de disparos**
   - Jugador: Un proyectil activo
   - Aliens: Múltiples proyectiles aleatorios
   - Colisiones con barreras y objetivos

### Mecánicas del juego
- **Oleadas**: Nuevos aliens aparecen al eliminar todos
- **Barreras**: 4 estructuras destructibles
- **Nave nodriza**: Aparece ocasionalmente arriba
- **Aceleración**: Aliens se mueven más rápido con menos números

## Implementación por pasos

### Paso 1: Estructura base
- Canvas y sistema de renderizado
- Clases Player, Alien, Bullet, Barrier
- Loop principal del juego

### Paso 2: Nave del jugador
- Movimiento horizontal
- Sistema de disparo
- Animación y sprites

### Paso 3: Invasores alienígenas
- Grid de aliens con tipos diferentes
- Movimiento en formación
- Animación de sprites

### Paso 4: Sistema de disparos
- Proyectiles del jugador
- Proyectiles enemigos aleatorios
- Detección de colisiones

### Paso 5: Barreras destructibles
- Estructuras pixeladas
- Destrucción por impactos
- Regeneración entre niveles

### Paso 6: Nave nodriza y bonus
- Aparición aleatoria
- Movimiento horizontal
- Puntuación bonus variable

### Paso 7: Niveles y progresión
- Oleadas infinitas
- Aumento de dificultad
- Sistema de puntuación

## Tipos de aliens

### Alien Tipo 1 (Inferior)
```javascript
const ALIEN_SQUID = {
    points: 10,
    sprite: ['  ▄▄▄▄▄▄  ', ' ████████ ', '██▄▄▄▄▄▄██', '██ ████ ██', '  ██  ██  '],
    color: '#00ff00'
};
```

### Alien Tipo 2 (Medio)
```javascript
const ALIEN_CRAB = {
    points: 20,
    sprite: [' ▄ ▄▄▄▄ ▄ ', '  ██████  ', ' ████████ ', '██ ████ ██', '██      ██'],
    color: '#ffff00'
};
```

### Alien Tipo 3 (Superior)
```javascript
const ALIEN_OCTOPUS = {
    points: 30,
    sprite: ['   ████   ', ' ████████ ', '██████████', '██ ████ ██', '  ██  ██  '],
    color: '#ff00ff'
};
```

## Sistema de puntuación
- Alien inferior: 10 puntos
- Alien medio: 20 puntos  
- Alien superior: 30 puntos
- Nave nodriza: 50-300 puntos (aleatorio)
- Vida extra cada 1500 puntos

## Parámetros de juego
```javascript
const GAME_CONFIG = {
    player: {
        speed: 5,
        bulletSpeed: 8,
        maxBullets: 1
    },
    aliens: {
        rows: 5,
        cols: 11,
        speed: 1,
        dropDistance: 20,
        bulletSpeed: 3,
        bulletChance: 0.001
    },
    barriers: {
        count: 4,
        width: 80,
        height: 60
    },
    mothership: {
        speed: 2,
        spawnChance: 0.0005,
        points: [50, 100, 150, 300]
    }
};
```

## Algoritmo de movimiento de aliens
```javascript
function updateAliens() {
    let hitEdge = false;
    
    aliens.forEach(alien => {
        alien.x += alienDirection * alienSpeed;
        
        if (alien.x <= 0 || alien.x >= canvas.width - alienWidth) {
            hitEdge = true;
        }
    });
    
    if (hitEdge) {
        alienDirection *= -1;
        aliens.forEach(alien => {
            alien.y += ALIEN_DROP_DISTANCE;
        });
        
        // Increase speed as aliens get closer
        alienSpeed += 0.2;
    }
}
```

## Sistema de barreras destructibles
```javascript
class Barrier {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.pixels = this.generatePixels();
    }
    
    generatePixels() {
        // Generate destructible pixel matrix
        const pattern = [
            "████████████████",
            "████████████████",
            "████████████████",
            "████        ████",
            "████        ████",
            "████        ████"
        ];
        return pattern;
    }
    
    hit(x, y, radius = 8) {
        // Remove pixels in radius around hit point
        for (let dy = -radius; dy <= radius; dy++) {
            for (let dx = -radius; dx <= radius; dx++) {
                if (dx*dx + dy*dy <= radius*radius) {
                    this.removePixel(x + dx, y + dy);
                }
            }
        }
    }
}
```

## Estados del juego
- **MENU**: Pantalla de inicio
- **PLAYING**: Juego activo
- **PAUSED**: Juego pausado
- **GAME_OVER**: Sin vidas
- **LEVEL_TRANSITION**: Entre oleadas

## Efectos visuales
- Explosiones de aliens y nave
- Partículas de destrucción
- Flash en impactos
- Fondo estrellado en movimiento
- Animación de sprites de aliens

## Archivos a crear
- `space-invaders/index.html` - Juego completo
- `space-invaders/instrucciones.md` - Manual del juego

## Criterios de éxito
- Movimiento fluido de aliens en formación
- Sistema de disparos preciso
- Barreras destructibles realistas
- Progresión de dificultad balanceada
- Controles responsivos
- Efectos visuales atractivos
- Performance estable en oleadas grandes