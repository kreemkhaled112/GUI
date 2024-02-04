import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sqlite3

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.table_widget = QTableWidget(self)
        self.layout.addWidget(self.table_widget)

        self.init_db()
        self.populate_table()

        self.table_widget.itemChanged.connect(self.handle_item_change)

    def init_db(self):
        self.connection = sqlite3.connect('example.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS my_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                value INTEGER
            )
        ''')
        self.connection.commit()

    def populate_table(self):
        self.cursor.execute('SELECT * FROM my_table')
        rows = self.cursor.fetchall()

        self.table_widget.setRowCount(len(rows))
        self.table_widget.setColumnCount(3)

        for row_index, row_data in enumerate(rows):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.table_widget.setItem(row_index, col_index, item)

    def handle_item_change(self, item):
        row = item.row()
        col = item.column()

        # قم بالتحقق من العمود قبل تحديث البيانات
        if col in [1, 2]:  # افتراضيًا، 1 يشير إلى عمود الاسم و 2 يشير إلى عمود القيمة
            new_value = item.text()

            # تحديث الاسم أو القيمة في قاعدة البيانات
            if col == 1:
                self.cursor.execute('UPDATE my_table SET name = ? WHERE id = ?', (new_value, row + 1))
            elif col == 2:
                self.cursor.execute('UPDATE my_table SET value = ? WHERE id = ?', (new_value, row + 1))

            self.connection.commit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
