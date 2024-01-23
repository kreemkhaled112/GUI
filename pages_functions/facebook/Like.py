from pages_functions.__init__ import *

from ui.Facebook.Like_ui import Ui_Form

class Like(QWidget):
    def __init__(self):
        super(Like, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        