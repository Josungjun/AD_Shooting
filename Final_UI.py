import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import PyshootingR
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
        settingGrid.addWidget(self.music(), 1, 1)
        settingGrid.addWidget(self.button(), 0, 2)


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
        radio1.clicked.connect(self.buttonClicked)
        radio2.clicked.connect(self.buttonClicked)
        radio3.clicked.connect(self.buttonClicked)
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox

    def ship(self):
        groupbox = QGroupBox('비행기')

        radio1 = QRadioButton('starwars')
        radio2 = QRadioButton('likeBug')
        radio1.clicked.connect(self.buttonClicked)
        radio2.clicked.connect(self.buttonClicked)

        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)

        groupbox.setLayout(vbox)

        return groupbox

    def background(self):
        groupbox = QGroupBox('배경')

        radio1 = QRadioButton('성운')
        radio2 = QRadioButton('우주인')
        radio3 = QRadioButton('별들')
        radio1.clicked.connect(self.buttonClicked)
        radio2.clicked.connect(self.buttonClicked)
        radio3.clicked.connect(self.buttonClicked)
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox

    def music(self):
        groupbox = QGroupBox('음악')

        radio1 = QRadioButton('잔잔')
        radio2 = QRadioButton('funny')
        radio3 = QRadioButton('신남')
        radio1.clicked.connect(self.buttonClicked)
        radio2.clicked.connect(self.buttonClicked)
        radio3.clicked.connect(self.buttonClicked)
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
        startbutton.clicked.connect(self.buttonClicked)
        quitbutton.clicked.connect(self.buttonClicked)
        vbox = QVBoxLayout()
        vbox.addWidget(startbutton)
        vbox.addWidget(quitbutton)
        groupbox.setLayout(vbox)

        return groupbox

    def buttonClicked(self):
        global max_speed, min_speed, background, occurrock, occurrock2, Fly, music

        button = self.sender()
        key = button.text()
        if key == '성운':
            background = "Nebula.jpg"
        elif key == '우주인':
            background = "Astronaut.jpg"
        elif key == '별들':
            background = "Star.jpg"
        elif key == 'starwars':
            Fly = 'fighterStar.png'
        elif key == 'likeBug':
            Fly = 'fighterBug.png'
        elif key == 'easy':
            max_speed = 200
            min_speed = 300
            occurrock = 200
            occurrock2 = 1
        elif key == 'normal':
            max_speed = 100
            min_speed = 200
            occurrock = 150
            occurrock2 = 2
        elif key == 'hard':
            max_speed = 50
            min_speed = 100
            occurrock = 100
            occurrock2 = 3
        elif key == '잔잔':
            music = "inspire.wav"
        elif key == 'funny':
            music = "funny.wav"
        elif key == '신남':
            music = "extreme.wav"
        elif key == 'Start':
            PyshootingR.main(background, max_speed, min_speed, occurrock, occurrock2, Fly, music)
        elif key == 'Quit':
            sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    shoot = Shoot()
    shoot.show()
    app.exec_()
