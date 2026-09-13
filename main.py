"""
Punto de entrada de la aplicación. Arma la base de datos, el
controlador y la ventana principal.
"""

import sys

from PySide6.QtWidgets import QApplication

from src.controllers.controller import GHEController
from src.database.db_handler import init_db
from src.ui.ui_handler import MainWindow


def main():
    init_db()

    app = QApplication(sys.argv)

    controller = GHEController()
    ventana = MainWindow(controller)
    ventana.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()