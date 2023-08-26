from PySide6.QtCore import *
from PySide6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stretch")
        self.layout = QHBoxLayout(self)
        previous = QPushButton("<<")
        titre = QLabel("Introduction à Python")
        titre.setAlignment(Qt.AlignCenter)
        next = QPushButton(">>")

        # Solution #1
        self.layout.addWidget(previous)
        self.layout.addStretch()
        self.layout.addWidget(titre)
        self.layout.addStretch()
        self.layout.addWidget(next)

        # Solution 2
        previous.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        next.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Solution 3
        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 10)
        self.layout.setStretch(2, 1)

        # Solution 4
        previous.setMaximumWidth(previous.sizeHint().width())
        next.setMaximumWidth(next.sizeHint().width())
        
        self.setFocus()


app = QApplication()
win = MainWindow()
win.show()
app.exec()