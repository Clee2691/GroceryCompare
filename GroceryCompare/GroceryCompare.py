from bs4 import BeautifulSoup
import requests
import sys

class GroceryItem():
    
    '''Creates the item instances found on each page'''
    def __init__(self, item_name, item_price, item_image):
        self.item_name = item_name
        self.item_price = item_price
        self.item_image = item_image

def parsePages(web_page):
   
    ''' Takes generic page and makes a working link of the ad for further processing''' 

    #Generic store link souped
    store_link_source = requests.get(web_page)
    store_link_souped = BeautifulSoup(store_link_source.content, 'html.parser')

    #Find the actual link to the circular
    week_ad_link = store_link_souped.select('.megadrop-circular-name')
    week_ad_link = week_ad_link[0].get('href')

    #Create the full link without pages
    full_link = web_page + str(week_ad_link)

    #Send link to make the dictionary of grocery pages
    page = requests.get(full_link)
    shop_dic, val_dates = makeGroceryDictionary(BeautifulSoup(page.content, 'html.parser'), full_link)

    return shop_dic, val_dates

def makeGroceryDictionary(store_page_source, actual_page):
    ''' Return a dictionary of all the pages of the ad '''

    grocery_page_dic = {}

    #Determine how many pages are in this weeks ads
    all_pages_tag = store_page_source.select('.pages')
  
    num_pages = int((len(all_pages_tag) + 2) / 2) # Use divided by "2" to correct for double "pages" effectively making the total pages twice as many

    #Obtain the valid dates for this week's ad
    valid_dates = store_page_source.select('#CircularValidDates')

    #Parses each ad page and makes them into BS objects
    x = 1

    for i in range(1, num_pages + 1):
        page_iter = requests.get(actual_page + '/' + str(i))

        grocery_page_dic[str(x)] = BeautifulSoup(page_iter.content, 'html.parser')

        x += 1

    return grocery_page_dic, valid_dates[0].get_text()
    
def findGroceryDetails(grocery_store):

    '''selects the css selector for the item details and puts them in a list'''

    prices = grocery_store.select('.itemPrice')
    titles = grocery_store.select('.itemTitle')
    images = grocery_store.select('.itemImage')

    return prices, titles, images

def createGroceryItem(page_dic):
    item_list = []

    for k,v in page_dic.items():
        # Returns a list of all the names, prices, and images for each item on the ad page
        price, names, images = findGroceryDetails(v)

        # Create instances of the grocery item using GroceryItem class
        for p, n, i in zip(price, names, images):
            item_list.append(GroceryItem(n.get_text(),p.get_text(),i.get('src')))

    return item_list

def searchItem(item_list, search_term):
    item_found_list = []
    
    if search_term == '':
        return item_found_list

    #Searches for the item that you specify
    for item in item_list:
        if search_term.lower() in item.item_name.lower():
            item_found_list.append(item)

    return item_found_list

def grabGroceries():

    #Parses each of the pages of the ad for each store. Returns a dictionary of the pages
    acme_dic, acme_val_date = parsePages('http://acmemarkets.mywebgrocer.com')
    shoprite_dic, shop_val_date = parsePages('http://plan.shoprite.com')

    acme_groceries = createGroceryItem(acme_dic)
    shoprite_groceries = createGroceryItem(shoprite_dic)

    return acme_groceries, shoprite_groceries, acme_val_date, shop_val_date