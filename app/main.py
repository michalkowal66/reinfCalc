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
        # Idea for elements container
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

    def saveFile(self):  # improved test saving method
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                            "Save File",
                                                            "",
                                                            "Reinforcement Calculator Files (*.rcalc)",
                                                            options=options)
        if fileName:
            with open(self.ensureFormat(fileName), 'w') as f:
                currentTab = self.ui.elements_tabs.currentWidget()
                saveData = {
                    "element": currentTab.objectName(),
                    # TODO check if data storing can be improved
                    "data": {
                        **{lineEdit.objectName(): lineEdit.text() for lineEdit in
                           currentTab.findChildren(QtWidgets.QLineEdit)},
                        **{comboBox.objectName(): comboBox.currentText() for comboBox in
                           currentTab.findChildren(QtWidgets.QComboBox)},
                        **{radioButton.objectName(): radioButton.isChecked() for radioButton in
                           currentTab.findChildren(QtWidgets.QRadioButton)}
                    },
                    "info": self.ui.info_textBrowser.toPlainText(),
                    "results": self.ui.results_textBrowser.toPlainText()
                }
                saveJson = json.dumps(saveData, indent=4)
                f.write(saveJson)

    def ensureFormat(self, filePath):  # ensures that proper file format was selected
        if not filePath.endswith(".rcalc"):
            if "." not in filePath:
                return filePath + ".rcalc"
            return filePath.split(".")[0] + ".rcalc"
        return filePath

    def openFile(self):  # improved test file open method
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '',
                                                         "Reinforcement Calculator Files (*.rcalc)", options=options)
        if fileName[0]:
            with open(fileName[0], 'r') as f:
                dataFromSave = json.load(f)
            element = self.ui.elements_tabs.findChild(QtWidgets.QWidget, dataFromSave["element"])
            if self.ui.stackedWidget.currentIndex() == 0:
                self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.elements_tabs.setCurrentWidget(element)
            # TODO improve for loop
            for key in dataFromSave["data"].keys():
                if key.endswith("lineEdit"):
                    element.findChild(QtWidgets.QLineEdit, key).setText(dataFromSave["data"][key])
                elif key.endswith("combo"):
                    element.findChild(QtWidgets.QComboBox, key).setCurrentText(dataFromSave["data"][key])
                elif key.endswith("radioBtn"):
                    element.findChild(QtWidgets.QRadioButton, key).setChecked(dataFromSave["data"][key])
            self.ui.info_textBrowser.setText(dataFromSave["info"])
            self.ui.results_textBrowser.setText(dataFromSave["results"])

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
