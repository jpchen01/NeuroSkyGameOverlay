from PyQt5.QtWidgets import (
    QLabel, QMainWindow, QApplication,
    QHBoxLayout, QVBoxLayout, QWidget,
    QSizePolicy, QGraphicsOpacityEffect
    )
from PyQt5.QtGui import QPixmap, QWindow, QMovie
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # self.title = "Image Viewer"
        # self.setWindowTitle(self.title)

        self.setAttribute(Qt.WA_TranslucentBackground , True) 
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        # Set background invisible
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) # This works

        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.2)
        
        # Label
        label = QLabel(self)
        # pixmap = QPixmap('BlueTint.png')
        # pixmap.fill(Qt.transparent)
        # label.setPixmap(pixmap)
        label.setGraphicsEffect(self.opacity_effect)
        movie = QMovie("WispyEffect.gif")
        label.setMovie(movie)
        movie.start() 

        label.setScaledContents(True)
        self.setCentralWidget(label)
        # self.resize(pixmap.width(), pixmap.height())

        def change_opacity_signal(self, opacity):
            opacity_effect = QGraphicsOpacityEffect()
            opacity_effect.setOpacity(opacity)
            label.setGraphicsEffect(opacity_effect)


app = QApplication(sys.argv)
w = MainWindow()
w.showFullScreen()
sys.exit(app.exec_())