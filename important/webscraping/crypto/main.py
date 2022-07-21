import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"
headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 OPR/78.0.4093.184"
}
result = requests.get(url, headers=headers).text
soup = BeautifulSoup(result, "lxml")

tbody = soup.find("tbody")
coins = tbody.find_all("tr")

for coin in coins:
    name = coin.find(class_="cmc-link").get("href").replace(
        "/currencies/", "")[:-1]
    price = coin.find(class_="sc-131di3y-0 cLgOOr")

    if price:
        price = price.text
        print(f"{name} --> {price[1:]}$")
    else:
        price = coin.find_all("td")[-2].find("span").text
        print(f"{name} --> {price[1:]}$")
