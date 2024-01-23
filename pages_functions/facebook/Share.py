from pages_functions.__init__ import *

from ui.Facebook.Share_ui import Ui_Form

class Share(QWidget):
    def __init__(self):
        super(Share, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        