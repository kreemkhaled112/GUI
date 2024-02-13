from pages_functions.__init__ import *

from ui.Facebook.Manger_face_ui import Ui_Form

from pages_functions.Public.Add_Account import Add_Account
from pages_functions.Facebook.Checker import Checker
from pages_functions.Public.Info import Info
from pages_functions.Public.Export import Export_insta
from pages_functions.Facebook.Data.Chrome import *
from pages_functions.Facebook.Data.Edit import *

class Manger_Face(QWidget):
    def __init__(self):
        super(Manger_Face, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Info = Info()
        layout = QVBoxLayout(self.ui.widget_Info); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.Info)
        self.ui.Save.setVisible(False)
        
        # Connect signal and slot
        self.ui.comboBox.currentIndexChanged.connect(self.filter_table)
        self.ui.lineEdit.textChanged.connect(self.filter_table)
        self.ui.Select.clicked.connect(self.select_all_rows)
        self.ui.Checker.clicked.connect(lambda : Thread(target=self.Checker).start())
        self.ui.Add_Account.clicked.connect(self.Add_Account)
        self.ui.AddMultiAccount.clicked.connect(self.Add_Multi_Account)
        self.ui.Export.clicked.connect(self.Export)
        self.ui.Refresh.clicked.connect(self.Refresh)
        self.ui.Write_Change.clicked.connect(self.handle_item_change)

        # self.ui.tableWidget.horizontalHeader().sectionClicked.connect(self.sortTable)

        
        self.ui.table.verticalHeader().hide()
        self.Refresh()
        self.ui.table.itemChanged.connect(lambda item: {self.changed_items.append(item) , self.ui.Write_Change.setEnabled(True)})

        self.changed_items = []
    def loadTableData(self,data):
        try:
            self.ui.table.setRowCount(len(data))
            for row, row_data in enumerate(data):
                select_checkbox_item = QTableWidgetItem()
                select_checkbox_item.setFlags(select_checkbox_item.flags() | Qt.ItemIsUserCheckable)
                select_checkbox_item.setCheckState(Qt.CheckState.Unchecked)
                select_checkbox_item.setText(str(row + 1))
                self.ui.table.setItem(row, 0, select_checkbox_item)

                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.ui.table.setItem(row, col + 1, item)

            self.ui.table.setColumnWidth(0, 50)
            self.ui.table.setColumnWidth(1, 100)
            self.ui.table.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
            headers = ["#"] + [description[0] for description in cursor.description]
            self.ui.table.setHorizontalHeaderLabels(headers)
            self.ui.table.setContextMenuPolicy(Qt.CustomContextMenu)
            self.ui.table.customContextMenuRequested.connect(self.show_context_menu)
            self.ui.Write_Change.setEnabled(False)
            self.changed_items.clear()
        except:pass
    def Refresh(self):
        self.data = cursor.execute("SELECT * FROM account").fetchall()
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
            if all_selected:
                checkbox_item.setCheckState(Qt.Unchecked)  
            else:
                checkbox_item.setCheckState(Qt.Checked)  
                
    def filter_table(self):
        search_text = self.ui.lineEdit.text().lower()
        selected_column = self.ui.comboBox.currentIndex()

        if not search_text: pass
        else: 
            filtered_data = [item for item in self.data if item[selected_column] and search_text in item[selected_column].lower()]
            self.loadTableData(filtered_data)
    def handle_item_change(self):
        try:
            for i in self.changed_items:
                item = [self.ui.table.item(i.row(), col).text() for col in range(1, self.ui.table.columnCount())]
                cursor.execute('UPDATE account SET groupname = ? WHERE email = ?', (item[0], item[2]))
                cursor.execute('UPDATE account SET name = ? WHERE email = ?', (item[1], item[2]))
                cursor.execute('UPDATE account SET username = ? WHERE email = ?', (item[4], item[2]))
                cursor.execute('UPDATE account SET cookies = ? WHERE email = ?', (item[5], item[2]))
                cursor.execute('UPDATE account SET insta = ? WHERE email = ?', (item[7], item[2]))
                conn.commit()
            self.ui.Write_Change.setEnabled(False)
            self.changed_items.clear()
        except Exception as e:
            print(e)
            pass
    
    def Add_Account(self):
        table_dialog = Add_Account(self)
        table_dialog.exec()
    def Add_Multi_Account(self):
        group = "None"
        name= "None"
        email = "None"
        password= "None"
        username= "None"
        cookies= "None"
        type= "None"
        insta= "None"
        fname = QFileDialog.getOpenFileName(self, 'Open File', '')
        with open(fname[0], 'r', encoding='utf-8') as file:
            line =  file.readlines()
            for i in line:
                try:
                    elements = i.split(':')
                    if len(elements) == 2:
                        email , password = elements
                    elif len(elements) == 3:    
                        email , password , cookies = elements
                    cursor.execute('INSERT INTO account (groupname ,name ,email, password, username ,cookies, gendar, insta) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (group, name, email, password,username, cookies, type, insta)); conn.commit()
                except Exception as e: print(f'Failed Format {e}')
    def Update(self):
        for row in range(self.ui.table.rowCount()):
            checkbox_item = self.ui.table.item(row, 0)
            if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                item = self.ui.table.item(row, 6)
                if item is None or item.text() == '' or item.text() == 'None':
                    i = [self.ui.table.item(row, col).text() for col in range(1,self.ui.table.columnCount())]
                    self.Info.ui.label.setText(f"Logging {i[2]}:{i[3]}")
                    result = Chrom().Login(i[2],i[3])
                    if result[0]  == 'success':
                        cursor.execute('UPDATE account SET name = ? WHERE email = ?', (result[2], i[2])); conn.commit()
                        cursor.execute('UPDATE account SET username = ? WHERE email = ?', (re.search(r'c_user=(\d+)', result[1]).group(1), i[2])); conn.commit()
                        cursor.execute('UPDATE account SET cookies = ? WHERE email = ?', (result[1], i[2])); conn.commit()
                        self.Info.Add(1,result[2],"Login",f"Done Login {i[2]}:{i[3]}")
                    else :
                        self.Info.ui.label.setText(f"Faield Login {i[2]}:{i[3]}")
                        self.Info.Add(0,f"{i[2]}:{i[3]}","Login",f'{result}')
                else:
                    item = self.ui.table.item(row, 2)
                    if item is None or item.text() == '' or item.text() == 'None':
                        i = [self.ui.table.item(row, col).text() for col in range(1,self.ui.table.columnCount())]
                        result = Get_Name(i[5]).Get()
                        cursor.execute('UPDATE account SET name = ? WHERE email = ?', (result, i[2])); conn.commit()
                        cursor.execute('UPDATE account SET username = ? WHERE email = ?', (re.search(r'c_user=(\d+)', i[5]).group(1), i[2])); conn.commit()
        self.Info.ui.label.setText(f"Finished")
    def View(self):
        selected_row = self.ui.table.currentRow()
        if selected_row >= 0:
            deleted_row_data = []
            for col in range(1,self.ui.table.columnCount()):
                item = self.ui.table.item(selected_row, col)
                deleted_row_data.append(item.text())
            value = Chrom().View(deleted_row_data[5])
            self.ui.table.setItem(selected_row, 6, QTableWidgetItem(str(value)))
        else: print("لا يوجد صف محدد.")
    def Delete(self):
        selected_row = self.ui.table.currentRow()
        if selected_row >= 0:
            deleted_row_data = []
            for col in range(self.ui.table.columnCount()):
                item = self.ui.table.item(selected_row, col)
                deleted_row_data.append(item.text())
            self.ui.table.removeRow(selected_row)
            cursor.execute(f'DELETE FROM account WHERE email = "{deleted_row_data[3]}" '); conn.commit()
            self.ui.Write_Change.setEnabled(False)
            self.changed_items.clear()
        else: print("لا يوجد صف محدد.")
    def Checker(self):
        for row in range(self.ui.table.rowCount()):
            checkbox_item = self.ui.table.item(row, 0)
            if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                data = [self.ui.table.item(row, col).text() for col in range(1, self.ui.table.columnCount())]
                value = Chrom().View(data[5])
                if value == 'checkpoint':
                    cursor.execute(f'DELETE FROM account WHERE email = "{data[2]}" '); conn.commit()
                else: self.ui.table.setItem(row, 6, QTableWidgetItem(str(value)))
    def Export(self):
        table_dialog = Export_insta(self,self.ui.table )
        table_dialog.exec()
