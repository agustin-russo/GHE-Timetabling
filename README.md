# GHE - School Timetabling Engine

![Version](https://img.shields.io/badge/version-0.0.1-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-green)
![PySide6](https://img.shields.io/badge/PySide6-planned-yellow)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

GHE (**Generador de Horarios Escolares**) es un motor para la generación automática de horarios escolares. El objetivo del proyecto es desarrollar una herramienta capaz de construir horarios válidos respetando restricciones como la disponibilidad de docentes, la ocupación de cursos y otros criterios propios de una institución educativa.

El desarrollo comenzó con una implementación propia basada en backtracking, utilizada para modelar el problema, validar ideas y experimentar con distintas heurísticas. Una vez consolidado el modelo, el motor evolucionará hacia una implementación basada en CP-SAT (Google OR-Tools), permitiendo resolver instancias reales de manera eficiente y servir como base para la aplicación final.

## Estado actual

Actualmente el proyecto se encuentra en una etapa temprana de desarrollo. Ya cuenta con:

- Implementación de un solver básico mediante backtracking.
- Generación de instancias de prueba simples.
- Sistema de benchmarking simple (tiempo de ejecución y nodos explorados).

### Próximamente

- Heurísticas de búsqueda (MRV, Forward Checking, etc.).
- Implementación mediante OR-Tools CP-SAT.
- Interfaz gráfica desarrollada con **PySide6**.
- Importación y exportación de datos.
- Gestión completa de horarios escolares.

## 📦 Instalación

```bash
git clone https://github.com/agustin-russo/GHE.git
cd GHE
pip install -r requirements.txt
```
