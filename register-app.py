# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register-app.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabRegister = QtWidgets.QWidget()
        self.tabRegister.setObjectName("tabRegister")
        self.formLayoutRegister = QtWidgets.QFormLayout(self.tabRegister)
        self.formLayoutRegister.setObjectName("formLayoutRegister")
        self.labelName = QtWidgets.QLabel(self.tabRegister)
        self.labelName.setObjectName("labelName")
        self.formLayoutRegister.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(self.tabRegister)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayoutRegister.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.labelDepartment = QtWidgets.QLabel(self.tabRegister)
        self.labelDepartment.setObjectName("labelDepartment")
        self.formLayoutRegister.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelDepartment)
        self.lineEditDepartment = QtWidgets.QLineEdit(self.tabRegister)
        self.lineEditDepartment.setObjectName("lineEditDepartment")
        self.formLayoutRegister.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditDepartment)
        self.labelCardInfo = QtWidgets.QLabel(self.tabRegister)
        self.labelCardInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCardInfo.setObjectName("labelCardInfo")
        self.formLayoutRegister.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.labelCardInfo)
        self.buttonAssignCard = QtWidgets.QPushButton(self.tabRegister)
        self.buttonAssignCard.setObjectName("buttonAssignCard")
        self.formLayoutRegister.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.buttonAssignCard)
        self.labelAccess = QtWidgets.QLabel(self.tabRegister)
        self.labelAccess.setObjectName("labelAccess")
        self.formLayoutRegister.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.labelAccess)
        self.groupBoxAccess = QtWidgets.QGroupBox(self.tabRegister)
        self.groupBoxAccess.setObjectName("groupBoxAccess")
        self.verticalLayoutAccess = QtWidgets.QVBoxLayout(self.groupBoxAccess)
        self.verticalLayoutAccess.setObjectName("verticalLayoutAccess")
        self.checkBoxSala1 = QtWidgets.QCheckBox(self.groupBoxAccess)
        self.checkBoxSala1.setObjectName("checkBoxSala1")
        self.verticalLayoutAccess.addWidget(self.checkBoxSala1)
        self.checkBoxSala2 = QtWidgets.QCheckBox(self.groupBoxAccess)
        self.checkBoxSala2.setObjectName("checkBoxSala2")
        self.verticalLayoutAccess.addWidget(self.checkBoxSala2)
        self.checkBoxSala3 = QtWidgets.QCheckBox(self.groupBoxAccess)
        self.checkBoxSala3.setObjectName("checkBoxSala3")
        self.verticalLayoutAccess.addWidget(self.checkBoxSala3)
        self.checkBoxSala4 = QtWidgets.QCheckBox(self.groupBoxAccess)
        self.checkBoxSala4.setObjectName("checkBoxSala4")
        self.verticalLayoutAccess.addWidget(self.checkBoxSala4)
        self.checkBoxSala5 = QtWidgets.QCheckBox(self.groupBoxAccess)
        self.checkBoxSala5.setObjectName("checkBoxSala5")
        self.verticalLayoutAccess.addWidget(self.checkBoxSala5)
        self.checkBoxSala6 = QtWidgets.QCheckBox(self.groupBoxAccess)
        self.checkBoxSala6.setObjectName("checkBoxSala6")
        self.verticalLayoutAccess.addWidget(self.checkBoxSala6)
        self.formLayoutRegister.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.groupBoxAccess)
        self.buttonSave = QtWidgets.QPushButton(self.tabRegister)
        self.buttonSave.setObjectName("buttonSave")
        self.formLayoutRegister.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.buttonSave)
        self.tabWidget.addTab(self.tabRegister, "")
        self.tabEmployees = QtWidgets.QWidget()
        self.tabEmployees.setObjectName("tabEmployees")
        self.verticalLayoutEmployees = QtWidgets.QVBoxLayout(self.tabEmployees)
        self.verticalLayoutEmployees.setObjectName("verticalLayoutEmployees")
        self.tableEmployees = QtWidgets.QTableWidget(self.tabEmployees)
        self.tableEmployees.setRowCount(0)
        self.tableEmployees.setColumnCount(2)
        self.tableEmployees.setObjectName("tableEmployees")
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(1, item)
        self.verticalLayoutEmployees.addWidget(self.tableEmployees)
        self.tabWidget.addTab(self.tabEmployees, "")
        self.tabAccessLogs = QtWidgets.QWidget()
        self.tabAccessLogs.setObjectName("tabAccessLogs")
        self.verticalLayoutLogs = QtWidgets.QVBoxLayout(self.tabAccessLogs)
        self.verticalLayoutLogs.setObjectName("verticalLayoutLogs")
        self.tableLogs = QtWidgets.QTableWidget(self.tabAccessLogs)
        self.tableLogs.setRowCount(0)
        self.tableLogs.setColumnCount(3)
        self.tableLogs.setObjectName("tableLogs")
        item = QtWidgets.QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(2, item)
        self.verticalLayoutLogs.addWidget(self.tableLogs)
        self.tabWidget.addTab(self.tabAccessLogs, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonExit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExit.setObjectName("buttonExit")
        self.verticalLayout.addWidget(self.buttonExit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "System Identyfikacji Pracowników"))
        self.labelTitle.setText(_translate("MainWindow", "System Identyfikacji Pracowników"))
        self.labelName.setText(_translate("MainWindow", "Imię i Nazwisko:"))
        self.labelDepartment.setText(_translate("MainWindow", "Dział:"))
        self.labelCardInfo.setText(_translate("MainWindow", "Zbliż kartę RFID do czytnika..."))
        self.buttonAssignCard.setText(_translate("MainWindow", "Przypisz Kartę"))
        self.labelAccess.setText(_translate("MainWindow", "Dostęp do sal:"))
        self.checkBoxSala1.setText(_translate("MainWindow", "Sala 1"))
        self.checkBoxSala2.setText(_translate("MainWindow", "Sala 2"))
        self.checkBoxSala3.setText(_translate("MainWindow", "Sala 3"))
        self.checkBoxSala4.setText(_translate("MainWindow", "Sala 4"))
        self.checkBoxSala5.setText(_translate("MainWindow", "Sala 5"))
        self.checkBoxSala6.setText(_translate("MainWindow", "Sala 6"))
        self.buttonSave.setText(_translate("MainWindow", "Zapisz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRegister), _translate("MainWindow", "Rejestracja"))
        item = self.tableEmployees.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Imię i Nazwisko"))
        item = self.tableEmployees.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Dział"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEmployees), _translate("MainWindow", "Pracownicy"))
        item = self.tableLogs.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data i Czas"))
        item = self.tableLogs.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Imię i Nazwisko"))
        item = self.tableLogs.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAccessLogs), _translate("MainWindow", "Logi Dostępów"))
        self.buttonExit.setText(_translate("MainWindow", "Wyjście"))
