from pages_functions.__init__ import *

from ui.Facebook.Checker_ui import Ui_Form

from pages_functions.Public.Info import Info
from pages_functions.Facebook.Data.Chrome import *
from pages_functions.Facebook.Data.Edit import *

class Checker(QDialog):
    def __init__(self ,parent=None, data=None):
        super(Checker, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Info = Info()
        layout = QVBoxLayout(self.ui.widget_Info); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.Info)
        self.ui.Start.clicked.connect(lambda : Thread(target= self.Start).start())
        self.data = data
    def Start(self):
        if self.ui.Email_Password.isChecked():
            for i in self.data:
                result = Chrom().Login(i[2],i[3])
                input(".......")
        elif self.ui.Cookie.isChecked():
            for i in self.data:
                result = Chrom().View(i[5])
                input(".......")
        self.accept()
