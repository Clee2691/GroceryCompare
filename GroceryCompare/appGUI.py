from bs4 import BeautifulSoup
import requests
import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from designLayout import Ui_MainWindow
import GroceryCompare
from functools import partial

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

    def displayItems(self, acme_list, shoprite_list, acme_date, shop_date):

        self.grocery_table.setRowCount(0)
        self.grocery_table.clearContents()

        if self.store_picker.currentText() == 'Acme':
            self.store_week_label.setText(acme_date)

            self.grocery_table.setRowCount(len(acme_list))
            x = 0
            for item in acme_list:
                self.grocery_table.setItem(x, 0, QtWidgets.QTableWidgetItem(item.item_name))
                self.grocery_table.setItem(x, 1, QtWidgets.QTableWidgetItem(item.item_price))
                x += 1

        elif self.store_picker.currentText() == 'ShopRite':
            self.store_week_label.setText(shop_date)
            self.grocery_table.setRowCount(len(shoprite_list))
            x = 0
            for item in shoprite_list:

                self.grocery_table.setItem(x, 0, QtWidgets.QTableWidgetItem(item.item_name))
                self.grocery_table.setItem(x, 1, QtWidgets.QTableWidgetItem(item.item_price))

                x += 1

    def searchItem(self, acme_list, shoprite_list):

        search_term = self.search_input.text()

        if self.store_picker.currentText() == 'Acme':
            found_items = GroceryCompare.searchItem(acme_list, search_term)
        else:
            found_items = GroceryCompare.searchItem(shoprite_list, search_term)

        if len(found_items) > 0:
            for item in found_items:
                item = item.item_name
                print(item)
                #print('Item name: ' + item.item_name, 'Price: ' + item.item_price)
        else:
            print("Either you didn't enter anything or no items found in this week's circular")

if __name__ == '__main__':
    
    #Ensures it works in virtualEnv by setting paths
    QtCore.QCoreApplication.setLibraryPaths(['E:\Visual Studio 2015\Projects\GroceryCompare\GroceryCompare\env34\Lib\site-packages\PyQt5\plugins'])

    #Create the main window
    app = QtWidgets.QApplication(sys.argv)
    window = GroceryLayout()
    window.show()
    app.exec_()