from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor
import sys
import random


class ui(QWidget):
    def __init__(self):
        super().__init__()
        self.pushButton = QPushButton('Окружность', self)
        self.pushButton.resize(100, 50)
        self.pushButton.move(200, 200)


class paint(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui()
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)
        self.painter = QPainter()
        self.r = False
        self.ui.pushButton.pressed.connect(self.draw)
        self.ui.pushButton.show()

    def draw(self):
        self.r = True
        self.update()

    def paintEvent(self, event):
        if self.r:
            self.painter = QPainter()
            self.painter.begin(self)
            self.make()
            self.painter.end()

    def make(self):
        self.painter.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        x = random.randint(10, 300)
        self.painter.drawEllipse(100, 30, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = paint()
    ex.setGeometry(100, 100, 500, 300)
    ex.show()
    sys.exit(app.exec())













