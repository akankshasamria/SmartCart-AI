
from flask import Flask, render_template, request
from database import (
    initialize_database,
    get_database_products,
    save_search,
)
from recommender import search_products, recommend_products

app = Flask(__name__)

# Create the database tables and synchronize products
initialize_database()


@app.route("/")
def home():
    query = request.args.get("q", "").strip()
    selected_category = request.args.get("category", "").strip()

    # Read products from SQLite
    products = get_database_products()

    # Search products using the recommendation module
    if query:
        save_search(query)
        products = search_products(query)

    # Filter by category
    if selected_category:
        products = [
            product for product in products
            if product.get("category", "").lower()
            == selected_category.lower()
        ]

    # Support category links that use ?q=Electronics
    categories = {
        "electronics", "clothing", "shoes", "books",
        "home", "beauty", "accessories", "sports"
    }

    if query.lower() in categories and not selected_category:
        products = [
            product for product in get_database_products()
            if product.get("category", "").lower() == query.lower()
        ]

    return render_template(
        "index.html",
        products=products,
        query=query,
        recommendations=[],
        selected_product=None,
    )


@app.route("/recommend/<int:product_id>")
def recommend(product_id):
    products = get_database_products()

    selected_product = next(
        (product for product in products
         if product["id"] == product_id),
        None,
    )

    if selected_product is None:
        return "Product not found", 404

    recommendations = recommend_products(product_id)

    return render_template(
        "index.html",
        products=products,
        query="",
        recommendations=recommendations,
        selected_product=selected_product,
    )


if __name__ == "__main__":
    app.run(debug=True)
