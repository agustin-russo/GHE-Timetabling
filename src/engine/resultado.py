"""
Envuelve la salida de Solver.solve() en objetos simples que la UI (o
el controlador) puede recorrer sin saber nada de ortools ni de cómo
está armado el modelo del motor.
"""

from dataclasses import dataclass

from ortools.sat.python import cp_model

from src.engine.availability import minutos_a_hhmm

MINUTOS_POR_DIA = 24 * 60
DIAS = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")


@dataclass
class Clase:
    """Una clase ya ubicada en un horario resuelto."""

    profesor: str
    curso: str
    materia: str
    dia: int
    minuto_inicio: int
    minuto_fin: int

    @property
    def dia_nombre(self) -> str:
        return DIAS[self.dia] if 0 <= self.dia < len(DIAS) else f"Día {self.dia}"

    @property
    def horario_texto(self) -> str:
        return f"{minutos_a_hhmm(self.minuto_inicio)}-{minutos_a_hhmm(self.minuto_fin)}"


class ResultadoHorario:
    """
    Resultado de una corrida del solver, ya traducido a algo que la UI
    puede mostrar directamente. Una vez construido, no depende más del
    solver ni del modelo de ortools.
    """

    ESTADOS_OK = (cp_model.OPTIMAL, cp_model.FEASIBLE)

    def __init__(self, status, solver: cp_model.CpSolver, teachers):
        self.status = status
        self.estado_texto = solver.status_name(status)
        self.clases: list[Clase] = []

        if self.es_valido:
            self._extraer_clases(solver, teachers)

    @property
    def es_valido(self) -> bool:
        return self.status in self.ESTADOS_OK

    def _extraer_clases(self, solver, teachers):
        for teacher in teachers:
            for info in teacher.class_intervals:
                inicio_absoluto = solver.value(info["start"])
                dia, minuto_inicio = divmod(inicio_absoluto, MINUTOS_POR_DIA)

                self.clases.append(Clase(
                    profesor=teacher.name,
                    curso=str(info["course"]),
                    materia=info["subject"] or "",
                    dia=dia,
                    minuto_inicio=minuto_inicio,
                    minuto_fin=minuto_inicio + info["length"],
                ))

    def por_curso(self) -> dict:
        agrupado: dict[str, list[Clase]] = {}
        for clase in self.clases:
            agrupado.setdefault(clase.curso, []).append(clase)
        return agrupado

    def por_profesor(self) -> dict:
        agrupado: dict[str, list[Clase]] = {}
        for clase in self.clases:
            agrupado.setdefault(clase.profesor, []).append(clase)
        return agrupado