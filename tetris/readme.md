# Tetris Game - Plan de Implementación

## Objetivo
Crear el juego clásico Tetris en un solo archivo HTML con JavaScript vanilla, compatible con desktop y mobile.

## Características del juego
- 7 tipos de tetrominos (I, O, T, S, Z, J, L)
- Rotación de piezas en sentido horario
- Eliminación de líneas completas
- Aumento progresivo de velocidad
- Sistema de puntuación por líneas y nivel
- Preview de siguiente pieza
- Hold/reserva de pieza

## Estructura técnica

### Canvas
- Tamaño: 300x600px (10x20 celdas de 30px)
- Panel lateral para puntuación, nivel, siguiente pieza
- Grid de juego 10 columnas x 20 filas

### Controles
- **Desktop**: 
  - Flechas: mover y rotar
  - Espacio: drop rápido
  - C: hold pieza
  - P: pausa
- **Mobile**: 
  - Botones táctiles
  - Gestos de swipe
  - Tap para rotar

### Lógica del juego
1. **Tetrominos**
   - 7 formas diferentes con rotaciones
   - Sistema de coordenadas relativas
   - Colores únicos por tipo

2. **Mecánicas**
   - Caída automática por tiempo
   - Detección de colisiones
   - Rotación con wall kicks
   - Line clearing con animación
   - Nivel aumenta cada 10 líneas

3. **Puntuación**
   - 1 línea: 100 * nivel
   - 2 líneas: 300 * nivel  
   - 3 líneas: 500 * nivel
   - 4 líneas (Tetris): 800 * nivel

### Estados del juego
- MENU: pantalla inicial
- PLAYING: juego activo
- PAUSED: juego pausado
- GAME_OVER: fin del juego

## Implementación por pasos

### Paso 1: Estructura base
- Canvas y layout responsive
- Sistema de grid
- Clases básicas (Tetromino, Board)

### Paso 2: Tetrominos
- Definir las 7 formas
- Sistema de rotación
- Renderizado con colores

### Paso 3: Mecánicas básicas
- Caída de piezas
- Movimiento lateral
- Detección de colisiones
- Colocación de piezas

### Paso 4: Line clearing
- Detección de líneas completas
- Animación de eliminación
- Actualización de puntuación

### Paso 5: Controles
- Input de teclado
- Controles táctiles
- Gestos para mobile

### Paso 6: UI y estados
- Pantallas de menú y game over
- Sistema de pausa
- Preview y hold
- Efectos visuales

### Paso 7: Optimización
- Performance y animaciones
- Analytics
- Responsive design

## Tetrominos y rotaciones

### Formas base
```
I: ####
O: ##
   ##
T: ###
    #
S:  ##
   ##
Z: ##
    ##
J: #
   ###
L:   #
   ###
```

### Sistema de rotación
- 4 estados por pieza (excepto O que tiene 1)
- Wall kicks para rotaciones cerca de bordes
- Super Rotation System (SRS)

## Archivos a crear
- `tetris/index.html` - Juego completo
- `tetris/instrucciones.md` - Manual del juego

## Criterios de éxito
- Mecánicas clásicas de Tetris
- Controles fluidos en desktop y mobile
- Sistema de puntuación preciso
- Performance estable
- Interfaz intuitiva