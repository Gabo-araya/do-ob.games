# Flappy Bird Game - Plan de Implementación

## Objetivo
Crear el juego clásico Flappy Bird en un solo archivo HTML con JavaScript vanilla, compatible con desktop y mobile.

## Características del juego
- Pájaro que vuela al hacer clic/tap
- Tuberías que se mueven de derecha a izquierda
- Física de gravedad y salto
- Detección de colisiones precisa
- Sistema de puntuación por tuberías pasadas
- Dificultad progresiva

## Estructura técnica

### Canvas
- Tamaño: 400x600px (responsive)
- Scrolling horizontal infinito
- Parallax background opcional

### Controles
- **Desktop**: 
  - Clic del mouse
  - Barra espaciadora
  - Flecha arriba
- **Mobile**: 
  - Tap en pantalla
  - Botón de salto

### Física del juego
1. **Pájaro**
   - Gravedad constante hacia abajo
   - Impulso hacia arriba al hacer clic/tap
   - Rotación basada en velocidad vertical
   - Límites de pantalla (arriba/abajo)

2. **Tuberías**
   - Generación procedural con gaps aleatorios
   - Velocidad constante hacia la izquierda
   - Reciclaje cuando salen de pantalla
   - Gap mínimo para mantener jugabilidad

3. **Colisiones**
   - Detección pixel-perfect o por rectángulos
   - Colisión con tuberías superiores e inferiores
   - Colisión con suelo y techo

### Mecánicas del juego
1. **Estados**
   - READY: pantalla de inicio
   - PLAYING: juego activo
   - GAME_OVER: fin del juego

2. **Puntuación**
   - +1 punto por cada tubería pasada
   - Detección cuando el pájaro pasa el centro de la tubería
   - High score persistente

3. **Dificultad**
   - Velocidad de tuberías aumenta gradualmente
   - Gap entre tuberías se reduce ligeramente
   - Frecuencia de aparición de tuberías

## Implementación por pasos

### Paso 1: Estructura base
- Canvas y controles básicos
- Clase Bird con física básica
- Loop de juego principal

### Paso 2: Física del pájaro
- Implementar gravedad
- Sistema de salto/impulso
- Rotación del sprite
- Límites de pantalla

### Paso 3: Sistema de tuberías
- Clase Pipe con movimiento
- Generación procedural
- Sistema de reciclaje
- Gaps aleatorios

### Paso 4: Detección de colisiones
- Colisión pájaro-tubería
- Colisión con límites
- Sistema preciso de hitboxes

### Paso 5: Puntuación y estados
- Contador de puntos
- Estados de juego
- Pantallas de inicio y game over
- High score

### Paso 6: Controles y UI
- Input de mouse y teclado
- Controles táctiles
- Interfaz responsive
- Efectos visuales

### Paso 7: Polish y optimización
- Animaciones suaves
- Efectos de sonido (opcional)
- Partículas y feedback visual
- Analytics

## Elementos visuales

### Sprites/Formas
- **Pájaro**: Círculo amarillo con rotación
- **Tuberías**: Rectángulos verdes
- **Fondo**: Gradiente azul cielo
- **Suelo**: Franja verde/marrón

### Animaciones
- Aleteo del pájaro (rotación)
- Movimiento suave de tuberías
- Efectos de impacto
- Transiciones de estado

## Parámetros de juego
```javascript
const GRAVITY = 0.5;
const JUMP_FORCE = -8;
const PIPE_SPEED = 2;
const PIPE_GAP = 150;
const PIPE_FREQUENCY = 90; // frames
```

## Archivos a crear
- `flappy-bird/index.html` - Juego completo
- `flappy-bird/instrucciones.md` - Manual del juego

## Criterios de éxito
- Física realista y responsiva
- Controles precisos en desktop y mobile
- Colisiones justas y precisas
- Jugabilidad adictiva
- Performance fluido (60fps)
- Interfaz clara e intuitiva