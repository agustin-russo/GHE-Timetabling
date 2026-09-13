# Development Log

## 2026-07-05

Implementé la primera versión del solver utilizando un algoritmo de backtracking básico. Además, desarrollé un generador de instancias aleatorias junto con un pequeño sistema de benchmarking para medir el tiempo de ejecución y la cantidad de nodos explorados.

Como era de esperar, el rendimiento del solver es limitado: solo logra resolver instancias pequeñas antes de que el espacio de búsqueda crezca demasiado. Aun así, esta implementación cumple su objetivo principal, que es validar el modelo del problema y servir como punto de partida para incorporar heurísticas de búsqueda.

## 2026-07-09

Implementé una versión mejorada del algoritmo de backtracking usando MRV (Minimum Remaining Value) y LCV (Least Constraining Value). Esperaba que el rendimiento de esta versión, una vez fuera correctamente implementada, superara con creces a su predecesor. Sin embargo, me topé con una limitación muy conocida en el mundo de la optimización: la Transición de Fase (Phase Transition) en Problemas de Satisfacción de Restricciones (CSP).

En los problemas NP-hard (como la generación de horarios de este estilo), la dificultad o complejidad del problema no crece de manera lineal con el tamaño, sino que depende de qué tan restringido está el problema. Si la ocupación es muy baja, sobran opciones y cualquier camino lleva a una solución. Si es excesivamente alta, el problema es matemáticamente imposible y el algoritmo falla en milisegundos. El verdadero obstáculo está en el medio: la "Transición de Fase". En este punto (ej. 60%-80% de ocupación), el sistema está críticamente restringido, obligando al algoritmo a explorar ramas inmensas sin salida antes de rendirse, que es exactamente donde el programa se cuelga. Esto sucede principalmente porque mi generador de casos de prueba es casi completamente aleatorio.

En los benchmarks, parecería que esta nueva versión es peor que la anterior, pero tiene una explicación. Primero, aplicar MRV y LCV dinámicamente tiene un costo, entonces en los casos más simples donde realmente no es necesario el algoritmo de backtracking simple lo vence. Y por la transición de fase, nunca llegamos a ver un caso donde las ventajas de las heurísticas muestren la diferencia con la versión anterior.

Para que estas heurísticas funcionen correctamente, necesitaría un generador por "Construcción Inversa": crear primero un horario perfecto, extraer sus disponibilidades, añadir ruido y pasárselo al solver para garantizar que existe un camino exitoso. Sin embargo, armar este generador es casi un proyecto aparte. Entender por qué fallan estas heurísticas me sirve como cierre para esta etapa, dejándome el camino libre para el verdadero objetivo: implementar el motor definitivo con CP-SAT (Google OR-Tools). Si en algún momento me parece necesario, podría llegar a implementar este generador para poder comparar correctamente todos los algoritmos.

## 2026-08-20

Comencé a trabajar de lleno con OR-Tools, la librería elegida para implementar el motor definitivo de generación de horarios. Al ser una librería orientada a programación por restricciones y optimización combinatoria, y no contar con experiencia previa en este tipo de herramientas, gran parte de este período lo dediqué a su estudio.

La primera versión del modelo que implementé representaba cada clase mediante variables booleanas asociadas a bloques de tiempo fijos de 40 minutos, con un horario de inicio y fin común para todos los cursos. Bajo este esquema, logré que el modelo generara una solución válida para un caso de prueba con dos cursos. No realicé pruebas con una cantidad mayor por limitaciones de tiempo y falta de datos reales representativos. Sin embargo, al tratarse de un problema definido exclusivamente por restricciones matemáticas, no hay razones estructurales para esperar que el modelo deje de ser válido al aumentar la cantidad de cursos, siempre que las restricciones estén correctamente definidas.

