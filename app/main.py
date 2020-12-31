from templates.ui import Ui_MainWindow
from materialProperties.properties import properties
import json
# TODO come up with better module and containers naming
from PyQt5 import QtCore, QtGui, QtWidgets


class Main(QtWidgets.QMainWindow):
    """
    Main script class handling gui actions

    ...

    Attributes
    ----------
    fileExtension : str
        File extension used by application
    """
    fileExtension = ".rcalc"

    def __init__(self):
        """
        Call parent init method and UI construct methods

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi()
        self.loadImgs()
        self.loadData()
        self.loadDummies()

    def setupUi(self):
        """
        Construct window's ui elements and create buttons and menu actions connections.

        Call setupUi method from imported, generated by puic GUI file constructing window's
        ui elements, then create connections between button and menu action elements and methods

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.ui.setupUi(self)
        self.ui.plate_btn.clicked.connect(lambda: self.showElement(self.ui.plate_btn))
        self.ui.beam_btn.clicked.connect(lambda: self.showElement(self.ui.beam_btn))
        self.ui.col_btn.clicked.connect(lambda: self.showElement(self.ui.col_btn))
        self.ui.foot_btn.clicked.connect(lambda: self.showElement(self.ui.foot_btn))

        self.ui.recently_opened_list.itemDoubleClicked.connect(
            lambda item: self.openFile(filePath=item.data(QtCore.Qt.UserRole)))

        # TODO can these radio buttons be grouped to make one signal instead?
        self.ui.p_span_section_radioBtn.toggled.connect(
            lambda: self.ui.results_stackedWidget.findChild(QtWidgets.QLabel, "p_span_elementDraw").raise_())
        self.ui.p_sup_section_radioBtn.toggled.connect(
            lambda: self.ui.results_stackedWidget.findChild(QtWidgets.QLabel, "p_sup_elementDraw").raise_())
        self.ui.b_span_section_radioBtn.toggled.connect(
            lambda: self.ui.results_stackedWidget.findChild(QtWidgets.QLabel, "b_span_elementDraw").raise_())
        self.ui.b_sup_section_radioBtn.toggled.connect(
            lambda: self.ui.results_stackedWidget.findChild(QtWidgets.QLabel, "b_sup_elementDraw").raise_())

        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionOpen.triggered.connect(self.openFile)

    def loadData(self):  # improved test data loading method
        """
        Load imported data from materialProperties module to appropriate containers in application

        Find children of tabWidget using locally defined dictionary of element core names
        and append to them imported data.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        names = {"steel": "steel_grade", "concr": "concrete_class", "exp": "exp_class", "diam": "diameters"}
        combos = self.ui.elements_tabs.findChildren(QtWidgets.QComboBox)
        combosDict = {names[key]: [element for element in combos if key in element.objectName()] for key in names.keys()}
        for key in combosDict.keys():
            if key == "diameters":
                for element in combosDict[key]:
                    element.addItems(str(diam) for diam in properties[key])
            else:
                for element in combosDict[key]:
                    element.addItems(
                        [value_class.value[key] for value_class in properties[key]])

    def loadImgs(self):
        for button in self.ui.welcome_page.findChildren(QtWidgets.QPushButton):
            button.setIcon(QtGui.QIcon(f"resources/buttons/{button.objectName()}.jpg"))
            button.setIconSize(QtCore.QSize(200, 200))
        for drawingPlaceholder in self.ui.results_stackedWidget.findChildren(QtWidgets.QLabel):
            drawingPlaceholder.setPixmap(QtGui.QPixmap(
                f"resources/placeholders/{drawingPlaceholder.objectName().split('_elementDraw')[0]}.jpg"))

    def saveFile(self):  # improved test saving method
        """
        Save values from currently displayed tab to appointed location.

        Open file dialog that takes path to a save file, call ensureFormat
        on the path and save values from currently active tab to that location.
        File is saved in '.rcalc' format containing JSON object with attributes
        containing extracted values.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,
                                                            "Save File",
                                                            "",
                                                            f"Reinforcement Calculator Files (*{Main.fileExtension})",
                                                            options=options)
        if fileName:
            with open(self.ensureFormat(fileName), 'w') as f:
                currentTab = self.ui.elements_tabs.currentWidget()
                saveData = {
                    "element": currentTab.objectName(),
                    "data": {
                        **{lineEdit.objectName(): lineEdit.text() for lineEdit in
                           currentTab.findChildren(QtWidgets.QLineEdit)},
                        **{comboBox.objectName(): comboBox.currentText() for comboBox in
                           currentTab.findChildren(QtWidgets.QComboBox)},
                        **{radioButton.objectName(): radioButton.isChecked() for radioButton in
                           currentTab.findChildren(QtWidgets.QRadioButton)}
                    },
                    "info": {
                        **{textBrowser.objectName(): textBrowser.toPlainText()
                           for textBrowser in
                           self.ui.results_stackedWidget.currentWidget().findChildren(QtWidgets.QTextBrowser)}
                    }
                }
                saveJson = json.dumps(saveData, indent=4)
                f.write(saveJson)

    def ensureFormat(self, filePath):  # ensures that proper file format was selected
        """
        Return path with proper file format

        Parameters
        ----------
        filePath : str, mandatory
            Path to a save file

        Returns
        -------
        str
            Modified path to file with proper save file format '.rcalc'
        """
        if not filePath.endswith(Main.fileExtension):
            if "." not in filePath:
                return filePath + Main.fileExtension
            return filePath.split(".")[0] + Main.fileExtension
        return filePath

    def openFile(self, filePath=None):  # improved test file open method
        """
        Open appropriate tab and loads values containers from appointed file.

        Open file dialog and parses appointed '.rcalc' file to Python dictionary.
        Open appropriate element tab and set containers content using dictionary
        values.

        Parameters
        ----------
        filePath : str, optional
            Path to a save file

        Returns
        -------
        None
        """
        if not filePath:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '',
                                                                f"Reinforcement Calculator Files (*{Main.fileExtension})",
                                                                options=options)
        if filePath:
            with open(filePath, 'r') as f:
                dataFromSave = json.load(f)
            element = self.ui.elements_tabs.findChild(QtWidgets.QWidget, dataFromSave["element"])
            if self.ui.stackedWidget.currentIndex() == 0:
                self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.elements_tabs.setCurrentWidget(element)
            for dataKey in dataFromSave["data"].keys():
                if dataKey.endswith("lineEdit"):
                    element.findChild(QtWidgets.QLineEdit, dataKey).setText(dataFromSave["data"][dataKey])
                elif dataKey.endswith("combo"):
                    element.findChild(QtWidgets.QComboBox, dataKey).setCurrentText(dataFromSave["data"][dataKey])
                elif dataKey.endswith("radioBtn"):
                    element.findChild(QtWidgets.QRadioButton, dataKey).setChecked(dataFromSave["data"][dataKey])
            for infoKey in dataFromSave["info"].keys():
                self.ui.results_stackedWidget.findChild(QtWidgets.QTextBrowser, infoKey).setPlainText(
                    dataFromSave["info"][infoKey])

    def showElement(self, buttonClicked):
        """
        Take PyQt5 button object and change window view to appropriate tab

        Strip core name of button representing related element, find tab having corresponding
        element name and set current widget of tab widget to that element and current widget
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

    def loadDummies(self):  # testing dummy data
        self.ui.recently_opened_list.item(0).setData(QtCore.Qt.UserRole, "../dummy_data/beam_span_example.rcalc")
        self.ui.recently_opened_list.item(1).setData(QtCore.Qt.UserRole, "../dummy_data/beam_support_example.rcalc")
        self.ui.recently_opened_list.item(2).setData(QtCore.Qt.UserRole, "../dummy_data/column_example.rcalc")
        self.ui.recently_opened_list.item(3).setData(QtCore.Qt.UserRole, "../dummy_data/foot_example.rcalc")
        self.ui.recently_opened_list.item(4).setData(QtCore.Qt.UserRole, "../dummy_data/plate_example.rcalc")
        self.ui.menuFile.actions()[3].triggered.connect(
            lambda: self.openFile(filePath="../dummy_data/beam_span_example.rcalc"))
        self.ui.menuFile.actions()[4].triggered.connect(
            lambda: self.openFile(filePath="../dummy_data/beam_support_example.rcalc"))
        self.ui.menuFile.actions()[5].triggered.connect(
            lambda: self.openFile(filePath="../dummy_data/column_example.rcalc"))
        self.ui.menuFile.actions()[6].triggered.connect(
            lambda: self.openFile(filePath="../dummy_data/foot_example.rcalc"))
        self.ui.menuFile.actions()[7].triggered.connect(
            lambda: self.openFile(filePath="../dummy_data/plate_example.rcalc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
