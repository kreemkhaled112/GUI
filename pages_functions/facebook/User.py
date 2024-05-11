from pages_functions.__init__ import *

from ui.Facebook.User_ui import Ui_Form
from pages_functions.Public.Info import Info
from pages_functions.Public.Edit import Edit
from pages_functions.Facebook.Data.Edit import *
from pages_functions.Facebook.Data.Action import *

class User(QWidget):
    def __init__(self):
        super(User, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Run = False

        self.ui_Edit = Edit(Info())
        layout = QVBoxLayout(self.ui.widget_Edit); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.ui_Edit)

        self.ui_Edit.ui.Add_Profile_Photo_check.hide()
        self.ui_Edit.ui.Add_Cover_check.hide()
        self.ui_Edit.ui.Add_City_check.hide()
        self.ui_Edit.ui.Add_Hometown_check.hide()
        self.ui_Edit.ui.Add_Post_check.hide()
        self.ui_Edit.ui.Add_Bio_check.hide()
        self.ui_Edit.ui.Like_check.hide()
        self.ui_Edit.ui.Comment_check.hide()
        self.ui_Edit.ui.Comment_Like_check.hide()
        self.ui_Edit.ui.Share_check.hide()
        self.ui_Edit.ui.Profrssional_check.hide()
        self.ui_Edit.ui.Change_Password_check.hide()
        self.ui_Edit.ui.Lock_Profile.hide()

        self.ui_Edit.ui.widget_friend.hide()
        self.ui_Edit.ui.widget_group.hide()
        self.ui_Edit.ui.widget_follow.hide()
        self.ui_Edit.ui.widget_follow_2.hide()
        self.ui_Edit.Info.ui.table.setColumnHidden(3, True)


        self.ui.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table.setColumnWidth(0, 50)

        self.ui.add.clicked.connect(self.Add)
        self.ui_Edit.ui.Start.clicked.connect(lambda : Thread(target=self.Start).start())
        self.ui_Edit.Info.ui.label.setText("welcom User")

    def Add(self):
        value = self.ui.lineEdit.text()

        current_row = self.ui.table.rowCount()
        self.ui.table.insertRow(current_row)
        self.ui.table.setItem(current_row, 0, QTableWidgetItem(str(current_row + 1)))

        try: 
            id  = re.search(r'/([^/]+)$', value).group(1) if re.search(r'/([^/]+)$', value) else None
            self.ui.table.setItem(current_row, 1 , QTableWidgetItem(id))
        except:Thread(target=self.name,args=(value,current_row)).start()

        self.ui.table.setItem(current_row, 2 , QTableWidgetItem(value))
        delete_button = QPushButton('حذف', self)
        delete_button.clicked.connect(lambda _, row=current_row: self.delete_row(row))
        self.ui.table.setCellWidget(current_row, 3, delete_button)

        self.ui.table.verticalHeader().hide()
        self.ui.lineEdit.clear()      
    def name (self,value,row):
        item = QTableWidgetItem(Name().Get(value))
        self.ui.table.setItem(row, 1 , item)

    def Import(self):
        pass
    def delete_row(self, row):
        self.ui.table.removeRow(row)
    def Edit(self,url,name,cookie):
        try:
            if  self.ui_Edit.ui.Follow_check.isChecked():
                result = Follow_www(url, cookie).Start()  
                self.ui_Edit.Info.ui.label.setText(f"{name} {result[0]}")
                self.ui_Edit.Info.Add(result[1],name,'User',"Follow",f'{result[0]} To {url}')
                self.success += 1 if result[1] == 1 else self.failed + 1 ; self.ui_Edit.Info.Update(s=self.success,f=self.failed)
            if self.ui_Edit.ui.Un_Follow_check.isChecked():
                result = Un_Follow(url, cookie).Start()  
                self.ui_Edit.Info.ui.label.setText(f"{name} {result[0]}")
                self.ui_Edit.Info.Add(result[1],name,'User',"Un Follow",f'{result[0]} To {url}')
                self.success += 1 if result[1] == 1 else self.failed + 1 ; self.ui_Edit.Info.Update(s=self.success,f=self.failed)
            if self.ui_Edit.ui.Join_Group_check.isChecked():
                result = JoinGroup(url, cookie).Start()
                self.ui_Edit.Info.ui.label.setText(f"{name} {result[0]}")
                self.ui_Edit.Info.Add(result[1],name,'User',"JoinGroup",f'{result[0]} To {url}')
                self.success += 1 if result[1] == 1 else self.failed + 1 ; self.ui_Edit.Info.Update(s=self.success,f=self.failed)
            return 'succes'
        except Exception as e: 
            self.ui_Edit.Info.ui.label.setText(f"{name} Error Edit")
            self.ui_Edit.Info.Add(0,name,'User',"None",f'{e}')
            return 'Error Edit'
    def Start(self):
        self.success = 0
        self.failed = 0
        if self.ui_Edit.ui.Number_Account.text() == '0': QMessage(text = 'No Account Selected').mainloop()
        else :
            second_column_data = [self.ui.table.item(row, 2).text() for row in range(self.ui.table.rowCount())]
            if second_column_data :
                self.Run = not self.Run
                if self.Run:
                    self.ui_Edit.ui.Start.setText("Stop")
                    self.ui_Edit.Info.Update(0,0,0) ; self.succes=0 ; self.failed=0
                else:
                    self.ui_Edit.ui.Start.setText("Start")
                    return
                for url in second_column_data :
                    for info in self.ui_Edit.info :
                        if self.Run :
                            self.Edit(url,info[1],info[5])
                self.ui_Edit.Info.ui.label.setText("Finished")
                self.ui_Edit.ui.Start.setText("Start")
                self.ui_Edit.ui.Start.setChecked(False)
                self.Run = False
            else: QMessage(text = 'No Url Add').mainloop()

        