from PyQt6.QtWidgets import QApplication, QWidget, QUiLoader
from PyQt6.uic import loadUiType

# تحميل ملف UI
Ui_Form, QMainWindow = loadUiType('your_ui_file.ui')

class YourWidget(QWidget, Ui_Form):
    def __init__(self):
        super(YourWidget, self).__init__()
        self.setupUi(self)

# تستخدم الكود الآتي لاستخدام الويدجت الخاصة بك
if __name__ == '__main__':
    app = QApplication([])
    widget = YourWidget()
    widget.show()
    app.exec()
