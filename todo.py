from PySide6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self) :
        super().__init__()
        
        self.setWindowTitle("To Do list")
        
        self.main_layout = QVBoxLayout(self)  
          
        self.lw_todo = QListWidget()
        self.le_task = QLineEdit()
        self.le_task.setPlaceholderText("Ecrivez la tâche à effectuer")
        self.btn_clear = QPushButton("Tout supprimer")
        
        self.main_layout.addWidget(self.lw_todo)
        self.main_layout.addWidget(self.le_task)
        self.main_layout.addWidget(self.btn_clear)
        
        self.le_task.returnPressed.connect(self.add_todo)
        self.btn_clear.clicked.connect(self.lw_todo.clear)
        
        
        self.lw_todo.itemDoubleClicked.connect(self.delete_todo)
        
    def add_todo(self):
        self.lw_todo.addItem(self.le_task.text())
        self.le_task.clear()
        
    def delete_todo(self, item):
        #print(item.text())
        self.lw_todo.takeItem(self.lw_todo.row(item))
        
        
        
app = QApplication()
win = MainWindow()


win.show()
app.exec()