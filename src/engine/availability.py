"""
Conversión entre el texto de disponibilidad que carga el usuario en la
UI y los intervalos de minutos que usa el motor.

Cada bloque de texto representa un horario en el que el profesor NO
puede dar clase (no uno en el que sí puede): alcanza con cargar unas
pocas excepciones en vez de tener que listar todo lo que sí está
disponible.

Formato: "HH:MM-HH:MM,HH:MM-HH:MM,..."
Ejemplo: "08:00-09:30,13:00-14:00"
"""

MINUTOS_POR_DIA = 24 * 60
DIAS_A_MINUTOS = {
     "Lunes": 0,
     "Martes": MINUTOS_POR_DIA,
     "Miercoles": MINUTOS_POR_DIA * 2,
     "Jueves": MINUTOS_POR_DIA * 3,
     "Viernes": MINUTOS_POR_DIA * 4,
     "Sabado": MINUTOS_POR_DIA * 5,
     "Domingo": MINUTOS_POR_DIA * 6,
}


def minutos_a_hhmm(minutos: int) -> str:
    minutos = minutos % MINUTOS_POR_DIA
    return f"{minutos // 60:02d}:{minutos % 60:02d}"


def minutos_a_dia(minutos: int) -> str:
     dias = list(DIAS_A_MINUTOS.keys())
     return dias[minutos // MINUTOS_POR_DIA]


def formatear_disponibilidad(bloques: list[tuple[int, int]]) -> str:
    return ",".join(f"{minutos_a_hhmm(i)}-{minutos_a_hhmm(f)}" for i, f in bloques)


def es_disponibilidad_valida(hora1, hora2, dia) -> tuple:
    inicio, fin = (hora1.hour() * 60) + hora1.minute(), (hora2.hour() * 60) + hora2.minute()

    if fin <= inicio:
            return ()
    
    return (inicio + DIAS_A_MINUTOS[dia], fin + DIAS_A_MINUTOS[dia])
