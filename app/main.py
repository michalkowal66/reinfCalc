from templates.ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class Main(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        ui = Ui_MainWindow()
        ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
