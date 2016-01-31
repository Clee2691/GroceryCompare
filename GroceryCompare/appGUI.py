from bs4 import BeautifulSoup
import requests
import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from designLayout import Ui_MainWindow
import GroceryCompare
from functools import partial
import chardet

class GroceryLayout(QtWidgets.QMainWindow, Ui_MainWindow):
    
    '''GUI of the program'''

    def __init__(self):
        super(GroceryLayout, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        print('Getting items from the ad pages. This may take a moment. Please wait!')

        acme_list, shoprite_list, acme_date, shop_date = GroceryCompare.grabGroceries()

        print("DONE!!")

        self.store_picker.activated.connect(partial(self.displayItems, acme_list, shoprite_list, acme_date, shop_date))
        self.search_button.clicked.connect(partial(self.searchItem,acme_list, shoprite_list))
        self.reset_btn.clicked.connect(self.resetTable)

    def resetTable(self):
        '''Resets the table'''
        self.grocery_table.setRowCount(0)
        self.grocery_table.clearContents()

    def displayItems(self, acme_list, shoprite_list, acme_date, shop_date):
        '''Displays items from the grocery store depending on which store is picked'''
        #Make QPixmap object of the image
        acme_icon = QtGui.QPixmap(r"Images\acmeimage.png")
        shoprite_icon = QtGui.QPixmap(r'Images\shopriteimage.png')

        #Clear the table if there is anything
        self.grocery_table.setRowCount(0)
        self.grocery_table.clearContents()

        #Depending on the store, display the items, icon, and effective ad date
        if self.store_picker.currentText() == 'Acme':
            self.store_week_label.setText(acme_date)
            self.store_icon_label.setPixmap(acme_icon)

            self.grocery_table.setRowCount(len(acme_list))
            x = 0
            for item in acme_list:
                self.grocery_table.setItem(x, 0, QtWidgets.QTableWidgetItem(item.item_name))
                self.grocery_table.setItem(x, 1, QtWidgets.QTableWidgetItem(item.item_price))
                x += 1

        elif self.store_picker.currentText() == 'ShopRite':
            self.store_week_label.setText(shop_date)
            self.store_icon_label.setPixmap(shoprite_icon)

            self.grocery_table.setRowCount(len(shoprite_list))
            x = 0
            for item in shoprite_list:

                self.grocery_table.setItem(x, 0, QtWidgets.QTableWidgetItem(item.item_name))
                self.grocery_table.setItem(x, 1, QtWidgets.QTableWidgetItem(item.item_price))

                x += 1

    def searchItem(self, acme_list, shoprite_list):
        '''Search for a specific item depending on the store'''
        search_term = self.search_input.text()

        if self.store_picker.currentText() == 'Acme':
            found_items = GroceryCompare.searchItem(acme_list, search_term)
        else:
            found_items = GroceryCompare.searchItem(shoprite_list, search_term)

        if len(found_items) > 0:
            #Clear the table if there is anything
            self.grocery_table.setRowCount(0)
            self.grocery_table.clearContents()

            self.grocery_table.setRowCount(len(found_items))
            x = 0

            for item in found_items:

                self.grocery_table.setItem(x, 0, QtWidgets.QTableWidgetItem(item.item_name))
                self.grocery_table.setItem(x, 1, QtWidgets.QTableWidgetItem(item.item_price))
                x += 1

        else:
            QtWidgets.QMessageBox.warning(self,'Search Error' , "Either you didn't enter anything in or the item is not on sale this week.", QtWidgets.QMessageBox.Ok)

if __name__ == '__main__':
    
    #Ensures it works in virtualEnv by setting paths
    QtCore.QCoreApplication.setLibraryPaths(['env34\Lib\site-packages\PyQt5\plugins'])
    #E:\Visual Studio 2015\Projects\GroceryCompare\GroceryCompare\

    #Create the main window
    app = QtWidgets.QApplication(sys.argv)
    window = GroceryLayout()
    window.show()
    app.exec_()