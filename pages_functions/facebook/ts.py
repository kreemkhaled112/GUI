from pages_functions.__init__ import *


class MyTableWidget(QTableWidget):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)

        # إعداد البيانات التجريبية
        for row in range(rows):
            for col in range(cols):
                item = QTableWidgetItem(f'Row {row}, Col {col}')
                self.setItem(row, col, item)

        # إضافة خانة اختيار لكل صف
        for row in range(rows):
            check_box = QCheckBox(self)
            self.setCellWidget(row, 0, check_box)

        # إنشاء خانة اختيار "Select All"
        select_all_checkbox = QCheckBox(self)
        select_all_checkbox.setText("Select All")

        # إضافة خانة اختيار "Select All" في العنوان الرأسي
        header_layout = QVBoxLayout()
        header_layout.addWidget(select_all_checkbox)
        header_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        header_widget = QWidget()
        header_widget.setLayout(header_layout)
        
        # تحديد العناوين
        header_labels = ["", "Column 1", "Column 2"]
        self.setVerticalHeaderLabels(header_labels)
        
        # إضافة خانة اختيار "Select All" في العنوان الرأسي
        self.setCellWidget(0, 0, header_widget)

        # تحديد وظيفة فعالة للتحقق من حالة خانة "Select All"
        select_all_checkbox.stateChanged.connect(self.toggle_select_all)

        # إضافة منيو للجدول
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def toggle_select_all(self, state):
        for row in range(1, self.rowCount()):
            item = self.cellWidget(row, 0)
            if item is not None:
                item.setCheckState(state)

    def show_context_menu(self, position):
        context_menu = QMenu(self)
        
        show= QAction("Show in Browser", self)
        Edit= QAction("Edit", self)
        Update= QAction("Update", self)
        Delet= QAction("Delet", self)

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
        for row in range(1, self.rowCount()):
            item = self.cellWidget(row, 0)
            if item is not None:
                item.setCheckState(Qt.Checked)

if __name__ == '__main__':
    app = QApplication([])
    table = MyTableWidget(5, 3)
    table.show()
    app.exec_()
