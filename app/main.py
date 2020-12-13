from templates.ui import Ui_MainWindow
from resources.resources import resources
import json
# TODO come up with better module and containers naming
from PyQt5 import QtCore, QtGui, QtWidgets


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.exp_combos = dict()
        self.concr_combos = dict()
        self.steel_combos = dict()
        self.bars_combos = dict()
        # should this be initialized along with other containers in its own method?
        self.setupUi()
        self.loadData()

    def setupUi(self):
        self.ui.setupUi(self)
        # should this be defined in separate method?
        # is use of such container appropriate and 'pythonic'?
        self.exp_combos = {
            "p_exp_combo": self.ui.p_exp_combo,
            "b_exp_combo": self.ui.b_exp_combo,
            "c_exp_combo": self.ui.c_exp_combo,
            "f_exp_combo": self.ui.f_exp_combo,
        }
        self.concr_combos = {
            "p_concr_class_combo": self.ui.p_concr_class_combo,
            "b_concr_class_combo": self.ui.b_concr_class_combo,
            "c_concr_class_combo": self.ui.c_concr_class_combo,
            "f_concr_class_combo": self.ui.f_concr_class_combo
        }
        self.steel_combos = {
            "p_steel_class_combo": self.ui.p_steel_class_combo,
            "b_steel_class_combo": self.ui.b_steel_class_combo,
            "c_steel_class_combo": self.ui.c_steel_class_combo,
            "f_steel_class_combo": self.ui.f_steel_class_combo
        }
        self.bars_combos = {
            "p_bar_diam_combo": self.ui.p_bar_diam_combo,
            "b_bar_diam_combo": self.ui.b_bar_diam_combo,
            "c_bar_diam_combo": self.ui.c_bar_diam_combo,
            "f_bar_diam_combo": self.ui.f_bar_diam_combo,
            "f_col_bar_diam_combo": self.ui.f_col_bar_diam_combo
        }
        # Another idea for elements container
        self.elements = {
            "plate": {
                "exp_class": self.ui.p_exp_combo,
                "concrete_class": self.ui.p_concr_class_combo,
                "concrete_cover": self.ui.p_concr_cover_lineEdit,
                "steel_class": self.ui.p_steel_class_combo,
                "bar_diam": self.ui.p_bar_diam_combo,
                "thickness": self.ui.p_th_lineEdit,
                "moment": self.ui.p_moment_lineEdit
            },
            "beam": {
                "exp_class": self.ui.b_exp_combo,
                "concrete_class": self.ui.b_concr_class_combo,
                "concrete_cover": self.ui.b_concr_cover_lineEdit,
                "steel_class": self.ui.b_steel_class_combo,
                "bar_diam": self.ui.b_bar_diam_combo,
                "height": self.ui.b_height_lineEdit,
                "width": self.ui.b_width_lineEdit,
                "moment": self.ui.b_moment_lineEdit
            },
            "column": {
                "exp_class": self.ui.c_exp_combo,
                "concrete_class": self.ui.c_concr_class_combo,
                "concrete_cover": self.ui.c_concr_cover_lineEdit,
                "steel_class": self.ui.c_steel_class_combo,
                "bar_diam": self.ui.c_bar_diam_combo,
                "height": self.ui.c_height_lineEdit,
                "width": self.ui.c_width_lineEdit,
                "moment": self.ui.c_moment_lineEdit
            },
            "foot": {
                "exp_class": self.ui.f_exp_combo,
                "concrete_class": self.ui.f_concr_class_combo,
                "concrete_cover": self.ui.f_concr_cover_lineEdit,
                "steel_class": self.ui.f_steel_class_combo,
                "bar_diam": self.ui.f_bar_diam_combo,
                "col_bar_diam": self.ui.f_col_bar_diam_combo,
                "height": self.ui.f_fheight_lineEdit,
                "width": self.ui.f_fwidth_lineEdit,
                "vertical": self.ui.f_vert_lineEdit
            }
        }
        self.ui.plate_btn.clicked.connect(self.newPlate)
        self.ui.beam_btn.clicked.connect(self.newBeam)
        self.ui.column_btn.clicked.connect(self.newColumn)
        self.ui.foot_btn.clicked.connect(self.newFoot)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionNew.triggered.connect(self.showWelcomePage)
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionOpen.triggered.connect(self.openFile)

    def loadData(self):  # data loading test
        # TODO complete loading functionality if accepted
        # for exp_combo in self.exp_combos.values():
        #     exp_combo.addItems([exposition_class.value["exp_class"] for exposition_class in resources["exp_classes"]])
        # for concr_combo in self.concr_combos.values():
        #     concr_combo.addItems([concrete_class.value["concrete_class"] for concrete_class in resources["concrete_classes"]])
        # for steel_combo in self.steel_combos.values():
        #     steel_combo.addItems([steel_class.value["class_name"] for steel_class in resources["steel_classes"]])
        # for bars_combo in self.bars_combos.values():
        #     bars_combo.addItems([str(n) for n in range(6, 42, 2)])

        # Another idea of data loading
        for element in self.elements.values():
            element["exp_class"].addItems(
                [exposition_class.value["exp_class"] for exposition_class in resources["exp_classes"]])
            element["concrete_class"].addItems(
                [concrete_class.value["concrete_class"] for concrete_class in resources["concrete_classes"]])
            element["steel_class"].addItems(
                [steel_class.value["class_name"] for steel_class in resources["steel_classes"]])
            element["bar_diam"].addItems([str(n) for n in range(6, 42, 2)])
            if element.get("col_bar_diam") is not None:
                element.get("col_bar_diam").addItems([str(n) for n in range(6, 42, 2)])

    def saveFile(self):  # saving test
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                            "QFileDialog.getSaveFileName()",
                                                            "",
                                                            "AllFiles(*);;TextFiles(*.txt)",
                                                            options=options)
        if fileName:
            with open(fileName, 'w') as f:
                # TODO replace with real saving method if accepted
                save_raw = {
                    "element": {
                        "plate": {
                            "exp_class": self.ui.p_exp_combo.currentText(),
                            "concrete_class": self.ui.p_concr_class_combo.currentText(),
                            "concrete_cover": self.ui.p_concr_cover_lineEdit.text(),
                            "steel_class": self.ui.p_steel_class_combo.currentText(),
                            "bar_diam": self.ui.p_bar_diam_combo.currentText(),
                            "thickness": self.ui.p_th_lineEdit.text(),
                            "moment": self.ui.p_moment_lineEdit.text()
                        }
                    },
                    "remarks": "Remarks about calculations",
                    "results": "Results of calculations"
                }
                save = json.dumps(save_raw)
                f.write(save)

    def openFile(self):  # file open test
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home', options=options)
        # TODO replace with real open method if accepted
        if fileName[0]:
            with open(fileName[0], 'r') as f:
                data = json.load(f)
            print(data)
            self.ui.p_exp_combo.setCurrentText(data["element"]["plate"]["exp_class"])
            self.ui.p_concr_class_combo.setCurrentText(data["element"]["plate"]["concrete_class"])
            self.ui.p_steel_class_combo.setCurrentText(data["element"]["plate"]["steel_class"])
            self.ui.p_bar_diam_combo.setCurrentText(str(data["element"]["plate"]["bar_diam"]))
            self.ui.p_concr_cover_lineEdit.setText(str(data["element"]["plate"]["concrete_cover"]))
            self.ui.p_th_lineEdit.setText(str(data["element"]["plate"]["thickness"]))
            self.ui.p_moment_lineEdit.setText(str(data["element"]["plate"]["moment"]))
            self.ui.info_textBrowser.setText(data["remarks"])
            self.ui.results_textBrowser.setText(data["results"])

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
