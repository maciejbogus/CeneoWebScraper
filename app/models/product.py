import requests
import json
import os
from bs4 import BeautifulSoup
from app.utils import get_item
from app.models.opinion import Opinion

class Product:
    def __init__(self, product_id_="", product_name_="", opinions_="", opinions_count_="", pros_count_="", cons_count_="", avarage_score_="", url_=""):
        self.product_id=product_id_
        self.product_name= product_name_
        self.opinions = opinions_
        self.opinions_count = opinions_count_
        self.pros_count = pros_count_
        self.cons_count = cons_count_
        self.avarage_score = avarage_score_
        self.url = url_
        return self
    
    def extract_product(self):
        url = f"https://www.ceneo.pl/{product_id}#tab=reviews"
        all_opinions = []

        while(url):
            response = requests.get(url)
            # print(response.status_code) // jak 200 to działa

            page = BeautifulSoup(response.text, "html.parser")

            self = self.product_name

            opinions = page.select("div.js_product-review")

            for  opinion in opinions:
                self.opinions.append(Opinion().extract_opinion(opinion))
            
            try:
                url = "https://www.ceneo.pl" + get_item(page, "a.pagination__next", "href")
            except TypeError:
                url = None
                
    def process_stats(self):
        self.opinions_count = len(self.opinions.index)
        self.pros_count = self.opinions.pros.map(bool).sum(),
        self.cons_count = self.opinions.cons.map(bool).sum(),
        self.avarage_score = self.opinions.stars.mean().round(2)
        return self
    
    
    def save_opinions(self):
        if not os.path.exists("app/opinions"):
            os.makedirs("app/opinions")
        with open(f"app/opinions/{self.product_id}.json", "w", encoding="UTF-8") as file:
            json.dump(all_opinions, file, indent=4, ensure_ascii=False)
            
    def save_stats(self):
        if not os.path.exists("app/opinions"):
            os.makedirs("app/opinions")
        with open(f"app/opinions/{self.product_id}.json", "w", encoding="UTF-8") as file:
            json.dump(all_opinions, file, indent=4, ensure_ascii=False)