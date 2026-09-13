import sqlite3
from pathlib import Path

from src.database.formatos import formatear_asignaciones

DIR = Path(__file__).resolve().parent
ROOT = DIR.parent.parent
DB = ROOT / "data" / "GHE.db"

# Cada tupla incluye la PK como primer elemento, para que insert/select/update
# puedan validar columnas de forma genérica sin tener que tratar la PK
# distinto en cada tabla.
TABLAS = {
    "Profesores": ("id_profesor", "nombre", "disponibilidad"),
    "Cursos": ("id_curso", "nivel", "grado", "division"),
    "Materias": ("id_materia", "nombre"),
    "Horarios": ("id_horario", "id_profesor", "id_curso", "minuto_inicio", "minuto_fin"),
    "Asignaciones": ("id_asignacion", "id_profesor", "id_curso", "id_materia", "cantidad"),
}

TABLAS_UI = [
    "Cursos", "Profesores",
]


def obtener_conexion():
    conexion = sqlite3.connect(DB)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def init_db():
    DB.parent.mkdir(parents=True, exist_ok=True)

    with obtener_conexion() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS Materias (
                id_materia INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Profesores (
                id_profesor INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                disponibilidad TEXT
            );

            CREATE TABLE IF NOT EXISTS Cursos (
                id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
                nivel TEXT NOT NULL,
                grado TEXT NOT NULL,
                division TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Asignaciones (
                id_asignacion INTEGER PRIMARY KEY AUTOINCREMENT,
                id_profesor INTEGER,
                id_curso INTEGER,
                id_materia INTEGER,
                cantidad INTEGER,
                FOREIGN KEY (id_profesor) REFERENCES Profesores(id_profesor),
                FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso),
                FOREIGN KEY (id_materia) REFERENCES Materias(id_materia)
            );

            CREATE TABLE IF NOT EXISTS Horarios (
                id_horario INTEGER PRIMARY KEY AUTOINCREMENT,
                id_profesor INTEGER,
                id_curso INTEGER,
                minuto_inicio INTEGER,
                minuto_fin INTEGER,
                FOREIGN KEY (id_profesor) REFERENCES Profesores(id_profesor),
                FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
            );
        """)


def _ejecutar(sql, params=(), fetchall=False):
    """
    Centraliza la apertura/cierre de conexión y el commit para que
    select/insert/update/delete no repitan la misma lógica. Devuelve
    las filas si fetchall=True, o el lastrowid en caso contrario.
    """
    conn = obtener_conexion()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params)
        resultado = cursor.fetchall() if fetchall else cursor.lastrowid
        conn.commit()
        return resultado
    finally:
        conn.close()


def select(tabla, campos=None, filtros=None):
    if tabla not in TABLAS:
        raise ValueError("Tabla no válida")

    if campos:
        if not set(campos).issubset(TABLAS[tabla]):
            raise ValueError(f"Columnas inválidas para {tabla}: {campos}")
        select_clause = ", ".join(campos)
    else:
        select_clause = "*"

    if filtros:
        where_clause = " WHERE " + " AND ".join(f"{campo} = ?" for campo in filtros)
        params = list(filtros.values())
    else:
        where_clause = ""
        params = []

    sql = f"SELECT {select_clause} FROM {tabla}{where_clause}"
    return _ejecutar(sql, params, fetchall=True)


def insert(tabla, datos):
    """Devuelve el id (autoincrement) de la fila insertada."""
    if tabla not in TABLAS:
        raise ValueError("Tabla no válida")

    columnas = list(datos.keys())
    if not set(columnas).issubset(TABLAS[tabla]):
        raise ValueError(f"Columnas inválidas para {tabla}: {columnas}")

    placeholders = ", ".join("?" for _ in columnas)
    columnas_sql = ", ".join(columnas)

    sql = f"INSERT INTO {tabla} ({columnas_sql}) VALUES ({placeholders})"
    return _ejecutar(sql, list(datos.values()))


def update(tabla, datos, filtros):
    """
    datos: diccionario {campo: valor_nuevo}.
    filtros: diccionario {campo: valor_a_buscar}.
    """
    if tabla not in TABLAS:
        raise ValueError("Tabla no válida")

    if not set(datos.keys()).issubset(TABLAS[tabla]):
        raise ValueError(f"Columnas inválidas para {tabla}: {list(datos.keys())}")

    set_clause = ", ".join(f"{campo} = ?" for campo in datos)
    where_clause = " AND ".join(f"{campo} = ?" for campo in filtros)
    valores = list(datos.values()) + list(filtros.values())

    sql = f"UPDATE {tabla} SET {set_clause} WHERE {where_clause}"
    _ejecutar(sql, valores)


def delete(tabla, filtros=None):
    if tabla not in TABLAS:
        raise ValueError("Tabla no válida")

    if filtros:
        where_clause = " WHERE " + " AND ".join(f"{campo} = ?" for campo in filtros)
        params = list(filtros.values())
    else:
        where_clause = ""
        params = []

    sql = f"DELETE FROM {tabla}{where_clause}"
    _ejecutar(sql, params)


# ---------------------------------------------------------------------------
# Helpers para las "Asignaciones" de un profesor. La UI las edita como un
# texto simple (ver src/database/formatos.py); acá se traducen a filas
# reales en la tabla relacional Asignaciones.
# ---------------------------------------------------------------------------

def obtener_o_crear_materia(nombre: str) -> int:
    filas = select("Materias", ("id_materia",), {"nombre": nombre})
    if filas:
        return filas[0]["id_materia"]
    return insert("Materias", {"nombre": nombre})


def obtener_curso_por_texto(texto_curso: str):
    """Busca un curso por su representación 'nivel grado division'."""
    for fila in select("Cursos"):
        if f"{fila['nivel']} {fila['grado']} {fila['division']}" == texto_curso:
            return fila["id_curso"]
    return None


def guardar_asignaciones(id_profesor: int, asignaciones):
    """
    asignaciones: lista de tuplas (nombre_materia, texto_curso, cantidad).
    Reemplaza todas las asignaciones actuales del profesor por estas.
    """
    delete("Asignaciones", {"id_profesor": id_profesor})
    for nombre_materia, texto_curso, cantidad in asignaciones:
        id_materia = obtener_o_crear_materia(nombre_materia)
        id_curso = obtener_curso_por_texto(texto_curso)
        if id_curso is None:
            raise ValueError(f"No existe el curso '{texto_curso}'")

        insert("Asignaciones", {
            "id_profesor": id_profesor,
            "id_curso": id_curso,
            "id_materia": id_materia,
            "cantidad": cantidad,
        })


def obtener_asignaciones_texto(id_profesor: int) -> str:
    partes = []
    for fila in select("Asignaciones", None, {"id_profesor": id_profesor}):
        materia = select("Materias", ("nombre",), {"id_materia": fila["id_materia"]})
        curso = select("Cursos", None, {"id_curso": fila["id_curso"]})
        if not materia or not curso:
            continue

        texto_curso = f"{curso[0]['nivel']} {curso[0]['grado']} {curso[0]['division']}"
        partes.append((materia[0]["nombre"], texto_curso, fila["cantidad"]))

    return formatear_asignaciones(partes)

