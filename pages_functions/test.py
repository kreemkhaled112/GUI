import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QCheckBox


class TableExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # إعداد النافذة والمكونات
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('PyQt Table Example')

        self.layout = QVBoxLayout()

        # إعداد الجدول
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['العنصر', 'تحديد'])

        # إضافة بيانات عينة
        data = [('عنصر 1', False), ('عنصر 2', False), ('عنصر 3', False), ('عنصر 4', False), ('عنصر 5', False)]
        for row, (item, checked) in enumerate(data):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(item))

            checkbox = QCheckBox()
            checkbox.setChecked(checked)
            self.tableWidget.setCellWidget(row, 1, checkbox)

        # إعداد زر التحديد/الغاء
        toggleButton = QPushButton('تحديد', self)
        toggleButton.clicked.connect(self.toggleSelection)

        # إعداد التخطيط
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(toggleButton)

        # تعيين التخطيط للنافذة
        self.setLayout(self.layout)

    def toggleSelection(self):
        current_text = self.sender().text()

        if current_text == 'تحديد':
            for row in range(self.tableWidget.rowCount()):
                checkbox = self.tableWidget.cellWidget(row, 1)
                checkbox.setSelected(True)
            self.sender().setText('إلغاء تحديد')
        else:
            for row in range(self.tableWidget.rowCount()):
                checkbox = self.tableWidget.cellWidget(row, 1)
                checkbox.setChecked(False)
            self.sender().setText('تحديد')


def main():
    app = QApplication(sys.argv)
    ex = TableExample()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
