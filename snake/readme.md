# Snake Game - Plan de Implementación

## Objetivo
Crear el juego clásico Snake en un solo archivo HTML con JavaScript vanilla, compatible con desktop y mobile.

## Características del juego
- Serpiente que crece al comer comida
- Controles: flechas del teclado (desktop) y gestos táctiles (mobile)
- Game over al chocar con paredes o consigo misma
- Puntuación basada en comida consumida
- Velocidad incrementa gradualmente

## Estructura técnica

### Canvas
- Tamaño: 400x400px (responsive)
- Grid: 20x20 celdas (20px cada una)
- Renderizado con requestAnimationFrame

### Controles
- **Desktop**: Flechas del teclado (↑↓←→)
- **Mobile**: Gestos de swipe en cualquier dirección
- Prevenir cambio de dirección opuesta inmediata

### Lógica del juego
1. **Inicialización**
   - Serpiente: 3 segmentos en el centro
   - Dirección inicial: derecha
   - Comida: posición aleatoria
   - Puntuación: 0

2. **Loop principal**
   - Mover serpiente según dirección
   - Verificar colisiones (paredes/cuerpo)
   - Verificar si come comida
   - Actualizar puntuación y velocidad
   - Renderizar frame

3. **Estados**
   - PLAYING: juego activo
   - GAME_OVER: mostrar puntuación final
   - PAUSED: juego pausado

### Analytics
- Evento: game_start
- Evento: game_over (con puntuación)
- Evento: food_eaten
- Almacenamiento local con sync al servidor

## Implementación por pasos

### Paso 1: Estructura HTML básica
- Canvas centrado
- Controles de UI (start, pause, restart)
- Puntuación visible
- Estilos responsive

### Paso 2: Lógica de la serpiente
- Clase Snake con métodos move(), grow(), checkCollision()
- Sistema de coordenadas en grid
- Renderizado básico

### Paso 3: Sistema de comida
- Generación aleatoria evitando cuerpo de serpiente
- Detección de colisión serpiente-comida
- Efectos visuales

### Paso 4: Controles
- Event listeners para teclado
- Touch events para mobile
- Prevención de movimientos inválidos

### Paso 5: Game states y UI
- Pantalla de inicio
- Pantalla de game over
- Sistema de pausa
- Puntuación y high score

### Paso 6: Analytics y optimización
- Integración con sistema de tracking
- Optimización de performance
- Pruebas en dispositivos

## Archivos a crear
- `snake/index.html` - Juego completo en un archivo
- Estilos CSS embebidos
- JavaScript embebido
- Sin dependencias externas

## Criterios de éxito
- Jugable en desktop y mobile
- Responsive design
- Performance fluido (60fps)
- Controles intuitivos
- Analytics funcional