
from PySide6.QtWidgets import *


class Button(QListWidget):
    def __init__(self) :
        super().__init__()
        
        self.addItems(["Item1", "Item2", "Item3"])
        
        


    
app = QApplication()

button = Button()

button.show()
app.exec()
    
