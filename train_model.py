
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from recommender import PRODUCTS


# Project paths
BASE_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "recommendation_model.joblib"


def train_model():
    """Train the product recommendation model and save its artifacts."""

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    # Load the product catalog
    products_df = pd.DataFrame(PRODUCTS)

    # Combine text features used for recommendations
    products_df["features"] = (
        products_df["title"].fillna("") + " "
        + products_df["category"].fillna("") + " "
        + products_df["description"].fillna("")
    )

    # Train the TF-IDF text representation
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        max_features=5000
    )

    tfidf_matrix = vectorizer.fit_transform(
        products_df["features"]
    )

    # Calculate similarities between products
    similarity_matrix = cosine_similarity(tfidf_matrix)

    # Save the trained model components
    model_artifacts = {
        "vectorizer": vectorizer,
        "tfidf_matrix": tfidf_matrix,
        "similarity_matrix": similarity_matrix,
        "product_ids": products_df["id"].tolist(),
        "model_name": "SmartCart TF-IDF Recommender",
        "model_version": "1.0"
    }

    joblib.dump(model_artifacts, MODEL_PATH)

    print("Model training completed successfully!")
    print(f"Products processed: {len(products_df)}")
    print(f"Text features learned: {len(vectorizer.get_feature_names_out())}")
    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()
