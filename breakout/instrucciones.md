# Breakout Game - Instrucciones

## Cómo jugar

### Objetivo
Destruye todos los bloques de colores usando una pelota que rebota. Controla la paleta para mantener la pelota en juego y dirigir sus rebotes hacia los bloques.

### Controles

#### Desktop (Computadora)
- **←** Flecha izquierda: Mover paleta hacia la izquierda
- **→** Flecha derecha: Mover paleta hacia la derecha
- **A**: Mover paleta hacia la izquierda (alternativo)
- **D**: Mover paleta hacia la derecha (alternativo)
- **Mouse**: Mover paleta siguiendo el cursor
- **Espacio**: Lanzar pelota (cuando está en la paleta)
- **P**: Pausar/Reanudar juego
- **Enter**: Reiniciar juego (cuando termina)

#### Mobile (Teléfono/Tablet)
- **Botones ←/→**: Mover paleta
- **Deslizar dedo**: Mover paleta siguiendo el toque
- **Tap "LANZAR"**: Lanzar pelota
- **Botón Pausa**: Pausar/Reanudar
- **Tocar "Jugar de nuevo"**: Reiniciar juego

### Elementos del juego

#### 🏓 Tu Paleta
- **Función**: Rebota la pelota hacia los bloques
- **Movimiento**: Solo horizontal en la parte inferior
- **Zonas de rebote**: 
  - Centro: Rebote recto hacia arriba
  - Extremos: Rebote en ángulo (hasta 60°)
- **Tamaño**: Puede cambiar con power-ups

#### ⚪ Pelota
- **Comportamiento**: Rebota en paredes, paleta y bloques
- **Velocidad**: Constante, puede modificarse con power-ups
- **Ángulo**: Cambia según dónde golpee la paleta
- **Pérdida**: Si cae por debajo de la paleta

#### 🧱 Bloques de Colores
Diferentes tipos con distintas características:

**🟥 Bloques Rojos**
- **Resistencia**: 1 golpe
- **Puntos**: 7 puntos
- **Posición**: Fila superior

**🟧 Bloques Naranjas**
- **Resistencia**: 1 golpe
- **Puntos**: 5 puntos
- **Posición**: Segunda fila

**🟨 Bloques Amarillos**
- **Resistencia**: 1 golpe
- **Puntos**: 3 puntos
- **Posición**: Tercera fila

**🟩 Bloques Verdes**
- **Resistencia**: 1 golpe
- **Puntos**: 1 punto
- **Posición**: Cuarta fila

**🟦 Bloques Azules**
- **Resistencia**: 2 golpes
- **Puntos**: 10 puntos
- **Característica**: Cambian de color al primer golpe

**🟪 Bloques Púrpuras**
- **Resistencia**: 2 golpes
- **Puntos**: 15 puntos
- **Característica**: Más resistentes

**⬜ Bloques Plateados**
- **Resistencia**: 3 golpes
- **Puntos**: 25 puntos
- **Característica**: Muy resistentes

**🟨 Bloques Dorados**
- **Resistencia**: Indestructibles
- **Puntos**: 50 puntos (si se destruyen con power-up)
- **Característica**: Solo se destruyen con power-ups especiales

#### 🎁 Power-ups
Caen ocasionalmente de bloques destruidos:

**↔️ Expandir Paleta (Verde)**
- **Efecto**: Aumenta el tamaño de la paleta
- **Duración**: 10 segundos
- **Estrategia**: Más fácil atrapar la pelota

**↔️ Encoger Paleta (Rojo)**
- **Efecto**: Reduce el tamaño de la paleta
- **Duración**: 10 segundos
- **Peligro**: Más difícil controlar la pelota

**⚪ Multi-pelota (Amarillo)**
- **Efecto**: Añade 2 pelotas adicionales
- **Duración**: Hasta que se pierdan
- **Ventaja**: Más oportunidades de golpear bloques

**🐌 Pelota Lenta (Azul)**
- **Efecto**: Reduce la velocidad de la pelota
- **Duración**: 8 segundos
- **Ventaja**: Más tiempo para reaccionar

**⚡ Pelota Rápida (Magenta)**
- **Efecto**: Aumenta la velocidad de la pelota
- **Duración**: 8 segundos
- **Desafío**: Requiere reflejos más rápidos

**❤️ Vida Extra (Dorado)**
- **Efecto**: Añade una vida adicional
- **Duración**: Permanente
- **Valor**: Muy raro y valioso

### Mecánicas del juego

#### Sistema de rebote
- **Paredes laterales**: Rebote horizontal
- **Pared superior**: Rebote vertical
- **Paleta**: Ángulo variable según punto de impacto
- **Bloques**: Rebote según lado de impacto

#### Física de la paleta
- **Centro (40% medio)**: Rebote recto (0°)
- **Zonas medias (30% cada lado)**: Rebote en ángulo moderado (15-30°)
- **Extremos (15% cada lado)**: Rebote en ángulo máximo (45-60°)

