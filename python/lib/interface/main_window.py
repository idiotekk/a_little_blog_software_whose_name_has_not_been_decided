# this file defined the interface of the app
import sys, os
from argparse import ArgumentParser
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QAction, QTextEdit, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont
from ..backend.post import Post
from ..backend.database import DataBase
import logging as log

parser = ArgumentParser()
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()
log.basicConfig(level=log.DEBUG if args.debug else log.INFO)


__all__ = [
    "MainWindow"
]

database = DataBase()

class MainWindow(QMainWindow):

    def __init__(self) -> None:

        super(MainWindow, self).__init__()
        self.setGeometry(100, 300, 300, 300)    # first two numbers = location of window; 3rd and 4th numbers = window height and width
        self.setWindowTitle("mini mini blog")   # window title
        self._create_menu_bar()                 # create menu bar (file, edit, help, etc.)
        self.home()                             # go to home page by default

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
        file_new.triggered.connect(self.new_post)

        # file -> save
        file_save = QAction("save", self)
        file_menu.addAction(file_save)
        file_save.triggered.connect(self.save_post)

        # file -> edit
        edit_menu = menu_bar.addMenu("&edit")

        # help
        help_menu = menu_bar.addMenu("&help")

        # help
        settings_menu = menu_bar.addMenu("&settings")
        menu_bar.addMenu(settings_menu)

        # home
        home_menu = QAction("home", self)
        menu_bar.addAction(home_menu)
        home_menu.triggered.connect(self.home)

    def new_post(self):
        post = Post()
        self.edit_post(post)

    def load_post(self, post_id):
        post = database.read_post(post_id)
        self.edit_post(post)

    def edit_post(self, post: Post):
        self.current_post = post

        layout = QVBoxLayout()

        self.body_editor = QTextEdit()
        self.body_editor.setPlainText(post.text)
        layout.addWidget(self.body_editor)
  
        self.wid = QtWidgets.QWidget(self)
        self.setCentralWidget(self.wid)
        self.wid.setLayout(layout)
    

    def save_post(self):

        self.current_post.text = self.body_editor.toPlainText()
        log.debug(self.current_post)
        database.save_post(self.current_post)
