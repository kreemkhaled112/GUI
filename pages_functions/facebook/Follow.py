from pages_functions.__init__ import *

from ui.Facebook.Follow_ui import Ui_Form
from pages_functions.Facebook.Edit_Face import Edit_Face

class Follow(QWidget):
    def __init__(self):
        super(Follow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        QVBoxLayout(self.ui.widget_Edit).addWidget(Edit_Face())
        self.ui.table.horizontalHeader().setStretchLastSection(True)
        self.ui.table.setColumnWidth(0, 50)
        self.ui.table.setColumnWidth(2, 350)
        self.ui.add.clicked.connect(self.Add)

    def Add(self):
        value = self.ui.lineEdit.text()

        item = QTableWidgetItem(value)
        self.ui.table.setRowCount(1)

        self.ui.table.setItem(0, 2, item)
        self.ui.table.verticalHeader().hide()

        self.ui.lineEdit.clear()      
          
    def Import(self):
        pass

    def Start(self):
        pass