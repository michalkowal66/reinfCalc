# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/main_temp.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 480)
        MainWindow.setMinimumSize(QtCore.QSize(750, 480))
        MainWindow.setMaximumSize(QtCore.QSize(750, 480))
        MainWindow.setStyleSheet("font: 12px \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(750, 450))
        self.centralwidget.setMaximumSize(QtCore.QSize(750, 450))
        self.centralwidget.setObjectName("centralwidget")
        self.Tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.Tab_widget.setGeometry(QtCore.QRect(0, 0, 480, 460))
        self.Tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.Tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Tab_widget.setElideMode(QtCore.Qt.ElideNone)
        self.Tab_widget.setTabBarAutoHide(False)
        self.Tab_widget.setObjectName("Tab_widget")
        self.plate_tab = QtWidgets.QWidget()
        self.plate_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plate_tab.setObjectName("plate_tab")
        self.p_concrete_label = QtWidgets.QLabel(self.plate_tab)
        self.p_concrete_label.setGeometry(QtCore.QRect(10, 60, 111, 21))
        self.p_concrete_label.setObjectName("p_concrete_label")
        self.p_concr_class_label = QtWidgets.QLabel(self.plate_tab)
        self.p_concr_class_label.setGeometry(QtCore.QRect(30, 90, 101, 21))
        self.p_concr_class_label.setObjectName("p_concr_class_label")
        self.p_concr_class_combo = QtWidgets.QComboBox(self.plate_tab)
        self.p_concr_class_combo.setGeometry(QtCore.QRect(140, 90, 91, 22))
        self.p_concr_class_combo.setObjectName("p_concr_class_combo")
        self.p_concr_class_combo.addItem("")
        self.p_concr_class_combo.addItem("")
        self.p_concr_cover_label = QtWidgets.QLabel(self.plate_tab)
        self.p_concr_cover_label.setGeometry(QtCore.QRect(250, 90, 131, 21))
        self.p_concr_cover_label.setObjectName("p_concr_cover_label")
        self.p_concr_cover_lineEdit = QtWidgets.QLineEdit(self.plate_tab)
        self.p_concr_cover_lineEdit.setGeometry(QtCore.QRect(380, 90, 50, 20))
        self.p_concr_cover_lineEdit.setInputMask("")
        self.p_concr_cover_lineEdit.setObjectName("p_concr_cover_lineEdit")
        self.p_steel_labe = QtWidgets.QLabel(self.plate_tab)
        self.p_steel_labe.setGeometry(QtCore.QRect(10, 120, 111, 21))
        self.p_steel_labe.setObjectName("p_steel_labe")
        self.p_steel_class_label = QtWidgets.QLabel(self.plate_tab)
        self.p_steel_class_label.setGeometry(QtCore.QRect(30, 150, 91, 21))
        self.p_steel_class_label.setObjectName("p_steel_class_label")
        self.p_steel_class_combo = QtWidgets.QComboBox(self.plate_tab)
        self.p_steel_class_combo.setGeometry(QtCore.QRect(140, 150, 91, 22))
        self.p_steel_class_combo.setObjectName("p_steel_class_combo")
        self.p_steel_class_combo.addItem("")
        self.p_steel_class_combo.addItem("")
        self.p_bar_label = QtWidgets.QLabel(self.plate_tab)
        self.p_bar_label.setGeometry(QtCore.QRect(250, 150, 121, 21))
        self.p_bar_label.setObjectName("p_bar_label")
        self.p_bar_diam_combo = QtWidgets.QComboBox(self.plate_tab)
        self.p_bar_diam_combo.setGeometry(QtCore.QRect(380, 150, 41, 22))
        self.p_bar_diam_combo.setObjectName("p_bar_diam_combo")
        self.p_bar_diam_combo.addItem("")
        self.p_bar_diam_combo.addItem("")
        self.p_bar_diam_combo.addItem("")
        self.p_geom_label = QtWidgets.QLabel(self.plate_tab)
        self.p_geom_label.setGeometry(QtCore.QRect(10, 180, 111, 21))
        self.p_geom_label.setObjectName("p_geom_label")
        self.p_th_label = QtWidgets.QLabel(self.plate_tab)
        self.p_th_label.setGeometry(QtCore.QRect(30, 210, 91, 21))
        self.p_th_label.setObjectName("p_th_label")
        self.p_th_lineEdit = QtWidgets.QLineEdit(self.plate_tab)
        self.p_th_lineEdit.setGeometry(QtCore.QRect(140, 210, 50, 20))
        self.p_th_lineEdit.setInputMask("")
        self.p_th_lineEdit.setObjectName("p_th_lineEdit")
        self.p_env_label = QtWidgets.QLabel(self.plate_tab)
        self.p_env_label.setGeometry(QtCore.QRect(10, 0, 111, 21))
        self.p_env_label.setObjectName("p_env_label")
        self.p_exp_label = QtWidgets.QLabel(self.plate_tab)
        self.p_exp_label.setGeometry(QtCore.QRect(30, 30, 91, 21))
        self.p_exp_label.setObjectName("p_exp_label")
        self.p_exp_combo = QtWidgets.QComboBox(self.plate_tab)
        self.p_exp_combo.setGeometry(QtCore.QRect(140, 30, 91, 22))
        self.p_exp_combo.setObjectName("p_exp_combo")
        self.p_exp_combo.addItem("")
        self.p_exp_combo.addItem("")
        self.p_load_label = QtWidgets.QLabel(self.plate_tab)
        self.p_load_label.setGeometry(QtCore.QRect(10, 240, 111, 21))
        self.p_load_label.setObjectName("p_load_label")
        self.p_moment_lineEdit = QtWidgets.QLineEdit(self.plate_tab)
        self.p_moment_lineEdit.setGeometry(QtCore.QRect(190, 270, 50, 20))
        self.p_moment_lineEdit.setInputMask("")
        self.p_moment_lineEdit.setObjectName("p_moment_lineEdit")
        self.p_moment_label = QtWidgets.QLabel(self.plate_tab)
        self.p_moment_label.setGeometry(QtCore.QRect(30, 270, 151, 21))
        self.p_moment_label.setObjectName("p_moment_label")
        self.Tab_widget.addTab(self.plate_tab, "")
        self.beam_tab = QtWidgets.QWidget()
        self.beam_tab.setObjectName("beam_tab")
        self.label_12 = QtWidgets.QLabel(self.beam_tab)
        self.label_12.setGeometry(QtCore.QRect(30, 30, 91, 21))
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.beam_tab)
        self.label_10.setGeometry(QtCore.QRect(10, 180, 111, 21))
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.beam_tab)
        self.label_13.setGeometry(QtCore.QRect(10, 60, 111, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.beam_tab)
        self.label_14.setGeometry(QtCore.QRect(250, 90, 121, 21))
        self.label_14.setObjectName("label_14")
        self.comboBox_5 = QtWidgets.QComboBox(self.beam_tab)
        self.comboBox_5.setGeometry(QtCore.QRect(380, 150, 41, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_15 = QtWidgets.QLabel(self.beam_tab)
        self.label_15.setGeometry(QtCore.QRect(10, 0, 111, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.beam_tab)
        self.label_16.setGeometry(QtCore.QRect(10, 120, 111, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.beam_tab)
        self.label_17.setGeometry(QtCore.QRect(30, 150, 91, 21))
        self.label_17.setObjectName("label_17")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.beam_tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 210, 50, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_18 = QtWidgets.QLabel(self.beam_tab)
        self.label_18.setGeometry(QtCore.QRect(250, 150, 121, 21))
        self.label_18.setObjectName("label_18")
        self.comboBox_6 = QtWidgets.QComboBox(self.beam_tab)
        self.comboBox_6.setGeometry(QtCore.QRect(140, 30, 91, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_19 = QtWidgets.QLabel(self.beam_tab)
        self.label_19.setGeometry(QtCore.QRect(30, 90, 101, 21))
        self.label_19.setObjectName("label_19")
        self.comboBox_7 = QtWidgets.QComboBox(self.beam_tab)
        self.comboBox_7.setGeometry(QtCore.QRect(140, 150, 91, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_8 = QtWidgets.QComboBox(self.beam_tab)
        self.comboBox_8.setGeometry(QtCore.QRect(140, 90, 91, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.beam_tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 90, 50, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_20 = QtWidgets.QLabel(self.beam_tab)
        self.label_20.setGeometry(QtCore.QRect(30, 210, 91, 21))
        self.label_20.setObjectName("label_20")
        self.label_41 = QtWidgets.QLabel(self.beam_tab)
        self.label_41.setGeometry(QtCore.QRect(180, 210, 91, 21))
        self.label_41.setObjectName("label_41")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.beam_tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(260, 210, 50, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.radioButton = QtWidgets.QRadioButton(self.beam_tab)
        self.radioButton.setGeometry(QtCore.QRect(20, 250, 141, 17))
        self.radioButton.setObjectName("radioButton")
        self.label_42 = QtWidgets.QLabel(self.beam_tab)
        self.label_42.setGeometry(QtCore.QRect(230, 280, 111, 21))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.beam_tab)
        self.label_43.setGeometry(QtCore.QRect(30, 280, 131, 21))
        self.label_43.setObjectName("label_43")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.beam_tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(170, 280, 50, 20))
        self.lineEdit_10.setReadOnly(False)
        self.lineEdit_10.setClearButtonEnabled(False)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.beam_tab)
        self.lineEdit_11.setGeometry(QtCore.QRect(350, 280, 50, 20))
        self.lineEdit_11.setReadOnly(False)
        self.lineEdit_11.setClearButtonEnabled(False)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_91 = QtWidgets.QLabel(self.beam_tab)
        self.label_91.setGeometry(QtCore.QRect(30, 340, 171, 21))
        self.label_91.setObjectName("label_91")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.beam_tab)
        self.lineEdit_25.setGeometry(QtCore.QRect(190, 340, 50, 20))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.label_92 = QtWidgets.QLabel(self.beam_tab)
        self.label_92.setGeometry(QtCore.QRect(10, 310, 111, 21))
        self.label_92.setObjectName("label_92")
        self.Tab_widget.addTab(self.beam_tab, "")
        self.col_tab = QtWidgets.QWidget()
        self.col_tab.setObjectName("col_tab")
        self.label_21 = QtWidgets.QLabel(self.col_tab)
        self.label_21.setGeometry(QtCore.QRect(30, 30, 91, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.col_tab)
        self.label_22.setGeometry(QtCore.QRect(10, 180, 111, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.col_tab)
        self.label_23.setGeometry(QtCore.QRect(10, 60, 111, 21))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.col_tab)
        self.label_24.setGeometry(QtCore.QRect(250, 90, 121, 21))
        self.label_24.setObjectName("label_24")
        self.comboBox_9 = QtWidgets.QComboBox(self.col_tab)
        self.comboBox_9.setGeometry(QtCore.QRect(380, 150, 41, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.label_25 = QtWidgets.QLabel(self.col_tab)
        self.label_25.setGeometry(QtCore.QRect(10, 0, 111, 21))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.col_tab)
        self.label_26.setGeometry(QtCore.QRect(10, 120, 111, 21))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.col_tab)
        self.label_27.setGeometry(QtCore.QRect(30, 150, 91, 21))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.col_tab)
        self.label_28.setGeometry(QtCore.QRect(250, 150, 121, 21))
        self.label_28.setObjectName("label_28")
        self.comboBox_10 = QtWidgets.QComboBox(self.col_tab)
        self.comboBox_10.setGeometry(QtCore.QRect(140, 30, 91, 22))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.label_29 = QtWidgets.QLabel(self.col_tab)
        self.label_29.setGeometry(QtCore.QRect(30, 90, 101, 21))
        self.label_29.setObjectName("label_29")
        self.comboBox_11 = QtWidgets.QComboBox(self.col_tab)
        self.comboBox_11.setGeometry(QtCore.QRect(140, 150, 91, 22))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_12 = QtWidgets.QComboBox(self.col_tab)
        self.comboBox_12.setGeometry(QtCore.QRect(140, 90, 91, 22))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.col_tab)
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 90, 50, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_141 = QtWidgets.QLabel(self.col_tab)
        self.label_141.setGeometry(QtCore.QRect(180, 210, 91, 21))
        self.label_141.setObjectName("label_141")
        self.label_142 = QtWidgets.QLabel(self.col_tab)
        self.label_142.setGeometry(QtCore.QRect(30, 210, 91, 21))
        self.label_142.setObjectName("label_142")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.col_tab)
        self.lineEdit_40.setGeometry(QtCore.QRect(110, 210, 50, 20))
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.col_tab)
        self.lineEdit_41.setGeometry(QtCore.QRect(260, 210, 50, 20))
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.label_143 = QtWidgets.QLabel(self.col_tab)
        self.label_143.setGeometry(QtCore.QRect(30, 270, 151, 21))
        self.label_143.setObjectName("label_143")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.col_tab)
        self.lineEdit_42.setGeometry(QtCore.QRect(190, 270, 50, 20))
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.label_144 = QtWidgets.QLabel(self.col_tab)
        self.label_144.setGeometry(QtCore.QRect(10, 240, 111, 21))
        self.label_144.setObjectName("label_144")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.col_tab)
        self.lineEdit_43.setGeometry(QtCore.QRect(380, 270, 50, 19))
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.label_145 = QtWidgets.QLabel(self.col_tab)
        self.label_145.setGeometry(QtCore.QRect(260, 270, 121, 20))
        self.label_145.setObjectName("label_145")
        self.Tab_widget.addTab(self.col_tab, "")
        self.foot_tab = QtWidgets.QWidget()
        self.foot_tab.setObjectName("foot_tab")
        self.label_31 = QtWidgets.QLabel(self.foot_tab)
        self.label_31.setGeometry(QtCore.QRect(30, 30, 91, 21))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.foot_tab)
        self.label_32.setGeometry(QtCore.QRect(10, 220, 111, 21))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.foot_tab)
        self.label_33.setGeometry(QtCore.QRect(10, 60, 111, 21))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.foot_tab)
        self.label_34.setGeometry(QtCore.QRect(250, 90, 121, 21))
        self.label_34.setObjectName("label_34")
        self.comboBox_13 = QtWidgets.QComboBox(self.foot_tab)
        self.comboBox_13.setGeometry(QtCore.QRect(380, 150, 41, 22))
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.label_35 = QtWidgets.QLabel(self.foot_tab)
        self.label_35.setGeometry(QtCore.QRect(10, 0, 111, 21))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.foot_tab)
        self.label_36.setGeometry(QtCore.QRect(10, 120, 111, 21))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.foot_tab)
        self.label_37.setGeometry(QtCore.QRect(30, 150, 91, 21))
        self.label_37.setObjectName("label_37")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.foot_tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(110, 280, 50, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_38 = QtWidgets.QLabel(self.foot_tab)
        self.label_38.setGeometry(QtCore.QRect(250, 150, 121, 21))
        self.label_38.setObjectName("label_38")
        self.comboBox_14 = QtWidgets.QComboBox(self.foot_tab)
        self.comboBox_14.setGeometry(QtCore.QRect(140, 30, 91, 22))
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.label_39 = QtWidgets.QLabel(self.foot_tab)
        self.label_39.setGeometry(QtCore.QRect(30, 90, 101, 21))
        self.label_39.setObjectName("label_39")
        self.comboBox_15 = QtWidgets.QComboBox(self.foot_tab)
        self.comboBox_15.setGeometry(QtCore.QRect(140, 150, 91, 22))
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_16 = QtWidgets.QComboBox(self.foot_tab)
        self.comboBox_16.setGeometry(QtCore.QRect(140, 90, 91, 22))
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.foot_tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(380, 90, 50, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_40 = QtWidgets.QLabel(self.foot_tab)
        self.label_40.setGeometry(QtCore.QRect(30, 280, 91, 21))
        self.label_40.setObjectName("label_40")
        self.label_93 = QtWidgets.QLabel(self.foot_tab)
        self.label_93.setGeometry(QtCore.QRect(170, 280, 91, 21))
        self.label_93.setObjectName("label_93")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.foot_tab)
        self.lineEdit_26.setGeometry(QtCore.QRect(250, 280, 50, 20))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.label_146 = QtWidgets.QLabel(self.foot_tab)
        self.label_146.setGeometry(QtCore.QRect(30, 190, 231, 21))
        self.label_146.setObjectName("label_146")
        self.comboBox_50 = QtWidgets.QComboBox(self.foot_tab)
        self.comboBox_50.setGeometry(QtCore.QRect(260, 190, 41, 22))
        self.comboBox_50.setObjectName("comboBox_50")
        self.comboBox_50.addItem("")
        self.comboBox_50.addItem("")
        self.comboBox_50.addItem("")
        self.label_147 = QtWidgets.QLabel(self.foot_tab)
        self.label_147.setGeometry(QtCore.QRect(20, 250, 111, 21))
        self.label_147.setObjectName("label_147")
        self.label_148 = QtWidgets.QLabel(self.foot_tab)
        self.label_148.setGeometry(QtCore.QRect(30, 340, 91, 21))
        self.label_148.setObjectName("label_148")
        self.label_149 = QtWidgets.QLabel(self.foot_tab)
        self.label_149.setGeometry(QtCore.QRect(20, 310, 151, 21))
        self.label_149.setObjectName("label_149")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.foot_tab)
        self.lineEdit_44.setGeometry(QtCore.QRect(110, 340, 50, 20))
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.foot_tab)
        self.lineEdit_45.setGeometry(QtCore.QRect(250, 340, 50, 20))
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.label_150 = QtWidgets.QLabel(self.foot_tab)
        self.label_150.setGeometry(QtCore.QRect(170, 340, 91, 21))
        self.label_150.setObjectName("label_150")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.foot_tab)
        self.lineEdit_46.setGeometry(QtCore.QRect(390, 280, 50, 20))
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.label_151 = QtWidgets.QLabel(self.foot_tab)
        self.label_151.setGeometry(QtCore.QRect(310, 280, 91, 21))
        self.label_151.setObjectName("label_151")
        self.label_152 = QtWidgets.QLabel(self.foot_tab)
        self.label_152.setGeometry(QtCore.QRect(30, 400, 111, 20))
        self.label_152.setObjectName("label_152")
        self.label_153 = QtWidgets.QLabel(self.foot_tab)
        self.label_153.setGeometry(QtCore.QRect(10, 370, 111, 21))
        self.label_153.setObjectName("label_153")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.foot_tab)
        self.lineEdit_47.setGeometry(QtCore.QRect(150, 400, 50, 19))
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.Tab_widget.addTab(self.foot_tab, "")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(480, 0, 270, 450))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 420, 110, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 250, 170))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(7, 190, 251, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 200, 20, 211))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(250, 200, 20, 211))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(10, 400, 251, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 420, 110, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 231, 191))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionInlcuded_data = QtWidgets.QAction(MainWindow)
        self.actionInlcuded_data.setObjectName("actionInlcuded_data")
        self.actionrecently_opened_file = QtWidgets.QAction(MainWindow)
        self.actionrecently_opened_file.setObjectName("actionrecently_opened_file")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionrecently_opened2_file = QtWidgets.QAction(MainWindow)
        self.actionrecently_opened2_file.setObjectName("actionrecently_opened2_file")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionrecently_opened_file)
        self.menuFile.addAction(self.actionrecently_opened2_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionexit)
        self.menuInfo.addAction(self.actionInlcuded_data)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        self.Tab_widget.setCurrentIndex(3)
        self.radioButton.toggled['bool'].connect(self.lineEdit_10.setDisabled)
        self.radioButton.toggled['bool'].connect(self.lineEdit_11.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Tab_widget, self.p_exp_combo)
        MainWindow.setTabOrder(self.p_exp_combo, self.p_concr_class_combo)
        MainWindow.setTabOrder(self.p_concr_class_combo, self.p_concr_cover_lineEdit)
        MainWindow.setTabOrder(self.p_concr_cover_lineEdit, self.p_steel_class_combo)
        MainWindow.setTabOrder(self.p_steel_class_combo, self.p_bar_diam_combo)
        MainWindow.setTabOrder(self.p_bar_diam_combo, self.p_th_lineEdit)
        MainWindow.setTabOrder(self.p_th_lineEdit, self.p_moment_lineEdit)
        MainWindow.setTabOrder(self.p_moment_lineEdit, self.comboBox_6)
        MainWindow.setTabOrder(self.comboBox_6, self.comboBox_8)
        MainWindow.setTabOrder(self.comboBox_8, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.comboBox_7)
        MainWindow.setTabOrder(self.comboBox_7, self.comboBox_5)
        MainWindow.setTabOrder(self.comboBox_5, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_9)
        MainWindow.setTabOrder(self.lineEdit_9, self.radioButton)
        MainWindow.setTabOrder(self.radioButton, self.lineEdit_10)
        MainWindow.setTabOrder(self.lineEdit_10, self.lineEdit_11)
        MainWindow.setTabOrder(self.lineEdit_11, self.lineEdit_25)
        MainWindow.setTabOrder(self.lineEdit_25, self.comboBox_10)
        MainWindow.setTabOrder(self.comboBox_10, self.comboBox_12)
        MainWindow.setTabOrder(self.comboBox_12, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.comboBox_11)
        MainWindow.setTabOrder(self.comboBox_11, self.comboBox_9)
        MainWindow.setTabOrder(self.comboBox_9, self.lineEdit_40)
        MainWindow.setTabOrder(self.lineEdit_40, self.lineEdit_41)
        MainWindow.setTabOrder(self.lineEdit_41, self.lineEdit_42)
        MainWindow.setTabOrder(self.lineEdit_42, self.lineEdit_43)
        MainWindow.setTabOrder(self.lineEdit_43, self.comboBox_14)
        MainWindow.setTabOrder(self.comboBox_14, self.comboBox_16)
        MainWindow.setTabOrder(self.comboBox_16, self.lineEdit_8)
        MainWindow.setTabOrder(self.lineEdit_8, self.comboBox_15)
        MainWindow.setTabOrder(self.comboBox_15, self.comboBox_13)
        MainWindow.setTabOrder(self.comboBox_13, self.comboBox_50)
        MainWindow.setTabOrder(self.comboBox_50, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_26)
        MainWindow.setTabOrder(self.lineEdit_26, self.lineEdit_46)
        MainWindow.setTabOrder(self.lineEdit_46, self.lineEdit_44)
        MainWindow.setTabOrder(self.lineEdit_44, self.lineEdit_45)
        MainWindow.setTabOrder(self.lineEdit_45, self.lineEdit_47)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.p_concrete_label.setText(_translate("MainWindow", "Concrete:"))
        self.p_concr_class_label.setText(_translate("MainWindow", "Class of concrete:"))
        self.p_concr_class_combo.setItemText(0, _translate("MainWindow", "C30/37"))
        self.p_concr_class_combo.setItemText(1, _translate("MainWindow", "C35/45"))
        self.p_concr_cover_label.setText(_translate("MainWindow", "Concrete cover[cm]:"))
        self.p_steel_labe.setText(_translate("MainWindow", "Steel:"))
        self.p_steel_class_label.setText(_translate("MainWindow", "Class of steel:"))
        self.p_steel_class_combo.setItemText(0, _translate("MainWindow", "RB500"))
        self.p_steel_class_combo.setItemText(1, _translate("MainWindow", "RB500W"))
        self.p_bar_label.setText(_translate("MainWindow", "Bar diameter[mm]:"))
        self.p_bar_diam_combo.setItemText(0, _translate("MainWindow", "16"))
        self.p_bar_diam_combo.setItemText(1, _translate("MainWindow", "18"))
        self.p_bar_diam_combo.setItemText(2, _translate("MainWindow", "20"))
        self.p_geom_label.setText(_translate("MainWindow", "Geometry:"))
        self.p_th_label.setText(_translate("MainWindow", "Thickness [cm]:"))
        self.p_env_label.setText(_translate("MainWindow", "Environment:"))
        self.p_exp_label.setText(_translate("MainWindow", "Exposition class:"))
        self.p_exp_combo.setItemText(0, _translate("MainWindow", "X0"))
        self.p_exp_combo.setItemText(1, _translate("MainWindow", "XC1"))
        self.p_load_label.setText(_translate("MainWindow", "Load:"))
        self.p_moment_label.setText(_translate("MainWindow", "Bending moment [kN*m]:"))
        self.Tab_widget.setTabText(self.Tab_widget.indexOf(self.plate_tab), _translate("MainWindow", "Plate"))
        self.label_12.setText(_translate("MainWindow", "Exposition class:"))
        self.label_10.setText(_translate("MainWindow", "Geometry:"))
        self.label_13.setText(_translate("MainWindow", "Concrete:"))
        self.label_14.setText(_translate("MainWindow", "Concrete cover[cm]:"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "16"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "18"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "20"))
        self.label_15.setText(_translate("MainWindow", "Environment:"))
        self.label_16.setText(_translate("MainWindow", "Steel:"))
        self.label_17.setText(_translate("MainWindow", "Class of steel:"))
        self.label_18.setText(_translate("MainWindow", "Bar diameter[mm]:"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "X0"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "XC1"))
        self.label_19.setText(_translate("MainWindow", "Class of concrete:"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "RB500"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "RB500W"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "C30/37"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "C35/45"))
        self.label_20.setText(_translate("MainWindow", "Height [cm]:"))
        self.label_41.setText(_translate("MainWindow", "Width [cm]:"))
        self.radioButton.setText(_translate("MainWindow", "Support section"))
        self.label_42.setText(_translate("MainWindow", "Flange width [cm]:"))
        self.label_43.setText(_translate("MainWindow", "Flange thickness [cm]:"))
        self.label_91.setText(_translate("MainWindow", "Bending moment [kN*m]:"))
        self.label_92.setText(_translate("MainWindow", "Load:"))
        self.Tab_widget.setTabText(self.Tab_widget.indexOf(self.beam_tab), _translate("MainWindow", "Beam"))
        self.label_21.setText(_translate("MainWindow", "Exposition class:"))
        self.label_22.setText(_translate("MainWindow", "Geometry:"))
        self.label_23.setText(_translate("MainWindow", "Concrete:"))
        self.label_24.setText(_translate("MainWindow", "Concrete cover[cm]:"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "16"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "18"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "20"))
        self.label_25.setText(_translate("MainWindow", "Environment:"))
        self.label_26.setText(_translate("MainWindow", "Steel:"))
        self.label_27.setText(_translate("MainWindow", "Class of steel:"))
        self.label_28.setText(_translate("MainWindow", "Bar diameter[mm]:"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "X0"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "XC1"))
        self.label_29.setText(_translate("MainWindow", "Class of concrete:"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "RB500"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "RB500W"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "C30/37"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "C35/45"))
        self.label_141.setText(_translate("MainWindow", "Width [cm]:"))
        self.label_142.setText(_translate("MainWindow", "Height [cm]:"))
        self.label_143.setText(_translate("MainWindow", "Bending moment [kN*m]:"))
        self.label_144.setText(_translate("MainWindow", "Load:"))
        self.label_145.setText(_translate("MainWindow", "Vertical force [kN]:"))
        self.Tab_widget.setTabText(self.Tab_widget.indexOf(self.col_tab), _translate("MainWindow", "Column"))
        self.label_31.setText(_translate("MainWindow", "Exposition class:"))
        self.label_32.setText(_translate("MainWindow", "Geometry:"))
        self.label_33.setText(_translate("MainWindow", "Concrete:"))
        self.label_34.setText(_translate("MainWindow", "Concrete cover[cm]:"))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "16"))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "18"))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "20"))
        self.label_35.setText(_translate("MainWindow", "Environment:"))
        self.label_36.setText(_translate("MainWindow", "Steel:"))
        self.label_37.setText(_translate("MainWindow", "Class of steel:"))
        self.label_38.setText(_translate("MainWindow", "Bar diameter[mm]:"))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "X0"))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "XC1"))
        self.label_39.setText(_translate("MainWindow", "Class of concrete:"))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "RB500"))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "RB500W"))
        self.comboBox_16.setItemText(0, _translate("MainWindow", "C30/37"))
        self.comboBox_16.setItemText(1, _translate("MainWindow", "C35/45"))
        self.label_40.setText(_translate("MainWindow", "Width [cm]:"))
        self.label_93.setText(_translate("MainWindow", "Length [cm]:"))
        self.label_146.setText(_translate("MainWindow", "Column reinforcement diameter[mm]:"))
        self.comboBox_50.setItemText(0, _translate("MainWindow", "16"))
        self.comboBox_50.setItemText(1, _translate("MainWindow", "18"))
        self.comboBox_50.setItemText(2, _translate("MainWindow", "20"))
        self.label_147.setText(_translate("MainWindow", "Foot:"))
        self.label_148.setText(_translate("MainWindow", "Height [cm]:"))
        self.label_149.setText(_translate("MainWindow", "Column cross-section:"))
        self.label_150.setText(_translate("MainWindow", "Width [cm]:"))
        self.label_151.setText(_translate("MainWindow", "Height [cm]:"))
        self.label_152.setText(_translate("MainWindow", "Vertical force [kN]:"))
        self.label_153.setText(_translate("MainWindow", "Load:"))
        self.Tab_widget.setTabText(self.Tab_widget.indexOf(self.foot_tab), _translate("MainWindow", "Foot"))
        self.pushButton.setText(_translate("MainWindow", "Run calculations"))
        self.label.setText(_translate("MainWindow", "Drawing placeholder here"))
        self.pushButton_2.setText(_translate("MainWindow", "Generate report"))
        self.label_2.setText(_translate("MainWindow", "Calculations information, progress, errors etc."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionInlcuded_data.setText(_translate("MainWindow", "Inlcuded data"))
        self.actionrecently_opened_file.setText(_translate("MainWindow", "recently_opened.file"))
        self.actionexit.setText(_translate("MainWindow", "Close"))
        self.actionrecently_opened2_file.setText(_translate("MainWindow", "recently_opened2.file"))
        self.actionNew.setText(_translate("MainWindow", "New"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())