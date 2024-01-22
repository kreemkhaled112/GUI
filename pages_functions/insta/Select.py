from pages_functions.__init__ import *

from ui.Select_ui import Ui_Form
from pages_functions.__init__ import *


class Select_insta(QDialog):
    def __init__(self, parent=None, data=None):
        super(Select_insta, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        with open("static\style.qss", "r",encoding='utf-8') as style_file:
            style_str = style_file.read()
        self.setStyleSheet(style_str)
        
        self.ui.pushButton.clicked.connect(self.filter_table)
        self.ui.comboBox.currentIndexChanged.connect(self.filter_table)
        self.ui.lineEdit.textChanged.connect(self.filter_table)

        self.ui.Save.clicked.connect(lambda : Thread(target=self.save).start())
        self.loadTableData(data)
    
    def loadTableData(self,data):
        
        self.ui.tableWidget.setRowCount(len(data))
        for row, row_data in enumerate(data):
            select_checkbox_item = QTableWidgetItem()
            select_checkbox_item.setFlags(select_checkbox_item.flags() | 2) 
            select_checkbox_item.setCheckState(False)
            select_checkbox_item.setText(str(row + 1))
            self.ui.tableWidget.setItem(row, 0, select_checkbox_item)

            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, col + 1, item)  
        self.ui.tableWidget.verticalHeader().hide()
        self.ui.tableWidget.setColumnWidth(0, 50)
        headers = ["#"] + [description[0] for description in cursor.description]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

    def filter_table(self):
        search_text = self.ui.lineEdit.text().lower()
        selected_column = self.ui.comboBox.currentIndex()

        if not search_text: 
            self.filtered_data = self.data
        else:
            self.filtered_data = [item for item in self.data if item[selected_column] and search_text in item[selected_column].lower()]
        self.loadTableData(self.filtered_data)
        
    def save(self):
        data_to_save = []
        for row in range(self.ui.tableWidget.rowCount()):
            checkbox_item = self.ui.tableWidget.item(row, 0)
            if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                data = [self.ui.tableWidget.item(row, col).text() for col in range(1, self.ui.tableWidget.columnCount())]
                data_to_save.append(data)
        input(data_to_save)
        self.parent().Update_info(data_to_save)
        self.accept()