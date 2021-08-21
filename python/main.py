import os, sys

from PyQt5.QtCore import qsrand
from lib.interface import MainWindow
from PyQt5.QtWidgets import QApplication, QStyle



if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
