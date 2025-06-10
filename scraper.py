import requests
from bs4 import BeautifulSoup

def scrape_quotes(max_pages=3):
    results = []

    for page in range(1, max_pages + 1):
        url = f"https://quotes.toscrape.com/page/{page}/"
        response = requests.get(url)

        # Ако не е успешен response (пример 404), прекини
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text = quote.find("span", class_="text").get_text(strip=True)
            author = quote.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]
            tag_string = ", ".join(tags)
            results.append(f"💬 {text} — *{author}* [Tags: {tag_string}]")

    return results
