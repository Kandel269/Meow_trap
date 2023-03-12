import os
import sys
import time
from random import sample

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

def new_mem_window(cat_time):
    mem_list = []
    files = os.listdir()
    for file in files:
        if file.endswith('.jpg'):
            mem_list.append(file)

    mem = sample(mem_list,1)
    w = MemWindow(f"./{str(mem[0])}",cat_time)
    w.show()

def sample_event(cat_time):
    time.sleep(int(cat_time))
    events_lists = ["mem"]
    event  = sample(events_lists,1)
    if event[0] == "mem":
        new_mem_window(cat_time)


class MemWindow(QMainWindow):
    def __init__(self,image_load,cat_time):
        super().__init__()
        self.image_load = image_load
        self.cat_time = cat_time
        self.setWindowTitle("MIAU_MIAU_MIAU")
        self.show_mem()
        self.destroyed.connect(self.handle_destroyed)
        self.closeEvent = self.handle_destroyed

    def show_mem(self):
        self.widget = QLabel()
        self.pixmap = QPixmap(self.image_load)
        self.widget.setPixmap(self.pixmap)
        self.setCentralWidget(self.widget)
        self.resize(self.pixmap.width(), self.pixmap.height())


    def handle_destroyed(self, event=None):
        self.close()
        self.deleteLater()
        sample_event(self.cat_time)



class MainApp(QMainWindow):
    def __init__(self,hide_or_no = 1):
        super().__init__()
        self.setFixedSize(QSize(500, 400))
        self.hide_or_no = hide_or_no
        if self.hide_or_no == 0:
            self.button_start_clicked()
        else:
            self.show()
        self.main_window()

    def main_window(self):
        self.setWindowTitle("Evil Meow")

        self.time_start = QLineEdit()
        self.time_start.setPlaceholderText('2')

        self.cat_time = QLineEdit()
        self.cat_time.setPlaceholderText("600")

        button_start = QPushButton()
        button_start.clicked.connect(self.button_start_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.time_start)
        layout.addWidget(self.cat_time)
        layout.addWidget(button_start)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def button_start_clicked(self):
        # self.hide()
        try:
            time.sleep(int(self.time_start.text()))
        except:
            time.sleep(2)

        self.close()
        self.deleteLater()
        sample_event(int(self.cat_time.text()))



app = QApplication(sys.argv)
window = MainApp()
app.exec()