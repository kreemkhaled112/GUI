from pages_functions.__init__ import *

from ui.Facebook.Manger_face_ui import Ui_Form
from pages_functions.Public.Info import Info
from pages_functions.Public.Export import Export
from pages_functions.Facebook.Data.Chrome import *
from pages_functions.Facebook.Login import *

class Manager_Face(QWidget):
    def __init__(self):
        super(Manager_Face, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.succes = 0
        self.failed = 0
        self.order = 0
        self.checkpoint = 0
        self.Info = Info()
        layout = QVBoxLayout(self.ui.widget_Info); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.Info)
        self.ui.Save.hide()
        self.ui.Change_Password.hide()
        
        # Connect signal and slot
        self.ui.comboBox.currentIndexChanged.connect(self.filter_table)
        self.ui.lineEdit.textChanged.connect(self.filter_table)
        self.ui.Select.clicked.connect(self.select_all_rows)
        self.ui.AddMultiAccount.clicked.connect(self.Add_Multi_Account)
        self.ui.Export.clicked.connect(self.Export)
        self.ui.Login.clicked.connect(lambda : Thread(target=self.Login).start())
        self.ui.Refresh.clicked.connect(self.Refresh)
        self.ui.Delete_all.clicked.connect(lambda : Thread(target=self.Delete).start())
        self.ui.Write_Change.clicked.connect(self.handle_item_change)
        self.ui.Update.clicked.connect(lambda : Thread(target=self.Update).start())
        self.ui.Change.clicked.connect(lambda : Thread(target=self.Change).start())
        self.ui.Epsilon.clicked.connect(lambda : Thread(target=self.Epsilon).start())
        self.ui.Change_Password.clicked.connect(lambda : Thread(target=self.Change_Password).start())
        
        self.ui.table.verticalHeader().hide()
        self.Refresh()
        self.ui.table.itemChanged.connect(lambda item: (self.changed_items.append(item), self.ui.Write_Change.setEnabled(True)) if item.column() != 0 else None)
        self.changed_items = []
        self.Run = False
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
            self.ui.table.setColumnWidth(1, 80)
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
        self.data = cursor.execute("SELECT * FROM Account").fetchall()
        self.loadTableData(self.data)
    def show_context_menu(self, position):
        context_menu = QMenu(self)
    
        Update = context_menu.addAction("Update" , lambda : Thread(target=self.Update, args=(context_menu,)).start())
        show = context_menu.addAction("Show in Browser", lambda: Thread(target=self.View, args=(context_menu,)).start())
        Delete = context_menu.addAction("Delete", lambda : Thread(target=self.Delete_row, args=(context_menu,)).start())

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
        search_text = self.ui.lineEdit.text().lower().strip()
        selected_column = self.ui.comboBox.currentIndex()

        if not search_text: self.loadTableData(self.data)
        else: 
            self.changed_items.clear()
            filtered_data = [item for item in self.data if item[selected_column] and search_text in item[selected_column].lower()]
            self.loadTableData(filtered_data)
    def handle_item_change(self):
        try:
            for i in self.changed_items:
                item = [self.ui.table.item(i.row(), col).text() for col in range(1, self.ui.table.columnCount())]
                cursor.execute('UPDATE Account SET groupname = ? WHERE email = ?', (item[0], item[2]))
                cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (item[1], item[2]))
                cursor.execute('UPDATE Account SET password = ? WHERE email = ?', (item[3], item[2]))
                cursor.execute('UPDATE Account SET username = ? WHERE email = ?', (item[4], item[2]))
                cursor.execute('UPDATE Account SET cookies = ? WHERE email = ?', (item[5], item[2]))
                conn.commit()
            self.ui.Write_Change.setEnabled(False)
            self.changed_items.clear()
        except Exception as e:
            print(e)
            pass
    def Add_Multi_Account(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '')
        def thread():
            self.Info.Update(0,0,0) ;self.succes = 0 ; self.failed = 0
            with open(fname[0], 'r', encoding='utf-8') as file:
                line =  file.readlines()
                for index,i in enumerate(line):
                    group = "None"
                    name= "None"
                    email = "None"
                    password= "None"
                    username= "None"
                    cookies= "None"
                    try:
                        if i.strip():
                            elements = i.replace(" ", "").split(':')
                            self.Info.ui.label.setText(f"Try Add {index}")
                            if len(elements) == 2:
                                email , password = elements
                            elif len(elements) == 3:
                                email , password , cookies = elements
                            cookies = cookies.strip().replace(" ", "")
                            existing_id = cursor.execute(f"SELECT * FROM Account WHERE email = '{email}' ").fetchall()
                            if not existing_id:
                                cursor.execute('INSERT INTO Account (groupname ,name ,email, password, username ,cookies) VALUES (?, ?, ?, ?, ?, ?)', (group, name, email.strip(), password.strip(),username, cookies )); conn.commit() 
                                self.succes += 1
                            else : self.failed += 1
                    except Exception as e: print(f'Failed Format Line {index}:{e}')
                self.Info.Add(1,'Add Multi Account','Account Manager',"Add Account",f'Total : {len(line)} Succes : {self.succes} Failed : {self.failed}')
                self.succes += 1 ; self.Info.Update(s=self.succes,f=self.failed,o=self.order)
                self.Refresh()
                self.Info.ui.label.setText(f"Finished")
        if fname[0]:
            Thread(target=thread).start()

    def Login(self):
        self.Run = not self.Run
        if self.Run:
            self.ui.Login.setText("Stop")
            self.Info.Update(0, 0, 0) ;self.succes = 0 ; self.failed = 0
        else:
            self.ui.Login.setText("Login") ; self.ui.Login.setChecked(False)
            self.Info.ui.label.setText("Finished Login")
            return
        for row in range(self.ui.table.rowCount()):
            if self.Run:
                checkbox_item = self.ui.table.item(row, 0)
                if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                    item = self.ui.table.item(row, 6)
                    i = [self.ui.table.item(row, col).text() for col in range(1,self.ui.table.columnCount())]
                    self.Info.ui.label.setText(f"Logging {i[2]}:{i[3]}")
                    result = Chrom('headless').Login(i[2],i[3])
                    try:
                        if result[0]  == 'success':
                            try:
                                cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (result[2], i[2])); self.ui.table.setItem(row, 2, QTableWidgetItem(str(result[2])))
                                cursor.execute('UPDATE Account SET cookies = ? WHERE email = ?', (result[1], i[2])); self.ui.table.setItem(row, 6, QTableWidgetItem(str(result[1])))
                                try:cursor.execute('UPDATE Account SET username = ? WHERE email = ?', (re.search(r'c_user=(\d+)', result[1]).group(1), i[2])); self.ui.table.setItem(row, 5, QTableWidgetItem(str(re.search(r'c_user=(\d+)', result[1]).group(1))))
                                except:pass
                                conn.commit()
                                self.Info.Add(1,result[2],'Account Manager',"Login",f"Done Login {i[2]}:{i[3]}")
                                self.succes += 1 ; self.Info.Update(s=self.succes,f=self.failed,o=self.order)
                                checkbox_item.setCheckState(Qt.Unchecked)
                            except Exception as e:
                                self.Info.ui.label.setText(f"Faield Log {i[2]}:{i[3]}")
                                self.Info.Add(0,f"{i[2]}:{i[3]}",'Account Manager',"Login",f'{e}')
                                self.failed += 1 ; self.Info.Update(s=self.succes,f=self.failed,o=self.order)
                        else :
                            self.Info.ui.label.setText(f"Faield Login {i[2]}:{i[3]}")
                            cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (result[0], i[2])); self.ui.table.setItem(row, 2, QTableWidgetItem(str(result[0])))
                            cursor.execute('UPDATE Account SET cookies = ? WHERE email = ?', (result[1], i[2])); self.ui.table.setItem(row, 6, QTableWidgetItem(str(result[1])))
                            try:cursor.execute('UPDATE Account SET username = ? WHERE email = ?', (re.search(r'c_user=(\d+)', result[1]).group(1), i[2])); self.ui.table.setItem(row, 5, QTableWidgetItem(str(re.search(r'c_user=(\d+)', result[1]).group(1))))
                            except:pass
                            conn.commit()
                            self.Info.Add(0,f"{i[2]}:{i[3]}",'Account Manager',"Login",f'{result[0]}')
                            self.succes += 1 ;self.Info.Update(s=self.succes,f=self.failed,o=self.order)
                    except:pass
        self.ui.Login.setText("Login") ; self.ui.Login.setChecked(False)
        self.Info.ui.label.setText(f"Finished Login")
        self.Run = False
        
    def View(self,menu):
        menu.hide()
        selected_row = self.ui.table.currentRow()
        if selected_row >= 0:
            i = []
            for col in range(1,self.ui.table.columnCount()):
                item = self.ui.table.item(selected_row, col)
                i.append(item.text())
            value = Chrom().View(i[5])
            if value == "" : pass
            else :
                cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (value[0], i[2])); self.ui.table.setItem(selected_row, 2, QTableWidgetItem(str(value[0])))
                cursor.execute('UPDATE account SET cookies = ? WHERE email = ?', (value[1], i[2])); self.ui.table.setItem(selected_row, 6, QTableWidgetItem(str(value[1])))
                conn.commit()
    def Delete_row(self,menu):
        menu.hide()
        selected_row = self.ui.table.currentRow()
        if selected_row >= 0:
            deleted_row_data = []
            for col in range(1,self.ui.table.columnCount()):
                item = self.ui.table.item(selected_row, col)
                deleted_row_data.append(item.text())
            self.ui.table.removeRow(selected_row)
            cursor.execute(f'DELETE FROM Account WHERE email = "{deleted_row_data[2]}" '); conn.commit()
            self.ui.Write_Change.setEnabled(False)
            self.changed_items.clear()
            self.Refresh()
        else: print("لا يوجد صف محدد.")
    def Delete(self):
        self.Run = not self.Run
        if self.Run:
            self.ui.Delete_all.setText("Stop")
        else:
            self.ui.Delete_all.setText("Delete") ; self.ui.Delete_all.setChecked(False)
            self.Info.ui.label.setText("Finished Delete")
            return
        for row in reversed(range(self.ui.table.rowCount())):
            checkbox_item = self.ui.table.item(row, 0)
            if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                item = self.ui.table.item(row, 3)
                cursor.execute(f'DELETE FROM Account WHERE email = "{item.text()}" ')
                self.ui.table.removeRow(row)
        conn.commit()
        self.ui.Delete_all.setText("Delete") ; self.ui.Delete_all.setChecked(False)
        self.Info.ui.label.setText("Finished Delete")
        self.Run = False
        self.Refresh()
    def Update(self):
        self.Run = not self.Run
        if self.Run:
            self.ui.Update.setText("Stop")
            self.Info.Update(0, 0, 0) ;self.succes = 0 ; self.failed = 0
        else:
            self.ui.Update.setText("Update") ; self.ui.Update.setChecked(False)
            self.Info.ui.label.setText("Finished Update")
            return
        for row in range(self.ui.table.rowCount()):
            if self.Run:
                checkbox_item = self.ui.table.item(row, 0)
                if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                    i = [self.ui.table.item(row, col).text() for col in range(1, self.ui.table.columnCount())]
                    self.Info.ui.label.setText(f"Update {i[2]}:{i[3]}")
                    value = Chrom('headless').View(i[5],'check',"close")
                    if value == "" : pass
                    else :
                        cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (value[0], i[2])); self.ui.table.setItem(row, 2, QTableWidgetItem(str(value[0])))
                        cursor.execute('UPDATE account SET cookies = ? WHERE email = ?', (value[1], i[2])); self.ui.table.setItem(row, 6, QTableWidgetItem(str(value[1]))) ; conn.commit()
                        checkbox_item.setCheckState(Qt.Unchecked)
                        self.Info.Add(0,f"{i[2]}:{i[3]}",'Account Manager',"Update",'success')
                        self.succes += 1 ;self.Info.Update(s=self.succes,f=self.failed,o=self.order)
        self.ui.Update.setText("Update") ; self.ui.Update.setChecked(False)
        self.Info.ui.label.setText(f"Finished Update ")
        self.Run = False
    def Epsilon(self):
        self.Run = not self.Run
        if self.Run:
            self.ui.Epsilon.setText("Stop")
            self.Info.Update(0, 0, 0) ;self.succes = 0 ; self.failed = 0
            try:
                self.Info.ui.label.setText(f"Try to start the browser ")
                bot = yandex()
            except : 
                print(f"Failed to start the browser ")
                self.ui.Epsilon.setText("Epsilon") ; self.ui.Epsilon.setChecked(False)
                self.Info.ui.label.setText(f"Finished Epsilon ")
                self.Run = False
        else:
            self.ui.Epsilon.setText("Epsilon") ; self.ui.Epsilon.setChecked(False)
            self.Info.ui.label.setText("Finished Epsilon")
            return
        for row in range(self.ui.table.rowCount()):
            if self.Run:
                checkbox_item = self.ui.table.item(row, 0)
                if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                    i = [self.ui.table.item(row, col).text() for col in range(1, self.ui.table.columnCount())]
                    self.Info.ui.label.setText(f"Epsilon {i[2]}:{i[3]}")
                    value = Chrom().Epsilon(i[5],bot)
                    if value == "" : pass
                    else :
                        cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (value[0], i[2])); self.ui.table.setItem(row, 2, QTableWidgetItem(str(value[0])))
                        cursor.execute('UPDATE account SET cookies = ? WHERE email = ?', (value[1], i[2])); self.ui.table.setItem(row, 6, QTableWidgetItem(str(value[1]))) ; conn.commit()
                        checkbox_item.setCheckState(Qt.Unchecked)
        self.ui.Epsilon.setText("Epsilon") ; self.ui.Epsilon.setChecked(False)
        self.Info.ui.label.setText("Finished Epsilon")
        bot.quit()
        self.Run = False
        self.Refresh()
    def moakt(self):
        self.Run = not self.Run
        if self.Run:
            self.ui.Epsilon.setText("Stop")
            self.Info.Update(0, 0, 0) ;self.succes = 0 ; self.failed = 0
        else:
            self.ui.Epsilon.setText("Epsilon") ; self.ui.Epsilon.setChecked(False)
            self.Info.ui.label.setText("Finished Epsilon")
            return
        for row in range(self.ui.table.rowCount()):
            if self.Run:
                checkbox_item = self.ui.table.item(row, 0)
                if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                    i = [self.ui.table.item(row, col).text() for col in range(1, self.ui.table.columnCount())]
                    value = Chrom().Moakt(i[2],i[5])
                    if value == "" : pass
                    else :
                        cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (value[0], i[2])); self.ui.table.setItem(row, 2, QTableWidgetItem(str(value[0])))
                        cursor.execute('UPDATE account SET cookies = ? WHERE email = ?', (value[1], i[2])); self.ui.table.setItem(row, 6, QTableWidgetItem(str(value[1]))) ; conn.commit()
                        checkbox_item.setCheckState(Qt.Unchecked)
        self.ui.Epsilon.setText("Epsilon") ; self.ui.Epsilon.setChecked(False)
        self.Run = False
        self.Info.ui.label.setText(f"Finished Epsilon")
    def Change(self):
        self.Run = not self.Run
        if self.Run:
            self.ui.Change.setText("Stop")
            self.Info.Update(0, 0, 0) ;self.succes = 0 ; self.failed = 0
            try:
                self.Info.ui.label.setText(f"Try to start the browser ")
                bot = yandex()
            except : 
                self.Info.ui.label.setText(f"Failed to start the browser ")
                self.ui.Change.setText("Change Email") ; self.ui.Change.setChecked(False)
                self.Run = False
        else:
            self.ui.Change.setText("Change Email") ; self.ui.Change.setChecked(False)
            self.Info.ui.label.setText("Finished Change Email")
            return
        for row in range(self.ui.table.rowCount()):
            if self.Run:
                checkbox_item = self.ui.table.item(row, 0)
                if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                    i = [self.ui.table.item(row, col).text() for col in range(1, self.ui.table.columnCount())]
                    self.Info.ui.label.setText(f"Change {i[2]}:{i[3]}")
                    email = config['email']['email'].split("+")
                    chrs = 'abcdefghijklmnopqrstuvwxyz'
                    if config['email']['number']:
                        chrs = ''.join((chrs, '0123456789'))
                        k = ''.join(random.choices(chrs, k=random.randrange(6,7)))
                    else: k = ''.join(random.choices(chrs,k=random.randrange(6,7)))
                    value = Chrom().Change((email[0]+'+'+k+email[1]),i[5],bot)
                    if value == "" : pass
                    else :
                        cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (value[0], i[2])); self.ui.table.setItem(row, 2, QTableWidgetItem(str(value[0])))
                        cursor.execute('UPDATE Account SET email = ? WHERE email = ?', (value[1], i[2])); self.ui.table.setItem(row, 3, QTableWidgetItem(str(value[1])))
                        cursor.execute('UPDATE account SET cookies = ? WHERE email = ?', (value[2], i[2])); self.ui.table.setItem(row, 6, QTableWidgetItem(str(value[2]))) ; conn.commit()
                        checkbox_item.setCheckState(Qt.Unchecked)
        self.ui.Change.setText("Change Email") ; self.ui.Change.setChecked(False)
        self.Info.ui.label.setText("Finished Change Email")
        try:bot.quit()  
        except:pass
        self.Run = False
        self.Refresh()
    def Change_Password(self):
        self.Run = not self.Run
        if self.Run:
            self.ui.Change_Password.setText("Stop")
            try:
                self.Info.ui.label.setText(f"Try to start the browser ")
                bot = yandex()
            except : 
                self.Info.ui.label.setText(f"Failed to start the browser ")
                self.ui.Change.setText("Change Email") ; self.ui.Change.setChecked(False)
                self.Run = False
        else:
            self.ui.Change_Password.setText("Change Password") ; self.ui.Change_Password.setChecked(False)
            self.Info.ui.label.setText("Finished Checker")
            return
        for row in range(self.ui.table.rowCount()):
            if self.Run:
                checkbox_item = self.ui.table.item(row, 0)
                if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                    i = [self.ui.table.item(row, col).text() for col in range(1, self.ui.table.columnCount())]
                    self.Info.ui.label.setText(f"Checker {i[2]}:{i[3]}")
                    new = '01142060194'.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=2))
                    print(new,i[3])
                    value = Chrom().change_password(i[3],new,i[5],bot)
                    if value == "" : pass
                    else :
                        cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (value[0], i[2])); self.ui.table.setItem(row, 2, QTableWidgetItem(str(value[0])))
                        cursor.execute('UPDATE Account SET password = ? WHERE email = ?', (value[1], i[2])); self.ui.table.setItem(row, 4, QTableWidgetItem(str(value[1]))) 
                        cursor.execute('UPDATE account SET cookies = ? WHERE email = ?', (value[2], i[2])); self.ui.table.setItem(row, 6, QTableWidgetItem(str(value[2]))) ; conn.commit()
                        checkbox_item.setCheckState(Qt.Unchecked)
        self.ui.Change_Password.setText("Change Password") ; self.ui.Change_Password.setChecked(False)
        self.Info.ui.label.setText(f"Finished Change Password ")
        self.Run = False
    
    def Export(self):
        table_dialog = Export(self,self.ui.table )
        table_dialog.exec()
# n01142060194y