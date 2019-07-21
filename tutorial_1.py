from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myurl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# Opening up connection, grabbing the page
uClient = uReq(myurl)
# offloads raw html content into a variable
page_html = uClient.read()
# close the internet connection
uClient.close()

# At this point the html is a big jumble of text so
# we need to parse it

# html parser
page_soup = soup(page_html, "html.parser")

# The <div> with a class='item-container' stores
# all the information about each graphic card
# Let's store it into a variable using a function
# from the soup module called findAll()
containers = page_soup.findAll('div', {'class': 'item-container'})

# Save the file to a csv format
filename = 'products.csv'
f = open(filename, 'w')
headers = 'brand, product_name, shipping\n'
# This line tells the file that the first line will be a header
f.write(headers)
# Grabbing the title for each graphic card's name
# we need to loop through each container and
# travel trough some html tags in order to grab
# the desired object (it's usefull to test it in
# the command line)
for container in containers:
    brand_container = container.findAll('a', {'class': 'item-brand'})
    brand = brand_container[0].img['title']

    # grab the title for each product
    # At this point its best to use a text editor or inspect the web page to search for
    # the tags(or the path) to find the desired item
    title_container = container.findAll('a', {'class': 'item-title'})
    product_name = title_container[0].text

    shipping_container = container.findAll('li', {'class': 'price-ship'})
    shipping = shipping_container[0].text.strip()

    print('brand: ' + brand)
    print('product name: ' + product_name)
    print('shipping: ' + shipping)

    f.write(brand + "," + product_name.replace(",", "|") + "," + "shipping" + "\n")

f.close()