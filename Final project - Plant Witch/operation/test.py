import sys
from PyQt6.QtWidgets import *
from pathlib import Path
from PyQt6.QtGui import QIcon

class mainwindow(QWidget):
    def __init__(self, parent = None):
        super(mainwindow, self).__init__(parent)
        self.setGeometry(500, 500, 500, 100)
        self.setWindowTitle("Plant Witch Login")


        labels = ['Your Name', 'Garden Name', 'E-mail', 'Phone']
        self.textboxes = {}

        mainlayout = QVBoxLayout()
        formlayout = QFormLayout()
        self.setLayout(mainlayout)
        mainlayout.addLayout(formlayout)
        
        heading = QLabel( 'Welcome!')
        heading.setObjectName('heading')

        subheading = QLabel('Please enter your email and password to log in.')
        subheading.setObjectName('subheading')

        
        for l in labels:
            #add the label

            #now add a textbox for that lable,
            # and also hold it in the dictionary so we cn use it later
            txt = QLineEdit()
            formlayout.addRow(l, txt)
            self.textboxes[l] = txt

    

        #finally, add a button
        b = QPushButton("Submit")
        b.clicked.connect(self.button_clicked)
        mainlayout.addWidget(b)

    
        self.labelResult = QLabel()
        mainlayout.addWidget(self.labelResult)
        
        self.show()

    def button_clicked(self):
        self.labelResult.setText(self.textboxes['Your Name'].text())

def main():
    app = QApplication([])
    app.setStyleSheet(Path('login.qss').read_text())
    w = mainwindow()
    w.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()


