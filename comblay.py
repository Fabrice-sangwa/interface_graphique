from PySide6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
       
        self.setWindowTitle("Mon aplication")
        
        main_layout = QHBoxLayout(self)
        
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

    

        for i in range(1, 11):  
            buton = QPushButton(str(i))
            left_layout.addWidget(buton)
            
        for i in range(11, 21):  
            buton = QPushButton(str(i))
            right_layout.addWidget(buton)


    
app = QApplication()

main_window = MainWindow()

main_window.show()
app.exec()
    
