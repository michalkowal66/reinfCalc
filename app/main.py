from templates.ui import Ui_MainWindow
from resources.resources import resources
import json
# TODO come up with better module and containers naming
from PyQt5 import QtCore, QtGui, QtWidgets


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi()
        self.loadData()
        self.fileExtension = ".rcalc"

    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.plate_btn.clicked.connect(lambda: self.showElement(self.ui.plate_btn))
        self.ui.beam_btn.clicked.connect(lambda: self.showElement(self.ui.beam_btn))
        self.ui.column_btn.clicked.connect(lambda: self.showElement(self.ui.column_btn))
        self.ui.foot_btn.clicked.connect(lambda: self.showElement(self.ui.foot_btn))
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionNew.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_page))
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionOpen.triggered.connect(self.openFile)

    def loadData(self):  # improved test data loading method
        # TODO check if method can be improved
        names = {"steel": "steel_class", "concr": "concrete_class", "exp": "exp_class", "diam": "diameters"}
        combos = self.ui.elements_tabs.findChildren(QtWidgets.QComboBox)
        combosDict = {names[key]: [element for element in combos if key in element.objectName()] for key in names.keys()}
        for key in combosDict.keys():
            if key == "diameters":
                for element in combosDict[key]:
                    element.addItems(str(diam) for diam in resources[key])
            else:
                for element in combosDict[key]:
                    element.addItems(
                        [value_class.value[key] for value_class in resources[key]])

    def saveFile(self):  # improved test saving method
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                            "Save File",
                                                            "",
                                                            f"Reinforcement Calculator Files (*{self.fileExtension})",
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
        if not filePath.endswith(self.fileExtension):
            if "." not in filePath:
                return filePath + self.fileExtension
            return filePath.split(".")[0] + self.fileExtension
        return filePath

    def openFile(self):  # improved test file open method
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '',
                                                         f"Reinforcement Calculator Files (*{self.fileExtension})",
                                                         options=options)
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

    def showElement(self, buttonClicked):
        """
        Takes PyQt5 button object and changes window view to appropriate tab

        Strips core name of button representing related element, finds tab having corresponding
        element name and sets current widget of tab widget to that element and current widget
        of stacked widget to main page

        Parameters
        ----------
        buttonClicked : PyQt5.QtWidgets.QPushButton object, mandatory
            PyQt5 button object

        Returns
        -------
        None
        """
        element, _ = buttonClicked.objectName().split("_btn")
        element_tab = self.ui.elements_tabs.findChild(QtWidgets.QWidget, f"{element}_tab")
        self.ui.elements_tabs.setCurrentWidget(element_tab)
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_page)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
