from pages_functions.__init__ import *

from ui.Insta.Manger_insta_ui import Ui_Form
from pages_functions.__init__ import *
from pages_functions.Public.Add_Account import Add_Account
from pages_functions.Public.Export import Export
from pages_functions.Public.Info import Info


class Manger_Insta(QWidget):
    def __init__(self):
        super(Manger_Insta, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Info = Info()
        layout = QVBoxLayout(self.ui.widget_Info); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.Info)
        self.ui.Save.hide()
        self.changed_items = []
        self.update_run = False

        self.ui.comboBox.currentIndexChanged.connect(self.filter_table)
        self.ui.lineEdit.textChanged.connect(self.filter_table)
        self.ui.Select.clicked.connect(self.select_all_rows)
        self.ui.Checker.clicked.connect(lambda : Thread(target=self.Checker).start())
        self.ui.Add_Account.clicked.connect(self.Add_Account)
        self.ui.AddMultiAccount.clicked.connect(self.Add_Multi_Account)
        self.ui.Export.clicked.connect(self.Export)
        self.ui.Update_all.clicked.connect(lambda : Thread(target=self.Update).start())
        self.ui.Refresh.clicked.connect(self.Refresh)
        self.ui.Write_Change.clicked.connect(self.handle_item_change)
        
        self.ui.table.verticalHeader().hide()
        self.Refresh()
        self.ui.table.itemChanged.connect(lambda item: {self.changed_items.append(item) , self.ui.Write_Change.setEnabled(True)})
        
        
    def loadTableData(self,data):
        self.ui.table.setRowCount(len(data))
        for row, row_data in enumerate(data):
            select_checkbox_item = QTableWidgetItem()
            select_checkbox_item.setFlags(select_checkbox_item.flags() | 2) 
            select_checkbox_item.setCheckState(False)
            select_checkbox_item.setText(str(row + 1))
            self.ui.table.setItem(row, 0, select_checkbox_item)

            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.ui.table.setItem(row, col + 1, item)  

        headers = ["#"] + [description[0] for description in cursor.description]
        self.ui.table.setHorizontalHeaderLabels(headers)
        self.ui.table.setColumnWidth(0, 50)
        self.ui.table.setColumnWidth(1, 100)

        self.ui.table.horizontalHeader().setSectionResizeMode(5, QHeaderView.Stretch)
        self.ui.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.table.customContextMenuRequested.connect(self.show_context_menu)
        self.ui.Write_Change.setEnabled(False)
        self.changed_items.clear()

    def Refresh(self):
        self.data = cursor.execute("SELECT * FROM insta").fetchall()
        self.loadTableData(self.data)
    def show_context_menu(self, position):
        context_menu = QMenu(self)
    
        Update = context_menu.addAction("Update" , lambda : Thread(target=self.Update).start())
        show = context_menu.addAction("Show in Browser", lambda : Thread(target=self.View).start())
        Delete = context_menu.addAction("Delete", lambda : Thread(target=self.Delete).start())

        show.setShortcut(Qt.CTRL + Qt.Key_S)
        Update.setShortcut(Qt.CTRL + Qt.Key_U)
        Delete.setShortcut(Qt.Key_Delete)
        context_menu.exec_(self.mapToGlobal(position))

    def select_all_rows(self): 
        all_selected = all(self.ui.table.item(row, 0).checkState() == Qt.Checked for row in range(self.ui.table.rowCount()))
        for row in range(self.ui.table.rowCount()):
            checkbox_item = self.ui.table.item(row, 0)
            if all_selected: checkbox_item.setCheckState(Qt.Unchecked)  
            else: checkbox_item.setCheckState(Qt.Checked)  
    
    def filter_table(self):
        search_text = self.ui.lineEdit.text().lower()
        selected_column = self.ui.comboBox.currentIndex()

        if not search_text: self.filtered_data = self.data
        else: self.filtered_data = [item for item in self.data if item[selected_column] and search_text in item[selected_column].lower()]
        self.loadTableData(self.filtered_data)
        
    def handle_item_change(self):
        try:
            for i in self.changed_items:
                item = [self.ui.table.item(i.row(), col).text() for col in range(1, self.ui.table.columnCount())]
                cursor.execute('UPDATE insta SET groupname = ? WHERE username = ?', (item[0], item[1]))
                cursor.execute('UPDATE insta SET password = ? WHERE username = ?', (item[3], item[1]))
                cursor.execute('UPDATE insta SET cookies = ? WHERE username = ?', (item[4], item[1]))
                cursor.execute('UPDATE insta SET type = ? WHERE username = ?', (item[5], item[1]))
                conn.commit()
            self.ui.Write_Change.setEnabled(False)
            self.changed_items.clear()
        except Exception as e:
            print(e)
            pass
    def Add_Account(self):
        table_dialog = Add_Account(self)
        table_dialog.exec_()

    def Add_Multi_Account(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '')
        with open(fname[0], 'r', encoding='utf-8') as file:
            line =  file.readlines()
            for name in line:
                try:
                    group,username,email,password,cookies,type = name.split(':')
                    cursor.execute('INSERT INTO insta (groupname , username , email, password, cookies, type) VALUES (?, ?, ?, ?, ?, ?)', (group, username, email, password, cookies, type)); conn.commit()
                except: print('Failed Format')

    def Export(self):
        table_dialog = Export(self,self.ui.tableWidget )
        table_dialog.exec()
