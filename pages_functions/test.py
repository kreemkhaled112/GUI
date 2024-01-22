import sys
from pages_functions.__init__ import *

from ui.pages_insta.Select_ui import Ui_Form
from pages_functions.__init__ import *

class MyForm(QWidget):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.save)

        # Connect checkbox to the selectAll function
        # self.checkBoxSelectAll.stateChanged.connect(self.selectAll)

        # Connect table cell clicks to the sortTable function
        # self.ui.tableWidget.cellClicked.connect(self.sortTable)

        # Connect the search button to the search function
        self.ui.pushButton.clicked.connect(self.search)
        header = self.ui.tableWidget.horizontalHeader()
        checkbox_in_header = QCheckBox(self)
        checkbox_in_header.stateChanged.connect(self.selectAllFromHeader)
        header.setSectionWidget(0, checkbox_in_header)

        self.loadTableData()
    def selectAllFromHeader(self, state):
        # Function to select/deselect all table elements from the header checkbox
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item is not None:
                item.setCheckState(Qt.Checked if state == Qt.Checked else Qt.Unchecked)
    def sortTable(self, row, col):
        # Function to sort the table based on the clicked column
        header = self.ui.tableWidget.horizontalHeaderItem(col)
        order = Qt.DescendingOrder if header.sortOrder() == Qt.AscendingOrder else Qt.AscendingOrder
        # set the sort role to Qt.UserRole
        self.ui.tableWidget.setSortRole(Qt.UserRole)
        self.ui.tableWidget.sortItems(col, order)
        header.setSortOrder(order)

    def selectAll(self):
        # Function to select/deselect all table elements
        state = self.checkBoxSelectAll.isChecked()
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item is not None:
                item.setCheckState(Qt.Checked if state else Qt.Unchecked)
    def search(self):
        # Function to search within the table elements
        search_text = self.ui.lineEdit.text()
        column_index = self.ui.comboBox.currentIndex()

        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, column_index)
            if item is not None and search_text.lower() in item.text().lower():
                self.ui.tableWidget.selectRow(row)

    def loadTableData(self):
        # Function to load data from the database into the table
        data = cursor.execute("SELECT * FROM edit").fetchall()

        self.ui.tableWidget.setRowCount(len(data))
        for row, row_data in enumerate(data):
            # Add a checkbox in the first column of each row
            select_checkbox_item = QTableWidgetItem()
            select_checkbox_item.setFlags(select_checkbox_item.flags() | 2)  # Add ItemIsUserCheckable flag
            select_checkbox_item.setCheckState(False)
            select_checkbox_item.setText(str(row + 1))
            self.ui.tableWidget.setItem(row, 0, select_checkbox_item)

            # Add data to the remaining columns
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, col + 1, item)  # Offset by 1 to skip the first column
        self.ui.tableWidget.verticalHeader().hide()
        # Set up column headers
        headers = ["#"] + [description[0] for description in cursor.description]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
    def save(self):
        # Function to save the modified data to the database
        for row in range(self.ui.tableWidget.rowCount()):
            # Assuming the first column is the checkbox column
            checkbox_item = self.ui.tableWidget.item(row, 0)
            if checkbox_item is not None and checkbox_item.checkState() == Qt.Checked:
                # The data to be saved is in the remaining columns
                data_to_save = [self.ui.tableWidget.item(row, col).text() for col in range(1, self.ui.tableWidget.columnCount())]
                print(data_to_save)
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())
