from PySide6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
        
        self.setWindowTitle("Pluri Fentre")
        
        self.main_window = QHBoxLayout(self)
        
        self.btn_new_window = QPushButton("Nouvelle fenêtre")
        
        self.btn_new_window.clicked.connect(self.create_new_window)
        
        self.main_window.addWidget(self.btn_new_window)
        
        self.resize(600, 400)
        
        
    def create_new_window(self):
        pass
        
        
        
        
        
app = QApplication()
win = MainWindow()


win.show()
app.exec()