from ortools.sat.python import cp_model


class Course:
    """
    Representa un curso del colegio.
    """
    def __init__(self, level, grade, division):
        self.level = level
        self.grade = grade
        self.division = division

        self.subjects = []

    def add_subject(self, interval):
        self.subjects.append(interval)

    def add_no_overlap(self, model: cp_model.CpModel):
        model.add_no_overlap(self.subjects)

    def __str__(self) -> str:
        return f"{self.level}_{self.grade}_{self.division}"


class Teacher:
    """
    Representa el perfil de un profesor con su disponibilidad.
    """
    def __init__(self, name, assignments, availability=None):
        """
        name: str, nombre del profesor.
        assignments: list, lista de diccionarios.
        {"modules": x, "subject": s, "course": c (Course()), "module_lenght": l, "start_times": hs}
        availability: list, lista de tuplas (inicio, fin) en minutos.
        Cada tupla es un bloque de tiempo en el que el profesor NO puede
        dar clase. None o lista vacía si no tiene restricciones.
        """
        self.name = name
        self.assignments = assignments
        self.availability = availability or []

        self.intervals = []        # todos los intervalos (clases + bloqueos): se usa para el no_overlap
        self.class_intervals = []  # sólo las clases, con su metadata: se usa para leer resultados

    def initialize(self, model: cp_model.CpModel):
        for assignment in self.assignments:
            course = assignment["course"]
            domain = cp_model.Domain.FromValues(assignment["start_times"])

            for module in range(assignment["modules"]):
                start = model.new_int_var_from_domain(domain, f"start_{course}_{module}_{self.name}")
                interval = model.new_fixed_size_interval_var(
                    start, assignment["module_lenght"], f"interval_{course}_{module}_{self.name}"
                )

                self.intervals.append(interval)
                self.class_intervals.append({
                    "start": start,
                    "length": assignment["module_lenght"],
                    "course": course,
                    "subject": assignment.get("subject"),
                })
                course.add_subject(interval)


        for i, (inicio, fin) in enumerate(self.availability):
            bloqueo = model.new_fixed_size_interval_var(inicio, fin - inicio, f"bloqueo_{self.name}_{i}")
            self.intervals.append(bloqueo)

        model.add_no_overlap(self.intervals)

    def __str__(self) -> str:
        return self.name