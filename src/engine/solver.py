from ortools.sat.python import cp_model

from src.engine.resultado import ResultadoHorario


class Solver:
    def __init__(self, courses, teachers) -> None:
        self.model = cp_model.CpModel()
        self.solver = cp_model.CpSolver()
        self.courses = courses
        self.teachers = teachers

    def initialize_model(self) -> None:
        for teacher in self.teachers:
            teacher.initialize(self.model)

        for course in self.courses:
            course.add_no_overlap(self.model)

    def solve(self) -> ResultadoHorario:
        status = self.solver.solve(self.model)
        return ResultadoHorario(status, self.solver, self.teachers)