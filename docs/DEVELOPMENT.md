# Development Log

## 2026-07-05

Implementé la primera versión del solver utilizando un algoritmo de backtracking básico. Además, desarrollé un generador de instancias aleatorias junto con un pequeño sistema de benchmarking para medir el tiempo de ejecución y la cantidad de nodos explorados.

Como era de esperar, el rendimiento del solver es limitado: solo logra resolver instancias pequeñas antes de que el espacio de búsqueda crezca demasiado. Aun así, esta implementación cumple su objetivo principal, que es validar el modelo del problema y servir como punto de partida para incorporar heurísticas de búsqueda.

## 2026-07-09

Implementé una versión mejorada del algoritmo de backtracking usando MRV (Minimum Remaining Value) y LCV (Least Constraining Value). Esperaba que el rendimiento de esta versión, una vez fuera correctamente implementada, superara con creces a su predecesor. Sin embargo, me topé con una limitación muy conocida en el mundo de la optimización: la Transición de Fase (Phase Transition) en Problemas de Satisfacción de Restricciones (CSP).

En los problemas NP-hard (como la generación de horarios de este estilo), la dificultad o complejidad del problema no crece de manera lineal con el tamaño, sino que depende de qué tan restringido está el problema. Si la ocupación es muy baja, sobran opciones y cualquier camino lleva a una solución. Si es excesivamente alta, el problema es matemáticamente imposible y el algoritmo falla en milisegundos. El verdadero obstáculo está en el medio: la "Transición de Fase". En este punto (ej. 60%-80% de ocupación), el sistema está críticamente restringido, obligando al algoritmo a explorar ramas inmensas sin salida antes de rendirse, que es exactamente donde el programa se cuelga. Esto sucede principalmente porque mi generador de casos de prueba es casi completamente aleatorio.

En los benchmarks, parecería que esta nueva versión es peor que la anterior, pero tiene una explicación. Primero, aplicar MRV y LCV dinámicamente tiene un costo, entonces en los casos más simples donde realmente no es necesario el algoritmo de backtracking simple lo vence. Y por la transición de fase, nunca llegamos a ver un caso donde las ventajas de las heurísticas muestren la diferencia con la versión anterior.

Para que estas heurísticas funcionen correctamente, necesitaría un generador por "Construcción Inversa": crear primero un horario perfecto, extraer sus disponibilidades, añadir ruido y pasárselo al solver para garantizar que existe un camino exitoso. Sin embargo, armar este generador es casi un proyecto aparte. Entender por qué fallan estas heurísticas me sirve como cierre para esta etapa, dejándome el camino libre para el verdadero objetivo: implementar el motor definitivo con CP-SAT (Google OR-Tools). Si en algún momento me parece necesario, podría llegar a implementar este generador para poder comparar correctamente todos los algoritmos.
