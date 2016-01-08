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
        MainWindow.resize(651, 741)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/grocery_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.week_HLay = QtWidgets.QHBoxLayout()
        self.week_HLay.setObjectName("week_HLay")
        self.store_week_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.store_week_label.setFont(font)
        self.store_week_label.setText("")
        self.store_week_label.setObjectName("store_week_label")
        self.week_HLay.addWidget(self.store_week_label)
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.week_HLay.addWidget(self.reset_btn)
        self.verticalLayout_2.addLayout(self.week_HLay)
        self.store_pick_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.store_pick_label.setFont(font)
        self.store_pick_label.setObjectName("store_pick_label")
        self.verticalLayout_2.addWidget(self.store_pick_label, 0, QtCore.Qt.AlignHCenter)
        self.store_picker_HLay = QtWidgets.QHBoxLayout()
        self.store_picker_HLay.setObjectName("store_picker_HLay")
        self.store_icon_label = QtWidgets.QLabel(self.centralwidget)
        self.store_icon_label.setText("")
        self.store_icon_label.setObjectName("store_icon_label")
        self.store_picker_HLay.addWidget(self.store_icon_label, 0, QtCore.Qt.AlignRight)
        self.store_picker = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(18)
        self.store_picker.setFont(font)
        self.store_picker.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.store_picker.setAutoFillBackground(False)
        self.store_picker.setFrame(True)
        self.store_picker.setObjectName("store_picker")
        self.store_picker.addItem("")
        self.store_picker.addItem("")
        self.store_picker_HLay.addWidget(self.store_picker, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.store_picker_HLay)
        self.table_HLay = QtWidgets.QHBoxLayout()
        self.table_HLay.setObjectName("table_HLay")
        self.grocery_table = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grocery_table.setFont(font)
        self.grocery_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.grocery_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.grocery_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.grocery_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.grocery_table.setTabKeyNavigation(False)
        self.grocery_table.setDragDropOverwriteMode(False)
        self.grocery_table.setAlternatingRowColors(True)
        self.grocery_table.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.grocery_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.grocery_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.grocery_table.setObjectName("grocery_table")
        self.grocery_table.setColumnCount(2)
        self.grocery_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.grocery_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.grocery_table.setHorizontalHeaderItem(1, item)
        self.grocery_table.horizontalHeader().setVisible(True)
        self.grocery_table.horizontalHeader().setCascadingSectionResizes(False)
        self.grocery_table.horizontalHeader().setDefaultSectionSize(300)
        self.grocery_table.horizontalHeader().setStretchLastSection(True)
        self.grocery_table.verticalHeader().setVisible(False)
        self.table_HLay.addWidget(self.grocery_table)
        self.verticalLayout_2.addLayout(self.table_HLay)
        self.search_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.search_label.setFont(font)
        self.search_label.setObjectName("search_label")
        self.verticalLayout_2.addWidget(self.search_label)
        self.search_HLay = QtWidgets.QHBoxLayout()
        self.search_HLay.setObjectName("search_HLay")
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.search_input.setFont(font)
        self.search_input.setAcceptDrops(False)
        self.search_input.setInputMask("")
        self.search_input.setText("")
        self.search_input.setMaxLength(100)
        self.search_input.setClearButtonEnabled(True)
        self.search_input.setObjectName("search_input")
        self.search_HLay.addWidget(self.search_input)
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setObjectName("search_button")
        self.search_HLay.addWidget(self.search_button)
        self.verticalLayout_2.addLayout(self.search_HLay)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grocery Comparer"))
        self.reset_btn.setText(_translate("MainWindow", "Reset Table"))
        self.store_pick_label.setToolTip(_translate("MainWindow", "Why are you reading the tool tip? Just pick a goddamn store!"))
        self.store_pick_label.setText(_translate("MainWindow", "Pick Your Store"))
        self.store_picker.setToolTip(_translate("MainWindow", "Obviously the store picker >.>"))
        self.store_picker.setCurrentText(_translate("MainWindow", "Acme"))
        self.store_picker.setItemText(0, _translate("MainWindow", "Acme"))
        self.store_picker.setItemText(1, _translate("MainWindow", "ShopRite"))
        self.grocery_table.setSortingEnabled(True)
        item = self.grocery_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.grocery_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        self.search_label.setText(_translate("MainWindow", "Search Item"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Enter name of item to search!"))
        self.search_button.setText(_translate("MainWindow", "Search"))

