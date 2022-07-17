import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
import threading
from update_receipt_window import Ui_MainWindow_update_receipt
import pandas as pd


class Ui_MainWindow_view_receipt(object):
    def setupUi(self, MainWindow_view_receipt):
        MainWindow_view_receipt.setObjectName("MainWindow_view_receipt")
        MainWindow_view_receipt.resize(1400, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow_view_receipt)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.comboBox_search_by = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_search_by.sizePolicy().hasHeightForWidth())
        self.comboBox_search_by.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_search_by.setFont(font)
        self.comboBox_search_by.setObjectName("comboBox_search_by")
        self.gridLayout.addWidget(self.comboBox_search_by, 5, 2, 1, 2)
        self.comboBox_type = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_type.sizePolicy().hasHeightForWidth())
        self.comboBox_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_type.setFont(font)
        self.comboBox_type.setObjectName("comboBox_type")
        self.gridLayout.addWidget(self.comboBox_type, 3, 9, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 11, 1, 1)
        self.comboBox_paid_for = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_paid_for.sizePolicy().hasHeightForWidth())
        self.comboBox_paid_for.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_paid_for.setFont(font)
        self.comboBox_paid_for.setObjectName("comboBox_paid_for")
        self.gridLayout.addWidget(self.comboBox_paid_for, 3, 7, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 10, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 4, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(42)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 11)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 9, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 8, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 2, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_search.sizePolicy().hasHeightForWidth())
        self.pushButton_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 5, 8, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 8, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 10, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 11, 2, 1, 1)
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_refresh.sizePolicy().hasHeightForWidth())
        self.pushButton_refresh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.gridLayout.addWidget(self.pushButton_refresh, 5, 10, 1, 2)
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_update.sizePolicy().hasHeightForWidth())
        self.pushButton_update.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.gridLayout.addWidget(self.pushButton_update, 10, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem10, 6, 1, 1, 1)
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
        self.gridLayout.addWidget(self.tableWidget, 8, 1, 1, 11)
        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 5, 12, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 2, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 3, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 2, 7, 1, 1)
        self.comboBox_date = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_date.sizePolicy().hasHeightForWidth())
        self.comboBox_date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_date.setFont(font)
        self.comboBox_date.setObjectName("comboBox_date")
        self.gridLayout.addWidget(self.comboBox_date, 3, 2, 1, 2)
        spacerItem15 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 2, 9, 1, 1)
        self.lineEdit_search_by = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_search_by.setFont(font)
        self.lineEdit_search_by.setObjectName("lineEdit_search_by")
        self.gridLayout.addWidget(self.lineEdit_search_by, 5, 4, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 4, 1, 3)
        spacerItem16 = QtWidgets.QSpacerItem(160, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem16, 10, 5, 1, 1)
        self.pushButton_xlsx = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_xlsx.sizePolicy().hasHeightForWidth())
        self.pushButton_xlsx.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_xlsx.setFont(font)
        self.pushButton_xlsx.setObjectName("pushButton_xlsx")
        self.gridLayout.addWidget(self.pushButton_xlsx, 10, 9, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow_view_receipt.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_view_receipt)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_view_receipt)
        MainWindow_view_receipt.setTabOrder(self.comboBox_date, self.comboBox_paid_for)
        MainWindow_view_receipt.setTabOrder(self.comboBox_paid_for, self.comboBox_type)
        MainWindow_view_receipt.setTabOrder(self.comboBox_type, self.comboBox_search_by)
        MainWindow_view_receipt.setTabOrder(self.comboBox_search_by, self.lineEdit_search_by)
        MainWindow_view_receipt.setTabOrder(self.lineEdit_search_by, self.pushButton_search)
        MainWindow_view_receipt.setTabOrder(self.pushButton_search, self.pushButton_refresh)
        MainWindow_view_receipt.setTabOrder(self.pushButton_refresh, self.tableWidget)
        MainWindow_view_receipt.setTabOrder(self.tableWidget, self.pushButton_update)
        MainWindow_view_receipt.setTabOrder(self.pushButton_update, self.pushButton_delete)
        MainWindow_view_receipt.setTabOrder(self.pushButton_delete, self.pushButton_xlsx)

        tableWidget_header = self.tableWidget.horizontalHeader()
        tableWidget_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        tableWidget_header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)

        self.assign()

    def retranslateUi(self, MainWindow_view_receipt):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_view_receipt.setWindowTitle(_translate("MainWindow_view_receipt", "Vouchers Information"))
        self.pushButton_delete.setText(_translate("MainWindow_view_receipt", "Delete"))
        self.label_2.setText(_translate("MainWindow_view_receipt", "Date"))
        self.label.setText(_translate("MainWindow_view_receipt", "Vouchers Information"))
        self.label_5.setText(_translate("MainWindow_view_receipt", "Type"))
        self.pushButton_search.setText(_translate("MainWindow_view_receipt", "Search"))
        self.pushButton_refresh.setText(_translate("MainWindow_view_receipt", "Refresh"))
        self.pushButton_update.setText(_translate("MainWindow_view_receipt", "Update"))
        self.label_4.setText(_translate("MainWindow_view_receipt", "Search By"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_view_receipt", "#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_view_receipt", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_view_receipt", "Member ID"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_view_receipt", "Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow_view_receipt", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow_view_receipt", "Type"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow_view_receipt", "Paid For"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow_view_receipt", "Method"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow_view_receipt", "Reference"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow_view_receipt", "Remarks"))
        self.label_3.setText(_translate("MainWindow_view_receipt", "Paid For (MM/yyyy)"))
        self.pushButton_xlsx.setText(_translate("MainWindow_view_receipt", "To XLSX"))

    def assign(self):
        self.pushButton_refresh.clicked.connect(lambda : self.refresh())
        self.pushButton_search.clicked.connect(lambda : self.search())
        self.pushButton_update.clicked.connect(lambda : self.update())
        self.pushButton_delete.clicked.connect(lambda : self.delete())
        self.pushButton_xlsx.clicked.connect(lambda : self.to_xlsx())

        self.comboBox_date.activated.connect(lambda : self.search())
        self.comboBox_type.activated.connect(lambda : self.search())
        self.comboBox_paid_for.activated.connect(lambda : self.search())
        self.comboBox_search_by.activated.connect(lambda : self.search())
        self.lineEdit_search_by.textEdited.connect(lambda : self.search())

        types = ["Due/Current/Advance", "Admit/Fine", "All"]
        for type in types:
            self.comboBox_type.addItem(type)



        search_bys = ["Name", "ID", "Reference"]
        for search_by in search_bys:
            self.comboBox_search_by.addItem(search_by)

        self.refresh()

    def update_table_widget(self, items):
        for row in range(len(items)):
            for column in range(len(items[row])):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(items[row][column])))

    def refresh(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = "SELECT oid, * FROM receipt WHERE payment_type = 'Due/Current/Advance'"
        try:
            cur.execute(sql)
            items = cur.fetchall()
            conn.commit()
            self.tableWidget.setRowCount(len(items))
            threading.Thread(target=self.update_table_widget, args=(items, )).start()

        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

        sql = "SELECT date FROM receipt"
        try:
            cur.execute(sql)
            dates = cur.fetchall()
            conn.commit()
            self.comboBox_date.setEditable(True)
            self.comboBox_date.addItem("")
            for date in dates:
                self.comboBox_date.addItem(date[0])
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

        sql = "SELECT paid_for FROM receipt"
        try:
            cur.execute(sql)
            paid_fors = cur.fetchall()
            conn.commit()
            self.comboBox_paid_for.setEditable(True)
            self.comboBox_paid_for.addItem("")
            for paid_for in paid_fors:
                self.comboBox_paid_for.addItem(paid_for[0])
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()

        self.comboBox_search_by.setCurrentText("Name")
        self.comboBox_paid_for.setCurrentText("")
        self.comboBox_date.setCurrentText("")
        self.comboBox_type.setCurrentText("Due/Current/Advance")

    def search(self):
        self.tableWidget.clearContents()

        date = str(self.comboBox_date.currentText())
        paid_for = str(self.comboBox_paid_for.currentText())
        type = str(self.comboBox_type.currentText())
        search_by = str(self.comboBox_search_by.currentText())
        search_key = str(self.lineEdit_search_by.text())

        if type == "Due/Current/Advance":
            if search_by == "ID":
                sql = """SELECT oid, * FROM receipt WHERE 
                date LIKE '%%""" + date + """%%' AND 
                paid_for LIKE '%%""" + paid_for + """%%' AND 
                member_id = '""" + search_key + """' AND 
                payment_type = 'Due/Current/Advance'"""
            if search_by == "Name":
                sql = """SELECT oid, * FROM receipt WHERE 
                date LIKE '%%""" + date + """%%' AND 
                paid_for LIKE '%%""" + paid_for + """%%' AND 
                member_name LIKE '%%""" + search_key + """%%' AND 
                payment_type = 'Due/Current/Advance'"""
            if search_by == "Reference":
                sql = """SELECT oid, * FROM receipt WHERE 
                date LIKE '%%""" + date + """%%' AND 
                paid_for LIKE '%%""" + paid_for + """%%' AND 
                reference LIKE '%%""" + search_key + """%%' AND 
                payment_type = 'Due/Current/Advance'"""
        elif type == "Admit/Fine":
            if search_by == "ID":
                sql = """SELECT oid, * FROM receipt WHERE 
                        date LIKE '%%""" + date + """%%' AND 
                        paid_for LIKE '%%""" + paid_for + """%%' AND 
                        member_id = '""" + search_key + """' AND 
                        payment_type = 'Admit/Fine'"""
            if search_by == "Name":
                sql = """SELECT oid, * FROM receipt WHERE 
                        date LIKE '%%""" + date + """%%' AND 
                        paid_for LIKE '%%""" + paid_for + """%%' AND 
                        member_name LIKE '%%""" + search_key + """%%' AND 
                        payment_type = 'Admit/Fine'"""
            if search_by == "Reference":
                sql = """SELECT oid, * FROM receipt WHERE 
                        date LIKE '%%""" + date + """%%' AND 
                        paid_for LIKE '%%""" + paid_for + """%%' AND 
                        reference LIKE '%%""" + search_key + """%%' AND 
                        payment_type = 'Admit/Fine'"""
        elif type == "All":
            if search_by == "ID":
                sql = """SELECT oid, * FROM receipt WHERE 
                        date LIKE '%%""" + date + """%%' AND 
                        paid_for LIKE '%%""" + paid_for + """%%' AND 
                        member_id = '""" + search_key + """'"""
            if search_by == "Name":
                sql = """SELECT oid, * FROM receipt WHERE 
                        date LIKE '%%""" + date + """%%' AND 
                        paid_for LIKE '%%""" + paid_for + """%%' AND 
                        member_name LIKE '%%""" + search_key + """%%'"""
            if search_by == "Reference":
                sql = """SELECT oid, * FROM receipt WHERE 
                        date LIKE '%%""" + date + """%%' AND 
                        paid_for LIKE '%%""" + paid_for + """%%' AND 
                        member_name LIKE '%%""" + search_key + """%%'"""

        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()

        try:
            cur.execute(sql)
            items = cur.fetchall()
            conn.commit()
            self.tableWidget.setRowCount(len(items))
            threading.Thread(target=self.update_table_widget, args=(items, )).start()

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
            oid = str(self.tableWidget.item(index, 0).text())
            sql = "DELETE FROM receipt WHERE oid = '" + oid + "'"
            cur.execute(sql)
            conn.commit()
            threading.Thread(target=self.refresh).start()
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()
            threading.Thread(target=self.refresh).start()

    def update(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        try:
            index = self.tableWidget.currentRow()
            oid = str(self.tableWidget.item(index, 0).text())

            sql = "SELECT oid, * FROM receipt WHERE oid = '" + oid + "'"
            cur.execute(sql)
            items = cur.fetchone()
            conn.commit()

            self.update_receipt_window = QtWidgets.QMainWindow()
            self.ui_update_receipt_window = Ui_MainWindow_update_receipt()
            self.ui_update_receipt_window.setupUi(self.update_receipt_window, self.refresh, oid)
            self.update_receipt_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self.update_receipt_window.show()

            dates = datetime.datetime.strptime(items[1], "%d/%m/%Y")
            dates = str(dates.date())
            dates = dates.split("-")
            self.ui_update_receipt_window.dateEdit_entry_date.setDate(QtCore.QDate(int(dates[0]), int(dates[1]), int(dates[2])))

            self.ui_update_receipt_window.comboBox_member_id.addItem(str(items[2]))
            self.ui_update_receipt_window.lineEdit_member_name.setText(str(items[3]))
            self.ui_update_receipt_window.lineEdit_amount.setText(str(items[4]))
            self.ui_update_receipt_window.comboBox_type.setCurrentText(str(items[5]))

            paid_for = datetime.datetime.strptime(items[6], "%m/%Y")
            paid_for = str(paid_for.date())
            paid_for = paid_for.split("-")
            self.ui_update_receipt_window.dateEdit_paid_for.setDate(QtCore.QDate(int(paid_for[0]), int(paid_for[1]), int(dates[2])))

            self.ui_update_receipt_window.comboBox_method.setCurrentText(str(items[7]))
            self.ui_update_receipt_window.lineEdit_receipt_number.setText(str(items[8]))
            self.ui_update_receipt_window.lineEdit_remarks.setText(str(items[9]))

        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()

    def to_xlsx(self):
        column_headers = []
        key = self.lineEdit_search_by.text()
        search_by = self.comboBox_search_by.currentText()
        type = str(self.comboBox_type.currentText())
        if type == "Due/Current/Advance":
            if key == "":
                file_name = "RSKT_Vouchers_Information_Due_Current_Advance.xlsx"
            else:
                file_name = "RSKT_Vouchers_Information_Due_Current_Advance_Search_By_" + search_by + "_" + key + ".xlsx"
        elif type == "Admit/Fine":
            if key == "":
                file_name = "RSKT_Vouchers_Information_Admit_Fine.xlsx"
            else:
                file_name = "RSKT_Vouchers_Information_Admit_Fine_Search_By_" + search_by + "_" + key + ".xlsx"
        else:
            if key == "":
                file_name = "RSKT_Vouchers_Information.xlsx"
            else:
                file_name = "RSKT_Vouchers_Information_Search_By_" + search_by + "_" + key + ".xlsx"
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_view_receipt()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
