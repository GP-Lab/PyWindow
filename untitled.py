# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_4)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_4)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_2.addWidget(self.graphicsView_2)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 7, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 6, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTime_Domain = QtWidgets.QAction(MainWindow)
        self.actionTime_Domain.setObjectName("actionTime_Domain")
        self.actionFrequency_Domain = QtWidgets.QAction(MainWindow)
        self.actionFrequency_Domain.setObjectName("actionFrequency_Domain")
        self.actionFrequency_Domain_2 = QtWidgets.QAction(MainWindow)
        self.actionFrequency_Domain_2.setObjectName("actionFrequency_Domain_2")
        self.actionAnalyse_Parameter = QtWidgets.QAction(MainWindow)
        self.actionAnalyse_Parameter.setObjectName("actionAnalyse_Parameter")
        self.actionFull_View = QtWidgets.QAction(MainWindow)
        self.actionFull_View.setObjectName("actionFull_View")
        self.actionLegend = QtWidgets.QAction(MainWindow)
        self.actionLegend.setObjectName("actionLegend")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuFile.addAction(self.actionExport)
        self.menuView.addAction(self.actionTime_Domain)
        self.menuView.addAction(self.actionFrequency_Domain_2)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionLegend)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionAnalyse_Parameter)
        self.menuTool.addAction(self.actionFull_View)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Window Viewer"))
        self.groupBox.setTitle(_translate("MainWindow", "Window_list"))
        self.pushButton.setText(_translate("MainWindow", "Add_Window"))
        self.pushButton_4.setText(_translate("MainWindow", "Copy_Window"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.groupBox_3.setTitle(_translate("MainWindow", " Current Window Information"))
        self.label_3.setText(_translate("MainWindow", "Length"))
        self.label_4.setText(_translate("MainWindow", "Parameter"))
        self.comboBox.setItemText(0, _translate("MainWindow", "hamming"))
        self.comboBox.setItemText(1, _translate("MainWindow", "triang"))
        self.comboBox.setItemText(2, _translate("MainWindow", "blackman"))
        self.comboBox.setItemText(3, _translate("MainWindow", "hann"))
        self.comboBox.setItemText(4, _translate("MainWindow", "kaiser"))
        self.comboBox.setItemText(5, _translate("MainWindow", "flattop"))
        self.comboBox.setItemText(6, _translate("MainWindow", "lanczos"))
        self.comboBox.setItemText(7, _translate("MainWindow", "boxcar"))
        self.comboBox.setItemText(8, _translate("MainWindow", "parzen"))
        self.comboBox.setItemText(9, _translate("MainWindow", "bohman"))
        self.comboBox.setItemText(10, _translate("MainWindow", "blackmanharris"))
        self.comboBox.setItemText(11, _translate("MainWindow", "nuttall"))
        self.comboBox.setItemText(12, _translate("MainWindow", "barthann"))
        self.comboBox.setItemText(13, _translate("MainWindow", "cosine"))
        self.comboBox.setItemText(14, _translate("MainWindow", "exponential"))
        self.comboBox.setItemText(15, _translate("MainWindow", "tukey"))
        self.comboBox.setItemText(16, _translate("MainWindow", "taylor"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "Type"))
        self.label_5.setText(_translate("MainWindow", "Parameter2"))
        self.label_6.setText(_translate("MainWindow", "Sampling"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "symmetric"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "periodic"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTool.setTitle(_translate("MainWindow", "Tool"))
        self.actionTime_Domain.setText(_translate("MainWindow", "Time Domain"))
        self.actionFrequency_Domain.setText(_translate("MainWindow", "Frequency Domain"))
        self.actionFrequency_Domain_2.setText(_translate("MainWindow", "Frequency Domain"))
        self.actionAnalyse_Parameter.setText(_translate("MainWindow", "Analyse Parameter"))
        self.actionFull_View.setText(_translate("MainWindow", "Full View"))
        self.actionLegend.setText(_translate("MainWindow", "Legend"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
