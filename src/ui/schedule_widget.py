from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView, QHeaderView, QLabel, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget,
)

from src.engine.availability import minutos_a_hhmm
from src.engine.resultado import Clase, DIAS


class GrillaHorario(QWidget):
    """
    Grilla semanal (días x horarios) que muestra las clases de un curso
    o de un profesor. Se arma dinámicamente a partir de los horarios
    que efectivamente aparecen en las clases recibidas: no asume una
    cantidad fija de días ni de módulos.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.tabla = QTableWidget(self)
        self.tabla.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tabla.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        layout.addWidget(self.tabla)

        self.aviso_vacio = QLabel("Todavía no hay un horario generado para mostrar.", self)
        self.aviso_vacio.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.aviso_vacio)

        self.tabla.hide()

    def mostrar(self, clases: list[Clase], etiqueta_secundaria: str = "curso"):
        """
        clases: lista de Clase a mostrar (ya filtradas para un curso o
        un profesor puntual).
        etiqueta_secundaria: qué mostrar en cada celda además de la
        materia. "curso" cuando se está viendo el horario de un
        profesor, "profesor" cuando se está viendo el de un curso.
        """
        if not clases:
            self.tabla.clear()
            self.tabla.setRowCount(0)
            self.tabla.setColumnCount(0)
            self.tabla.hide()
            self.aviso_vacio.show()
            return

        self.aviso_vacio.hide()
        self.tabla.show()

        dias_usados = sorted({clase.dia for clase in clases})
        inicios_usados = sorted({clase.minuto_inicio for clase in clases})

        self.tabla.setColumnCount(len(dias_usados))
        self.tabla.setHorizontalHeaderLabels([
            DIAS[dia] if dia < len(DIAS) else f"Día {dia}" for dia in dias_usados
        ])

        self.tabla.setRowCount(len(inicios_usados))
        self.tabla.setVerticalHeaderLabels([minutos_a_hhmm(m) for m in inicios_usados])

        columna_de_dia = {dia: i for i, dia in enumerate(dias_usados)}
        fila_de_inicio = {inicio: i for i, inicio in enumerate(inicios_usados)}

        for clase in clases:
            fila = fila_de_inicio[clase.minuto_inicio]
            columna = columna_de_dia[clase.dia]

            secundaria = clase.curso if etiqueta_secundaria == "curso" else clase.profesor
            texto = clase.materia or "(sin materia)"
            if secundaria:
                texto += f"\n{secundaria}"

            item = QTableWidgetItem(texto)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tabla.setItem(fila, columna, item)

        self.tabla.resizeRowsToContents()
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)