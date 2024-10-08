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
        
        # Create Text box
        text1 = qtw.QTextEdit(self,
                            acceptRichText=True,
                            lineWrapMode = qtw.QTextEdit.FixedColumnWidth,
                             lineWrapColumnOrWidth = 50,
                             placeholderText = 'Enter your text here'
                             )   
        
        # Set the size of the  text box and  the font type
        text1.setFont(qtg.QFont('Comic Sans MS', 12))
                
        
        # Put Spin box on the screen
        self.layout().addWidget(text1)
        
        # create a button
        button1 = qtw.QPushButton('Select', clicked = lambda : fbutton())
        self.layout().addWidget(button1)
        
        def fbutton():
            label1.setText(f'You have selected {text1.toPlainText()}')

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

# Execute the program

app.exec_()
    