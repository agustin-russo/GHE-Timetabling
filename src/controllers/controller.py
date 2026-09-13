"""
Capa que conecta la UI con el motor de generación de horarios. La UI
nunca importa nada de src.engine directamente: le pide las cosas a
este controlador y recibe un ResultadoHorario ya armado.
"""

from src.database.db_handler import select
from src.engine.availability import parsear_disponibilidad
from src.engine.classes import Course, Teacher
from src.engine.solver import Solver
from src.engine.resultado import ResultadoHorario, MINUTOS_POR_DIA

# La base todavía no guarda la duración de los módulos ni el horario
# escolar, así que por ahora quedan fijos acá. El día que eso se pueda
# configurar desde la UI, esto se reemplaza por esos valores.
DURACION_MODULO = 40          # minutos
DIAS_HABILES = 5
HORA_INICIO_ESCOLAR = 8 * 60  # 08:00
HORA_FIN_ESCOLAR = 13 * 60    # 13:00


def _horarios_de_inicio_posibles():
    """
    Todos los minutos absolutos (offset de día + hora) en los que puede
    arrancar un módulo, repetidos de lunes a viernes.
    """
    posibles = []
    for dia in range(DIAS_HABILES):
        offset = dia * MINUTOS_POR_DIA
        inicio = HORA_INICIO_ESCOLAR
        while inicio + DURACION_MODULO <= HORA_FIN_ESCOLAR:
            posibles.append(offset + inicio)
            inicio += DURACION_MODULO
    return posibles


def _disponibilidad_semanal(texto_disponibilidad):
    """
    Convierte el texto de un profesor en bloqueos repetidos los 5 días
    (ver el aviso en el README/resumen sobre esta simplificación).
    """
    bloques = parsear_disponibilidad(texto_disponibilidad)
    semanal = []
    for dia in range(DIAS_HABILES):
        offset = dia * MINUTOS_POR_DIA
        for inicio, fin in bloques:
            semanal.append((offset + inicio, offset + fin))
    return semanal


class GHEController:
    def __init__(self):
        self._ultimo_resultado = None

    def generar_horarios(self) -> ResultadoHorario:
        cursos_db = select("Cursos")
        profesores_db = select("Profesores")

        if not cursos_db or not profesores_db:
            raise ValueError("Cargá al menos un curso y un profesor antes de generar horarios.")

        cursos = {}
        for fila in cursos_db:
            curso = Course(fila["nivel"], fila["grado"], fila["division"])
            cursos[str(curso)] = curso

        inicios_posibles = _horarios_de_inicio_posibles()
        teachers = []

        for fila_p in profesores_db:
            assignments = []

            for fila_a in select("Asignaciones", None, {"id_profesor": fila_p["id_profesor"]}):
                curso_fila = select("Cursos", None, {"id_curso": fila_a["id_curso"]})
                materia_fila = select("Materias", None, {"id_materia": fila_a["id_materia"]})
                if not curso_fila or not materia_fila:
                    continue

                texto_curso = str(Course(curso_fila[0]["nivel"], curso_fila[0]["grado"], curso_fila[0]["division"]))
                curso = cursos.get(texto_curso)
                if curso is None:
                    continue

                assignments.append({
                    "modules": fila_a["cantidad"],
                    "subject": materia_fila[0]["nombre"],
                    "course": curso,
                    "module_lenght": DURACION_MODULO,
                    "start_times": inicios_posibles,
                })

            disponibilidad = _disponibilidad_semanal(fila_p["disponibilidad"] or "")
            teachers.append(Teacher(fila_p["nombre"], assignments, disponibilidad))

        solver = Solver(list(cursos.values()), teachers)
        solver.initialize_model()
        resultado = solver.solve()

        self._ultimo_resultado = resultado
        return resultado

    @property
    def ultimo_resultado(self):
        return self._ultimo_resultado