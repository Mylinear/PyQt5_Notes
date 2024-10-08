import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # Add a Title
        self.setWindowTitle('First Window')
        
        # Set Vertical layout
        self.setLayout(qtw.QVBoxLayout())
        
        # Create a label
        label1 = qtw.QLabel("Hi!!! What's your name")
        
        # Change the font size of a label
        label1.setFont(qtg.QFont('Arial', 18))
        self.layout().addWidget(label1)
        
        # Create an etnry box
        entry1 = qtw.QLineEdit()
        self.layout().addWidget(entry1)
            
        # Create a Button
        button1 = qtw.QPushButton('Press the Button',clicked = lambda: fbutton1())
        self.layout().addWidget(button1)
        
        # Show the App
        self.show()
        
        def fbutton1():
            # Add name to label
            label1.setText(f"Hi!!! {entry1.text()}")
            # Clear the entry box
            entry1.setText('')
        
app = qtw.QApplication([])
mw = MainWindow()

# Run the App

app.exec_()