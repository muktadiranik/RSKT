# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'income_expense_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_income_expense(object):
    def setupUi(self, MainWindow_income_expense):
        MainWindow_income_expense.setObjectName("MainWindow_income_expense")
        MainWindow_income_expense.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow_income_expense)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(42)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 6)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 7, 6, 1, 1)
        self.lineEdit_search_by = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_search_by.setFont(font)
        self.lineEdit_search_by.setObjectName("lineEdit_search_by")
        self.gridLayout.addWidget(self.lineEdit_search_by, 3, 2, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 8, 2, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 3, 6, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.gridLayout.addWidget(self.tableWidget, 5, 1, 1, 6)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 3, 7, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 7, 1, 1, 1)
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.gridLayout.addWidget(self.pushButton_update, 7, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 7, 3, 1, 1)
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.gridLayout.addWidget(self.pushButton_refresh, 7, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow_income_expense.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_income_expense)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_income_expense)
        MainWindow_income_expense.setTabOrder(self.lineEdit_search_by, self.pushButton_search)
        MainWindow_income_expense.setTabOrder(self.pushButton_search, self.tableWidget)
        MainWindow_income_expense.setTabOrder(self.tableWidget, self.pushButton_add)
        MainWindow_income_expense.setTabOrder(self.pushButton_add, self.pushButton_update)
        MainWindow_income_expense.setTabOrder(self.pushButton_update, self.pushButton_2)
        MainWindow_income_expense.setTabOrder(self.pushButton_2, self.pushButton_refresh)
        MainWindow_income_expense.setTabOrder(self.pushButton_refresh, self.pushButton_3)

    def retranslateUi(self, MainWindow_income_expense):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_income_expense.setWindowTitle(_translate("MainWindow_income_expense", "MainWindow"))
        self.label.setText(_translate("MainWindow_income_expense", "Income Expense Miscellaneous"))
        self.pushButton_3.setText(_translate("MainWindow_income_expense", "To XLSX"))
        self.label_2.setText(_translate("MainWindow_income_expense", "Search By Year"))
        self.pushButton_search.setText(_translate("MainWindow_income_expense", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_income_expense", "#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_income_expense", "Year"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_income_expense", "Monthly Contribution"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_income_expense", "Admit/Fine"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow_income_expense", "Form"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow_income_expense", "Donation"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow_income_expense", "Death Allowance"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow_income_expense", "Disaster Allowance"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow_income_expense", "Previous Balance"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow_income_expense", "New Balance"))
        self.pushButton_add.setText(_translate("MainWindow_income_expense", "Add"))
        self.pushButton_update.setText(_translate("MainWindow_income_expense", "Update"))
        self.pushButton_2.setText(_translate("MainWindow_income_expense", "Delete"))
        self.pushButton_refresh.setText(_translate("MainWindow_income_expense", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_income_expense = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_income_expense()
    ui.setupUi(MainWindow_income_expense)
    MainWindow_income_expense.show()
    sys.exit(app.exec_())
