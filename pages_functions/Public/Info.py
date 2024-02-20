from pages_functions.__init__ import *
from ui.Public.Info_ui import Ui_Form

class Info(QDialog):
    def __init__(self ):
        super(Info, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Success = 0
        self.Failed = 0
        self.ui.table.hide()
        self.ui.table.verticalHeader().hide()
        self.ui.table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.ui.table.setColumnWidth(0, 18)
        self.ui.table.setColumnWidth(1, 120)
        self.ui.table.setColumnWidth(2, 120)
    def Add(self,type,name,section,action,message):
        if     type == 0 :  type = "❌"
        elif   type == 1 :  type = "✅"
        else : type = "⚠️"

        self.ui.table.insertRow(0)  
        self.ui.table.setItem(0, 0,  QTableWidgetItem(type))
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ui.table.setItem(0, 1,  QTableWidgetItem(data))
        self.ui.table.setItem(0, 2 , QTableWidgetItem(name)) 
        self.ui.table.setItem(0, 3 , QTableWidgetItem(section)) 
        self.ui.table.setItem(0, 4 , QTableWidgetItem(action)) 
        self.ui.table.setItem(0, 5 , QTableWidgetItem(message))
        try: cursor.execute('INSERT INTO Reports (type, Data , Name, Section, Acction ,Message) VALUES ( ?, ?, ?, ?, ?, ?)', ( type ,data, name, section, action, message)) ;conn.commit()
        except: print("Faild Update")
    def Update(self,s=None,f=None,time=None):
        if s :
            if s == 0 :
                self.Success = 0
                self.Failed = 0
            else: self.Success += s
        if f : self.Failed += f

        self.ui.successful.setText(str(self.Success))
        self.ui.faild.setText(str(self.Failed))
        self.ui.total.setText(str(self.Success+self.Failed))
        self.ui.time.setText(str(time))