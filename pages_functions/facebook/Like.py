from pages_functions.__init__ import *

from ui.Facebook.Follow_ui import Ui_Form

from pages_functions.Facebook.Edit_Face import Edit_Face
from pages_functions.Facebook.Data.Edit import *
from pages_functions.Facebook.Data.Like import Like as like

class Like(QWidget):
    def __init__(self ):
        super(Like, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.is_running = False

        self.ui_Edit = Edit_Face()
        QVBoxLayout(self.ui.widget_Edit).addWidget(self.ui_Edit)

        self.ui_Edit.ui.Add_Profile_Photo_check.hide()
        self.ui_Edit.ui.Add_Cover_check.hide()
        self.ui_Edit.ui.Add_Post_check.hide()
        self.ui_Edit.ui.Add_Bio_check.hide()
        self.ui_Edit.ui.Profrssional_check.hide()
        self.ui_Edit.ui.Change_Password_check.hide()

        self.ui_Edit.ui.scrollArea_Like.hide()
        self.ui_Edit.ui.widget_follow.hide()
        self.ui_Edit.ui.widget_friend.hide()
        self.ui_Edit.ui.widget_group.hide()
        self.ui_Edit.ui.widget_share.hide()


        self.ui.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table.setColumnWidth(0, 50)

        self.ui.add.clicked.connect(self.Add)
        self.ui_Edit.ui.Start.clicked.connect(lambda : Thread(target=self.Start).start())

    def Add(self):
        value = self.ui.lineEdit.text()

        current_row = self.ui.table.rowCount()
        self.ui.table.insertRow(current_row)

        item = QTableWidgetItem(str(current_row + 1))
        self.ui.table.setItem(current_row, 0, item)

        # Thread(target=self.name,args=(value,current_row)).start()

        item = QTableWidgetItem(value)
        self.ui.table.setItem(current_row, 2 , item)

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
    def Start(self):
        success = 0
        failed = 0
        if self.ui_Edit.ui.Number_Account.text() == '0': QMessage(text = 'No Account Selected').mainloop()
        else :
            second_column_data = [self.ui.table.item(row, 2).text() for row in range(self.ui.table.rowCount())]
            if second_column_data :
                if self.is_running == False :
                    self.ui_Edit.ui.Start.setText("Stop")
                    self.is_running = True
                elif self.is_running :
                    self.ui_Edit.ui.Start.setText("Start")
                    self.is_running = False
                if self.ui_Edit.ui.Like_radio.isChecked():
                    reaction_type = "Like"
                elif self.ui_Edit.ui.Love_radio.isChecked():
                    reaction_type = "Love"
                elif self.ui_Edit.ui.Care_radio.isChecked():
                    reaction_type = "Care"
                elif self.ui_Edit.ui.Haha_radio.isChecked():
                    reaction_type = "Haha"
                elif self.ui_Edit.ui.Wow_radio.isChecked():
                    reaction_type = "Wow"
                elif self.ui_Edit.ui.Sad_radio.isChecked():
                    reaction_type = "Sad"
                elif self.ui_Edit.ui.Random_radio.isChecked():
                    reaction_type = "Random"
                for url in second_column_data :
                    for cookie in self.ui_Edit.info :
                        self.ui_Edit.Info.ui.label.setText(f"{cookie[1]} Try {reaction_type} ")
                        result = self.ui_Edit.Edit(cookie[5],id_like=url,type=reaction_type)
                        self.ui_Edit.Info.ui.label.setText(f"{cookie[1]} {result[8][0]}")

                        if result[1] == 0 : failed += 0 ; type = "❌"
                        elif result[1] == 1 : success += 1 ; type = "✅"
                        else :  failed += 0 ;  type = "⚠️"

                        self.ui_Edit.Info.Update(s=success,f=failed)
                        self.ui_Edit.Info.Add(type,cookie[1],"Like",f"{result[8][0]} To {url}")
                print('Fineshed')
                self.ui_Edit.ui.Start.setText("Start")
                self.is_running = False
            else: QMessage(text = 'No Url Add').mainloop()
        