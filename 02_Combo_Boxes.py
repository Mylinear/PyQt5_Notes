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
        
        # Create a Combo box
        combo1 = qtw.QComboBox(self,editable = True)
        
        # Add items to the combo box
        combo1.addItems(['Python','C++', 'C#', 'Kotlin'])
        
        # Put Combo box on the screen
        self.layout().addWidget(combo1)
        
        # create a button
        button1 = qtw.QPushButton('Select', clicked = lambda : fbutton())
        self.layout().addWidget(button1)
        
        def fbutton():
            label1.setText(f'You have selected {combo1.currentText()}')

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

# Execute the program

app.exec_()
    