import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLineEdit, QPushButton

class MyTable(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # إضافة مربع نصي لإدخال القيمة
        self.input_line_edit = QLineEdit(self)
        self.layout.addWidget(self.input_line_edit)

        # إضافة زر لإضافة القيمة إلى الجدول
        self.add_button = QPushButton('إضافة', self)
        self.add_button.clicked.connect(self.add_value_to_table)
        self.layout.addWidget(self.add_button)

        # إضافة الجدول
        self.table = QTableWidget(self)
        self.table.setRowCount(1)
        self.table.setColumnCount(5)

        for col in range(5):
            item = QTableWidgetItem("عمود {}".format(col + 1))
            self.table.setItem(0, col, item)

        self.table.horizontalHeader().setStretchLastSection(True)
        self.layout.addWidget(self.table)

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('جدول PyQt5')

    def add_value_to_table(self):
        # الحصول على القيمة من مربع النص
        value = self.input_line_edit.text()

        # إضافة القيمة إلى الجدول في العمود الأول (index 0) للصف الوحيد
        item = QTableWidgetItem(value)
        self.table.setItem(0, 0, item)

        # مسح محتوى مربع النص بعد إضافة القيمة
        self.input_line_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyTable()
    window.show()
    sys.exit(app.exec_())
