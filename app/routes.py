from app import app
from flask import render_template, redirect, url_for, request
from urllib import response
from bs4 import BeautifulSoup
import requests
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/extract', methods=["POST", "GET"])
def extract():
    if request.method == "POST":
        product_id = request.form.get("product_id")
        url = f"https://www.ceneo.pl/{product_id}#tab=reviews"
        all_opinions = []

        while(url):
            response = requests.get(url)
            # print(response.status_code) // jak 200 to działa

            page = BeautifulSoup(response.text, "html.parser")

            opinions = page.select("div.js_product-review")

            for  opinion in opinions:
                
                single_opinion = {
                    key:get_item(opinion, *value)
                        for key, value in selectors.items()
                }
                
                single_opinion["opinion_id"] = opinion["data-entry-id"]
                
                all_opinions.append(single_opinion)
            
            try:
                url = "https://www.ceneo.pl" + get_item(page, "a.pagination__next", "href")
            except TypeError:
                url = None

        with open(f"opinions\{product_id}.json", "w", encoding="UTF-8") as file:
            json.dump(all_opinions, file, indent=4, ensure_ascii=False)
        return redirect(url_for("product", product_id = product_id))
    else:
        return render_template("extract.html.jinja")

@app.route('/products')
def products():
    products = [filename.split(".")[0] for filename in os.listdir("app/opinions")]
    return render_template("products.html.jinja", products=products)

@app.route('/author')
def author():
    return render_template("author.html.jinja")


@app.route('/product/<product_id>')
def product(product_id):
    opinions = pd.read_json(f"opinions/{product_id}.json")
    print(opinions)
    opinions.stars = opinions.stars.map(lambda x: float(x.split("/")[0].replace(",", ".")))
    opinions_count = len(opinions.index)
    stats = {
        "pros_count" : opinions.pros.map(bool).sum(),
        "cons_count" : opinions.cons.map(bool).sum(),
        "avarage_score" : opinions.stars.mean().round(2)
    }

    recommendation = opinions.recomendation.value_counts(dropna = False)
    recommendation.plot.pie(
        label="", 
        autopct="%1.1f%%", 
        colors=["green", "blue", "red"]
    )
    plt.title("Rekomendacja")
    plt.savefig(f"plots/{product_id}_recomendations.png")
    plt.close()

    stars = opinions.stars.value_counts()
    stars.plot.bar()
    plt.title("Ocenty produktów")
    plt.xlabel("Liczba gwiazdek")
    plt.ylabel("Liczba opinii")
    plt.grid(True)
    plt.xticks(rotation=0)
    plt.show()
    return render_template("product.html.jinja", product_id=product_id, stats=stats, opinions=opinions)