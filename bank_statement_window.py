from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import pandas as pd
import threading
import datetime


class Ui_MainWindow_bank_statement(object):
    def setupUi(self, MainWindow_bank_statement):
        MainWindow_bank_statement.setObjectName("MainWindow_bank_statement")
        MainWindow_bank_statement.resize(1400, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow_bank_statement)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_xlsx = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_xlsx.setFont(font)
        self.pushButton_xlsx.setObjectName("pushButton_xlsx")
        self.gridLayout.addWidget(self.pushButton_xlsx, 10, 5, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 10, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 9, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 10, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 10, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 10, 6, 1, 1)
        self.pushButton_edit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_edit.setFont(font)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.gridLayout.addWidget(self.pushButton_edit, 10, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem6, 2, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem7, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem8, 1, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 2, 5, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 7, 1, 1)
        self.lineEdit_credit = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_credit.setFont(font)
        self.lineEdit_credit.setObjectName("lineEdit_credit")
        self.gridLayout_2.addWidget(self.lineEdit_credit, 2, 7, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 9, 1, 1)
        self.lineEdit_balance = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_balance.setFont(font)
        self.lineEdit_balance.setObjectName("lineEdit_balance")
        self.gridLayout_2.addWidget(self.lineEdit_balance, 2, 8, 1, 1)
        self.lineEdit_transaction_code = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_transaction_code.setFont(font)
        self.lineEdit_transaction_code.setObjectName("lineEdit_transaction_code")
        self.gridLayout_2.addWidget(self.lineEdit_transaction_code, 2, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 4, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout_2.addWidget(self.pushButton_save, 4, 9, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 2, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem9, 3, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 5, 1, 1)
        self.lineEdit_debit = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_debit.setFont(font)
        self.lineEdit_debit.setObjectName("lineEdit_debit")
        self.gridLayout_2.addWidget(self.lineEdit_debit, 2, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 8, 1, 1)
        self.lineEdit_remarks = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_remarks.setFont(font)
        self.lineEdit_remarks.setObjectName("lineEdit_remarks")
        self.gridLayout_2.addWidget(self.lineEdit_remarks, 2, 9, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 0, 1, 1, 1)
        self.comboBox_account_type = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_account_type.setFont(font)
        self.comboBox_account_type.setObjectName("comboBox_account_type")
        self.gridLayout_2.addWidget(self.comboBox_account_type, 2, 0, 1, 2)
        self.pushButton_update = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.gridLayout_2.addWidget(self.pushButton_update, 4, 8, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 3, 4, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout_2.addWidget(self.pushButton_cancel, 4, 7, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 5)
        spacerItem12 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem12, 7, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem13, 11, 1, 1, 1)
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.gridLayout.addWidget(self.pushButton_refresh, 10, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(42)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 5)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        self.gridLayout.addWidget(self.tableWidget, 8, 1, 1, 5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem14, 2, 8, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem15, 0, 9, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem16, 2, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem17, 2, 9, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem18, 2, 7, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem19, 2, 10, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 4, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem20, 2, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 0, 3, 3, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 6, 1, 1)
        self.comboBox_search_by = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_search_by.setFont(font)
        self.comboBox_search_by.setObjectName("comboBox_search_by")
        self.gridLayout_3.addWidget(self.comboBox_search_by, 1, 7, 1, 2)
        self.lineEdit_search_by = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_search_by.setFont(font)
        self.lineEdit_search_by.setObjectName("lineEdit_search_by")
        self.gridLayout_3.addWidget(self.lineEdit_search_by, 1, 9, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout_3.addWidget(self.pushButton_search, 1, 10, 1, 2)
        spacerItem21 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem21, 2, 11, 1, 1)
        self.comboBox_account_type_search = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_account_type_search.setFont(font)
        self.comboBox_account_type_search.setObjectName("comboBox_account_type_search")
        self.gridLayout_3.addWidget(self.comboBox_account_type_search, 1, 1, 1, 2)
        self.comboBox_date_search = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_date_search.setFont(font)
        self.comboBox_date_search.setObjectName("comboBox_date_search")
        self.gridLayout_3.addWidget(self.comboBox_date_search, 1, 5, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem22, 2, 5, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.gridLayout.addWidget(self.groupBox_2, 4, 1, 1, 5)
        spacerItem23 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem23, 5, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem24 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem24, 2, 4, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem25, 2, 2, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem26, 2, 3, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem27, 0, 5, 1, 1)
        self.comboBox_view_by = QtWidgets.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_view_by.setFont(font)
        self.comboBox_view_by.setObjectName("comboBox_view_by")
        self.gridLayout_6.addWidget(self.comboBox_view_by, 1, 1, 1, 2)
        spacerItem28 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem28, 2, 6, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 1, 0, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem29, 2, 1, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem30, 2, 7, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem31, 2, 5, 1, 1)
        self.pushButton_view = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_view.setFont(font)
        self.pushButton_view.setObjectName("pushButton_view")
        self.gridLayout_6.addWidget(self.pushButton_view, 1, 4, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem32, 1, 5, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_6)
        self.gridLayout.addWidget(self.groupBox_3, 6, 1, 1, 5)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow_bank_statement.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_bank_statement)
        self.statusbar.setObjectName("statusbar")
        MainWindow_bank_statement.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_bank_statement)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_bank_statement)
        MainWindow_bank_statement.setTabOrder(self.comboBox_account_type, self.dateEdit)
        MainWindow_bank_statement.setTabOrder(self.dateEdit, self.lineEdit_transaction_code)
        MainWindow_bank_statement.setTabOrder(self.lineEdit_transaction_code, self.lineEdit_debit)
        MainWindow_bank_statement.setTabOrder(self.lineEdit_debit, self.lineEdit_credit)
        MainWindow_bank_statement.setTabOrder(self.lineEdit_credit, self.lineEdit_balance)
        MainWindow_bank_statement.setTabOrder(self.lineEdit_balance, self.lineEdit_remarks)
        MainWindow_bank_statement.setTabOrder(self.lineEdit_remarks, self.pushButton_cancel)
        MainWindow_bank_statement.setTabOrder(self.pushButton_cancel, self.pushButton_update)
        MainWindow_bank_statement.setTabOrder(self.pushButton_update, self.pushButton_save)
        MainWindow_bank_statement.setTabOrder(self.pushButton_save, self.comboBox_account_type_search)
        MainWindow_bank_statement.setTabOrder(self.comboBox_account_type_search, self.comboBox_date_search)
        MainWindow_bank_statement.setTabOrder(self.comboBox_date_search, self.comboBox_search_by)
        MainWindow_bank_statement.setTabOrder(self.comboBox_search_by, self.lineEdit_search_by)
        MainWindow_bank_statement.setTabOrder(self.lineEdit_search_by, self.pushButton_search)
        MainWindow_bank_statement.setTabOrder(self.pushButton_search, self.comboBox_view_by)
        MainWindow_bank_statement.setTabOrder(self.comboBox_view_by, self.pushButton_view)
        MainWindow_bank_statement.setTabOrder(self.pushButton_view, self.tableWidget)
        MainWindow_bank_statement.setTabOrder(self.tableWidget, self.pushButton_edit)
        MainWindow_bank_statement.setTabOrder(self.pushButton_edit, self.pushButton_delete)
        MainWindow_bank_statement.setTabOrder(self.pushButton_delete, self.pushButton_refresh)
        MainWindow_bank_statement.setTabOrder(self.pushButton_refresh, self.pushButton_xlsx)

        tableWidget_header = self.tableWidget.horizontalHeader()
        tableWidget_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        tableWidget_header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)

        self.assign()

    def retranslateUi(self, MainWindow_bank_statement):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_bank_statement.setWindowTitle(_translate("MainWindow_bank_statement", "Bank Statement"))
        self.pushButton_xlsx.setText(_translate("MainWindow_bank_statement", "To XLSX"))
        self.pushButton_delete.setText(_translate("MainWindow_bank_statement", "Delete"))
        self.pushButton_edit.setText(_translate("MainWindow_bank_statement", "Edit"))
        self.groupBox.setTitle(_translate("MainWindow_bank_statement", "New Statement Entry"))
        self.label_9.setText(_translate("MainWindow_bank_statement", "Account Type"))
        self.label_5.setText(_translate("MainWindow_bank_statement", "Credit"))
        self.label_4.setText(_translate("MainWindow_bank_statement", "Debit"))
        self.label_7.setText(_translate("MainWindow_bank_statement", "Remarks"))
        self.label_2.setText(_translate("MainWindow_bank_statement", "Date"))
        self.pushButton_save.setText(_translate("MainWindow_bank_statement", "Save"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow_bank_statement", "dd/MM/yyyy"))
        self.label_3.setText(_translate("MainWindow_bank_statement", "Transaction Code"))
        self.label_6.setText(_translate("MainWindow_bank_statement", "Balance"))
        self.pushButton_update.setText(_translate("MainWindow_bank_statement", "Update"))
        self.pushButton_cancel.setText(_translate("MainWindow_bank_statement", "Cancel"))
        self.pushButton_refresh.setText(_translate("MainWindow_bank_statement", "Refresh"))
        self.label.setText(_translate("MainWindow_bank_statement", "Bank Statement"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_bank_statement", "#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_bank_statement", "Account Type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_bank_statement", "Date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_bank_statement", "Transaction Code"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow_bank_statement", "Debit"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow_bank_statement", "Credit"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow_bank_statement", "Balance"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow_bank_statement", "Remarks"))
        self.groupBox_2.setTitle(_translate("MainWindow_bank_statement", "Search"))
        self.label_10.setText(_translate("MainWindow_bank_statement", "Account Type"))
        self.label_12.setText(_translate("MainWindow_bank_statement", "Date"))
        self.label_8.setText(_translate("MainWindow_bank_statement", "Search By"))
        self.pushButton_search.setText(_translate("MainWindow_bank_statement", "Search"))
        self.groupBox_3.setTitle(_translate("MainWindow_bank_statement", "View"))
        self.label_11.setText(_translate("MainWindow_bank_statement", "View Records By Account Type"))
        self.pushButton_view.setText(_translate("MainWindow_bank_statement", "View"))

    def assign(self):
        self.pushButton_save.clicked.connect(lambda: self.save())
        self.pushButton_edit.clicked.connect(lambda: self.edit())
        self.pushButton_cancel.clicked.connect(lambda: self.cancel())
        self.pushButton_view.clicked.connect(lambda: self.view())
        self.pushButton_refresh.clicked.connect(lambda: self.refresh())
        self.pushButton_delete.clicked.connect(lambda: self.delete())
        self.pushButton_xlsx.clicked.connect(lambda: self.to_xlsx())
        self.pushButton_update.clicked.connect(lambda: self.update())
        self.pushButton_search.clicked.connect(lambda: self.search())

        self.comboBox_account_type_search.activated.connect(lambda : self.search())
        self.comboBox_date_search.activated.connect(lambda : self.search())
        self.comboBox_search_by.activated.connect(lambda : self.search())
        self.lineEdit_search_by.textEdited.connect(lambda : self.search())

        account_types = ["All", "Savings Account", "FDR"]
        for type in account_types:
            self.comboBox_account_type_search.addItem(type)
            self.comboBox_view_by.addItem(type)

        account_types = ["Savings Account", "FDR"]
        for type in account_types:
            self.comboBox_account_type.addItem(type)

        search_bys = ["Transaction Code", "Remarks"]
        for search_by in search_bys:
            self.comboBox_search_by.addItem(search_by)

        self.refresh()

    def view(self):
        self.tableWidget.clearContents()
        account_type = str(self.comboBox_view_by.currentText())
        if account_type == "All":
            account_type = ""
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = "SELECT oid, * FROM bank_statement WHERE account_type LIKE '%%" + account_type + "%%'"
        try:
            cur.execute(sql)
            items = cur.fetchall()
            conn.commit()
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()

        self.tableWidget.setRowCount(len(items))

        try:
            threading.Thread(target=self.update_table_widget, args=(items,)).start()
            self.statusbar.showMessage(account_type)
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

    def refresh(self):
        self.tableWidget.clearContents()
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = "SELECT oid, * FROM bank_statement"
        try:
            cur.execute(sql)
            items = cur.fetchall()
            conn.commit()
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

        self.tableWidget.setRowCount(len(items))

        try:
            threading.Thread(target=self.update_table_widget, args=(items,)).start()
            self.statusbar.showMessage("")
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

        self.comboBox_date_search.addItem("")

        sql = "SELECT date FROM bank_statement"
        try:
            cur.execute(sql)
            items = cur.fetchall()
            conn.commit()
            for item in items:
                self.comboBox_date_search.addItem(item[0])
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()
        self.comboBox_date_search.setEditable(True)

        self.pushButton_update.setDisabled(True)
        self.pushButton_cancel.setDisabled(True)

    def clear(self):
        self.lineEdit_transaction_code.setText("")
        self.lineEdit_debit.setText("")
        self.lineEdit_credit.setText("")
        self.lineEdit_balance.setText("")
        self.lineEdit_remarks.setText("")

    def save(self):
        try:
            account_type = str(self.comboBox_account_type.currentText())
            date = str(self.dateEdit.text())
            transaction_code = str(self.lineEdit_transaction_code.text())
            debit = int(self.lineEdit_debit.text())
            credit = int(self.lineEdit_credit.text())
            balance = int(self.lineEdit_balance.text())
            remarks = str(self.lineEdit_remarks.text())
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = """INSERT INTO bank_statement VALUES (
        :account_type, 
        :date, 
        :transaction_code, 
        :debit, 
        :credit, 
        :balance, 
        :remarks
        )"""
        try:
            cur.execute(sql, {
                "account_type": account_type,
                "date": date,
                "transaction_code": transaction_code,
                "debit": debit,
                "credit": credit,
                "balance": balance,
                "remarks": remarks
            })
            conn.commit()
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "Success", f"New Bank Statement Saved")
            message.exec_()
            self.clear()
            self.refresh()
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()

    def search(self):
        self.tableWidget.clearContents()
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        try:
            search_by = str(self.comboBox_search_by.currentText())
            key = str(self.lineEdit_search_by.text())
            account_type = str(self.comboBox_account_type_search.currentText())
            date = str(self.comboBox_date_search.currentText())
            if account_type == "All":
                account_type = ""

            if search_by == "Transaction Code":
                sql = "SELECT oid, * FROM bank_statement WHERE transaction_code LIKE '%%" + key + "%%' AND account_type LIKE '%%" + account_type + "%%' AND date LIKE '%%" + date + "%%'"
            elif search_by == "Remarks":
                sql = "SELECT oid, * FROM bank_statement WHERE remarks LIKE '%%" + key + "%%' AND account_type LIKE '%%" + account_type + "%%' AND date LIKE '%%" + date + "%%'"
            else:
                sql = "SELECT oid, * FROM bank_statement WHERE account_type LIKE '%%" + account_type + "%%' AND date LIKE '%%" + date + "%%'"

            cur.execute(sql)
            items = cur.fetchall()
            conn.commit()

            self.tableWidget.setRowCount(len(items))
            threading.Thread(target=self.update_table_widget, args=(items,)).start()

        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()

    def update(self):
        try:
            index = int(self.tableWidget.currentRow())
            oid = str(self.tableWidget.item(index, 0).text())
            account_type = str(self.comboBox_account_type.currentText())
            date = str(self.dateEdit.text())
            transaction_code = str(self.lineEdit_transaction_code.text())
            debit = int(self.lineEdit_debit.text())
            credit = int(self.lineEdit_credit.text())
            balance = int(self.lineEdit_balance.text())
            remarks = str(self.lineEdit_remarks.text())
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = """UPDATE bank_statement SET 
                    account_type = :account_type, 
                    date = :date, 
                    transaction_code = :transaction_code, 
                    debit = :debit, 
                    credit = :credit, 
                    balance = :balance, 
                    remarks = :remarks WHERE oid = :oid
                    """
        try:
            cur.execute(sql, {
                "account_type": account_type,
                "date": date,
                "transaction_code": transaction_code,
                "debit": debit,
                "credit": credit,
                "balance": balance,
                "remarks": remarks,
                "oid": oid
            })
            conn.commit()
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "Success", f"Record Updated")
            message.exec_()
            self.cancel()
            self.refresh()
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()

    def edit(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        try:
            index = int(self.tableWidget.currentRow())
            oid = str(self.tableWidget.item(index, 0).text())
            sql = "SELECT oid, * FROM bank_statement WHERE oid = " + oid
            cur.execute(sql)
            item = cur.fetchone()
            conn.commit()
            print(item)

            self.comboBox_account_type.setCurrentText(str(item[1]))

            dates = datetime.datetime.strptime(item[2], "%d/%m/%Y")
            dates = str(dates.date())
            dates = dates.split("-")
            self.dateEdit.setDate(QtCore.QDate(int(dates[0]), int(dates[1]), int(dates[2])))

            self.lineEdit_transaction_code.setText(str(item[3]))
            self.lineEdit_debit.setText(str(item[4]))
            self.lineEdit_credit.setText(str(item[5]))
            self.lineEdit_balance.setText(str(item[6]))
            self.lineEdit_remarks.setText(str(item[7]))
            self.pushButton_cancel.setDisabled(False)
            self.pushButton_update.setDisabled(False)
            self.pushButton_save.setDisabled(True)
            self.statusbar.showMessage(f"Update Panel Activated")
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()

    def delete(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        try:
            index = self.tableWidget.currentRow()
            i = str(self.tableWidget.item(index, 0).text())
            sql = "DELETE FROM bank_statement WHERE oid = '" + i + "'"
            cur.execute(sql)
            conn.commit()
            threading.Thread(target=self.refresh).start()
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()
            threading.Thread(target=self.refresh).start()

    def to_xlsx(self):
        column_headers = []
        key = self.lineEdit_search_by.text()
        search_by = str(self.comboBox_search_by.currentText())
        account_type = str(self.comboBox_account_type_search.currentText())
        if account_type == "Savings Account":
            if key == "":
                file_name = "RSKT_Bank_Statement_Savings_Account.xlsx"
            else:
                file_name = "RSKT_Bank_Statement_Savings_Account_Search_By_" + search_by + "_" + key + ".xlsx"
        elif account_type == "FDR":
            if key == "":
                file_name = "RSKT_Bank_Statement_FDR.xlsx"
            else:
                file_name = "RSKT_Bank_Statement_FDR_Search_By_" + search_by + "_" + key + ".xlsx"
        else:
            if key == "":
                file_name = "RSKT_Bank_Statement.xlsx"
            else:
                file_name = "RSKT_Bank_Statement_Search_By_" + search_by + "_" + key + ".xlsx"

        try:
            for i in range(self.tableWidget.model().columnCount()):
                column_headers.append(self.tableWidget.horizontalHeaderItem(i).text())
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

        df = pd.DataFrame(columns=column_headers)

        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                df.at[row, column_headers[column]] = self.tableWidget.item(row, column).text()

        try:
            df.to_excel(file_name, index=False)
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "Success", f"Imported to {file_name}")
            message.exec_()
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

    def update_table_widget(self, items):
        for row in range(len(items)):
            for column in range(len(items[row])):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(items[row][column])))

    def cancel(self):
        self.clear()
        self.pushButton_update.setDisabled(True)
        self.pushButton_cancel.setDisabled(True)
        self.pushButton_save.setDisabled(False)

        self.statusbar.showMessage("")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_bank_statement = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_bank_statement()
    ui.setupUi(MainWindow_bank_statement)
    MainWindow_bank_statement.show()
    sys.exit(app.exec_())
