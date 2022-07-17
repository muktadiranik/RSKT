from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import qdarkstyle
from add_member_window import Ui_MainWindow_add_member
from receipt_entry_window import Ui_MainWindow_receipt_entry
from view_member_window import Ui_MainWindow_view_member
from view_receipt_window import Ui_MainWindow_view_receipt
from annual_report_window import Ui_MainWindow_annual_report
from income_expense_window import Ui_MainWindow_income_expense
from bank_statement_window import Ui_MainWindow_bank_statement
from self_expense_window import Ui_MainWindow_self_expense


class Ui_MainWindow_splash_screen(object):
    def setupUi(self, MainWindow_splash_screen):
        MainWindow_splash_screen.setObjectName("MainWindow_splash_screen")
        MainWindow_splash_screen.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow_splash_screen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(80)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow_splash_screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_splash_screen)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_splash_screen)

        MainWindow_splash_screen.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

    def retranslateUi(self, MainWindow_splash_screen):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_splash_screen.setWindowTitle(_translate("MainWindow_splash_screen", "MainWindow"))
        self.label.setText(_translate("MainWindow_splash_screen", "RSKT"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.commandLinkButton_annual_report = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_annual_report.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_annual_report.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton_annual_report.setFont(font)
        self.commandLinkButton_annual_report.setAutoFillBackground(True)
        self.commandLinkButton_annual_report.setObjectName("commandLinkButton_5")
        self.gridLayout.addWidget(self.commandLinkButton_annual_report, 7, 1, 1, 1)
        self.commandLinkButton_bank_statement = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_bank_statement.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_bank_statement.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton_bank_statement.setFont(font)
        self.commandLinkButton_bank_statement.setAutoFillBackground(True)
        self.commandLinkButton_bank_statement.setObjectName("commandLinkButton_3")
        self.gridLayout.addWidget(self.commandLinkButton_bank_statement, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.commandLinkButton_add_member = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_add_member.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_add_member.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton_add_member.setFont(font)
        self.commandLinkButton_add_member.setAutoFillBackground(True)
        self.commandLinkButton_add_member.setObjectName("commandLinkButton_8")
        self.gridLayout.addWidget(self.commandLinkButton_add_member, 9, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 8, 1, 1, 1)
        self.commandLinkButton_self_expense = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_self_expense.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_self_expense.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton_self_expense.setFont(font)
        self.commandLinkButton_self_expense.setAutoFillBackground(True)
        self.commandLinkButton_self_expense.setObjectName("commandLinkButton_6")
        self.gridLayout.addWidget(self.commandLinkButton_self_expense, 7, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 2, 1, 1)
        self.commandLinkButton_receipt_entry = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_receipt_entry.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_receipt_entry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton_receipt_entry.setFont(font)
        self.commandLinkButton_receipt_entry.setAutoFillBackground(True)
        self.commandLinkButton_receipt_entry.setObjectName("commandLinkButton")
        self.gridLayout.addWidget(self.commandLinkButton_receipt_entry, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 10, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 4, 1, 1, 1)
        self.commandLinkButton_view_member = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_view_member.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_view_member.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton_view_member.setFont(font)
        self.commandLinkButton_view_member.setAutoFillBackground(True)
        self.commandLinkButton_view_member.setObjectName("commandLinkButton_7")
        self.gridLayout.addWidget(self.commandLinkButton_view_member, 9, 1, 1, 1)
        self.commandLinkButton_income_expense = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_income_expense.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_income_expense.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton_income_expense.setFont(font)
        self.commandLinkButton_income_expense.setAutoFillBackground(True)
        self.commandLinkButton_income_expense.setObjectName("commandLinkButton_4")
        self.gridLayout.addWidget(self.commandLinkButton_income_expense, 5, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 2, 1, 1, 1)
        self.commandLinkButton_view_voucher = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_view_voucher.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_view_voucher.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton_view_voucher.setFont(font)
        self.commandLinkButton_view_voucher.setAutoFillBackground(True)
        self.commandLinkButton_view_voucher.setObjectName("commandLinkButton_2")
        self.gridLayout.addWidget(self.commandLinkButton_view_voucher, 3, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 3, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.commandLinkButton_receipt_entry, self.commandLinkButton_view_voucher)
        MainWindow.setTabOrder(self.commandLinkButton_view_voucher, self.commandLinkButton_bank_statement)
        MainWindow.setTabOrder(self.commandLinkButton_bank_statement, self.commandLinkButton_income_expense)
        MainWindow.setTabOrder(self.commandLinkButton_income_expense, self.commandLinkButton_annual_report)
        MainWindow.setTabOrder(self.commandLinkButton_annual_report, self.commandLinkButton_self_expense)
        MainWindow.setTabOrder(self.commandLinkButton_self_expense, self.commandLinkButton_view_member)
        MainWindow.setTabOrder(self.commandLinkButton_view_member, self.commandLinkButton_add_member)

        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.assign()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSKT"))
        self.commandLinkButton_annual_report.setText(_translate("MainWindow", "Annual Report"))
        self.commandLinkButton_bank_statement.setText(_translate("MainWindow", "Bank Statement"))
        self.commandLinkButton_add_member.setText(_translate("MainWindow", "Add Member"))
        self.commandLinkButton_self_expense.setText(_translate("MainWindow", "Self Expense"))
        self.commandLinkButton_receipt_entry.setText(_translate("MainWindow", "Voucher Entry"))
        self.label.setText(_translate("MainWindow", "RSKT"))
        self.commandLinkButton_view_member.setText(_translate("MainWindow", "View Members"))
        self.commandLinkButton_income_expense.setText(_translate("MainWindow", "Income Expense Miscellaneous"))
        self.commandLinkButton_view_voucher.setText(_translate("MainWindow", "View Vouchers"))

    def assign(self):
        self.commandLinkButton_add_member.clicked.connect(lambda : self.open_add_member_window())
        self.commandLinkButton_receipt_entry.clicked.connect(lambda : self.open_receipt_entry_window())
        self.commandLinkButton_view_member.clicked.connect(lambda : self.open_view_member_window())
        self.commandLinkButton_view_voucher.clicked.connect(lambda : self.open_view_receipt_window())
        self.commandLinkButton_annual_report.clicked.connect(lambda : self.open_annual_report_window())
        self.commandLinkButton_income_expense.clicked.connect(lambda : self.open_income_expense_window())
        self.commandLinkButton_bank_statement.clicked.connect(lambda : self.open_bank_statement_window())
        self.commandLinkButton_self_expense.clicked.connect(lambda : self.open_self_expense_window())

        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        sql = """CREATE TABLE if not exists member (
                id INTEGER PRIMARY KEY, 
                date TEXT, 
                name TEXT, 
                father_name TEXT, 
                profession TEXT, 
                workplace TEXT, 
                address TEXT, 
                phone TEXT, 
                remarks TEXT                
                )"""
        cur.execute(sql)
        conn.commit()

        sql = """CREATE TABLE if not exists receipt (
                date TEXT, 
                member_id INTEGER, 
                member_name TEXT, 
                amount INTEGER, 
                payment_type TEXT, 
                paid_for TEXT, 
                payment_method TEXT, 
                reference TEXT, 
                remarks TEXT
                )"""
        cur.execute(sql)
        conn.commit()

        sql = """CREATE TABLE if not exists income_expense (
                        year TEXT, 
                        monthly_contribution INTEGER, 
                        admit_fine INTEGER, 
                        form INTEGER, 
                        donation INTEGER, 
                        death_allowance INTEGER, 
                        disaster_allowance INTEGER, 
                        miscellaneous INTEGER, 
                        previous_balance INTEGER, 
                        new_balance INTEGER
                        )"""
        cur.execute(sql)
        conn.commit()

        sql = """CREATE TABLE if not exists bank_statement (
                        account_type TEXT, 
                        date TEXT, 
                        transaction_code TEXT, 
                        debit INTEGER, 
                        credit INTEGER, 
                        balance INTEGER, 
                        remarks TEXT 
                        )"""
        cur.execute(sql)
        conn.commit()

        sql = """CREATE TABLE if not exists self_expense (
                        date TEXT, 
                        purpose TEXT, 
                        amount INTEGER, 
                        remarks TEXT
                        )"""
        cur.execute(sql)
        conn.commit()

        conn.close()

    def open_bank_statement_window(self):
        self.bank_statement_window = QtWidgets.QMainWindow()
        self.ui_bank_statement_window = Ui_MainWindow_bank_statement()
        self.ui_bank_statement_window.setupUi(self.bank_statement_window)
        self.bank_statement_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.bank_statement_window.show()

    def open_income_expense_window(self):
        self.income_expense_window = QtWidgets.QMainWindow()
        self.ui_income_expense = Ui_MainWindow_income_expense()
        self.ui_income_expense.setupUi(self.income_expense_window)
        self.income_expense_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.income_expense_window.show()

    def open_add_member_window(self):
        self.add_member_window = QtWidgets.QMainWindow()
        self.ui_add_member_window = Ui_MainWindow_add_member()
        self.ui_add_member_window.setupUi(self.add_member_window)
        self.add_member_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.add_member_window.show()

    def open_receipt_entry_window(self):
        self.receipt_entry_window = QtWidgets.QMainWindow()
        self.ui_receipt_entry_window = Ui_MainWindow_receipt_entry()
        self.ui_receipt_entry_window.setupUi(self.receipt_entry_window)
        self.receipt_entry_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.receipt_entry_window.show()

    def open_view_member_window(self):
        self.view_member_window = QtWidgets.QMainWindow()
        self.ui_view_member_window = Ui_MainWindow_view_member()
        self.ui_view_member_window.setupUi(self.view_member_window)
        self.view_member_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.view_member_window.show()

    def open_view_receipt_window(self):
        self.view_receipt_window = QtWidgets.QMainWindow()
        self.ui_view_receipt_window = Ui_MainWindow_view_receipt()
        self.ui_view_receipt_window.setupUi(self.view_receipt_window)
        self.view_receipt_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.view_receipt_window.show()

    def open_annual_report_window(self):
        self.annual_report_window = QtWidgets.QMainWindow()
        self.ui_annual_report_window = Ui_MainWindow_annual_report()
        self.ui_annual_report_window.setupUi(self.annual_report_window)
        self.annual_report_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.annual_report_window.show()

    def open_self_expense_window(self):
        self.self_expense_window = QtWidgets.QMainWindow()
        self.ui_self_expense_window = Ui_MainWindow_self_expense()
        self.ui_self_expense_window.setupUi(self.self_expense_window)
        self.self_expense_window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.self_expense_window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setStyle("Fusion")
    MainWindow.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow_splash_screen = QtWidgets.QMainWindow()
    ui_splash_screen = Ui_MainWindow_splash_screen()
    ui_splash_screen.setupUi(MainWindow_splash_screen)
    MainWindow_splash_screen.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow_splash_screen.show()
    QtCore.QTimer.singleShot(1000, MainWindow_splash_screen.close)
    QtCore.QTimer.singleShot(500, MainWindow.show)
    sys.exit(app.exec_())
