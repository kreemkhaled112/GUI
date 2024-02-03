from pages_functions.__init__ import *
from ui.Public.Info_ui import Ui_Form

class Info(QDialog):
    def __init__(self ):
        super(Info, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.table.hide()
        self.ui.table.setColumnWidth(0, 20)
        self.ui.table.setColumnWidth(1, 120)
        self.ui.table.setColumnWidth(2, 100)
    def Add(self,type,name,action,value):
        if     type == 0 :  type = "❌"
        elif   type == 1 :  type = "✅"
        else : type = "⚠️"

        self.ui.table.insertRow(0)  
        self.ui.table.setItem(0, 0,  QTableWidgetItem(type))
        self.ui.table.setItem(0, 1,  QTableWidgetItem(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.ui.table.setItem(0, 2 , QTableWidgetItem(name)) 
        self.ui.table.setItem(0, 3 , QTableWidgetItem(action)) 
        self.ui.table.setItem(0, 4 , QTableWidgetItem(value)) 
        self.ui.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.ui.table.verticalHeader().hide()
    def Update(self,s=None,f=None,time=None):
        self.ui.successful.setText(str(s))
        self.ui.faild.setText(str(f))
        self.ui.total.setText(str(s+f))
        self.ui.time.setText(str(time))