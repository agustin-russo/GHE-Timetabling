class Disponibilidad:
    def __init__(self, dias=5, modulos=12):
        self.dias = dias
        self.modulos = modulos
        self.usados = [[] for _ in range(modulos * dias)]

    
    def disponibilidad(self, asg):
        for n, i in enumerate(asg.profesor.disponibilidad):
            self.usados[i].append((asg, n))


    def update(self, indice, delta):
        for asg, n in self.usados[indice]:
            asg.ranking += delta
            asg.options[n][0] += delta


class Horario:
    def __init__(self, disponibilidad: Disponibilidad):
        self.dis = disponibilidad
        self.horario = [-1] * (self.dis.modulos * self.dis.dias)
        

    def __str__(self):
        s = ""
        for i, materia in enumerate(self.horario):
            s += f"{materia:2} "
            if (i + 1) % self.dis.modulos == 0:
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

        self.curso.dis.disponibilidad(self)

        self.ranking = len(profesor.disponibilidad)
        self.options = [] # Hay que inicializarlas cuando esten todas las asignaciones creadas
        self.asignada = False


    def measure_options(self):
        for n, i in enumerate(self.profesor.disponibilidad):
            self.options.append([len(self.curso.dis.usados[i]), n])

    
    def __lt__(self, other):
        return self.ranking < other.ranking



class Stats:
    def __init__(self):
        self.nodos = 0

    
    def __str__(self) -> str:
        return str(self.nodos)


def solve(indice, asignaciones, stats):
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


def MRV_LCV(pendientes, stats):
    stats.nodos += 1
    if not pendientes:  # Si la lista está vacía, terminamos
        return True

    asg = min(pendientes) 

    idx = pendientes.index(asg)
    pendientes[idx], pendientes[-1] = pendientes[-1], pendientes[idx]
    pendientes.pop()
    
    profe = asg.profesor
    
    for _, i in sorted(asg.options):
        slot = profe.disponibilidad[i]

        if profe.usados[i] or asg.curso.horario[slot] != -1:
            continue

        profe.usados[i] = True
        asg.curso.horario[slot] = asg.materia
        asg.curso.dis.update(slot, -1)
        asg.asignada = True

        if MRV_LCV(pendientes, stats):
            return True

        # Backtrack
        profe.usados[i] = False
        asg.curso.horario[slot] = -1
        asg.curso.dis.update(slot, 1)
        asg.asignada = False

    pendientes.append(asg)
    return False


