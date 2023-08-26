import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
from cal import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())