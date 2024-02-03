from pages_functions.__init__ import *

from pages_functions.Public.Edit import Edit
from pages_functions.Public.Info import Info
from pages_functions.Facebook.Data.Chrome import *
from pages_functions.Facebook.Data.Edit import *
from pages_functions.Facebook.Data.AddFriend import *
from pages_functions.Facebook.Data.Share import *
from pages_functions.Facebook.Data.Like import *
from pages_functions.Facebook.Data.JoinGroup import *
from pages_functions.Facebook.Data.Follow import *
from pages_functions.Public.Select import Select

class Edit_Face(QWidget):
    def __init__(self):
        super(Edit_Face, self).__init__()

        self.ui_Edit = Edit(Info())
        layout = QVBoxLayout()
        layout.addWidget(self.ui_Edit)
        self.setLayout(layout)
        self.ui_Edit.ui.Start.clicked.connect(lambda : Thread(target=self.ui_Edit.Start).start())