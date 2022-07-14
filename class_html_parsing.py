from bs4 import BeautifulSoup
import requests
import re


# TODO split classes to individual files

class ParsedItemLocators:
    # Find the locators encapsulated in a class
    NAME_LOCATOR = 'article.product_pod h3 a'
    RATING_LOCATOR = 'article.product_pod p.star-rating'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'


class ParsedItem:

    def __init__(self, page):
        url = page
        req = requests.get(url)
        self.soup = BeautifulSoup(req.content, 'html.parser')

    @property
    def name(self):
        locater = ParsedItemLocators.NAME_LOCATOR
        item_link = self.soup.select(locater)
        for each_link in item_link:
            item_name = each_link.attrs['title']
            # What do we want to do with the names in the loop??
            return item_name

    @property
    def link(self):
        locator = ParsedItemLocators.LINK_LOCATOR
        item_link = self.soup.select_one(locator).attrs['href']
        return item_link

    @property
    def pricing(self):
        paragraph_contents = self.soup.find_all('p', attrs={"class": "price_color"})
        price_pattern = '([0-9]+\.[0-9]+)'  # Regex pattern (quit PEP erroring already!)
        for each_price in paragraph_contents:
            each_price = each_price.string
            price_matching = re.search(price_pattern, each_price)
            return float(price_matching.group(0))

    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = filter(lambda x: x != 'star-rating', classes)
        return rating_classes


my_parsed_item = ParsedItem('http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html')
print(my_parsed_item.name)
print(my_parsed_item.pricing)
print(my_parsed_item.link)

print(my_parsed_item.rating)

# [ParsedItem(p) for p in soup.findall('article')]   For finding all items without looping in the class.
