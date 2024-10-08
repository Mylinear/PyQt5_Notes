import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Forms')
        
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)
        
        label1 = qtw.QLabel('Label1 text')
        label1.setFont(qtg.QFont('Comic Sans MS', 18))
        
        # self.layout().addWidget(label1)
        # form_layout.addWidget(label1)
        
        button1 = qtw.QPushButton('Press the Button',clicked = lambda: fbutton1())
        
        first_name = qtw.QLineEdit(self)
        last_name = qtw.QLineEdit(self)
        
        # Add Rows to App
        form_layout.addRow(label1)
        form_layout.addRow('First Name',first_name)
        form_layout.addRow('Last Name', last_name)
        form_layout.addRow(button1)
        
        def fbutton1():
            label1.setText(f'You Clicked the button {first_name.text()} {last_name.text()}')
            
        
        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()