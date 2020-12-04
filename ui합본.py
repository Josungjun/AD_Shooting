import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import Shooting
class Shoot(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.ReadyWindow = QTextEdit()
        self.ReadyWindow.setReadOnly(True)
        self.ReadyWindow.setAlignment(Qt.AlignLeft)
        self.ReadyWindow.setText("이동 : 좌우 방향키 \n"
                                 "미사일 발사 : 스패이스바 \n"
                                 "easy 모드 : \n"
                                 "Normal 모드 : \n"
                                 "Hard 모드 : \n"
                                 "1번 비행기 : \n"
                                 "2번 비행기 : \n")
        self.ReadyWindowT = QLabel()
        self.ReadyWindowT.setText("기본 환경 설정 설명")
        GameReadyLayout = QGridLayout()
        GameReadyLayout.addWidget(self.ReadyWindowT, 0, 0)
        GameReadyLayout.addWidget(self.ReadyWindow, 1, 0)

        self.startbutton = QPushButton('Start')
        self.quitbutton = QPushButton('Quit')

        settingGrid = QGridLayout()
        settingGrid.addWidget(self.difficulty(), 0, 0)
        settingGrid.addWidget(self.ship(), 1, 0)
        settingGrid.addWidget(self.background(), 0, 1)
        settingGrid.addWidget(self.button(), 1, 1)


        mainLayout = QGridLayout()
        mainLayout.addLayout(GameReadyLayout, 0, 0)
        mainLayout.addLayout(settingGrid, 1, 0)


        self.setLayout(mainLayout)
        self.setWindowTitle("Shooting")


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

        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)

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

    def button(self):
        groupbox = QGroupBox()

        startbutton = QPushButton('Start')
        quitbutton = QPushButton('Quit')
        vbox = QVBoxLayout()
        vbox.addWidget(startbutton)
        vbox.addWidget(quitbutton)
        groupbox.setLayout(vbox)

        return groupbox











if __name__ == "__main__":
    app = QApplication(sys.argv)
    shoot = Shoot()
    shoot.show()
    app.exec_()