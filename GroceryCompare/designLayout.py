# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designLayout.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 714)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.acme_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(20)
        self.acme_label.setFont(font)
        self.acme_label.setTextFormat(QtCore.Qt.AutoText)
        self.acme_label.setScaledContents(False)
        self.acme_label.setAlignment(QtCore.Qt.AlignCenter)
        self.acme_label.setOpenExternalLinks(True)
        self.acme_label.setObjectName("acme_label")
        self.horizontalLayout_2.addWidget(self.acme_label)
        self.shoprite_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(20)
        self.shoprite_label.setFont(font)
        self.shoprite_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shoprite_label.setObjectName("shoprite_label")
        self.horizontalLayout_2.addWidget(self.shoprite_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acme_table = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.acme_table.setFont(font)
        self.acme_table.setObjectName("acme_table")
        self.acme_table.setColumnCount(2)
        self.acme_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.acme_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.acme_table.setHorizontalHeaderItem(1, item)
        self.acme_table.horizontalHeader().setVisible(True)
        self.acme_table.horizontalHeader().setCascadingSectionResizes(False)
        self.acme_table.horizontalHeader().setDefaultSectionSize(200)
        self.acme_table.horizontalHeader().setStretchLastSection(True)
        self.acme_table.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.acme_table)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout_3.addWidget(self.search_input)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grocery Comparer"))
        self.acme_label.setText(_translate("MainWindow", "Acme"))
        self.shoprite_label.setText(_translate("MainWindow", "ShopRite"))
        item = self.acme_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.acme_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item Price"))
        self.search_input.setText(_translate("MainWindow", "Enter name of item to search"))
        self.pushButton.setText(_translate("MainWindow", "Search"))

