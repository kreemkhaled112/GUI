from __init__ import *


app = QApplication([])
window1 = QWidget()
window2 = QWidget()
window2.setWindowFlags(window2.windowFlags() | Qt.WindowStaysOnTopHint)
window2.setParent(window1)
window1.show()
app.exec_()

