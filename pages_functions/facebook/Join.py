from pages_functions.__init__ import *

from ui.Facebook.Join_ui import Ui_Form

class Join(QWidget):
    def __init__(self):
        super(Join, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        