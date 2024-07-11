import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Custom Dark-Blue Theme")
        self.setGeometry(100, 100, 400, 300)

        # Create a checkbox
        self.checkbox = QCheckBox("Check Me", self)
        self.checkbox.setGeometry(150, 100, 100, 30)
        self.checkbox.setFont(QFont("Roboto", 14))

        # Create a line edit
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(100, 150, 200, 30)
        self.line_edit.setFont(QFont("Roboto", 14))
        self.line_edit.setPlaceholderText("Enter text...")

        # Create a button
        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(150, 200, 100, 40)
        self.button.setFont(QFont("Roboto", 14))
        self.button.clicked.connect(self.on_button_click)

        # Apply custom styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2e3b4e;
            }
            QCheckBox {
                color: #ffffff;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
            QCheckBox::indicator:unchecked {
                border: 2px solid #1e90ff;
                background-color: #2e3b4e;
            }
            QCheckBox::indicator:checked {
                border: 2px solid #1e90ff;
                background-color: #1e90ff;
                image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAAAXNSR0IArs4c6QAAAAlwSFlzAAAL3wAAC98BZoV4nQAAAAd0SU1FB+MGDA0NK6ijSHUAAAG6SURBVDjL7Zc9a1NRFIbn7vlrKb0WUtKWtNQS8TFVWVxMIrsYdPgzkIRz8V/wVrTbwK40YNbHhxoqI+gDQqCBBGEFElRaQiKO/1h7u4k3udmZ2ZyYe/PeX/nm+fcc05LAV8LTDdrjeNLViIf+a8qZ5hQewVcm1oTcAYYTh6gmArAGfG92uzHcG5diOMy2tvjXEpbiCeJYpq/QDohOXrZhdPofRei54mhuGECrRuxMZBtm0U2sDhN6Wyr4sagbmKw3WlcHkNCHmniQMA6Lt2JJ+DHQRlD/ClpdNQTRbF0LvQ4ev5FAUOAbVJ0sx6PY6mE8gJ2IZ/0EQaggbLzZFTLpjsG8yhc3AaQgNTyMl7Dc9jS5h8ThCWMDKtFMA5FZqJZws9NJoAd/AETbdIHRyDlTmYjG8gDRt9eU2yR+mZoFeEhlA7HRYlXEgPSNY1+E8HMcqgG0f5mWb5qVQa/L07heRsiwn6MTRjHcAp+I9uXrhmR5znVC2WTgKZ8YAS7E3xRSisZWxMJquHVYXfU6C/TiTs+shasMDmAOKpy5GYC7ZWDLGOnjbEnV+YSAymR7b8wCHiNZMyzZTMRWa5qxI9CKlu9cCN0K6z0uMAmB0n5pUtEGuxuH81g9geBBh9xNOrEG4rUAAAAASUVORK5CYII=)
            }
            QLineEdit {
                background-color: #3a4d63;
                color: #ffffff;
                border: 2px solid #1e90ff;
                border-radius: 5px;
                padding: 5px;
            }
            QLineEdit:focus {
                border: 2px solid #3ea6ff;
            }
            QPushButton {
                background-color: #1e90ff;
                color: #ffffff;
                border-radius: 10px;
                border: 2px solid #1e90ff;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #3ea6ff;
            }
            QPushButton:pressed {
                background-color: #1c86ee;
            }
        """)

    def on_button_click(self):
        if self.checkbox.isChecked():
            self.checkbox.setText("Checked!")
        else:
            self.checkbox.setText("Check Me")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
