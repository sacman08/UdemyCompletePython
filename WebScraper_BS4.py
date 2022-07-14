# TODO join in a class to allow encapsulation

from bs4 import BeautifulSoup
import requests
import re

url = "http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')


def find_item_name():
    locater = 'article.product_pod h3 a'
    item_link = soup.select(locater)
    for each_link in item_link:
        item_name = each_link.attrs['title']
        # What do we want to do with the titles??
        print(item_name)


def find_pricing():
    paragraph_contents = soup.find_all('p', attrs={"class": "price_color"})
    price_pattern = '([0-9]+\.[0-9]+)'
    for each_price in paragraph_contents:
        each_price = each_price.string
        price_matching = re.search(price_pattern, each_price)
        print(float(price_matching.group(0)))

def find_item_rating():
    locator = 'article.product_pod p.star-rating'
    star_rating_tag = soup.select_one(locator)
    classes = star_rating_tag.attrs['class']
    rating_classes = filter(lambda x: x != 'star-rating', classes)
    print(rating_classes)

find_item_name()
find_pricing()
find_item_rating()
