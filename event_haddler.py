    def buttonClicked(self):
        global max_speed, min_speed, background, occurrock

        button = self.sender()
        key = button.text()
        if key == '1':
            background = "background.png"
        elif key == '2':
            background = "background2.jpg"
        elif key == '3':
            background = "background3.jpg"
        elif key == '11':
            Fly = '3'
        elif key == '22':
            Fly = '2'
        elif key == 'easy':
            max_speed = 200
            min_speed = 300
            occurrock = 100
        elif key == 'normal':
            max_speed = 100
            min_speed = 200
            occurrock = 150
        elif key == 'hard':
            max_speed = 50
            min_speed= 100
            occurrock = 200
        elif key == 'Start':
            PyshootingR.main(background, max_speed, min_speed, occurrock)
        elif key == 'Quit':
            sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
