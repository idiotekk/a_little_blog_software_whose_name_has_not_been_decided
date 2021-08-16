import os, sys
from interface import MainWindow
from PyQt5.QtWidgets import QApplication



if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
