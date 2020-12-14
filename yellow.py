import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from random import randrange


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(600, 600)
        self.setWindowTitle('Круги')
        self.btn = QPushButton('Кнопка', self)
        self.btn.move(250, 20)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False
        self.label = QLabel(self)
        self.label.move(0, 50)
        self.label.resize(400, 300)

    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            qp = QPainter(self.label)
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_flag(qp)
            # Завершаем рисование
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
        a = randrange(10, 500)
        qp.drawEllipse(150, 150, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
