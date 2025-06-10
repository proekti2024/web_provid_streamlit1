import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books(num_pages=3):
    base_url = "https://quotes.toscrape.com/"
    titles, prices, ratings = [], [], []

    for page in range(1, num_pages + 1):
        url = base_url.format(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            title = book.h3.a['title']
            price = float(book.find('p', class_='price_color').text[1:])
            rating = book.p['class'][1]

            titles.append(title)
            prices.append(price)
            ratings.append(rating)

    df = pd.DataFrame({
        'Title': titles,
        'Price (£)': prices,
        'Rating': ratings
    })
    return df
