from PyQt5.QtWidgets import (QApplication, QWidget, QListWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog)
import os
from imageProcessor import ImageProcessor


app = QApplication([])
window = QWidget()
window.setWindowTitle("Easy editior")
window.resize(600, 600)

main_line = QHBoxLayout()

line1 = QVBoxLayout()
btn_folder = QPushButton("folder")
list_widget = QListWidget()

line1.addWidget(btn_folder)
line1.addWidget(list_widget)

main_line.addLayout(line1)

line2 = QVBoxLayout()
image  =QLabel("image")

button_line = QHBoxLayout()
btn1 = QPushButton("1")
btn2 = QPushButton("2")
btn3 = QPushButton("3")
btn4 = QPushButton("4")
btn5 = QPushButton("5")
button_line.addWidget(btn1)
button_line.addWidget(btn2)
button_line.addWidget(btn3)
button_line.addWidget(btn4)
button_line.addWidget(btn5)

line2.addWidget(image)
line2.addLayout(button_line)

main_line.addLayout(line2)

window.setLayout(main_line)


def filter (files):
    img_files = []
    filters = ["png", "jpg", "jpeg", "gid"]
    
    for file in files:
        if file.split(".")[-1] == "png":
            img_files.append(file)

    return img_files        

def showFolder():
    workdir = QFileDialog.getExistingDirectory()
    filenames = filter(os.listdir(workdir))

    list_widget.addItems(filenames)

btn_folder.clicked.connect(showFolder)

workImage = ImageProcessor

def showChosenItem():
    filename = list_widget.currentItem().text()
    workImage.loadImage(filename, workdir)
    workImage.showImage(os.path.join(workdir, filename), image)

list_widget.currentRowChanged.connect(showChosenItem)

window.show()

app.exec_()
