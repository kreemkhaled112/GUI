from pages_functions.__init__ import *

from ui.Public.Select_ui import Ui_Form

class Select_insta(QDialog):
    update_info_signal = pyqtSignal(list)

    def __init__(self, parent=None, data=None):
        super(Select_insta, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.data = data
        self.filtered_data = []  # Initialize filtered_data

        self.ui.pushButton.clicked.connect(self.filter_table)
        self.ui.comboBox.currentIndexChanged.connect(self.filter_table)
        self.ui.lineEdit.textChanged.connect(self.filter_table)

        self.ui.Save.clicked.connect(self.save)

        self.loadTableData(data)

    def loadTableData(self, data):
        self.ui.tableWidget.setRowCount(len(data))
        for row, row_data in enumerate(data):
            select_checkbox_item = QTableWidgetItem()
            select_checkbox_item.setFlags(select_checkbox_item.flags() | Qt.ItemIsUserCheckable)
            select_checkbox_item.setCheckState(Qt.Unchecked)
            select_checkbox_item.setText(str(row + 1))
            self.ui.tableWidget.setItem(row, 0, select_checkbox_item)

            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, col + 1, item)
        self.ui.tableWidget.verticalHeader().hide()
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(6, QHeaderView.Stretch)
        self.ui.tableWidget.setColumnWidth(0, 50)
        headers = ["#"] + [description[0] for description in cursor.description]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

    def filter_table(self):
        search_text = self.ui.lineEdit.text().lower()
        selected_column = self.ui.comboBox.currentIndex()

        if not search_text:
            self.filtered_data = self.data
        else:
            # Use filter method for a concise list comprehension
            self.filtered_data = list(filter(lambda item: item[selected_column].lower().find(search_text) != -1, self.data))

        self.loadTableData(self.filtered_data)

    def save(self):
        data_to_save = []
        for row in range(self.ui.tableWidget.rowCount()):
            checkbox_item = self.ui.tableWidget.item(row, 0)
            if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                data = [self.ui.tableWidget.item(row, col).text() for col in range(1, self.ui.tableWidget.columnCount())]
                data_to_save.append(data)

        # Emit the signal to update info in the main thread
        self.parent().Update_info(data_to_save)
        self.accept()
