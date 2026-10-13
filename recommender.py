# recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Temporary sample catalog.
# Later, we will replace this with a real product dataset.

PRODUCTS = [
    # ELECTRONICS
    {
        "id": 1,
        "title": "Wireless Bluetooth Headphones",
        "category": "Electronics",
        "description": "Wireless headphones with Bluetooth, clear sound, and long battery life",
        "price": 1499,
        "emoji": "🎧",
    },
    {
        "id": 2,
        "title": "Bluetooth Portable Speaker",
        "category": "Electronics",
        "description": "Portable wireless speaker with Bluetooth and powerful sound",
        "price": 999,
        "emoji": "🔊",
    },
    {
        "id": 3,
        "title": "Smart Fitness Watch",
        "category": "Electronics",
        "description": "Smart watch with fitness tracking, heart rate monitoring, and notifications",
        "price": 1999,
        "emoji": "⌚",
    },
    {
        "id": 9,
        "title": "Wireless Gaming Mouse",
        "category": "Electronics",
        "description": "Wireless computer mouse for gaming, office work, and laptop use",
        "price": 799,
        "emoji": "🖱️",
    },
    {
        "id": 10,
        "title": "Laptop",
        "category": "Electronics",
        "description": "Laptop computer for coding, studying, programming, and everyday work",
        "price": 45999,
        "emoji": "💻",
    },

    # CLOTHING
    {
        "id": 11,
        "title": "Men's Casual Cotton T-Shirt",
        "category": "Clothing",
        "description": "Comfortable cotton T-shirt for casual wear, college, and everyday outfits",
        "price": 499,
        "emoji": "👕",
    },
    {
        "id": 12,
        "title": "Women's Floral Dress",
        "category": "Clothing",
        "description": "Floral printed dress for casual outings, parties, and everyday fashion",
        "price": 1299,
        "emoji": "👗",
    },
    {
        "id": 13,
        "title": "Denim Jeans",
        "category": "Clothing",
        "description": "Classic denim jeans for casual outfits, college, and daily wear",
        "price": 1199,
        "emoji": "👖",
    },
    {
        "id": 14,
        "title": "Winter Hoodie",
        "category": "Clothing",
        "description": "Soft warm hoodie for winter, travel, casual wear, and outdoor activities",
        "price": 999,
        "emoji": "🧥",
    },
    {
        "id": 15,
        "title": "Cotton Kurti",
        "category": "Clothing",
        "description": "Comfortable cotton kurti for everyday wear, college, and casual occasions",
        "price": 799,
        "emoji": "👚",
    },
    {
        "id": 16,
        "title": "Formal Office Shirt",
        "category": "Clothing",
        "description": "Formal shirt for office wear, interviews, meetings, and professional outfits",
        "price": 899,
        "emoji": "👔",
    },

    # SHOES
    {
        "id": 4,
        "title": "Running Sports Shoes",
        "category": "Shoes",
        "description": "Lightweight running shoes for jogging, sports, walking, and exercise",
        "price": 1299,
        "emoji": "👟",
    },
    {
        "id": 17,
        "title": "Casual Sneakers",
        "category": "Shoes",
        "description": "Casual sneakers for college, everyday outfits, walking, and travel",
        "price": 1499,
        "emoji": "👟",
    },
    {
        "id": 18,
        "title": "Women's Flat Sandals",
        "category": "Shoes",
        "description": "Comfortable flat sandals for casual wear, shopping, and daily use",
        "price": 599,
        "emoji": "🩴",
    },
    {
        "id": 19,
        "title": "Formal Leather Shoes",
        "category": "Shoes",
        "description": "Formal shoes for office, interviews, business meetings, and occasions",
        "price": 1799,
        "emoji": "👞",
    },

    # BOOKS
    {
        "id": 5,
        "title": "Programming for Beginners",
        "category": "Books",
        "description": "Beginner book for learning Python programming and computer science",
        "price": 499,
        "emoji": "📘",
    },
    {
        "id": 6,
        "title": "Python Coding Guide",
        "category": "Books",
        "description": "Practical Python coding examples, programming exercises, and projects",
        "price": 599,
        "emoji": "📚",
    },

    # HOME AND KITCHEN
    {
        "id": 7,
        "title": "Stainless Steel Water Bottle",
        "category": "Home",
        "description": "Reusable insulated water bottle for school, travel, and exercise",
        "price": 399,
        "emoji": "🥤",
    },
    {
        "id": 20,
        "title": "Coffee Maker",
        "category": "Home",
        "description": "Electric coffee maker for preparing fresh coffee at home and office",
        "price": 2499,
        "emoji": "☕",
    },
    {
        "id": 21,
        "title": "Desk Lamp",
        "category": "Home",
        "description": "LED desk lamp for studying, reading, working, and bedroom lighting",
        "price": 699,
        "emoji": "💡",
    },
    {
        "id": 22,
        "title": "Bedsheet Set",
        "category": "Home",
        "description": "Soft bedsheet set for bedroom decoration and comfortable sleeping",
        "price": 999,
        "emoji": "🛏️",
    },

    # BAGS AND ACCESSORIES
    {
        "id": 8,
        "title": "Laptop Backpack",
        "category": "Accessories",
        "description": "Laptop backpack with storage compartments for college, travel, and accessories",
        "price": 899,
        "emoji": "🎒",
    },
    {
        "id": 23,
        "title": "Women's Handbag",
        "category": "Accessories",
        "description": "Everyday handbag for carrying personal items, accessories, and essentials",
        "price": 1199,
        "emoji": "👜",
    },
    {
        "id": 24,
        "title": "Classic Wristwatch",
        "category": "Accessories",
        "description": "Classic wristwatch for everyday outfits, formal occasions, and casual fashion",
        "price": 999,
        "emoji": "⌚",
    },

    # BEAUTY AND PERSONAL CARE
    {
        "id": 25,
        "title": "Moisturizing Face Cream",
        "category": "Beauty",
        "description": "Face moisturizer for everyday skincare and keeping skin hydrated",
        "price": 349,
        "emoji": "🧴",
    },
    {
        "id": 26,
        "title": "Makeup Brush Set",
        "category": "Beauty",
        "description": "Makeup brushes for applying foundation, blush, powder, and eyeshadow",
        "price": 599,
        "emoji": "💄",
    },

    # SPORTS AND FITNESS
    {
        "id": 27,
        "title": "Yoga Mat",
        "category": "Sports",
        "description": "Non-slip exercise mat for yoga, stretching, fitness, and home workouts",
        "price": 699,
        "emoji": "🧘",
    },
    {
        "id": 28,
        "title": "Dumbbell Set",
        "category": "Sports",
        "description": "Home fitness dumbbells for strength training and general exercise",
        "price": 1499,
        "emoji": "🏋️",
    },
]

