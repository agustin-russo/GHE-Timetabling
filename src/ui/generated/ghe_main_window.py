# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ghe_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTimeEdit, QVBoxLayout, QWidget)
import src.ui.generated.main_logos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(799, 600)
        icon = QIcon()
        icon.addFile(u":/main/box.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.ventana_cursos = QWidget()
        self.ventana_cursos.setObjectName(u"ventana_cursos")
        self.horizontalLayout_2 = QHBoxLayout(self.ventana_cursos)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.caja_seleccion_cursos = QGroupBox(self.ventana_cursos)
        self.caja_seleccion_cursos.setObjectName(u"caja_seleccion_cursos")
        self.verticalLayout = QVBoxLayout(self.caja_seleccion_cursos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.b_agregar_cursos = QPushButton(self.caja_seleccion_cursos)
        self.b_agregar_cursos.setObjectName(u"b_agregar_cursos")

        self.verticalLayout.addWidget(self.b_agregar_cursos)

        self.lista_cursos = QListWidget(self.caja_seleccion_cursos)
        self.lista_cursos.setObjectName(u"lista_cursos")

        self.verticalLayout.addWidget(self.lista_cursos)


        self.horizontalLayout_2.addWidget(self.caja_seleccion_cursos)

        self.caja_edicion_cursos = QGroupBox(self.ventana_cursos)
        self.caja_edicion_cursos.setObjectName(u"caja_edicion_cursos")
        self.verticalLayout_4 = QVBoxLayout(self.caja_edicion_cursos)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.caja_nivel_cursos = QWidget(self.caja_edicion_cursos)
        self.caja_nivel_cursos.setObjectName(u"caja_nivel_cursos")
        self.horizontalLayout_8 = QHBoxLayout(self.caja_nivel_cursos)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.l_nivel = QLabel(self.caja_nivel_cursos)
        self.l_nivel.setObjectName(u"l_nivel")

        self.horizontalLayout_8.addWidget(self.l_nivel)

        self.input_nivel = QLineEdit(self.caja_nivel_cursos)
        self.input_nivel.setObjectName(u"input_nivel")

        self.horizontalLayout_8.addWidget(self.input_nivel)


        self.verticalLayout_4.addWidget(self.caja_nivel_cursos)

        self.caja_grado_cursos = QWidget(self.caja_edicion_cursos)
        self.caja_grado_cursos.setObjectName(u"caja_grado_cursos")
        self.horizontalLayout_9 = QHBoxLayout(self.caja_grado_cursos)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.l_grado = QLabel(self.caja_grado_cursos)
        self.l_grado.setObjectName(u"l_grado")

        self.horizontalLayout_9.addWidget(self.l_grado)

        self.input_grado = QLineEdit(self.caja_grado_cursos)
        self.input_grado.setObjectName(u"input_grado")

        self.horizontalLayout_9.addWidget(self.input_grado)


        self.verticalLayout_4.addWidget(self.caja_grado_cursos)

        self.caja_division_cursos = QWidget(self.caja_edicion_cursos)
        self.caja_division_cursos.setObjectName(u"caja_division_cursos")
        self.horizontalLayout_10 = QHBoxLayout(self.caja_division_cursos)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.l_division = QLabel(self.caja_division_cursos)
        self.l_division.setObjectName(u"l_division")

        self.horizontalLayout_10.addWidget(self.l_division)

        self.input_division = QLineEdit(self.caja_division_cursos)
        self.input_division.setObjectName(u"input_division")

        self.horizontalLayout_10.addWidget(self.input_division)


        self.verticalLayout_4.addWidget(self.caja_division_cursos)

        self.b_guardar_cursos = QPushButton(self.caja_edicion_cursos)
        self.b_guardar_cursos.setObjectName(u"b_guardar_cursos")

        self.verticalLayout_4.addWidget(self.b_guardar_cursos)


        self.horizontalLayout_2.addWidget(self.caja_edicion_cursos)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.tabWidget.addTab(self.ventana_cursos, "")
        self.ventana_profesores = QWidget()
        self.ventana_profesores.setObjectName(u"ventana_profesores")
        self.horizontalLayout_3 = QHBoxLayout(self.ventana_profesores)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.caja_seleccion_profesores = QGroupBox(self.ventana_profesores)
        self.caja_seleccion_profesores.setObjectName(u"caja_seleccion_profesores")
        self.verticalLayout_2 = QVBoxLayout(self.caja_seleccion_profesores)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.b_agregar_profesor = QPushButton(self.caja_seleccion_profesores)
        self.b_agregar_profesor.setObjectName(u"b_agregar_profesor")

        self.verticalLayout_2.addWidget(self.b_agregar_profesor)

        self.lista_profesores = QListWidget(self.caja_seleccion_profesores)
        self.lista_profesores.setObjectName(u"lista_profesores")

        self.verticalLayout_2.addWidget(self.lista_profesores)


        self.horizontalLayout_3.addWidget(self.caja_seleccion_profesores)

        self.caja_edicion_profesores = QGroupBox(self.ventana_profesores)
        self.caja_edicion_profesores.setObjectName(u"caja_edicion_profesores")
        self.verticalLayout_6 = QVBoxLayout(self.caja_edicion_profesores)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.caja_nombre_profesores = QWidget(self.caja_edicion_profesores)
        self.caja_nombre_profesores.setObjectName(u"caja_nombre_profesores")
        self.horizontalLayout_13 = QHBoxLayout(self.caja_nombre_profesores)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.l_nombre = QLabel(self.caja_nombre_profesores)
        self.l_nombre.setObjectName(u"l_nombre")

        self.horizontalLayout_13.addWidget(self.l_nombre)

        self.input_nombre = QLineEdit(self.caja_nombre_profesores)
        self.input_nombre.setObjectName(u"input_nombre")

        self.horizontalLayout_13.addWidget(self.input_nombre)


        self.verticalLayout_6.addWidget(self.caja_nombre_profesores)

        self.caja_asignaciones_profesores = QWidget(self.caja_edicion_profesores)
        self.caja_asignaciones_profesores.setObjectName(u"caja_asignaciones_profesores")
        self.horizontalLayout_12 = QHBoxLayout(self.caja_asignaciones_profesores)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.l_asignaciones = QLabel(self.caja_asignaciones_profesores)
        self.l_asignaciones.setObjectName(u"l_asignaciones")

        self.horizontalLayout_12.addWidget(self.l_asignaciones)

        self.input_asignaciones = QLineEdit(self.caja_asignaciones_profesores)
        self.input_asignaciones.setObjectName(u"input_asignaciones")

        self.horizontalLayout_12.addWidget(self.input_asignaciones)


        self.verticalLayout_6.addWidget(self.caja_asignaciones_profesores)

        self.caja_disponibilidad_profesores = QWidget(self.caja_edicion_profesores)
        self.caja_disponibilidad_profesores.setObjectName(u"caja_disponibilidad_profesores")
        self.horizontalLayout_11 = QHBoxLayout(self.caja_disponibilidad_profesores)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget = QWidget(self.caja_disponibilidad_profesores)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.l_disponibilidad = QLabel(self.widget)
        self.l_disponibilidad.setObjectName(u"l_disponibilidad")

        self.verticalLayout_8.addWidget(self.l_disponibilidad)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 5)

        self.horizontalLayout_11.addWidget(self.widget)

        self.caja_edicion_disponibilidad = QWidget(self.caja_disponibilidad_profesores)
        self.caja_edicion_disponibilidad.setObjectName(u"caja_edicion_disponibilidad")
        self.verticalLayout_7 = QVBoxLayout(self.caja_edicion_disponibilidad)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.caja_agregar_disponibilidad = QWidget(self.caja_edicion_disponibilidad)
        self.caja_agregar_disponibilidad.setObjectName(u"caja_agregar_disponibilidad")
        self.horizontalLayout_14 = QHBoxLayout(self.caja_agregar_disponibilidad)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label = QLabel(self.caja_agregar_disponibilidad)
        self.label.setObjectName(u"label")

        self.horizontalLayout_14.addWidget(self.label)

        self.input_hora_inicio_disponibilidad = QTimeEdit(self.caja_agregar_disponibilidad)
        self.input_hora_inicio_disponibilidad.setObjectName(u"input_hora_inicio_disponibilidad")
        self.input_hora_inicio_disponibilidad.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_14.addWidget(self.input_hora_inicio_disponibilidad)

        self.label_2 = QLabel(self.caja_agregar_disponibilidad)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_14.addWidget(self.label_2)

        self.input_hora_fin_disponibilidad = QTimeEdit(self.caja_agregar_disponibilidad)
        self.input_hora_fin_disponibilidad.setObjectName(u"input_hora_fin_disponibilidad")

        self.horizontalLayout_14.addWidget(self.input_hora_fin_disponibilidad)

        self.cb_fechas_disponibilidad = QComboBox(self.caja_agregar_disponibilidad)
        self.cb_fechas_disponibilidad.addItem("")
        self.cb_fechas_disponibilidad.addItem("")
        self.cb_fechas_disponibilidad.addItem("")
        self.cb_fechas_disponibilidad.addItem("")
        self.cb_fechas_disponibilidad.addItem("")
        self.cb_fechas_disponibilidad.setObjectName(u"cb_fechas_disponibilidad")

        self.horizontalLayout_14.addWidget(self.cb_fechas_disponibilidad)

        self.b_agregar_disponibilidad = QPushButton(self.caja_agregar_disponibilidad)
        self.b_agregar_disponibilidad.setObjectName(u"b_agregar_disponibilidad")

        self.horizontalLayout_14.addWidget(self.b_agregar_disponibilidad)


        self.verticalLayout_7.addWidget(self.caja_agregar_disponibilidad)

        self.lista_disponibilidades = QListWidget(self.caja_edicion_disponibilidad)
        self.lista_disponibilidades.setObjectName(u"lista_disponibilidades")

        self.verticalLayout_7.addWidget(self.lista_disponibilidades)


        self.horizontalLayout_11.addWidget(self.caja_edicion_disponibilidad)


        self.verticalLayout_6.addWidget(self.caja_disponibilidad_profesores)

        self.b_guardar_profesores = QPushButton(self.caja_edicion_profesores)
        self.b_guardar_profesores.setObjectName(u"b_guardar_profesores")

        self.verticalLayout_6.addWidget(self.b_guardar_profesores)


        self.horizontalLayout_3.addWidget(self.caja_edicion_profesores)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.tabWidget.addTab(self.ventana_profesores, "")
        self.ventana_horarios = QWidget()
        self.ventana_horarios.setObjectName(u"ventana_horarios")
        self.horizontalLayout_7 = QHBoxLayout(self.ventana_horarios)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.caja_izquierda_horarios = QGroupBox(self.ventana_horarios)
        self.caja_izquierda_horarios.setObjectName(u"caja_izquierda_horarios")
        self.horizontalLayout_6 = QHBoxLayout(self.caja_izquierda_horarios)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.caja_seleccion_horarios = QGroupBox(self.caja_izquierda_horarios)
        self.caja_seleccion_horarios.setObjectName(u"caja_seleccion_horarios")
        self.verticalLayout_3 = QVBoxLayout(self.caja_seleccion_horarios)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.caja_botones_horarios = QGroupBox(self.caja_seleccion_horarios)
        self.caja_botones_horarios.setObjectName(u"caja_botones_horarios")
        self.horizontalLayout_5 = QHBoxLayout(self.caja_botones_horarios)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, -1)
        self.b_cursos_horarios = QRadioButton(self.caja_botones_horarios)
        self.b_cursos_horarios.setObjectName(u"b_cursos_horarios")
        self.b_cursos_horarios.setChecked(True)

        self.horizontalLayout_5.addWidget(self.b_cursos_horarios)

        self.b_profesor_horarios = QRadioButton(self.caja_botones_horarios)
        self.b_profesor_horarios.setObjectName(u"b_profesor_horarios")

        self.horizontalLayout_5.addWidget(self.b_profesor_horarios)


        self.verticalLayout_3.addWidget(self.caja_botones_horarios)

        self.lista_horarios = QListWidget(self.caja_seleccion_horarios)
        self.lista_horarios.setObjectName(u"lista_horarios")

        self.verticalLayout_3.addWidget(self.lista_horarios)


        self.horizontalLayout_6.addWidget(self.caja_seleccion_horarios)

        self.horizontalLayout_6.setStretch(0, 1)

        self.horizontalLayout_7.addWidget(self.caja_izquierda_horarios)

        self.caja_derecha_horarios = QGroupBox(self.ventana_horarios)
        self.caja_derecha_horarios.setObjectName(u"caja_derecha_horarios")
        self.verticalLayout_5 = QVBoxLayout(self.caja_derecha_horarios)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.caja_generacion_horarios = QGroupBox(self.caja_derecha_horarios)
        self.caja_generacion_horarios.setObjectName(u"caja_generacion_horarios")
        self.horizontalLayout_4 = QHBoxLayout(self.caja_generacion_horarios)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.separador_horarios = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.separador_horarios)

        self.b_generar_horarios = QPushButton(self.caja_generacion_horarios)
        self.b_generar_horarios.setObjectName(u"b_generar_horarios")

        self.horizontalLayout_4.addWidget(self.b_generar_horarios)


        self.verticalLayout_5.addWidget(self.caja_generacion_horarios)

        self.caja_ver_horarios = QGroupBox(self.caja_derecha_horarios)
        self.caja_ver_horarios.setObjectName(u"caja_ver_horarios")
        self.gridLayout = QGridLayout(self.caja_ver_horarios)
        self.gridLayout.setObjectName(u"gridLayout")
        self.l_horarios = QLabel(self.caja_ver_horarios)
        self.l_horarios.setObjectName(u"l_horarios")

        self.gridLayout.addWidget(self.l_horarios, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.caja_ver_horarios)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 10)

        self.horizontalLayout_7.addWidget(self.caja_derecha_horarios)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.tabWidget.addTab(self.ventana_horarios, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 799, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GHE", None))
        self.caja_seleccion_cursos.setTitle("")
        self.b_agregar_cursos.setText(QCoreApplication.translate("MainWindow", u"Agregar Curso", None))
        self.caja_edicion_cursos.setTitle("")
        self.l_nivel.setText(QCoreApplication.translate("MainWindow", u"Nivel", None))
        self.l_grado.setText(QCoreApplication.translate("MainWindow", u"Grado/A\u00f1o", None))
        self.l_division.setText(QCoreApplication.translate("MainWindow", u"Divisi\u00f3n", None))
        self.b_guardar_cursos.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ventana_cursos), QCoreApplication.translate("MainWindow", u"Cursos", None))
        self.caja_seleccion_profesores.setTitle("")
        self.b_agregar_profesor.setText(QCoreApplication.translate("MainWindow", u"Agregar Profesor", None))
        self.caja_edicion_profesores.setTitle("")
        self.l_nombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.l_asignaciones.setText(QCoreApplication.translate("MainWindow", u"Asignaciones", None))
        self.l_disponibilidad.setText(QCoreApplication.translate("MainWindow", u"Disponibilidad", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"De", None))
        self.input_hora_inicio_disponibilidad.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.input_hora_fin_disponibilidad.setDisplayFormat(QCoreApplication.translate("MainWindow", u"h:mm", None))
        self.cb_fechas_disponibilidad.setItemText(0, QCoreApplication.translate("MainWindow", u"Lunes", None))
        self.cb_fechas_disponibilidad.setItemText(1, QCoreApplication.translate("MainWindow", u"Martes", None))
        self.cb_fechas_disponibilidad.setItemText(2, QCoreApplication.translate("MainWindow", u"Miercoles", None))
        self.cb_fechas_disponibilidad.setItemText(3, QCoreApplication.translate("MainWindow", u"Jueves", None))
        self.cb_fechas_disponibilidad.setItemText(4, QCoreApplication.translate("MainWindow", u"Viernes", None))

        self.b_agregar_disponibilidad.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.b_guardar_profesores.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ventana_profesores), QCoreApplication.translate("MainWindow", u"Profesores", None))
        self.caja_izquierda_horarios.setTitle("")
        self.caja_seleccion_horarios.setTitle("")
        self.caja_botones_horarios.setTitle("")
        self.b_cursos_horarios.setText(QCoreApplication.translate("MainWindow", u"Cursos", None))
        self.b_profesor_horarios.setText(QCoreApplication.translate("MainWindow", u"Profesores", None))
        self.caja_derecha_horarios.setTitle("")
        self.caja_generacion_horarios.setTitle("")
        self.b_generar_horarios.setText(QCoreApplication.translate("MainWindow", u"Generar", None))
        self.caja_ver_horarios.setTitle("")
        self.l_horarios.setText(QCoreApplication.translate("MainWindow", u"Generando...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ventana_horarios), QCoreApplication.translate("MainWindow", u"Horarios", None))
    # retranslateUi

