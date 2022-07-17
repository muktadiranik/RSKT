from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import threading
import pandas as pd


class Ui_MainWindow_annual_report(object):
    def setupUi(self, MainWindow_annual_report):
        MainWindow_annual_report.setObjectName("MainWindow_annual_report")
        MainWindow_annual_report.resize(1600, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow_annual_report)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_xlsx = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_xlsx.setFont(font)
        self.pushButton_xlsx.setObjectName("pushButton_xlsx")
        self.gridLayout.addWidget(self.pushButton_xlsx, 3, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 5, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 3, 2, 1, 1)
        self.pushButton_view = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_view.setFont(font)
        self.pushButton_view.setObjectName("pushButton_view")
        self.gridLayout.addWidget(self.pushButton_view, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(42)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 4)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 5, 1, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow_annual_report.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_annual_report)
        self.statusbar.setObjectName("statusbar")
        MainWindow_annual_report.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_annual_report)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_annual_report)
        MainWindow_annual_report.setTabOrder(self.comboBox, self.pushButton_view)
        MainWindow_annual_report.setTabOrder(self.pushButton_view, self.pushButton_xlsx)
        MainWindow_annual_report.setTabOrder(self.pushButton_xlsx, self.tableWidget)

        self.assign()

    def retranslateUi(self, MainWindow_annual_report):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_annual_report.setWindowTitle(_translate("MainWindow_annual_report", "Annual Report"))
        self.pushButton_xlsx.setText(_translate("MainWindow_annual_report", "To XLSX"))
        self.label_2.setText(_translate("MainWindow_annual_report", "View Report For"))
        self.pushButton_view.setText(_translate("MainWindow_annual_report", "View"))
        self.label.setText(_translate("MainWindow_annual_report", "Annual Report"))

    def assign(self):
        self.pushButton_view.clicked.connect(lambda : self.view())
        self.pushButton_xlsx.clicked.connect(lambda : self.to_xlsx())
        views = ["Due/Current/Advance", "Admit/Fine"]
        for view in views:
            self.comboBox.addItem(view)

        self.view()

    def update_table_widget(self, row_headers, column_headers, items, type):
        for row in range(len(row_headers)):
            for column in range(len(column_headers)):
                total = 0
                for item in items:
                    if row_headers[row][0] == item[1] and column_headers[column] == item[5].split("/")[1]:
                        total = total + item[3]
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(total)))
        self.statusbar.showMessage(type)

    def view(self):
        type = str(self.comboBox.currentText())
        self.tableWidget.clear()

        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = "SELECT * FROM receipt WHERE payment_type = '" + type + "'"
        try:
            cur.execute(sql)
            items = cur.fetchall()
            conn.commit()
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()

        paid_fors = []
        for item in items:
            paid_fors.append(item[5])

        column_headers = [i.split("/")[1] for i in paid_fors]
        column_headers = list(set(column_headers))
        column_headers.sort()

        self.tableWidget.setColumnCount(len(column_headers))
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        tableWidget_header = self.tableWidget.horizontalHeader()

        for i in range(len(column_headers)):
            tableWidget_header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        ids = [i[1] for i in items]
        ids = list(set(ids))
        ids.sort()

        row_headers = []
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        try:
            for i in range(len(ids)):
                sql = "SELECT id, name from member WHERE id = '" + str(ids[i]) + "'"
                cur.execute(sql)
                item = cur.fetchone()
                conn.commit()
                row_headers.append(item)
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()
        finally:
            conn.close()
        self.tableWidget.setRowCount(len(row_headers))
        self.tableWidget.setVerticalHeaderLabels([str(i) + "    " + str(j) for i, j in row_headers])

        threading.Thread(target=self.update_table_widget, args=(row_headers, column_headers, items, type)).start()


    def to_xlsx(self):
        column_headers = []
        row_headers = []
        try:
            for i in range(self.tableWidget.model().columnCount()):
                column_headers.append(self.tableWidget.horizontalHeaderItem(i).text())
            for i in range(self.tableWidget.model().rowCount()):
                row_headers.append(self.tableWidget.verticalHeaderItem(i).text())
        except Exception as e:
            self.statusbar.showMessage(f"{str(e)}")

        df = pd.DataFrame(columns=column_headers, index=row_headers)

        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                df.at[row_headers[row], column_headers[column]] = self.tableWidget.item(row, column).text()
        try:
            df.to_excel("RSKT_Annual_Report.xlsx")
        except Exception as e:
            message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Error", f"{str(e)}")
            message.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_annual_report = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_annual_report()
    ui.setupUi(MainWindow_annual_report)
    MainWindow_annual_report.show()
    sys.exit(app.exec_())
