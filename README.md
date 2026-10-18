# 🛒 SmartCart AI — Product Recommendation System

## 📌 Project Overview

SmartCart AI is a web-based product recommendation system developed using Python, Flask, and machine learning techniques. It helps users discover products by searching for items, browsing categories, and exploring similar products.

The system uses **TF-IDF vectorization and cosine similarity** to recommend products based on their titles, categories, and descriptions. SQLite is used to store product information and search history.

## 🎯 Project Objectives

- Develop an interactive product recommendation web application.
- Implement product search and category-based filtering.
- Recommend similar products using content-based filtering.
- Integrate a SQLite database for storing product details and search history.
- Build a responsive and user-friendly interface.
- Evaluate recommendation functionality through automated checks.

## ✨ Features

- **Product Search:** Search products by name or relevant keywords.
- **Category Filtering:** Browse products across different categories.
- **AI-Based Recommendations:** Discover similar products using text similarity.
- **Product Catalog:** View product names, descriptions, categories, and prices.
- **Search History:** Store user search queries in SQLite.
- **Interactive Web Interface:** Browse products through a Flask-powered website.
- **Recommendation Evaluation:** Test recommendations for availability, self-exclusion, and duplicate IDs.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask | Backend web framework |
| Pandas | Data manipulation, where used |
| NumPy | Numerical operations, where used |
| Scikit-learn | TF-IDF and cosine similarity |
| Joblib | Saving and loading model artifacts |
| SQLite | Database management |
| HTML | Webpage structure |
| CSS | Styling and responsive layout |
| Pytest | Automated testing |

## 📂 Project Structure

```text
SmartCart-AI/
├── artifacts/
│   └── recommendation_model.joblib
├── data/
├── notebooks/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   └── js/
├── templates/
│   └── index.html
├── app.py
├── recommender.py
├── train_model.py
├── database.py
├── evaluate_recommender.py
├── test_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

*Note: This is the intended structure. Keep only the files and folders that actually exist in your repository. The database file `smartcart.db` may be generated locally when the application runs.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd SmartCart-AI
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create a Virtual Environment

For Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

If Pytest is not included in your requirements file, install it using:

```powershell
python -m pip install pytest
```

## 🗄️ Database Initialization

Initialize the SQLite database and synchronize the product catalog:

```powershell
python database.py
```

The database stores product details in the `products` table and search queries in the `search_history` table.

## 🤖 Train the Recommendation Model

Run the training script:

```powershell
python train_model.py
```

The script prepares product text features and saves the model artifact if configured to do so.

Expected artifact location:

```text
artifacts/recommendation_model.joblib
```

## 🚀 Run the Application

Start the Flask application:

```powershell
python app.py
```

Open the following URL in your browser:

http://127.0.0.1:5000

You can now search for products, explore categories, and view similar product recommendations.

## 🧠 How the Recommendation System Works

SmartCart AI uses **content-based filtering** to identify products with similar textual features.

### Step 1: Product Text Preparation
The system uses product titles, categories, and descriptions to represent each product.

### Step 2: TF-IDF Vectorization
TF-IDF (Term Frequency–Inverse Document Frequency) converts product text into numerical vectors, assigning importance to terms based on their occurrence across the catalog.

### Step 3: Cosine Similarity
Cosine similarity measures how similar two product vectors are.

### Step 4: Recommendation Ranking
The system ranks candidate products by similarity and excludes the selected product from its own recommendations.

### Step 5: Display Results
The Flask application displays the recommended products through the web interface.

**Limitation:** The current approach uses product content rather than learning from actual user purchases, ratings, or individual shopping behavior.

## 🧪 Testing and Evaluation

### 1. Evaluate Recommendations

Run:

```powershell
python evaluate_recommender.py
```

The evaluation script checks:

- Recommendations are returned.
- The selected product is excluded.
- Duplicate product IDs are not returned.

**Current evaluation result: 30/30 checks passed across 10 products.**

This confirms that the implemented checks passed; it does not independently measure recommendation relevance or real-world recommendation accuracy.

### 2. Run Automated Application Tests

Run:

```powershell
python -m pytest -v
```

This executes the tests implemented in `test_app.py`, provided that the test file exists and contains the corresponding tests.

## 📸 Screenshots

Add screenshots of your actual running application to demonstrate its functionality.

Suggested screenshots:

1. Homepage and product catalog
2. Product search results
3. Category filtering
4. Similar product recommendations
5. Recommendation evaluation results

Save your screenshots in a `screenshots/` folder and insert them below.

Example:

```markdown
![SmartCart AI Homepage](screenshots/homepage.png)

![Product Recommendations](screenshots/recommendations.png)
```

Make sure these image files exist before adding the links.

## 🔮 Future Enhancements

- Integrate a larger, verified product dataset.
- Add user authentication and individual user profiles.
- Incorporate ratings and purchase history.
- Evaluate recommendation relevance using ranking metrics.
- Add advanced search filters and pagination.
- Deploy the application online.

## 🎓 Learning Outcomes

This project demonstrates practical experience with:

- Python application development
- Flask backend development
- Machine learning and text similarity
- TF-IDF vectorization
- SQLite database integration
- Automated testing
- HTML and CSS web development
- Git and GitHub version control

## 👩‍💻 Author

**Your Name**

GitHub: <YOUR-GITHUB-PROFILE-URL>

## 📄 License

Choose an appropriate open-source license if you intend to distribute this project publicly.
