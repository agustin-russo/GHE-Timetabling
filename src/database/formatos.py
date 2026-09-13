"""
Conversión entre el texto que carga el usuario en el campo
"Asignaciones" de un profesor y una lista de tuplas fáciles de
guardar en la tabla relacional Asignaciones.

Formato: "Materia,Curso,Cantidad;Materia,Curso,Cantidad;..."
Ejemplo: "Matemática,1ro A,4;Historia,1ro A,2"

"Curso" tiene que matchear exactamente el texto "nivel grado division"
de un curso ya cargado (ver db_handler.obtener_curso_por_texto).
"""


def parsear_asignaciones(texto: str) -> list[tuple[str, str, int]]:
    if not texto:
        return []

    asignaciones = []
    for parte in texto.split(";"):
        parte = parte.strip()
        if not parte:
            continue

        campos = [c.strip() for c in parte.split(",")]
        if len(campos) != 3:
            raise ValueError(f"Asignación inválida: '{parte}'")

        materia, curso, cantidad = campos
        if not materia or not curso:
            raise ValueError(f"Asignación inválida: '{parte}'")

        try:
            cantidad = int(cantidad)
        except ValueError:
            raise ValueError(f"La cantidad de módulos debe ser un número: '{parte}'")

        if cantidad <= 0:
            raise ValueError(f"La cantidad de módulos debe ser mayor a 0: '{parte}'")

        asignaciones.append((materia, curso, cantidad))

    return asignaciones


def formatear_asignaciones(asignaciones: list[tuple[str, str, int]]) -> str:
    return ";".join(f"{materia},{curso},{cantidad}" for materia, curso, cantidad in asignaciones)