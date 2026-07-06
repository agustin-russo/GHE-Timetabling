import random
from time import perf_counter

random.seed(11)

from backtracking import Disponibilidad, Horario, Profesor, Asignacion, Stats, solve, MRV_LCV


def generar_asignaciones(n_profes=10, ocupacion=0.5):
    dis = Disponibilidad()
    curso1 = Horario(dis)
    curso2 = Horario(dis)

    TOTAL_SLOTS = dis.dias * dis.modulos
    MODULOS_POR_CURSO = int(TOTAL_SLOTS * ocupacion)

    profesores = []
    capacidad = []

    for _ in range(n_profes):
        disponibles = random.randint(10, TOTAL_SLOTS)
        disponibilidad = random.sample(range(TOTAL_SLOTS), disponibles)

        profesores.append(Profesor(disponibilidad))
        capacidad.append(disponibles)

    asignaciones = []

    restantes = MODULOS_POR_CURSO

    while restantes > 0:
        # Profesores que todavía pueden recibir más módulos
        posibles = [i for i in range(n_profes) if capacidad[i] > 0]

        if not posibles:
            raise ValueError(
                "No hay suficiente disponibilidad para generar la instancia."
            )

        i = random.choice(posibles)

        asignaciones.append(Asignacion(i, profesores[i], curso1))
        asignaciones.append(Asignacion(i, profesores[i], curso2))

        capacidad[i] -= 2
        restantes -= 1

    random.shuffle(asignaciones)

    return dis, curso1, curso2, asignaciones


for i in range(1, 11):
    ocupacion =float(i) * 0.1
    dis, curso1, curso2, asignaciones = generar_asignaciones(ocupacion=ocupacion)

    for j in asignaciones:
        j.measure_options()


    print(f"Instancia: \n - 2 cursos \n - 10 profesores \n - Ocupación = {ocupacion:.1f}")
    print("Backtracking MRV y LCV")
    nodos = Stats()
    inicio = perf_counter()
    solucion = MRV_LCV(asignaciones, nodos)

    fin = perf_counter()

    print(f"Nodos: {nodos}")
    print(f"Tiempo: {fin - inicio:.6f} s")

    if solucion:
        print("Tabla: ")
        print(curso1)
        print(curso2)
    else:
        print("No solution")
