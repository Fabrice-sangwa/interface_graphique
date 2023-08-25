from typing import Optional

from PySide6.QtWidgets import *



class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
        
        self.setWindowTitle("Lecteur Vidéo")
        
        main_layout = QVBoxLayout(self)
       
        self.ln_edit = QLineEdit()
        self.btn_clear = QPushButton("Effacer")
        self.label_text = QLabel("...")
        
        main_layout.addWidget(self.ln_edit)
        main_layout.addWidget(self.label_text)
        main_layout.addWidget(self.btn_clear)
        
        
        self.ln_edit.textChanged.connect(self.label_text.setText)
        self.btn_clear.clicked.connect(self.clear_text)
    
    def clear_text(self):
        self.ln_edit.clear()
        self.label_text.setText("...")
       


    
app = QApplication()

main_window = MainWindow()

main_window.show()
app.exec()
    
