# GHE - School Timetabling Engine

![Version](https://img.shields.io/badge/version-0.03-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-green)
![PySide6](https://img.shields.io/badge/PySide6-implemented-brightgreen)
![OR-Tools](https://img.shields.io/badge/OR--Tools-CP--SAT-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

GHE (**Generador de Horarios Escolares**) es un motor para la generación automática de horarios escolares. El objetivo del proyecto es desarrollar una herramienta capaz de construir horarios válidos respetando restricciones como la disponibilidad de docentes, la ocupación de cursos y otros criterios propios de una institución educativa.

El desarrollo comenzó con una implementación propia basada en backtracking, utilizada para modelar el problema y experimentar con distintas heurísticas de búsqueda (MRV, LCV). Este proceso permitió validar el modelo del problema y sirvió como base conceptual para el motor definitivo, implementado actualmente con CP-SAT (Google OR-Tools) mediante variables de intervalo, lo que permite representar correctamente asignaciones docentes con distintos horarios de inicio y fin.

## Estado actual

El proyecto se encuentra en una etapa funcional temprana: las tres capas principales (datos, motor y presentación) están implementadas e integradas entre sí, aunque con varias limitaciones y simplificaciones propias de un prototipo.

- **Motor de generación de horarios** (OR-Tools / CP-SAT): genera horarios válidos mediante variables de intervalo, contemplando restricciones de no superposición entre clases y bloques de indisponibilidad horaria por docente. Todavía no incorpora un criterio de optimización (encuentra una solución válida, no necesariamente la mejor).
- **Base de datos** (SQLite): gestión de cursos, docentes, materias y asignaciones.
- **Interfaz gráfica** (PySide6 + Qt Designer): alta, edición y listado de cursos y docentes. Generación de horarios desde la interfaz y visualización en una grilla semanal construida dinámicamente.
- **Capa de control**: conecta la interfaz con el motor sin acoplarlas directamente, permitiendo evolucionar cada componente de forma independiente.

### Próximamente

- Horarios óptimos (no solo válidos) mediante una función objetivo en CP-SAT.
- Configuración de la duración de módulos y del horario escolar (actualmente definidos como constantes fijas).
- Restricciones de disponibilidad por día específico (actualmente se aplican de forma uniforme a toda la semana).
- Editor relacional para las asignaciones docentes (actualmente se cargan mediante un formato de texto simplificado).
- Mejoras visuales de la interfaz.
- Importación y exportación de datos.

## Estructura del proyecto

```
GHE/
├── main.py                # Punto de entrada de la aplicación
├── src/
│   ├── database/           # Acceso a datos (SQLite)
│   ├── engine/              # Modelo y motor de resolución (OR-Tools)
│   ├── controllers/         # Capa de control entre la interfaz y el motor
│   └── ui/                  # Interfaz gráfica (PySide6)
├── data/                   # Base de datos SQLite, generada en tiempo de ejecución (no versionada)
└── tests/                  # Pruebas (no versionadas)
```

## 📦 Instalación

```bash
git clone https://github.com/agustin-russo/GHE.git
cd GHE
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

La base de datos se crea automáticamente en `data/GHE.db` la primera vez que se ejecuta la aplicación.