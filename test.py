from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget

class MyTableWidget(QTableWidget):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)

        # Set up sample data
        for row in range(rows):
            for col in range(cols):
                item = QTableWidgetItem(f'Row {row}, Col {col}')
                self.setItem(row, col, item)

        # Connect the itemChanged signal to a custom slot
        self.itemChanged.connect(self.handle_item_change)

        # Add a button for handling item changes
        handle_change_button = QPushButton("Handle Item Change", self)
        handle_change_button.clicked.connect(self.handle_item_change_button_clicked)

        # Add a button for selecting all rows
        select_all_button = QPushButton("Select All", self)
        select_all_button.clicked.connect(self.select_all_rows)

        # Set up the layout
        layout = QVBoxLayout(self)
        layout.addWidget(handle_change_button)
        layout.addWidget(select_all_button)
        layout.addWidget(self)

        # List to store changed items
        self.changed_items = []

    def select_all_rows(self):
        for row in range(self.rowCount()):
            item = self.item(row, 0)
            if item is not None:
                item.setSelected(True)

    def handle_item_change(self, item):
        if item.column() == 0:
            # Handle changes for items in the first column
            print(f"Item {item.text()} in column {item.column()} changed. New state: {item.checkState()}")
            # Store changed item in the list
            self.changed_items.append((item.text(), item.checkState()))

    def handle_item_change_button_clicked(self):
        # Print the changed items
        print("Changed items:")
        for changed_item in self.changed_items:
            print(f"Item: {changed_item[0]}, State: {changed_item[1]}")
        # Clear the list after printing
        self.changed_items.clear()

if __name__ == '__main__':
    app = QApplication([])
    table = MyTableWidget(5, 3)
    table.show()
    app.exec_()
