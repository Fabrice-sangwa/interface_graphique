from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6 import QtCore

BUTTONS = {
        "C" : (1, 0, 1, 1), 
        "/" : (1, 3, 1, 1),
        "7" : (2, 0, 1, 1), 
        "8" : (2, 1, 1, 1),
        "9" : (2, 2, 1, 1),
        "X" : (2, 3, 1, 1),
        
        "4" : (3, 0, 1, 1), 
        "5" : (3, 1, 1, 1),
        "6" : (3, 2, 1, 1), 
        "-" : (3, 3, 1, 1),
        
        "1" : (4, 0, 1, 1), 
        "2" : (4, 1, 1, 1),
        "3" : (4, 2, 1, 1), 
        "+" : (4, 3, 1, 1),
        
        "0" : (5, 0, 1, 2), 
        "." : (5, 2, 1, 1),
        "=" : (5, 3, 1, 1),}
OPERATIONS = ["+", "-", "/", "X"]

class Caluclator(QWidget):
    def __init__(self) :
        super().__init__()
        
        self.setWindowTitle("Calculatice")
       
        self.setStyleSheet("""
                   
                background-color : rgb(20, 20, 20);
                color : rgb(220, 220, 220) ; 
                font-size : 20px;      
                           
                           
        """)
        
        self.buttons = {}
        
        self.main_layout = QGridLayout(self)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        
        self.le_result = QLineEdit("0")
        self.le_result.setEnabled(False)
        self.le_result.setMinimumHeight(70)
        self.le_result.setAlignment(QtCore.Qt.AlignRight)
        
        self.le_result.setStyleSheet("""
                    
                border : none; 
                border-bottom : 2px solid rgb(30, 30, 30);
                padding : 0 8px; 
                font-size : 24px; 
                font-weight : bold;                      
                                               
        """)
        
        
        self.main_layout.addWidget(self.le_result, 0, 0, 1, 4)
        
        for button_text, button_position in BUTTONS.items():
            btn = QPushButton(button_text)
            btn.setMinimumSize(50, 50)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            
            
            btn.setStyleSheet(f"""
                     
                     QPushButton{{
                        border : none; 
                        font-weight : bold; 
                        background-color: {'#1e1e2d' if button_text in OPERATIONS else 'none'}
                     }}
                    QPushButton:pressed {{background-color: #f31d58;}}
                           
            """)
            
            self.main_layout.addWidget(btn, *button_position)
            if button_text not in["=", "C"]:
                btn.clicked.connect(self.manipulation_number_opertation)
            
            self.buttons[button_text] = btn 
        
        self.buttons["C"].clicked.connect(self.clear_all) 
        self.buttons["="].clicked.connect(self.compute_result) 
        self.buttons["="].setStyleSheet("background-color: #f31d58;")
        
        self.connect_keyboard()
        
    @property
    def result(self):
        return self.le_result.text()
            
    def manipulation_number_opertation(self):
        if self.result == "0":
            self.le_result.clear()
        self.le_result.setText(self.result + self.sender().text())
    
    def clear_all(self):
        self.le_result.setText("0")
        
    def compute_result(self):
        try : 
            result = eval(self.result.replace('X', "*"))
        
        except SyntaxError:
            return 
        except ZeroDivisionError:
            return self.le_result.setText("0")
        
        self.le_result.setText(str(result))


    def connect_keyboard(self):
        for button_text, button in self.buttons.items():
            QShortcut(QKeySequence(button_text), self, button.clicked.emit)
         
        QShortcut(QKeySequence(QtCore.Qt.Key_Return), self, self.compute_result)
        QShortcut(QKeySequence(QtCore.Qt.Key_Backspace), self, self.remove_last_caracter)
    
    def remove_last_caracter(self):
        if len(self.result) > 1:
            self.le_result.setText(self.result[:-1])
        else :
            self.le_result.setText("0")
            
    def verify_operation(self):
        if self.sender().text() in OPERATIONS: 
            if self.result[-1] in OPERATIONS or self.result == "0":
                return 
        
        if self.result == "0":
            self.le_result.clear()
    
app = QApplication()
win = Caluclator()


win.show()
app.exec()
    