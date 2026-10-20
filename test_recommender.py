
from recommender import get_all_products, search_products, recommend_products


def test_product_catalog_is_not_empty():
    products = get_all_products()
    assert len(products) > 0


def test_search_returns_results():
    results = search_products("headphones")
    assert len(results) > 0


def test_recommendations_exclude_selected_product():
    products = get_all_products()
    assert len(products) > 0

    product_id = products[0]["id"]
    recommendations = recommend_products(product_id, limit=4)

    recommended_ids = [item["id"] for item in recommendations]
    assert product_id not in recommended_ids


def test_recommendations_have_no_duplicates():
    products = get_all_products()
    product_id = products[0]["id"]

    recommendations = recommend_products(product_id, limit=4)
    recommended_ids = [item["id"] for item in recommendations]

    assert len(recommended_ids) == len(set(recommended_ids))
