# Whack-a-Mole Game - Plan de Implementación

## Objetivo
Crear el juego clásico Whack-a-Mole en un solo archivo HTML con JavaScript vanilla, compatible con desktop y mobile.

## Características del juego
- Grid de agujeros donde aparecen topos
- Topos aparecen aleatoriamente por tiempo limitado
- Puntuación por topos golpeados
- Tiempo límite del juego
- Diferentes velocidades y dificultades
- Efectos visuales y sonoros

## Estructura técnica

### Layout
- Grid 3x3 de agujeros
- Topos que aparecen/desaparecen con animaciones
- Panel de puntuación y tiempo
- Martillo cursor para desktop

### Controles
- **Desktop**: 
  - Clic del mouse en topos
  - Cursor personalizado (martillo)
- **Mobile**: 
  - Tap en topos
  - Feedback táctil

### Lógica del juego
1. **Mecánicas básicas**
   - Topos aparecen aleatoriamente en agujeros
   - Tiempo de aparición variable (1-3 segundos)
   - Puntos por golpear topos
   - Penalty por fallar

2. **Sistema de dificultad**
   - Velocidad de aparición aumenta
   - Tiempo de visibilidad disminuye
   - Más topos simultáneos en niveles altos

3. **Estados del juego**
   - READY: pantalla de inicio
   - PLAYING: juego activo
   - GAME_OVER: tiempo agotado

### Sistema de puntuación
- Topo normal: +10 puntos
- Topo dorado (raro): +50 puntos
- Miss (clic en agujero vacío): -5 puntos
- Combo multiplier por golpes consecutivos

## Implementación por pasos

### Paso 1: Estructura base
- HTML con grid de agujeros
- CSS para animaciones de topos
- Cursor personalizado

### Paso 2: Lógica de aparición
- Sistema de spawn aleatorio
- Timers para aparición/desaparición
- Estados de agujeros (vacío, topo, golpeado)

### Paso 3: Detección de clics
- Event listeners en agujeros
- Validación de golpes exitosos
- Feedback visual inmediato

### Paso 4: Sistema de puntuación
- Contador de puntos
- Combo system
- Topos especiales (dorado, rápido)

### Paso 5: Timer y dificultad
- Countdown timer
- Progresión de dificultad
- Spawn rate dinámico

### Paso 6: Efectos visuales
- Animaciones de aparición/desaparición
- Efectos de golpe
- Partículas y feedback

### Paso 7: Optimización
- Performance en animaciones
- Responsive design
- Analytics

## Elementos visuales

### Sprites/Formas
- **Agujeros**: Círculos oscuros con sombra
- **Topos**: Emoji o formas marrones
- **Martillo**: Cursor personalizado
- **Efectos**: Estrellas, "+puntos"

### Animaciones
```css
.mole-appear {
    animation: popUp 0.3s ease-out;
}

.mole-disappear {
    animation: popDown 0.2s ease-in;
}

.mole-hit {
    animation: hit 0.4s ease-out;
}
```

### Topos especiales
- **Topo normal**: Marrón, 10 puntos
- **Topo dorado**: Dorado, 50 puntos, aparece menos
- **Topo rápido**: Rojo, 20 puntos, desaparece rápido
- **Topo bomba**: Negro, -20 puntos, evitar

## Parámetros de juego
```javascript
const GAME_CONFIG = {
    duration: 60, // seconds
    baseSpawnRate: 1500, // ms
    moleVisibleTime: 2000, // ms
    difficultyIncrease: 0.95, // multiplier per level
    specialMoleChance: 0.1, // 10%
    maxSimultaneousMoles: 3
};

const SCORING = {
    normalMole: 10,
    goldenMole: 50,
    fastMole: 20,
    bombMole: -20,
    missClick: -5,
    comboMultiplier: 1.5
};
```

## Estados de agujeros
- **EMPTY**: Sin topo, puede recibir spawn
- **MOLE**: Topo visible, puede ser golpeado
- **HIT**: Topo golpeado, animación de desaparición
- **COOLDOWN**: Agujero en cooldown después de hit

## Sistema de combos
- Golpes consecutivos sin fallar
- Multiplicador aumenta: x1, x1.5, x2, x2.5, x3 (máximo)
- Se resetea al fallar un golpe
- Feedback visual del combo actual

## Responsive design
- Grid se adapta al tamaño de pantalla
- Agujeros mantienen proporción
- Controles táctiles optimizados
- Feedback haptic en mobile (si disponible)

## Archivos a crear
- `whack-a-mole/index.html` - Juego completo
- `whack-a-mole/instrucciones.md` - Manual del juego

## Criterios de éxito
- Respuesta inmediata a clics/taps
- Animaciones fluidas de topos
- Sistema de puntuación balanceado
- Progresión de dificultad adecuada
- Feedback visual claro
- Performance estable en mobile
- Controles precisos y responsivos