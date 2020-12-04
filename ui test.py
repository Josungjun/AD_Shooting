
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton
, QPushButton, QMenu, QGridLayout, QVBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.startbutton = QPushButton('Start')
        self.quitbutton = QPushButton('Quit')

        grid = QGridLayout()
        grid.addWidget(self.difficulty(), 0, 0)
        grid.addWidget(self.ship(), 1, 0)
        grid.addWidget(self.background(), 0, 1)
        grid.addWidget(self.startbutton,1,1)
        grid.addWidget(self.quitbutton,2,1)
        #rid.addWidget(self.createPushButtonGroup(), 1, 1)


        self.setLayout(grid)

        self.setWindowTitle('Settomg game')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def difficulty(self):
        groupbox = QGroupBox('난이도')

        radio1 = QRadioButton('easy')
        radio2 = QRadioButton('normal')
        radio3 = QRadioButton('hard')
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox

    def ship(self):
        groupbox = QGroupBox('비행기')

        radio1 = QRadioButton('1')
        radio2 = QRadioButton('2')
        radio3 = QRadioButton('3')
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox

    def background(self):
        groupbox = QGroupBox('배경')

        radio1 = QRadioButton('1')
        radio2 = QRadioButton('2')
        radio3 = QRadioButton('3')
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())