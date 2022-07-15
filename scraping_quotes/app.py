import requests

from scraping_quotes.pages.quotes_page import QuotesPage

def scraper_request(url_to_get):
    page_content = requests.get(url_to_get).content
    page = QuotesPage(page_content)

    for quote in page.quotes:
        return quote.content
        # with open('Quotes.txt', 'a') as file:
        #     file.write(quote.content + '\n')ya aaron
        # file.close()

print(scraper_request.author('https://quotes.toscrape.com'))