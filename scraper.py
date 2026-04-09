import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/catalogue/category/books_1/index.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

names = []
prices = []

books = soup.find_all("article", class_="product_pod")

for book in books:
    name = book.h3.a["title"]
    price = book.find("p", class_="price_color").text

    names.append(name)
    prices.append(price)

data = pd.DataFrame({
    "Book": names,
    "Price": prices
})

data.to_csv("products.csv", index=False)

print("🔥 Products Scraped!")