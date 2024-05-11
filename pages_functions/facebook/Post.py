from pages_functions.__init__ import *

from ui.Facebook.User_ui import Ui_Form
from pages_functions.Public.Info import Info
from pages_functions.Public.Edit import Edit
from pages_functions.Facebook.Data.Action import *

class Post(QWidget):
    def __init__(self ):
        super(Post, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Run = False
        self.succes = 0
        self.failed = 0
        self.order = 0
        self.ui_Edit = Edit(Info())
        layout = QVBoxLayout(self.ui.widget_Edit); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.ui_Edit)

        self.ui_Edit.ui.Add_Profile_Photo_check.hide()
        self.ui_Edit.ui.Add_Cover_check.hide()
        self.ui_Edit.ui.Add_City_check.hide()
        self.ui_Edit.ui.Add_Hometown_check.hide()
        self.ui_Edit.ui.Add_Post_check.hide()
        self.ui_Edit.ui.Add_Bio_check.hide()
        self.ui_Edit.ui.Add_Friend_check.hide()
        self.ui_Edit.ui.Join_Group_check.hide()
        self.ui_Edit.ui.Follow_check.hide()
        self.ui_Edit.ui.Un_Follow_check.hide()
        self.ui_Edit.ui.Profrssional_check.hide()
        self.ui_Edit.ui.Change_Password_check.hide()
        self.ui_Edit.ui.Lock_Profile.hide()

        self.ui_Edit.ui.widget_73.hide()
        self.ui_Edit.ui.widget_75.hide()
        self.ui_Edit.ui.widget_share.hide()
        self.ui_Edit.Info.ui.table.setColumnHidden(3, True)



        self.ui.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table.setColumnWidth(0, 50)

        self.ui.add.clicked.connect(self.Add)
        self.ui_Edit.ui.Start.clicked.connect(lambda : Thread(target=self.Start).start())
        self.ui_Edit.Info.ui.label.setText("welcom like")

    def Add(self):
        value = self.ui.lineEdit.text()

        current_row = self.ui.table.rowCount()
        self.ui.table.insertRow(current_row)

        self.ui.table.setItem(current_row, 0, QTableWidgetItem(str(current_row + 1)))

        try:
            if "posts" in value :
                id  = re.search(r'facebook.com/([^/]+)', value).group(1)            
            self.ui.table.setItem(current_row, 1 , QTableWidgetItem(id))
        except:self.ui.table.setItem(current_row, 1 , QTableWidgetItem("Unknow"))

        self.ui.table.setItem(current_row, 2 , QTableWidgetItem(value))

        delete_button = QPushButton('حذف', self)
        delete_button.clicked.connect(lambda _, row=current_row: self.delete_row(row))
        self.ui.table.setCellWidget(current_row, 3, delete_button)

        self.ui.table.verticalHeader().hide()
        
        self.ui.lineEdit.clear() 

    def Import(self):
        pass
    def delete_row(self, row):
        self.ui.table.removeRow(row)
    def Edit(self,url,name,cookie):
        try:
            if  self.ui_Edit.ui.Like_check.isChecked():
                self.ui_Edit.Info.ui.label.setText(f"Try Like {name} ")
                result = Like(url, self.ui_Edit.reaction_id(), cookie).Start()  
                self.ui_Edit.Info.Add(result[1],name,'Post',"Like",f'{result[0]} To {url}')
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.ui_Edit.Info.Update(s=self.succes,f=self.failed,o=self.order) ;  sleep(self.time)
            if self.ui_Edit.ui.Comment_check.isChecked():
                self.ui_Edit.Info.ui.label.setText(f"Try Comment {name} ")
                result = Comment(url, 'good', cookie).Start()  
                self.ui_Edit.Info.Add(result[1],name,'Post',"Comment",f'{result[0]} To {url}')
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.ui_Edit.Info.Update(s=self.succes,f=self.failed,o=self.order) ;  sleep(self.time)
            if self.ui_Edit.ui.Share_check.isChecked():
                self.ui_Edit.Info.ui.label.setText(f"Try Share {name} ")
                result = Share(url, "", cookie).Start()
                self.ui_Edit.Info.Add(result[1],name,'Post',"Share",f'{result[0]} To {url}')
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.ui_Edit.Info.Update(s=self.succes,f=self.failed,o=self.order) ;  sleep(self.time)
            return 'succes'
        except: return "Error Edit"
    def Start(self):
        if self.ui_Edit.ui.Number_Account.text() == '0': self.ui_Edit.ui.Start.setChecked(False) ; QMessage(text = 'No Account Selected').mainloop()
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
            else: self.ui_Edit.ui.Start.setChecked(False) ; QMessage(text = 'No Url Add').mainloop()
        