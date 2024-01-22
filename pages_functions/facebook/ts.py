from PyQt6.QtWidgets import QApplication, QMainWindow, QAction

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a QAction
        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)

        # Create a menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        # Add the action to the menu
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QAction Example')
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    app.exec()
