
import sqlite3
from pathlib import Path

from recommender import get_all_products

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "smartcart.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    """Create database tables and synchronize the product catalog."""
    products = get_all_products()

    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                category TEXT,
                description TEXT,
                price TEXT,
                emoji TEXT
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS search_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT NOT NULL,
                searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        for product in products:
            connection.execute("""
                INSERT INTO products
                    (id, title, category, description, price, emoji)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    title = excluded.title,
                    category = excluded.category,
                    description = excluded.description,
                    price = excluded.price,
                    emoji = excluded.emoji
            """, (
                product["id"],
                product["title"],
                product.get("category", ""),
                product.get("description", ""),
                str(product.get("price", "")),
                product.get("emoji", ""),
            ))

    print(f"Database initialized: {DB_PATH}")
    print(f"Products synchronized: {len(products)}")


def get_database_products():
    """Retrieve all products from SQLite."""
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM products ORDER BY id"
        ).fetchall()

    return [dict(row) for row in rows]


def save_search(query):
    """Save a non-empty search query."""
    query = str(query).strip()

    if not query:
        return

    with get_connection() as connection:
        connection.execute(
            "INSERT INTO search_history (query) VALUES (?)",
            (query,),
        )


if __name__ == "__main__":
    initialize_database()

    products = get_database_products()
    print(f"Products retrieved from database: {len(products)}")

    if products:
        print("Sample product:", products[0]["title"])
