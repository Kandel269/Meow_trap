import sys
import time
import threading
from random import sample

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

def new_mem_window():
    print("aaaaaa")
    mem_window = MemWindow(r'./1.jpg')
    mem_window.show()

def sample_event(cat_time):
    print("aa")
    time.sleep(int(cat_time))
    events_lists = ["mem"]
    event = sample(events_lists,1)
    # create_new_thread(cat_time)
    if event[0] == "mem":
        print("xd")
        new_mem_window()


# def create_new_thread(cat_time):
#     print("dupa")
#     t = threading.Thread(target = sample_event, args=(cat_time,))
#     threads.append(t)
#     t.start()
#     print("aassss")
#     t.join()

class MemWindow(QMainWindow):
    def __init__(self,image_load):
        super().__init__()
        self.image_load = image_load
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
        self.hide()
        try:
            time.sleep(int(self.time_start.text()))
        except:
            time.sleep(2)

        self.close()
        self.deleteLater()
        sample_event(int(self.cat_time.text()))
        # create_new_thread(int(self.cat_time.text()))

threads= []
app = QApplication(sys.argv)
window = MainApp()
app.exec()
