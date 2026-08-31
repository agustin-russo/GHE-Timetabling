from ortools.sat.python import cp_model

class Profesor:
    """
    Representa el perfil de un profesor con su disponibilidad.
    """
    def __init__(self, name, assignments, availability):
        """
        name: str, nombre del profesor.
        assignments: list, lista de diccionarios.
        {"modules": x, "subject": s, "course": c, "module_lenght": l, start_times": hs}
        availability: list, lista de tuplas, intervalos de tiempo que el profesor tiene disponibles.
        (start, end)
        """
        self.name = name
        self.assignments = assignments
        self.availability = availability
        self.intervals = []

    def initialize(self, model: cp_model.CpModel):
        for assignment in self.assignments:
            for module in range(assignment["modules"]):
                domain = cp_model.Domain.FromValues(assignment["start_times"])
                start = model.new_int_var_from_domain(domain, f"start_{module}_{self.name}")
                interval = model.new_fixed_size_interval_var(start, assignment["module_lenght"], f"interval_{assignment["course"]}_{module}_{self.name}")

                self.intervals.append(interval)

    