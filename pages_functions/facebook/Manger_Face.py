from pages_functions.__init__ import *

from ui.Facebook.Manger_face_ui import Ui_Form
from pages_functions.Public.Add_Account import Add_Account_insta
from pages_functions.Public.Export import Export_insta

class Manger_Face(QWidget):
    def __init__(self):
        super(Manger_Face, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # tabel
        self.data = cursor.execute("SELECT * FROM account").fetchall()
        # self.ui.tableWidget.horizontalHeader().sectionClicked.connect(self.sortTable)
        self.loadTableData(self.data)

        # Connect signal and slot
        self.ui.pushButton.clicked.connect(self.filter_table)
        self.ui.comboBox.currentIndexChanged.connect(self.filter_table)
        self.ui.lineEdit.textChanged.connect(self.filter_table)
        self.ui.Add_Account.clicked.connect(self.Add_Account)
        self.ui.AddMultiAccount.clicked.connect(self.Add_Multi_Account)
        self.ui.Export.clicked.connect(self.Export)
        self.ui.table.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)

    def loadTableData(self, data):
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

        self.ui.table.verticalHeader().hide()
        self.ui.table.setColumnWidth(0, 100)
        self.ui.table.setColumnWidth(1, 100)
        self.ui.table.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
        headers = ["#"] + [description[0] for description in cursor.description]
        self.ui.table.setHorizontalHeaderLabels(headers)
        self.ui.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.table.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, position):
        context_menu = QMenu(self)
        
        show= QAction("Show in Browser", self)
        Edit= QAction("Edit", self)
        Update= QAction("Update", self)
        Delet= QAction("Delete", self)

        Edit.triggered.connect(self.select_all_rows)
        Update.triggered.connect(self.select_all_rows)
        show.triggered.connect(self.select_all_rows)
        Delet.triggered.connect(self.select_all_rows)

        show.setShortcut(Qt.CTRL + Qt.Key_S)
        Edit.setShortcut(Qt.CTRL + Qt.Key_E)
        Update.setShortcut(Qt.CTRL + Qt.Key_U)
        Delet.setShortcut(Qt.CTRL + Qt.Key_D)

        context_menu.addAction(Edit)
        context_menu.addAction(Update)
        context_menu.addAction(show)
        context_menu.addAction(Delet)

        context_menu.exec_(self.mapToGlobal(position))
    def select_all_rows(self):
        pass
    def filter_table(self):
        search_text = self.ui.lineEdit.text().lower()
        selected_column = self.ui.comboBox.currentIndex()

        if not search_text: self.filtered_data = self.data
        else: self.filtered_data = [item for item in self.data if item[selected_column] and search_text in item[selected_column].lower()]
        self.loadTableData(self.filtered_data)

    def Add_Account(self):
        table_dialog = Add_Account_insta(self)
        table_dialog.exec()

    def Add_Multi_Account(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '')
        with open(fname[0], 'r', encoding='utf-8') as file:
            line =  file.readlines()
            for name in line:
                try:
                    group,name,email,password,username,cookies,type,insta = name.split(':')
                    cursor.execute('INSERT INTO account (groupname ,name ,email, password, username cookies, type, insta) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (group, name, email, password,username, cookies, type, insta)); conn.commit()
                except: print('Failed Format')

    def Export(self):
        table_dialog = Export_insta(self,self.ui.table )
        table_dialog.exec()