A partir de una consulta con una persona con experiencia en la gestión de horarios docentes, identifiqué una limitación importante en el enfoque inicial: en la práctica, un mismo profesor puede dictar clases en cursos (o incluso instituciones) que comparten la duración del módulo pero no necesariamente los horarios de inicio y fin. El esquema de bloques fijos no podía representar esta situación, ya que cualquier diferencia entre los horarios de inicio o fin de los distintos cursos volvía el modelo incompatible.

Para resolverlo, reemplacé los bloques booleanos fijos por variables enteras que representan intervalos de tiempo (inicio, duración y fin), en una adaptación del problema clásico de job shop scheduling. OR-Tools ofrece soporte nativo para este enfoque mediante variables de intervalo y restricciones de no superposición (no-overlap), aunque esta parte de la API me era desconocida y requirió un proceso adicional de investigación. Como resultado, logré una versión del modelo basada en intervalos que genera horarios válidos de forma local, quedando pendiente para una etapa posterior la incorporación de un criterio de optimización.

## 2026-09-05

Con el modelo de generación de horarios válidos funcionando de forma local, decidí adelantar el desarrollo de la interfaz gráfica, inicialmente planificada para una etapa posterior del proyecto.

Elegí PySide6 como framework de interfaz por familiaridad previa con la librería y por sus capacidades para el desarrollo de aplicaciones de escritorio. Durante esta etapa identifiqué la necesidad de contar con una base de datos funcional antes de continuar con el desarrollo de la interfaz, dado que validar manualmente cada curso y profesor durante las pruebas resultaba poco práctico.

Para el diseño de la interfaz utilicé Qt Designer, una herramienta de edición visual que permite construir interfaces de PySide6 mediante composición de widgets. Su curva de aprendizaje inicial se compensa con una mayor velocidad de iteración sobre el diseño, lo cual considero especialmente relevante para etapas posteriores del proyecto, donde espero una mayor complejidad en la interfaz.

Al cierre de esta etapa, la base de datos se encuentra funcional, el modelo de generación de horarios válidos está implementado, y la interfaz cuenta con su estructura básica completa (gestión de cursos, profesores y visualización de horarios), aunque sin conexión entre estos tres componentes.

## 2026-09-13

Completé la integración de los tres componentes del sistema (base de datos, motor de generación de horarios e interfaz gráfica), correspondiente a la versión 0.03 del proyecto.

Durante una revisión exhaustiva de la capa de acceso a datos, necesaria para garantizar su correcto funcionamiento como dependencia directa de la interfaz, identifiqué y corregí varios errores.

En el motor de generación de horarios, incorporé el soporte para restricciones de disponibilidad horaria por profesor. La implementación reutiliza la misma restricción de no superposición ya empleada para las clases: cada bloque de indisponibilidad se modela como un intervalo adicional de duración fija, incorporado al mismo conjunto de intervalos sujeto a la restricción de no-overlap del profesor correspondiente. De esta manera, el solver queda automáticamente impedido de ubicar una clase sobre dicho bloque, sin necesidad de restricciones adicionales. Complementariamente, desarrollé una clase de resultado que traduce la salida del solver a una estructura de datos independiente de la librería de optimización, de forma que la interfaz pueda consumir los resultados sin conocer detalles de su implementación interna.

En la interfaz, completé la integración con la base de datos para la gestión de cursos y profesores (alta, edición y listado), e incorporé una capa de control intermedia responsable de construir las estructuras del motor a partir de los datos almacenados, ejecutar el proceso de resolución y devolver los resultados a la interfaz. Esta capa evita que la interfaz dependa directamente de la librería de optimización. Asimismo, reemplacé la visualización del horario generado por una grilla que se construye dinámicamente en función de los días y horarios efectivamente utilizados.

Quedan documentadas como limitaciones conocidas de esta versión: la duración de los módulos y el rango horario escolar se encuentran definidos como constantes fijas, y las restricciones de disponibilidad se aplican de manera uniforme a todos los días de la semana, sin posibilidad de especificar restricciones por día particular. Ambas limitaciones quedan previstas para versiones posteriores.