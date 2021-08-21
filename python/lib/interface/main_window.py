# this file defined the interface of the app
import sys, os
from argparse import ArgumentParser
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QMenuBar, QMenu, QAction, QTextEdit, QVBoxLayout, QLineEdit, QHBoxLayout, QFileDialog
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
        self.setStyle()

    def home(self):
        # greeting
        greeting = QLabel(os.path.expandvars("Welcome back $USER :)\n How was your day?"))
        greeting.setFont(QFont("Courier"))
        greeting.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(greeting)

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

        # help
        settings_menu = menu_bar.addMenu("&settings")
        menu_bar.addMenu(settings_menu)

        # home
        home_menu = QAction("home", self)
        menu_bar.addAction(home_menu)
        home_menu.triggered.connect(self.home)


    def open_file(self):

        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        # dlg.setFilter("Text files (*.txt)")
        filenames = QStringList()

        if dlg.exec_():
            filenames = dlg.selectedFiles()


    def new_post(self):
        post = Post()
        self.edit_post(post)

    def load_post(self, post_id):
        post = database.read_post(post_id)
        self.edit_post(post)

    def edit_post(self, post: Post):
        self.current_post = post

        layout = QVBoxLayout()

        self.editor = QTextEdit()
        self.editor.setPlainText(post.text)
        layout.addWidget(self.editor)
  
        self.wid = QtWidgets.QWidget(self)
        self.setCentralWidget(self.wid)
        self.wid.setLayout(layout)

    def save_post(self):

        self.cur_post.update(self.editor.toPlainText())
        database.save_post(self.cur_post)
