class Horario:
    def __init__(self, dias=5, modulos=12):
        self.dias = dias
        self.modulos = modulos
        self.horario = [-1] * (modulos * dias)


    def add(self, dia, hora, materia):
        self.horario[dia][hora] = materia
    

    def remove(self, dia, hora):
        self.horario[dia][hora] = -1

    def __str__(self):
        s = ""
        for i, materia in enumerate(self.horario):
            s += f"{materia:2} "
            if (i + 1) % self.modulos == 0:
                s += "\n"
        return s


class Profesor:
    """
    Representa el perfil de un profesor con su disponibilidad. Algo redundante por ahora, pero después para ver
    o manejar profesores en una base de datos va a ser más cómodo.
    """
    def __init__(self, disponibilidad: list):
        self.disponibilidad = disponibilidad
        """
        [hora 1, hora 2, hora 3, ...]
        hora = dia * 12  + modulo
        """
        self.usados = [False] * len(disponibilidad)

    

class Asignacion:
    """
    Representa 1 modulo de 1 materia dada por 1 profesor en específico.
    """
    def __init__(self, materia: int, profesor: Profesor, curso: Horario):
        self.materia = materia
        self.profesor = profesor
        self.curso = curso


class Stats:
    def __init__(self):
        self.nodos = 0

    
    def __str__(self) -> str:
        return str(self.nodos)


def solve(indice, asignaciones, stats):
    global nodos
    stats.nodos += 1
    if (indice == len(asignaciones)):
        return True
    
    asg = asignaciones[indice]
    profe = asg.profesor
    
    for i in range(len(profe.usados)):
        slot = profe.disponibilidad[i]

        if profe.usados[i]:
            continue

        if asg.curso.horario[slot] != -1:
            continue

        profe.usados[i] = True
        asg.curso.horario[slot] = asg.materia

        if solve(indice + 1, asignaciones, stats):
            return True

        profe.usados[i] = False
        asg.curso.horario[slot] = -1

    return False

