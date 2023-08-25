from PySide6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
       
        self.setWindowTitle("Mon aplication")
        
        main_layout = QHBoxLayout(self)
        
        for i in range(10):  
            buton = QPushButton("Salut")
            main_layout.addWidget(buton)


    
app = QApplication()

main_window = MainWindow()

main_window.show()
app.exec()
    
