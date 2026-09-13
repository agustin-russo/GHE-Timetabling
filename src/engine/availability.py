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


def hhmm_a_minutos(hhmm: str) -> int:
    horas, minutos = hhmm.strip().split(":")
    return int(horas) * 60 + int(minutos)


def minutos_a_hhmm(minutos: int) -> str:
    minutos = minutos % MINUTOS_POR_DIA
    return f"{minutos // 60:02d}:{minutos % 60:02d}"


def parsear_disponibilidad(texto: str) -> list[tuple[int, int]]:
    if not texto:
        return []

    bloques = []
    for parte in texto.split(","):
        parte = parte.strip()
        if not parte:
            continue

        try:
            inicio_str, fin_str = parte.split("-")
            inicio, fin = hhmm_a_minutos(inicio_str), hhmm_a_minutos(fin_str)
        except (ValueError, AttributeError):
            raise ValueError(f"Bloque de disponibilidad inválido: '{parte}'")

        if fin <= inicio:
            raise ValueError(f"El bloque '{parte}' termina antes de empezar")

        bloques.append((inicio, fin))

    return bloques


def formatear_disponibilidad(bloques: list[tuple[int, int]]) -> str:
    return ",".join(f"{minutos_a_hhmm(i)}-{minutos_a_hhmm(f)}" for i, f in bloques)


def es_disponibilidad_valida(texto: str) -> bool:
    try:
        parsear_disponibilidad(texto)
        return True
    except ValueError:
        return False