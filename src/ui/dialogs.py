from PySide6.QtWidgets import (
    QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QMessageBox, QVBoxLayout,
)

from src.database.db_handler import obtener_curso_por_texto
from src.database.formatos import parsear_asignaciones
from src.engine.availability import es_disponibilidad_valida


class DialogoCurso(QDialog):
    """Alta de un curso nuevo (nivel, grado, división)."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nuevo curso")

        self.input_nivel = QLineEdit(self)
        self.input_grado = QLineEdit(self)
        self.input_division = QLineEdit(self)

        formulario = QFormLayout()
        formulario.addRow("Nivel", self.input_nivel)
        formulario.addRow("Grado/Año", self.input_grado)
        formulario.addRow("División", self.input_division)

        botones = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botones.accepted.connect(self._validar_y_aceptar)
        botones.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(formulario)
        layout.addWidget(botones)

    def _validar_y_aceptar(self):
        if not all((
            self.input_nivel.text().strip(),
            self.input_grado.text().strip(),
            self.input_division.text().strip(),
        )):
            QMessageBox.warning(self, "Datos incompletos", "Completá nivel, grado y división.")
            return

        self.accept()

    def datos(self) -> dict:
        return {
            "nivel": self.input_nivel.text().strip(),
            "grado": self.input_grado.text().strip(),
            "division": self.input_division.text().strip(),
        }


class DialogoProfesor(QDialog):
    """Alta de un profesor nuevo (nombre, asignaciones, disponibilidad)."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nuevo profesor")

        self.input_nombre = QLineEdit(self)

        self.input_asignaciones = QLineEdit(self)
        self.input_asignaciones.setPlaceholderText("Materia,Curso,Cantidad;Materia,Curso,Cantidad")

        self.input_disponibilidad = QLineEdit(self)
        self.input_disponibilidad.setPlaceholderText("08:00-09:30,13:00-14:00")

        formulario = QFormLayout()
        formulario.addRow("Nombre", self.input_nombre)
        formulario.addRow("Asignaciones", self.input_asignaciones)
        formulario.addRow("Disponibilidad", self.input_disponibilidad)

        botones = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        botones.accepted.connect(self._validar_y_aceptar)
        botones.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addLayout(formulario)
        layout.addWidget(botones)

    def _validar_y_aceptar(self):
        if not self.input_nombre.text().strip():
            QMessageBox.warning(self, "Datos incompletos", "Completá el nombre.")
            return

        try:
            asignaciones = parsear_asignaciones(self.input_asignaciones.text())
        except ValueError as error:
            QMessageBox.warning(self, "Asignaciones inválidas", str(error))
            return

        for _, texto_curso, _ in asignaciones:
            if obtener_curso_por_texto(texto_curso) is None:
                QMessageBox.warning(
                    self, "Curso inexistente",
                    f"No existe el curso '{texto_curso}'. Creálo primero en la pestaña Cursos."
                )
                return

        if not es_disponibilidad_valida(self.input_disponibilidad.text()):
            QMessageBox.warning(
                self, "Disponibilidad inválida",
                "Usá el formato HH:MM-HH:MM separando los bloques con comas."
            )
            return

        self.accept()

    def datos(self) -> dict:
        return {
            "nombre": self.input_nombre.text().strip(),
            "asignaciones": self.input_asignaciones.text().strip(),
            "disponibilidad": self.input_disponibilidad.text().strip(),
        }