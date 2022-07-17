import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from add_income_expense_window import Ui_MainWindow_add_income_expense
from update_income_expense_window import Ui_MainWindow_update_income_expense
import threading
import pandas as pd


class Ui_MainWindow_income_expense(object):
    def setupUi(self, MainWindow_income_expense):
        MainWindow_income_expense.setObjectName("MainWindow_income_expense")
        MainWindow_income_expense.resize(1400, 800)
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
        self.pushButton_xlsx = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_xlsx.setFont(font)
        self.pushButton_xlsx.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_xlsx, 7, 6, 1, 1)
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
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_delete, 7, 3, 1, 1)
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
        MainWindow_income_expense.setTabOrder(self.pushButton_update, self.pushButton_delete)
        MainWindow_income_expense.setTabOrder(self.pushButton_delete, self.pushButton_refresh)
        MainWindow_income_expense.setTabOrder(self.pushButton_refresh, self.pushButton_xlsx)

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

    def retranslateUi(self, MainWindow_income_expense):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_income_expense.setWindowTitle(_translate("MainWindow_income_expense", "Income Expense Miscellaneous"))
        self.label.setText(_translate("MainWindow_income_expense", "Income Expense Miscellaneous"))
        self.pushButton_xlsx.setText(_translate("MainWindow_income_expense", "To XLSX"))
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
        self.pushButton_delete.setText(_translate("MainWindow_income_expense", "Delete"))
        self.pushButton_refresh.setText(_translate("MainWindow_income_expense", "Refresh"))

    def assign(self):
        self.pushButton_update.clicked.connect(lambda : self.update())
        self.pushButton_search.clicked.connect(lambda : self.search())
        self.pushButton_xlsx.clicked.connect(lambda : self.to_xlsx())
        self.pushButton_delete.clicked.connect(lambda : self.delete())
        self.pushButton_refresh.clicked.connect(lambda : self.refresh())
        self.pushButton_add.clicked.connect(lambda : self.open_add_income_expense_window())

        self.lineEdit_search_by.textEdited.connect(lambda : self.search())

        self.refresh()

    def refresh(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = "SELECT oid, * FROM income_expense"
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
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

    def update_table_widget(self, items):
        for row in range(len(items)):
            for column in range(len(items[row])):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(items[row][column])))

    def open_add_income_expense_window(self):
        self.add_income_expense_window = QtWidgets.QMainWindow()
        self.ui_add_income_expense = Ui_MainWindow_add_income_expense()
        self.ui_add_income_expense.setupUi(self.add_income_expense_window, self.refresh)
        self.add_income_expense_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.add_income_expense_window.show()

    def delete(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        try:
            index = self.tableWidget.currentRow()
            i = str(self.tableWidget.item(index, 0).text())
            sql = "DELETE FROM income_expense WHERE oid = '" + i + "'"
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
        if key == "":
            file_name = "RSKT_Income_Expense_Miscellaneous.xlsx"
        else:
            file_name = "RSKT_Member_Information_Search_By_year_" + key + ".xlsx"

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

    def update(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        try:
            index = int(self.tableWidget.currentRow())
            oid = str(self.tableWidget.item(index, 0).text())
            sql = "SELECT oid, * FROM income_expense WHERE oid = " + oid
            cur.execute(sql)
            item = cur.fetchone()
            conn.commit()
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()

        try:
            self.update_income_expense_window = QtWidgets.QMainWindow()
            self.ui_update_income_expense_window = Ui_MainWindow_update_income_expense()
            self.ui_update_income_expense_window.setupUi(self.update_income_expense_window, self.refresh, oid)
            self.update_income_expense_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self.update_income_expense_window.show()

            self.ui_update_income_expense_window.comboBox_year.addItem(item[1])
            self.ui_update_income_expense_window.lineEdit_monthly_contribution.setText(str(item[2]))
            self.ui_update_income_expense_window.lineEdit_admit_fine.setText(str(item[3]))
            self.ui_update_income_expense_window.lineEdit_form.setText(str(item[4]))
            self.ui_update_income_expense_window.lineEdit_donation.setText(str(item[5]))
            self.ui_update_income_expense_window.lineEdit_death_allowance.setText(str(item[6]))
            self.ui_update_income_expense_window.lineEdit_disaster_allowance.setText(str(item[7]))
            self.ui_update_income_expense_window.lineEdit_miscellaneous.setText(str(item[8]))
            self.ui_update_income_expense_window.lineEdit_previous_balance.setText(str(item[9]))
            self.ui_update_income_expense_window.lineEdit_new_balance.setText(str(item[10]))
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()

    def search(self):
        self.tableWidget.clearContents()
        key = str(self.lineEdit_search_by.text())
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = "SELECT oid, * FROM income_expense WHERE year LIKE '%%" + key + "%%'"
        try:
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_income_expense = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_income_expense()
    ui.setupUi(MainWindow_income_expense)
    MainWindow_income_expense.show()
    sys.exit(app.exec_())
