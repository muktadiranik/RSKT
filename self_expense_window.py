from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import pandas as pd
import threading
import datetime


class Ui_MainWindow_self_expense(object):
    def setupUi(self, MainWindow_self_expense):
        MainWindow_self_expense.setObjectName("MainWindow_self_expense")
        MainWindow_self_expense.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow_self_expense)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 7, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 9, 3, 1, 1)
        self.pushButton_xlsx = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_xlsx.setFont(font)
        self.pushButton_xlsx.setObjectName("pushButton_xlsx")
        self.gridLayout.addWidget(self.pushButton_xlsx, 9, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 9, 1, 1, 1)
        self.pushButton_edit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_edit.setFont(font)
        self.pushButton_edit.setObjectName("pushButton_update_2")
        self.gridLayout.addWidget(self.pushButton_edit, 9, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 8, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 9, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 3, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 0, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 0, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 9, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 6, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 10, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(42)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 6)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 4, 0, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout_2.addWidget(self.pushButton_save, 5, 6, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem11, 2, 1, 1, 1)
        self.lineEdit_remarks = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_remarks.setFont(font)
        self.lineEdit_remarks.setObjectName("lineEdit_remarks")
        self.gridLayout_2.addWidget(self.lineEdit_remarks, 3, 5, 1, 2)
        spacerItem12 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem12, 4, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem13, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 6, 1, 1)
        self.lineEdit_purpose = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_purpose.setFont(font)
        self.lineEdit_purpose.setObjectName("lineEdit_purpose")
        self.gridLayout_2.addWidget(self.lineEdit_purpose, 3, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 3, 1, 2)
        self.lineEdit_amount = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_amount.setFont(font)
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.gridLayout_2.addWidget(self.lineEdit_amount, 3, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 2)
        spacerItem14 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem14, 6, 1, 1, 1)
        self.dateEdit_add = QtWidgets.QDateEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_add.setFont(font)
        self.dateEdit_add.setCalendarPopup(True)
        self.dateEdit_add.setObjectName("dateEdit_add")
        self.gridLayout_2.addWidget(self.dateEdit_add, 3, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem15, 4, 1, 1, 1)
        self.pushButton_update = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.gridLayout_2.addWidget(self.pushButton_update, 5, 5, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem16, 4, 5, 1, 2)
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout_2.addWidget(self.pushButton_cancel, 5, 4, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 4, 1, 1, 6)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_search.sizePolicy().hasHeightForWidth())
        self.pushButton_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout_4.addWidget(self.pushButton_search, 1, 5, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem17, 0, 1, 1, 1)
        self.comboBox_search_by = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_search_by.setFont(font)
        self.comboBox_search_by.setObjectName("comboBox_search_by")
        self.gridLayout_4.addWidget(self.comboBox_search_by, 1, 3, 1, 1)
        self.pushButton_refresh = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_refresh.sizePolicy().hasHeightForWidth())
        self.pushButton_refresh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.gridLayout_4.addWidget(self.pushButton_refresh, 1, 6, 1, 1)
        self.comboBox_date_search = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_date_search.setFont(font)
        self.comboBox_date_search.setObjectName("comboBox_date_search")
        self.gridLayout_4.addWidget(self.comboBox_date_search, 1, 1, 1, 1)
        self.lineEdit_search = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_search.setFont(font)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.gridLayout_4.addWidget(self.lineEdit_search, 1, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem18, 2, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem19, 2, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem20, 2, 3, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem21, 2, 5, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem22, 2, 6, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 5, 1, 1, 6)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.gridLayout.addWidget(self.tableWidget, 7, 1, 1, 6)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow_self_expense.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_self_expense)
        self.statusbar.setObjectName("statusbar")
        MainWindow_self_expense.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_self_expense)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_self_expense)
        MainWindow_self_expense.setTabOrder(self.dateEdit_add, self.lineEdit_purpose)
        MainWindow_self_expense.setTabOrder(self.lineEdit_purpose, self.lineEdit_amount)
        MainWindow_self_expense.setTabOrder(self.lineEdit_amount, self.lineEdit_remarks)
        MainWindow_self_expense.setTabOrder(self.lineEdit_remarks, self.pushButton_cancel)
        MainWindow_self_expense.setTabOrder(self.pushButton_cancel, self.pushButton_update)
        MainWindow_self_expense.setTabOrder(self.pushButton_update, self.pushButton_save)
        MainWindow_self_expense.setTabOrder(self.pushButton_save, self.comboBox_date_search)
        MainWindow_self_expense.setTabOrder(self.comboBox_date_search, self.comboBox_search_by)
        MainWindow_self_expense.setTabOrder(self.comboBox_search_by, self.lineEdit_search)
        MainWindow_self_expense.setTabOrder(self.lineEdit_search, self.pushButton_search)
        MainWindow_self_expense.setTabOrder(self.pushButton_search, self.pushButton_refresh)
        MainWindow_self_expense.setTabOrder(self.pushButton_refresh, self.tableWidget)
        MainWindow_self_expense.setTabOrder(self.tableWidget, self.pushButton_edit)
        MainWindow_self_expense.setTabOrder(self.pushButton_edit, self.pushButton_delete)
        MainWindow_self_expense.setTabOrder(self.pushButton_delete, self.pushButton_xlsx)

        tableWidget_header = self.tableWidget.horizontalHeader()
        tableWidget_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        tableWidget_header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        tableWidget_header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)

        self.assign()

    def retranslateUi(self, MainWindow_self_expense):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_self_expense.setWindowTitle(_translate("MainWindow_self_expense", "Self Expense"))
        self.pushButton_xlsx.setText(_translate("MainWindow_self_expense", "To XLSX"))
        self.pushButton_edit.setText(_translate("MainWindow_self_expense", "Edit"))
        self.pushButton_delete.setText(_translate("MainWindow_self_expense", "Delete"))
        self.label.setText(_translate("MainWindow_self_expense", "Self Expense"))
        self.groupBox.setTitle(_translate("MainWindow_self_expense", "Add New Expense"))
        self.label_2.setText(_translate("MainWindow_self_expense", "Date"))
        self.pushButton_save.setText(_translate("MainWindow_self_expense", "Save"))
        self.label_5.setText(_translate("MainWindow_self_expense", "Remarks"))
        self.label_4.setText(_translate("MainWindow_self_expense", "Amount"))
        self.label_3.setText(_translate("MainWindow_self_expense", "Purpose"))
        self.dateEdit_add.setDisplayFormat(_translate("MainWindow_self_expense", "dd/MM/yyyy"))
        self.pushButton_update.setText(_translate("MainWindow_self_expense", "Update"))
        self.pushButton_cancel.setText(_translate("MainWindow_self_expense", "Cancel"))
        self.groupBox_2.setTitle(_translate("MainWindow_self_expense", "Search"))
        self.label_6.setText(_translate("MainWindow_self_expense", "Date"))
        self.pushButton_search.setText(_translate("MainWindow_self_expense", "Search"))
        self.pushButton_refresh.setText(_translate("MainWindow_self_expense", "Refresh"))
        self.label_7.setText(_translate("MainWindow_self_expense", "Search By"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_self_expense", "#"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_self_expense", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_self_expense", "Purpose"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_self_expense", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow_self_expense", "Remarks"))

    def assign(self):
        self.pushButton_update.clicked.connect(lambda : self.update())
        self.pushButton_search.clicked.connect(lambda : self.search())
        self.pushButton_cancel.clicked.connect(lambda : self.cancel())
        self.pushButton_refresh.clicked.connect(lambda : self.refresh())
        self.pushButton_delete.clicked.connect(lambda : self.delete())
        self.pushButton_edit.clicked.connect(lambda : self.edit())
        self.pushButton_save.clicked.connect(lambda : self.save())
        self.pushButton_xlsx.clicked.connect(lambda : self.to_xlsx())

        self.comboBox_date_search.activated.connect(lambda : self.search())
        self.comboBox_search_by.activated.connect(lambda : self.search())
        self.lineEdit_search.textEdited.connect(lambda : self.search())

        self.pushButton_update.setDisabled(True)
        self.pushButton_cancel.setDisabled(True)

        search_bys = ["Purpose", "Remarks"]
        for search_by in search_bys:
            self.comboBox_search_by.addItem(search_by)

        self.refresh()

    def search(self):
        self.tableWidget.clearContents()
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        try:
            search_by = str(self.comboBox_search_by.currentText())
            key = str(self.lineEdit_search.text())
            date = str(self.comboBox_date_search.currentText())
            if key == "":
                sql = "SELECT oid, * FROM self_expense WHERE date LIKE '%%" + date + "%%'"
            else:
                if search_by == "Purpose":
                    sql = "SELECT oid, * FROM self_expense WHERE date LIKE '%%" + date + "%%' AND purpose LIKE '%%" + key + "%%'"
                else:
                    sql = "SELECT oid, * FROM self_expense WHERE date LIKE '%%" + date + "%%' AND remarks LIKE '%%" + key + "%%'"
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

    def cancel(self):
        self.clear()
        self.pushButton_update.setDisabled(True)
        self.pushButton_cancel.setDisabled(True)
        self.pushButton_save.setDisabled(False)

        self.statusbar.showMessage("")

    def update(self):
        try:
            index = int(self.tableWidget.currentRow())
            oid = str(self.tableWidget.item(index, 0).text())
            date = str(self.dateEdit_add.text())
            purpose = str(self.lineEdit_purpose.text())
            amount = int(self.lineEdit_amount.text())
            remarks = str(self.lineEdit_remarks.text())
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = """UPDATE self_expense SET 
                    date = :date, 
                    purpose = :purpose, 
                    amount = :amount, 
                    remarks = :remarks WHERE oid = :oid
                    """
        try:
            cur.execute(sql, {
                "date": date,
                "purpose": purpose,
                "amount": amount,
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

    def save(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = """INSERT INTO self_expense VALUES (
                        :date, 
                        :purpose, 
                        :amount, 
                        :remarks
                        )"""
        try:
            date = str(self.dateEdit_add.text())
            purpose = str(self.lineEdit_purpose.text())
            amount = int(self.lineEdit_amount.text())
            remarks = str(self.lineEdit_remarks.text())
            cur.execute(sql, {
                "date": date,
                "purpose": purpose,
                "amount": amount,
                "remarks": remarks
            })
            conn.commit()
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, "Success", f"Record Saved")
            message.exec()
            threading.Thread(target=self.refresh).start()
            self.clear()

        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "error", f"{str(e)}")
            message.exec()
        finally:
            conn.close()

    def clear(self):
        self.lineEdit_purpose.setText("")
        self.lineEdit_amount.setText("")
        self.lineEdit_remarks.setText("")

    def refresh(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = "SELECT oid, * FROM self_expense"
        try:
            cur.execute(sql)
            items = cur.fetchall()
            conn.commit()
            self.tableWidget.setRowCount(len(items))
            threading.Thread(target=self.update_table_widget, args=(items, )).start()
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "error", f"{str(e)}")
            message.exec()

        self.comboBox_date_search.clear()
        self.comboBox_date_search.addItem("")
        self.comboBox_date_search.setEditable(True)

        sql = "SELECT date FROM self_expense"
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

    def edit(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        try:
            index = self.tableWidget.currentRow()
            i = str(self.tableWidget.item(index, 0).text())

            sql = "SELECT * FROM self_expense WHERE oid = '" + i + "'"
            cur.execute(sql)
            items = cur.fetchone()
            conn.commit()
            self.pushButton_save.setDisabled(True)
            self.pushButton_cancel.setDisabled(False)
            self.pushButton_update.setDisabled(False)

            dates = datetime.datetime.strptime(items[0], "%d/%m/%Y")
            dates = str(dates.date())
            dates = dates.split("-")
            self.dateEdit_add.setDate(QtCore.QDate(int(dates[0]), int(dates[1]), int(dates[2])))

            self.lineEdit_purpose.setText(str(items[1]))
            self.lineEdit_amount.setText(str(items[2]))
            self.lineEdit_remarks.setText(str(items[3]))

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
            sql = "DELETE FROM self_expense WHERE oid = '" + i + "'"
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
        key = self.lineEdit_search.text()
        search_by = str(self.comboBox_search_by.currentText())

        if key == "":
            file_name = "RSKT_Self_Expense.xlsx"
        else:
            file_name = "RSKT_Self_Expense_Search_By_" + search_by + "_" + key + ".xlsx"

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_self_expense = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_self_expense()
    ui.setupUi(MainWindow_self_expense)
    MainWindow_self_expense.show()
    sys.exit(app.exec_())
