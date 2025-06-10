import requests
from bs4 import BeautifulSoup

def scrape_books(max_pages=3):
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    results = []

    for page in range(1, max_pages + 1):
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip()
            rating = book.p.get("class")[1]  # e.g., "Three", "Four"
            results.append(f"📘 {title} — 💰 {price} — ⭐ {rating} stars")

    return results
