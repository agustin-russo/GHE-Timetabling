# Development Log

## 2026-07-05

Implementé la primera versión del solver utilizando un algoritmo de backtracking básico. Además, desarrollé un generador de instancias aleatorias junto con un pequeño sistema de benchmarking para medir el tiempo de ejecución y la cantidad de nodos explorados.

Como era de esperar, el rendimiento del solver es limitado: solo logra resolver instancias pequeñas antes de que el espacio de búsqueda crezca demasiado. Aun así, esta implementación cumple su objetivo principal, que es validar el modelo del problema y servir como punto de partida para incorporar heurísticas de búsqueda.

### Próximos pasos

- Implementar la heurística **Minimum Remaining Values (MRV)**.
- Agregar **Forward Checking** para detectar callejones sin salida de forma temprana.
- Comparar el rendimiento con la versión básica mediante benchmarks.