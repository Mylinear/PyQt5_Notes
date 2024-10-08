from PyQt5.QtCore import Qt
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # Add a title
        self.setWindowTitle('It is a Title')
        
        # Set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())
        
        # Create A Label
        label1 = qtw.QLabel('Select a Language')
        
        # Change the font and the size of label
        label1.setFont(qtg.QFont('Comic Sans MS', 18))
        self.layout().addWidget(label1)
        
        # Create a Spin box
        spin1 = qtw.QSpinBox(self,
                             value = 10,
                             maximum = 20,
                             minimum = 5,
                             singleStep = 2,
                             prefix = "Your Selection is ",
                             suffix = " !!!"
                             )
        spin1.setFont(qtg.QFont('Comic Sans MS', 12))
                
        
        # Put Spin box on the screen
        self.layout().addWidget(spin1)
        
        # create a button
        button1 = qtw.QPushButton('Select', clicked = lambda : fbutton())
        self.layout().addWidget(button1)
        
        def fbutton():
            label1.setText(f'You have selected {spin1.value()}')

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

# Execute the program

app.exec_()
    