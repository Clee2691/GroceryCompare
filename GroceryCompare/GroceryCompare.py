from bs4 import BeautifulSoup, UnicodeDammit
import requests

class GroceryItem():
    
    # Creates grocery item instance
    def __init__(self, item_name, item_price, item_image):
        self.item_name = item_name
        self.item_price = item_price
        self.item_image = item_image

def parsePage(web_page):

    #Parses webpage of requested ad page
    page = requests.get(web_page)
    return BeautifulSoup(page.content, 'html.parser')

def findGroceryDetails(grocery_store):

    #selects the css selector and puts them in a list
    prices = grocery_store.select('.itemPrice')
    titles = grocery_store.select('.itemTitle')
    images = grocery_store.select('.itemImage')

    return prices, titles, images

def createGroceryItem(page_source):
    
    # Returns a list of all the names, prices, and images for each item on the ad page
    price, names, images = findGroceryDetails(page_source)

    # Create instances of the grocery item using GroceryItem class
    item_list = []
    for p, n, i in zip(price, names, images):
        item_list.append(GroceryItem(n.get_text().encode(),p.get_text().encode(),i.get('src').encode()))

    # Debug info. Shows item name and price so far
    for item in item_list:
        print(item.item_name)
        print(item.item_price)


if __name__ == '__main__':

    acme_source = parsePage('http://acmemarkets.mywebgrocer.com/Circular/Philadelphia-19th-and-Oregon/744373054/Weekly/3')
    acmeGroceries = createGroceryItem(acme_source)
