import requests
from bs4 import BeautifulSoup

product_code = input("Podaj kod produktu: ")
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
respons = requests.get(url)
if respons.status_code == requests.codes.ok:
    page_dom = BeautifulSoup(respons.text, 'html.parser')
    opinions = page_dom.select("div.js_product-review")
    if len(opinions) > 0:
        print("Są opinie")
    else:
        print("Nie ma opinii")

 
