from pages_functions.__init__ import *

from ui.Facebook.Accept_ui import Ui_Form

class Accept(QWidget):
    def __init__(self):
        super(Accept, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        