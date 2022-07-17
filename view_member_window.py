import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import datetime
import threading
from update_member_window import Ui_MainWindow_update_member
import pandas as pd


class Ui_MainWindow_view_member(object):
    def setupUi(self, MainWindow_view_member):
        MainWindow_view_member.setObjectName("MainWindow_view_member")
        MainWindow_view_member.resize(1400, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow_view_member)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 8, 3, 1, 1)
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.gridLayout.addWidget(self.pushButton_update, 7, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.gridLayout.addWidget(self.pushButton_refresh, 3, 8, 1, 1)
        self.pushButton_xlsx = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_xlsx.setFont(font)
        self.pushButton_xlsx.setObjectName("pushButton_xlsx")
        self.gridLayout.addWidget(self.pushButton_xlsx, 7, 8, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 9, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 3, 7, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(42)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 8)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
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
        self.gridLayout.addWidget(self.tableWidget, 5, 1, 1, 8)
        spacerItem4 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 6, 3, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 7, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 4, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 0, 0, 1, 1)
        self.comboBox_search_by = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_search_by.setFont(font)
        self.comboBox_search_by.setObjectName("comboBox_search_by")
        self.gridLayout.addWidget(self.comboBox_search_by, 3, 2, 1, 1)
        self.lineEdit_search_by = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_search_by.sizePolicy().hasHeightForWidth())
        self.lineEdit_search_by.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_search_by.setFont(font)
        self.lineEdit_search_by.setObjectName("lineEdit_search_by")
        self.gridLayout.addWidget(self.lineEdit_search_by, 3, 3, 1, 4)
        spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 7, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 7, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 7, 6, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow_view_member.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_view_member)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_view_member)
        MainWindow_view_member.setTabOrder(self.comboBox_search_by, self.lineEdit_search_by)
        MainWindow_view_member.setTabOrder(self.lineEdit_search_by, self.pushButton_search)
        MainWindow_view_member.setTabOrder(self.pushButton_search, self.pushButton_refresh)
        MainWindow_view_member.setTabOrder(self.pushButton_refresh, self.tableWidget)
        MainWindow_view_member.setTabOrder(self.tableWidget, self.pushButton_update)
        MainWindow_view_member.setTabOrder(self.pushButton_update, self.pushButton_delete)
        MainWindow_view_member.setTabOrder(self.pushButton_delete, self.pushButton_xlsx)

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

        self.assign()

    def retranslateUi(self, MainWindow_view_member):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_view_member.setWindowTitle(_translate("MainWindow_view_member", "Member Information"))
        self.pushButton_update.setText(_translate("MainWindow_view_member", "Update"))
        self.label_2.setText(_translate("MainWindow_view_member", "Search By"))
        self.pushButton_refresh.setText(_translate("MainWindow_view_member", "Refresh"))
        self.pushButton_xlsx.setText(_translate("MainWindow_view_member", "To XLSX"))
        self.pushButton_search.setText(_translate("MainWindow_view_member", "Search"))
        self.label.setText(_translate("MainWindow_view_member", "Member Information"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_view_member", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_view_member", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_view_member", "Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_view_member", "Father\'s Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow_view_member", "Profession"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow_view_member", "Workplace"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow_view_member", "Address"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow_view_member", "Phone"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow_view_member", "Remarks"))
        self.pushButton_delete.setText(_translate("MainWindow_view_member", "Delete"))

    def assign(self):
        self.pushButton_update.clicked.connect(lambda : self.update())
        self.pushButton_search.clicked.connect(lambda : self.search())
        self.pushButton_delete.clicked.connect(lambda : self.delete())
        self.pushButton_refresh.clicked.connect(lambda : self.refresh())
        self.pushButton_xlsx.clicked.connect(lambda : self.to_xlsx())
        self.lineEdit_search_by.textChanged.connect(lambda : self.search())

        self.refresh()

        search_bys = ["Name", "ID"]
        for search_by in search_bys:
            self.comboBox_search_by.addItem(search_by)

    def update_table_widget(self, items):
        for row in range(len(items)):
            for column in range(len(items[row])):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(items[row][column])))

    def refresh(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = "SELECT * FROM member"
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

        self.comboBox_search_by.setCurrentText("ID")
        self.lineEdit_search_by.setText("")

    def search(self):
        self.tableWidget.clearContents()

        key = str(self.lineEdit_search_by.text())
        if self.comboBox_search_by.currentText() == "ID":
            sql = "SELECT * FROM member WHERE id = '" + key + "'"
        if self.comboBox_search_by.currentText() == "Name":
            sql = "SELECT * FROM member WHERE name LIKE '%%" + key + "%%'"

        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
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
        threading.Thread(target=self.update_table_widget, args=(items, )).start()

    def update(self):
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        try:
            index = self.tableWidget.currentRow()
            i = str(self.tableWidget.item(index, 0).text())

            sql = "SELECT * FROM member WHERE id = '" + i + "'"
            cur.execute(sql)
            items = cur.fetchone()
            conn.commit()

            self.update_member_window = QtWidgets.QMainWindow()
            self.ui_update_member_window = Ui_MainWindow_update_member()
            self.ui_update_member_window.setupUi(self.update_member_window, self.refresh)
            self.update_member_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
            self.update_member_window.show()

            self.ui_update_member_window.lineEdit_member_id.setText(str(items[0]))

            dates = datetime.datetime.strptime(items[1], "%d/%m/%Y")
            dates = str(dates.date())
            dates = dates.split("-")
            self.ui_update_member_window.dateEdit.setDate(QtCore.QDate(int(dates[0]), int(dates[1]), int(dates[2])))

            self.ui_update_member_window.lineEdit_name.setText(str(items[2]))
            self.ui_update_member_window.lineEdit_father_name.setText(str(items[3]))
            self.ui_update_member_window.lineEdit_profession.setText(str(items[4]))
            self.ui_update_member_window.lineEdit_workplace.setText(str(items[5]))
            self.ui_update_member_window.lineEdit_address.setText(str(items[6]))
            self.ui_update_member_window.lineEdit_phone.setText(str(items[7]))
            self.ui_update_member_window.lineEdit_remarks.setText(str(items[8]))

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
            sql = "DELETE FROM member WHERE id = '" + i + "'"
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
        search_by = self.comboBox_search_by.currentText()
        if key == "":
            file_name = "RSKT_Member_Information.xlsx"
        else:
            file_name = "RSKT_Member_Information_Search_By_" + search_by + "_" + key + ".xlsx"

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
    MainWindow_view_member = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_view_member()
    ui.setupUi(MainWindow_view_member)
    MainWindow_view_member.show()
    sys.exit(app.exec_())
