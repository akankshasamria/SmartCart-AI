
from recommender import get_all_products, recommend_products


def main():
    products = get_all_products()

    if not products:
        print("FAIL: No products found.")
        return

    passed = 0
    total = 0

    for product in products[:10]:
        product_id = product["id"]
        recommendations = recommend_products(product_id, limit=4)

        checks = {
            "Recommendations returned": len(recommendations) > 0,
            "Selected product excluded": all(
                item["id"] != product_id
                for item in recommendations
            ),
            "No duplicate product IDs": len({
                item["id"] for item in recommendations
            }) == len(recommendations),
        }

        print(f"\nProduct: {product['title']}")

        for name, result in checks.items():
            total += 1
            passed += int(result)
            print(f"  {'PASS' if result else 'FAIL'}: {name}")

    print(f"\nSummary: {passed}/{total} checks passed.")


if __name__ == "__main__":
    main()
