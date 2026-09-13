from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QListWidgetItem, QMainWindow, QMessageBox

from src.ui.generated.ghe_main_window import Ui_MainWindow
from src.ui.dialogs import DialogoCurso, DialogoProfesor
from src.ui.schedule_widget import GrillaHorario

from src.database.db_handler import (
    select, insert, update, guardar_asignaciones, obtener_asignaciones_texto,
)
from src.database.formatos import parsear_asignaciones
from src.engine.availability import es_disponibilidad_valida


class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.id_curso_actual = None
        self.id_profesor_actual = None
        self._resultado = None

        self._configurar_grilla_horarios()
        self.cargar_lista_cursos()
        self.cargar_lista_profesores()
        self.configurar_eventos()

    # ------------------------------------------------------------------
    # Cursos
    # ------------------------------------------------------------------

    def cargar_lista_cursos(self):
        self.ui.lista_cursos.clear()
        for fila in select("Cursos"):
            item = QListWidgetItem(f"{fila['nivel']} {fila['grado']} {fila['division']}")
            item.setData(Qt.ItemDataRole.UserRole, fila["id_curso"])
            self.ui.lista_cursos.addItem(item)

    def agregar_curso(self):
        dialogo = DialogoCurso(self)
        if dialogo.exec() != QDialog.DialogCode.Accepted:
            return

        datos = dialogo.datos()
        id_curso = insert("Cursos", datos)

        item = QListWidgetItem(f"{datos['nivel']} {datos['grado']} {datos['division']}")
        item.setData(Qt.ItemDataRole.UserRole, id_curso)
        self.ui.lista_cursos.addItem(item)

    def _al_cambiar_curso(self, actual, _anterior):
        if actual is None:
            return

        self.id_curso_actual = actual.data(Qt.ItemDataRole.UserRole)
        filas = select("Cursos", None, {"id_curso": self.id_curso_actual})
        if not filas:
            return

        fila = filas[0]
        self.ui.input_nivel.setText(fila["nivel"] or "")
        self.ui.input_grado.setText(fila["grado"] or "")
        self.ui.input_division.setText(fila["division"] or "")

    def guardar_curso(self):
        if self.id_curso_actual is None:
            QMessageBox.information(self, "Sin selección", "Elegí un curso de la lista para editarlo.")
            return

        nivel = self.ui.input_nivel.text().strip()
        grado = self.ui.input_grado.text().strip()
        division = self.ui.input_division.text().strip()

        if not (nivel and grado and division):
            QMessageBox.warning(self, "Datos incompletos", "Completá nivel, grado y división.")
            return

        update("Cursos", {"nivel": nivel, "grado": grado, "division": division}, {"id_curso": self.id_curso_actual})

        item = self.ui.lista_cursos.currentItem()
        if item is not None:
            item.setText(f"{nivel} {grado} {division}")

    # ------------------------------------------------------------------
    # Profesores
    # ------------------------------------------------------------------

    def cargar_lista_profesores(self):
        self.ui.lista_profesores.clear()
        for fila in select("Profesores", ("id_profesor", "nombre")):
            item = QListWidgetItem(fila["nombre"])
            item.setData(Qt.ItemDataRole.UserRole, fila["id_profesor"])
            self.ui.lista_profesores.addItem(item)

    def agregar_profesor(self):
        dialogo = DialogoProfesor(self)
        if dialogo.exec() != QDialog.DialogCode.Accepted:
            return

        datos = dialogo.datos()
        id_profesor = insert("Profesores", {
            "nombre": datos["nombre"],
            "disponibilidad": datos["disponibilidad"],
        })

        if datos["asignaciones"]:
            try:
                guardar_asignaciones(id_profesor, parsear_asignaciones(datos["asignaciones"]))
            except ValueError as error:
                QMessageBox.warning(
                    self, "Asignaciones no guardadas",
                    f"El profesor se creó, pero las asignaciones no se pudieron guardar: {error}"
                )

        item = QListWidgetItem(datos["nombre"])
        item.setData(Qt.ItemDataRole.UserRole, id_profesor)
        self.ui.lista_profesores.addItem(item)

    def _al_cambiar_profesor(self, actual, _anterior):
        if actual is None:
            return

        self.id_profesor_actual = actual.data(Qt.ItemDataRole.UserRole)
        filas = select("Profesores", None, {"id_profesor": self.id_profesor_actual})
        if not filas:
            return

        fila = filas[0]
        self.ui.input_nombre.setText(fila["nombre"] or "")
        self.ui.input_disponibilidad.setText(fila["disponibilidad"] or "")
        self.ui.input_asignaciones.setText(obtener_asignaciones_texto(self.id_profesor_actual))

    def guardar_profesor(self):
        if self.id_profesor_actual is None:
            QMessageBox.information(self, "Sin selección", "Elegí un profesor de la lista para editarlo.")
            return

        nombre = self.ui.input_nombre.text().strip()
        texto_disponibilidad = self.ui.input_disponibilidad.text().strip()
        texto_asignaciones = self.ui.input_asignaciones.text().strip()

        if not nombre:
            QMessageBox.warning(self, "Datos incompletos", "Completá el nombre.")
            return

        if not es_disponibilidad_valida(texto_disponibilidad):
            QMessageBox.warning(
                self, "Disponibilidad inválida",
                "Usá el formato HH:MM-HH:MM separando los bloques con comas."
            )
            return

        try:
            asignaciones = parsear_asignaciones(texto_asignaciones)
        except ValueError as error:
            QMessageBox.warning(self, "Asignaciones inválidas", str(error))
            return

        update(
            "Profesores",
            {"nombre": nombre, "disponibilidad": texto_disponibilidad},
            {"id_profesor": self.id_profesor_actual},
        )

        try:
            guardar_asignaciones(self.id_profesor_actual, asignaciones)
        except ValueError as error:
            QMessageBox.warning(self, "Asignaciones inválidas", str(error))
            return

        item = self.ui.lista_profesores.currentItem()
        if item is not None:
            item.setText(nombre)

    # ------------------------------------------------------------------
    # Horarios
    # ------------------------------------------------------------------

    def _configurar_grilla_horarios(self):
        self.ui.gridLayout.removeWidget(self.ui.l_horarios)
        self.ui.l_horarios.hide()

        self.grilla_horario = GrillaHorario(self.ui.caja_ver_horarios)
        self.ui.gridLayout.addWidget(self.grilla_horario, 0, 0)

    def generar_horarios(self):
        self.ui.b_generar_horarios.setEnabled(False)
        try:
            self._resultado = self.controller.generar_horarios()
        except Exception as error:
            QMessageBox.critical(self, "Error al generar", str(error))
            return
        finally:
            self.ui.b_generar_horarios.setEnabled(True)

        if not self._resultado.es_valido:
            QMessageBox.warning(
                self, "No se pudo generar",
                f"No se encontró un horario válido ({self._resultado.estado_texto})."
            )

        self.actualizar_lista_horarios()

    def actualizar_lista_horarios(self):
        self.ui.lista_horarios.clear()
        self.grilla_horario.mostrar([])

        if self._resultado is None or not self._resultado.es_valido:
            return

        agrupado = (
            self._resultado.por_curso()
            if self.ui.b_cursos_horarios.isChecked()
            else self._resultado.por_profesor()
        )
        for nombre in sorted(agrupado):
            self.ui.lista_horarios.addItem(nombre)

    def mostrar_horario_seleccionado(self, item):
        if self._resultado is None:
            return

        nombre = item.text()
        if self.ui.b_cursos_horarios.isChecked():
            clases = self._resultado.por_curso().get(nombre, [])
            self.grilla_horario.mostrar(clases, etiqueta_secundaria="profesor")
        else:
            clases = self._resultado.por_profesor().get(nombre, [])
            self.grilla_horario.mostrar(clases, etiqueta_secundaria="curso")

    # ------------------------------------------------------------------
    # Conexión de señales
    # ------------------------------------------------------------------

    def configurar_eventos(self):
        self.ui.lista_cursos.currentItemChanged.connect(self._al_cambiar_curso)
        self.ui.lista_profesores.currentItemChanged.connect(self._al_cambiar_profesor)

        self.ui.b_agregar_cursos.clicked.connect(self.agregar_curso)
        self.ui.b_guardar_cursos.clicked.connect(self.guardar_curso)

        self.ui.b_agregar_profesor.clicked.connect(self.agregar_profesor)
        self.ui.b_guardar_profesores.clicked.connect(self.guardar_profesor)

        self.ui.b_generar_horarios.clicked.connect(self.generar_horarios)
        self.ui.b_cursos_horarios.toggled.connect(self.actualizar_lista_horarios)
        self.ui.b_profesor_horarios.toggled.connect(self.actualizar_lista_horarios)
        self.ui.lista_horarios.itemClicked.connect(self.mostrar_horario_seleccionado)