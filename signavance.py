from PySide6.QtWidgets import *
from functools import partial


class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
        
        self.setWindowTitle("Les signaux")
        
        main_layout = QHBoxLayout(self)
        
        self.right_btn = QPushButton("Right")
        self.left_btn = QPushButton("Left")
        
        main_layout.addWidget(self.left_btn)
        main_layout.addWidget(self.right_btn)
        
        self.left_btn.clicked.connect(partial(self.btn_cliked, "Bouton de gauche"))
        self.right_btn.clicked.connect(partial(self.btn_cliked, "Bouton de droite"))
        
        
    """
     
    def btn_left(self):
        print("Le boutont de gauche")
        
    def btn_right(self):
        print("Le boutont de droite")
    
    """   
    def btn_cliked(self, message):
        print(message)
        




    
app = QApplication()

main_window = MainWindow()

main_window.show()
app.exec()
    
