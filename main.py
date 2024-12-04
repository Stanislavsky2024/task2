from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
import sys
import random
from PyQt6 import uic


class paint(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.painter = QPainter()
        self.r = False
        self.pushButton.pressed.connect(self.draw)

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
        self.painter.setBrush(QColor(255, 255, 0))
        x = random.randint(10, 300)
        self.painter.drawEllipse(100, 30, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = paint()
    ex.show()
    sys.exit(app.exec())













