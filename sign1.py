from typing import Optional

from PySide6.QtWidgets import *



class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
        
        self.setWindowTitle("Lecteur Vidéo")
        
        main_layout = QVBoxLayout(self)
        
        btn = QPushButton("Cliquez-moi")
        main_layout.addWidget(btn)
        
        
       #btn.clicked.connect(self.btn_click)
        btn.pressed.connect(self.btn_pre)
        btn.released.connect(self.btn_rel)
        
        
    def btn_click(self):
        print("Le boutont a été cliqué. ")
        
    def btn_pre(self):
        print("Le boutont a été pressé. ")
        
    def btn_rel(self):
        print("Le boutont a été relaché. ")
        



    
app = QApplication()

main_window = MainWindow()

main_window.show()
app.exec()
    
