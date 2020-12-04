import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

import Pyshooting
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

        SettingLayout = QGridLayout()

        self.MusicT = QLabel()
        self.MusicT.setText("음악 선택 ")
        self.Music = QComboBox()
        self.Music.addItems(['1', '2', '3'])
        SettingLayout.addWidget(self.MusicT, 0, 0)
        SettingLayout.addWidget(self.Music, 0, 1)
        self.FlyT = QLabel()
        self.FlyT.setText("비행기 선택")
        self.Fly = QComboBox()
        self.Fly.addItems(['1', '2'])
        SettingLayout.addWidget(self.FlyT, 1, 0)
        SettingLayout.addWidget(self.Fly, 1, 1)
        self.BackT = QLabel()
        self.BackT.setText("배경화면")
        self.Back = QComboBox()
        self.Back.addItems(['1', '2', '3'])
        SettingLayout.addWidget(self.BackT, 2, 0)
        SettingLayout.addWidget(self.Back, 2, 1)

        buttonLayout = QGridLayout()
        self.Start = QPushButton('start', self)
        buttonLayout.addWidget(self.Start, 0, 0)
        self.Quit = QPushButton('Quit', self)
        buttonLayout.addWidget(self.Quit, 0, 1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(GameReadyLayout, 0, 0)
        mainLayout.addLayout(SettingLayout, 1, 0)
        mainLayout.addLayout(buttonLayout, 2, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Shooting")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    shoot = Shoot()
    shoot.show()
    app.exec_()