#### Sistema de vidas
- **Vidas iniciales**: 3 pelotas
- **Pérdida**: Cuando la pelota cae por debajo de la paleta
- **Vida extra**: Con power-up o cada 10,000 puntos
- **Game Over**: Cuando se acaban todas las vidas

### Estrategias y consejos

#### 🎯 Estrategias básicas
1. **Control de ángulo**: Usa diferentes partes de la paleta para dirigir la pelota
2. **Paciencia**: No siempre golpees con los extremos
3. **Observa patrones**: Los rebotes son predecibles
4. **Posicionamiento**: Anticipa dónde caerá la pelota

#### 🏆 Estrategias avanzadas
1. **Ángulos calculados**: Usa rebotes para llegar a bloques difíciles
2. **Gestión de power-ups**: Algunos son mejores que otros según la situación
3. **Multi-pelota**: Mantén al menos una pelota segura
4. **Combos**: Golpes consecutivos dan más puntos

#### 🚨 Situaciones peligrosas
1. **Pelota muy horizontal**: Puede quedarse rebotando entre paredes
2. **Paleta encogida**: Requiere precisión extrema
3. **Pelota rápida**: Menos tiempo para reaccionar
4. **Últimos bloques**: Suelen estar en posiciones difíciles

### Sistema de puntuación

#### Puntos por bloque
- Bloque verde: 1 punto
- Bloque amarillo: 3 puntos
- Bloque naranja: 5 puntos
- Bloque rojo: 7 puntos
- Bloque azul: 10 puntos
- Bloque púrpura: 15 puntos
- Bloque plateado: 25 puntos
- Bloque dorado: 50 puntos

#### Bonificaciones
- **Power-up recogido**: +100 puntos
- **Combo de bloques**: Multiplicador x2, x3, x4
- **Nivel completado**: +1000 puntos
- **Vida restante**: +500 puntos por vida
- **Velocidad de completado**: Bonus por tiempo

### Progresión de niveles

#### Nivel 1-3: Principiante
- **Patrones**: Simples y simétricos
- **Bloques**: Principalmente de 1 golpe
- **Power-ups**: Frecuentes y útiles

#### Nivel 4-6: Intermedio
- **Patrones**: Más complejos
- **Bloques**: Mezcla de resistencias
- **Desafío**: Bloques en posiciones estratégicas

#### Nivel 7-9: Avanzado
- **Patrones**: Asimétricos y desafiantes
- **Bloques**: Muchos de múltiples golpes
- **Estrategia**: Requiere planificación

#### Nivel 10+: Experto
- **Patrones**: Muy complejos
- **Bloques**: Incluye indestructibles
- **Maestría**: Solo para jugadores expertos

### Consejos por nivel de habilidad

#### 👶 Principiante
- Concéntrate en mantener la pelota en juego
- Usa el centro de la paleta para rebotes seguros
- Recoge todos los power-ups positivos
- No te preocupes por la puntuación al inicio

#### 🧒 Intermedio
- Aprende a usar los ángulos de rebote
- Gestiona los power-ups estratégicamente
- Busca patrones en los rebotes
- Intenta crear combos de bloques

#### 👨 Avanzado
- Domina el control preciso de ángulos
- Planifica rutas para bloques difíciles
- Optimiza el uso de multi-pelota
- Maximiza la puntuación con combos

#### 🏅 Experto
- Control perfecto de la física de rebote
- Estrategias avanzadas para cada nivel
- Gestión óptima de todos los power-ups
- Completar niveles sin perder vidas

### Consejos técnicos

#### Control de la paleta
- **Mouse**: Más preciso para movimientos finos
- **Teclado**: Mejor para movimientos rápidos
- **Mobile**: Usa gestos suaves, no toques bruscos

#### Física de rebote
- Los rebotes son determinísticos
- El ángulo de salida depende del punto de impacto
- La velocidad se mantiene constante (salvo power-ups)
- Los rebotes en esquinas pueden ser impredecibles

#### Gestión de power-ups
- **Expandir paleta**: Siempre útil
- **Multi-pelota**: Mejor cuando quedan pocos bloques
- **Pelota lenta**: Útil en situaciones difíciles
- **Vida extra**: Siempre recógela

### Patrones de niveles comunes

#### Formaciones clásicas
- **Muro sólido**: Filas completas de bloques
- **Pirámide**: Bloques formando triángulo
- **Fortaleza**: Bloques formando estructura con huecos
- **Laberinto**: Caminos entre bloques

#### Estrategias por patrón
- **Muro**: Ataca desde los extremos
- **Pirámide**: Elimina la base primero
- **Fortaleza**: Busca puntos débiles
- **Laberinto**: Usa rebotes calculados

### Historia del juego
Breakout fue creado por Atari en 1976, diseñado por Nolan Bushnell y Steve Bristow. Steve Wozniak (co-fundador de Apple) creó una versión optimizada del hardware, estableciendo las bases para muchos juegos de arcade posteriores.

¡Destruye todos los bloques y conviértete en el maestro del Breakout!