df = pd.DataFrame(PRODUCTS)

# Combine text fields so the model can compare product meaning.
df["features"] = (
    df["title"] + " "
    + df["category"] + " "
    + df["description"]
)

# Convert text into numerical TF-IDF vectors.
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["features"])

# Compare each product with every other product.
similarity_matrix = cosine_similarity(tfidf_matrix)


def get_all_products():
    """Return all products for displaying on the website."""
    return df.drop(columns=["features"]).to_dict(orient="records")


def search_products(query):
    """Find products matching the user's search."""
    query = query.strip().lower()

    if not query:
        return get_all_products()

    matches = df[
        df["features"].str.lower().str.contains(
            query, regex=False, na=False
        )
    ]

    # If there are no direct text matches, use TF-IDF similarity.
    if matches.empty:
        query_vector = vectorizer.transform([query])
        scores = cosine_similarity(query_vector, tfidf_matrix).flatten()
        indices = scores.argsort()[::-1][:5]

        results = df.iloc[indices].copy()
        results["score"] = scores[indices]
        results = results[results["score"] > 0]

        return results.drop(
            columns=["features", "score"], errors="ignore"
        ).to_dict(orient="records")

    return matches.drop(columns=["features"]).to_dict(orient="records")


def recommend_products(product_id, limit=4):
    """Recommend products similar to a selected product."""
    matches = df.index[df["id"] == product_id].tolist()

    if not matches:
        return []

    product_index = matches[0]
    scores = list(enumerate(similarity_matrix[product_index]))

    # Highest similarity first, excluding the selected product.
    scores = sorted(scores, key=lambda item: item[1], reverse=True)
    scores = [
        (index, score)
        for index, score in scores
        if index != product_index
    ][:limit]

    recommendations = df.iloc[
        [index for index, score in scores]
    ].copy()

    recommendations["similarity"] = [
        round(score * 100, 1) for index, score in scores
    ]

    return recommendations.drop(
        columns=["features"]
    ).to_dict(orient="records")