from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        label = QLabel()
        pixmap = QPixmap('images.jpg')
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())

        pathBox = QLineEdit(self)
        pathBox.setPlaceholderText("Enter the Path Here")

        selectFileBtn = QPushButton("Select")
        convertButton = QPushButton("Convert")

        good_radiobutton = QRadioButton("Invoices")
        naive_radiobutton = QRadioButton("Credit Notes")

        layout.addWidget(pathBox, 0, 0)
        layout.addWidget(selectFileBtn, 0, 1)
        layout.addWidget(convertButton, 1, 0, 1, 2)
        layout.addWidget(good_radiobutton, 2, 0)
        layout.addWidget(naive_radiobutton, 2, 1)
        layout.addWidget(label, 3, 0, 1, 2)

        self.setLayout(layout)
