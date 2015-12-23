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

    return item_list

def searchItem(item_list):
    search_item = input('What is the name of the item to search for?: ')
    item_found_list = []

    for item in item_list:
        if item.item_name.find(search_item.encode()) > -1:
            item_found_list.append(item)

    return item_found_list

def display_items_found(found_list):
    for item in found_list:
        print('Item name: '.encode() + item.item_name, 'Price: '.encode() + item.item_price)

if __name__ == '__main__':
    #Make this loop over all pages of the ad. Try using a dictionary
    acme_source = parsePage('http://acmemarkets.mywebgrocer.com/Circular/Philadelphia-19th-and-Oregon/744373054/Weekly/3/1')
    shoprite_source = parsePage('http://plan.shoprite.com/Circular/ShopRite-of-Oregon-Ave/977B652/Weekly/2/1')
    acme_groceries = createGroceryItem(acme_source)
    shoprite_groceries = createGroceryItem(shoprite_source)

    while True:
        search_for_groceries = input('Do you want to search for specific items? (Y/N/Exit): ')
     
        # Affirmative to search for items
        if search_for_groceries == 'Y' or search_for_groceries == 'y':
            found_item_list = searchItem(acme_groceries)

            #Only print the items if things have been found
            if len(found_item_list) > 0:
                display_items_found(found_item_list)
            else:
                print('Sorry no items found this week. Try a different item.')
        
        #Print all items on the page
        elif search_for_groceries == 'N' or search_for_groceries == 'n':
            print('\nHere are this weeks groceries: \n' + 'ACME Store:\n')
            for item in acme_groceries:
                print('Item name: '.encode() + item.item_name, 'Price: '.encode() + item.item_price)
            
            print('\nHere are this weeks groceries: \n' + 'ShopRite Store\n')
            for item in shoprite_groceries:
                print('Item name: '.encode() + item.item_name, 'Price: '.encode() + item.item_price)
        #Exit the app
        elif search_for_groceries == 'exit' or search_for_groceries == 'Exit':
            break

        else:
            print('Please put Y or N')
