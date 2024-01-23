from pages_functions.__init__ import *

from ui.Facebook.Freind_ui import Ui_Form

class Friend(QWidget):
    def __init__(self):
        super(Friend, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        