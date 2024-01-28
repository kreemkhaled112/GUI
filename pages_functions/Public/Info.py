from pages_functions.__init__ import *

from ui.Public.Info_ui import Ui_Form

class Info(QDialog):
    def __init__(self ):
        super(Info, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.table.hide()