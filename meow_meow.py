import os
import sys
import time
from random import sample
import ctypes


from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
import pygame

events_lists = ["mem","file","change_background","sound"]

def change_background(cat_time, SPI_SETDESKWALLPAPER = 20) -> None:
    file_path = r"C:\Users\Domin\PycharmProjects\Meow_trap\Kot_wall.jpg"
    if os.name == 'nt':
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path, 0)

    sample_event(cat_time)

def new_mem_window(cat_time) -> None:
    mem_list = []
    files = os.listdir()
    for file in files:
        if file.endswith('.jpg'):
            mem_list.append(file)

    mem = sample(mem_list,1)
    w = MemWindow(f"./{str(mem[0])}",cat_time)
    w.show()

def meow_sound(cat_time) -> None:
    pygame.init()
    pygame.mixer.music.load("cat_meow.wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    sample_event(cat_time)

def new_file(cat_time) -> None:
    home_dir = os.path.expanduser('~')
    desktop_path_list = [r'Desktop',r'Pulpit',r'OneDrive\Desktop',r'OneDrive\Pulpit']
    for path in desktop_path_list:
        desktop_path = os.path.join(home_dir, path)
        try:
            for _ in range(3):
                counter = 1
                while True:
                    file = fr"Meow_meow_meow-{str(counter)}.txt"
                    full_path = os.path.join(desktop_path, file)
                    if file in os.listdir(desktop_path):
                        counter += 1
                        continue
                    try:
                        with open(full_path, mode = "w"):
                            break
                    except:
                        break
            break
        except:
            continue
    sample_event(cat_time)

def sample_event(cat_time) -> None:
    time.sleep(int(cat_time))
    event  = sample(events_lists,1)
    if event[0] == "mem":
        new_mem_window(cat_time)
    elif event[0] == "file":
        events_lists.remove("file")
        new_file(cat_time)
    elif event[0] == "change_background":
        events_lists.remove("change_background")
        change_background(cat_time, 20)
    elif event[0] == "sound":
        meow_sound(cat_time)


class MemWindow(QMainWindow):
    """
    Create window with mem
    """
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
    """
    Create Main window
    """
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