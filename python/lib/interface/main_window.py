# this file defined the interface of the app
from dataclasses import dataclass
import sys, os
from argparse import ArgumentParser
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
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
        self.setWindowTitle("")   # window title
        self._create_menu_bar()                 # create menu bar (file, edit, help, etc.)
        self.home()                             # go to home page by default

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
        file_menu = QMenu("&File", self)
        menu_bar.addMenu(file_menu)

        # file -> open
        file_open = QAction("Open", self)
        file_menu.addAction(file_open)
        file_open.triggered.connect(self.open_file)

        # file -> new
        file_new = QAction("New", self)
        file_menu.addAction(file_new)
        file_new.triggered.connect(self.new_post)

        # file -> save
        file_save = QAction("Save", self)
        file_menu.addAction(file_save)
        file_save.triggered.connect(self.save_post)

        # help
        settings_menu = menu_bar.addMenu("&Settings")
        menu_bar.addMenu(settings_menu)

        # home
        home_menu = QAction("Home", self)
        menu_bar.addAction(home_menu)
        home_menu.triggered.connect(self.home)

    def open_file(self):

        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setDirectory(database.post_dir)
        if dlg.exec_():
            try:
                file_path = dlg.selectedFiles()[-1]
                log.info(f"selected: {file_path=}")
                self.load_post(path=file_path)
            except:
                log.info(f"aborted file dialog")

    def new_post(self):
        post = Post()
        self.edit_post(post)

    def load_post(self, ID=None, path=None):
        post = Post(ID=database.path2ID(path), 
                    text=database.read_post(ID=ID, path=path))
        self.edit_post(post)

    def edit_post(self, post: Post):
        self.cur_post = post

        layout = QVBoxLayout()

        self.editor = QTextEdit()
        self.editor.setPlainText(post.text)
        layout.addWidget(self.editor)
  
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.wid.setLayout(layout)

    def save_post(self):

        self.cur_post.update(self.editor.toPlainText())
        database.save_post(self.cur_post)
