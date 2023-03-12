import os
import sys
import time
from random import sample
import ctypes
from PIL import Image

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

events_lists = ["mem", "file","change_background","lockscreen"]

def change_background(cat_time, SPI_SETDESKWALLPAPER) -> None:
    new_wallpaper_path = '.\wall.jpeg'

    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)

    image = Image.open('.\Kot_wall.jpg')
    image = image.resize((width, height), Image.LANCZOS)

    image.save(new_wallpaper_path, 'JPEG')

    try:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, new_wallpaper_path, 0)
    except:
        pass

    os.remove(new_wallpaper_path)

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

def check_onderive() -> str:
    home_dir = os.path.expanduser('~')
    onedrive_dir = os.path.join(home_dir, 'OneDrive')

    if os.path.isdir(onedrive_dir):
        desktop_path = os.path.join(onedrive_dir, 'Pulpit')
    else:
        desktop_path = os.path.join(home_dir, 'Pulpit')
    return desktop_path

def new_file(cat_time) -> None:
    desktop_path = check_onderive()

    for _ in range(3):
        counter = 1
        while True:
            file = f"Meow_meow_meow-{str(counter)}.txt"
            full_path = os.path.join(desktop_path, file)
            if file in os.listdir(desktop_path):
                counter += 1
                continue
            try:
                with open(full_path, mode = "w"):
                    break
            except:
                break

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
    elif event[0] == "lockscreen":
        events_lists.remove("lockscreen")
        change_background(cat_time, 474)

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