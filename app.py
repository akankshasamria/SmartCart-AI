# app.py

from flask import Flask, render_template, request
from recommender import get_all_products, search_products, recommend_products

app = Flask(__name__)


@app.route("/")
def home():
    query = request.args.get("q", "").strip()

    if query:
        products = search_products(query)
    else:
        products = get_all_products()

    return render_template(
        "index.html",
        products=products,
        query=query,
        recommendations=[],
        selected_product=None,
    )


@app.route("/recommend/<int:product_id>")
def recommend(product_id):
    all_products = get_all_products()

    selected_product = next(
        (p for p in all_products if p["id"] == product_id),
        None,
    )

    if selected_product is None:
        return "Product not found", 404

    recommendations = recommend_products(product_id)

    return render_template(
        "index.html",
        products=all_products,
        query="",
        recommendations=recommendations,
        selected_product=selected_product,
    )


if __name__ == "__main__":
    app.run(debug=True)