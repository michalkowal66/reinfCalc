from templates.ui import Ui_MainWindow
from resources.resources import resources
# TODO come up with better module and containers naming
from PyQt5 import QtCore, QtGui, QtWidgets


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.exp_combos = None
        # should this be initialized along with other containers in its own method?
        self.setupUi()
        self.loadData()

    def setupUi(self):
        self.ui.setupUi(self)
        self.exp_combos = {
            "p_exp_combo": self.ui.p_exp_combo,
            "b_exp_combo": self.ui.b_exp_combo,
            "c_exp_combo": self.ui.c_exp_combo,
            "f_exp_combo": self.ui.f_exp_combo,
        }
        # should this be defined in separate method?
        # is use of such container appropriate and 'pythonic'?
        self.ui.plate_btn.clicked.connect(self.newPlate)
        self.ui.beam_btn.clicked.connect(self.newBeam)
        self.ui.column_btn.clicked.connect(self.newColumn)
        self.ui.foot_btn.clicked.connect(self.newFoot)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionNew.triggered.connect(self.showWelcomePage)
        self.ui.actionSave.triggered.connect(self.saveFile)

    def loadData(self):  # data loading test
        # TODO complete loading functionality if accepted
        for exp_combo in self.exp_combos.values():
            exp_combo.addItems([exposition_class.value["exp_class"] for exposition_class in resources["exp_classes"]])

    def saveFile(self):  # saving test
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                            "QFileDialog.getSaveFileName()",
                                                            "",
                                                            "AllFiles(*);;TextFiles(*.txt)",
                                                            options = options)
        if fileName:
            with open(fileName, 'w') as f:
                # TODO replace with real saving method if accepted
                text = str(self.ui.p_concr_cover_lineEdit.text())
                f.write(text)

    def newPlate(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.elements_tabs.setCurrentIndex(0)

    def newBeam(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.elements_tabs.setCurrentIndex(1)

    def newColumn(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.elements_tabs.setCurrentIndex(2)

    def newFoot(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.elements_tabs.setCurrentIndex(3)

    def showWelcomePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
