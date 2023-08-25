from typing import Optional

from PySide6.QtWidgets import QApplication, QWidget



class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
        
        self.setWindowTitle("Lecteur Vidéo")
        #self.setFixedSize(400, 400)
        #self.setMinimumWidth(200)



    
app = QApplication()

main_window = MainWindow()

main_window.show()
app.exec()
    
