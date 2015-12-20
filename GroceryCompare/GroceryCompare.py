from bs4 import BeautifulSoup, UnicodeDammit
import requests

class groceryItem():
    def __init__(self, item_name, item_price, item_image):
        self.item_name = item_name
        self.item_price = item_price
        self.item_image = item_image

def parsePage():
    acmePage = requests.get('http://acmemarkets.mywebgrocer.com/Circular/Philadelphia-19th-and-Oregon/744373054/Weekly/3')
    acmeSource = BeautifulSoup(acmePage.content, 'html.parser')
    return acmeSource

def findGroceryDetails(grocery_store):

    #selects the css selector and puts them in a list
    all_p_prices = grocery_store.select('.itemPrice')
    all_p_titles = grocery_store.select('.itemTitle')
    all_p_images = grocery_store.select('.itemImage')

    return all_p_prices, all_p_titles, all_p_images

def createGroceryItem():
    acme_price, acme_names, acme_images = findGroceryDetails(acmeSource)

    for p, n, i in zip(acme_price, acme_names, acme_images):
        print ('Item: '.encode() + n.get_text().encode(), 'Price: '.encode() + p.get_text().encode(), 'Image: '.encode() + i.get_text().encode())

if __name__ == '__main__':

    acmeSource = parsePage()
    acmeGroceries = createGroceryItem()

    # for debugging purposes
    '''for prices in acme_price:
        print(prices.encode('UTF-8'))

    for titles in acme_names:
        print(titles.encode('UTF-8'))

    for images in acme_images:
        print(images.encode('UTF-8'))'''
