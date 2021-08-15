from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QAction, QTextEdit, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
import sys, os


class MainWindow(QMainWindow):

    def __init__(self) -> None:

        super(MainWindow, self).__init__()
        self.setGeometry(100, 300, 300, 300)
        self.setWindowTitle("mini mini blog")
        self._create_menu_bar()
        self.home()

    def home(self):
        # greeting
        self.greeting = QLabel(os.path.expandvars("Welcome back $USER :)\n How was your day?"))
        self.greeting.setFont(QFont("Courier"))
        self.greeting.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.greeting)

    def _create_menu_bar(self):

        menu_bar = QMenuBar(self)
        menu_bar.setNativeMenuBar(False)
        self.setMenuBar(menu_bar)

        # file menu
        file_menu = QMenu("&file", self)
        menu_bar.addMenu(file_menu)

        # file -> open
        file_open = QAction("open", self)
        file_menu.addAction(file_open)

        # file -> new
        file_new = QAction("new", self)
        file_menu.addAction(file_new)
        file_new.triggered.connect(self.new_article)

        # file -> save
        file_save = QAction("save", self)
        file_menu.addAction(file_save)

        # file -> edit
        edit_menu = menu_bar.addMenu("&edit")
        menu_bar.addMenu(edit_menu)

        # help
        help_menu = menu_bar.addMenu("&help")
        menu_bar.addMenu(help_menu)

        # view
        view_menu = menu_bar.addMenu("&view")
        menu_bar.addMenu(view_menu)

        # home
        home_menu = QAction("home", self)
        menu_bar.addAction(home_menu)
        home_menu.triggered.connect(self.home)

    #def new_article(self):
    def new_article(self):
        
        wid = QtWidgets.QWidget(self)
        self.setCentralWidget(wid)
        layout = QVBoxLayout()

        # add title
        self.article_title = QLineEdit()
        layout.addWidget(self.article_title)

        # add body
        self.article_body = QTextEdit()
        layout.addWidget(self.article_body)
        wid.setLayout(layout)


