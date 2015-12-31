from bs4 import BeautifulSoup, UnicodeDammit
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

        acme_list = GroceryCompare.grabGroceries()
        print("DONE!!")

        self.store_picker.activated.connect(partial(self.displayItems, acme_list))
        self.search_button.clicked.connect(partial(self.searchItem,acme_list))

    def displayItems(self, acme_list):

        self.grocery_table.setRowCount(0)
        self.grocery_table.clearContents()

        if self.store_picker.currentText() == 'Acme':

            self.grocery_table.setRowCount(len(acme_list))
            x = 0
            for item in acme_list:
                self.grocery_table.setItem(x, 1, QtWidgets.QTableWidgetItem(item.item_name.decode()))
                self.grocery_table.setItem(x, 2, QtWidgets.QTableWidgetItem(item.item_price.decode()))
                x += 1

        elif self.store_picker.currentText() == 'ShopRite':
            pass
            """x = 0
            for item in shoprite_list:
                self.grocery_table.setItem(x, 1, QtWidgets.QTableWidgetItem(item.item_name.decode('utf-8')))
                self.grocery_table.setItem(x, 2, QtWidgets.QTableWidgetItem(item.item_price.decode('utf-8')))
                x += 1 """

    def searchItem(self, acme_list):

        search_term = self.search_input.text()

        found_items = GroceryCompare.searchItem(acme_list, search_term)

        if len(found_items) > 0:
            for item in found_items:
                print('Item name: ' + item.item_name.decode(), 'Price: ' + item.item_price.decode())
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