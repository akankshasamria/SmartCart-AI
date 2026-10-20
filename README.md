# 🛒 SmartCart AI — Product Recommendation System

## 📌 Project Overview

SmartCart AI is a web-based product recommendation system built using Python, Flask, and machine-learning techniques. It helps users discover products by searching for items, browsing categories, and exploring similar products.

The system uses **TF-IDF vectorization and cosine similarity** to recommend products based on their titles, categories, and descriptions. SQLite is used to store product information and search history.

## 🎯 Project Objectives

- Develop an interactive product recommendation web application.
- Implement product search and category-based filtering.
- Recommend similar products using content-based filtering.
- Integrate SQLite for storing product details and search history.
- Build a responsive and user-friendly interface.
- Evaluate recommendation functionality through automated checks.

## ✨ Features

- **Product Search:** Search products by name or relevant keywords.
- **Category Filtering:** Browse products across different categories.
- **AI-Based Recommendations:** Discover similar products using text similarity.
- **Product Catalog:** View product names, descriptions, categories, and prices.
- **Search History:** Store user search queries in SQLite.
- **Interactive Web Interface:** Browse products through a Flask-powered website.
- **Recommendation Evaluation:** Check recommendation availability, selected-product exclusion, and duplicate IDs.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask | Backend web framework |
| scikit-learn | TF-IDF and cosine similarity |
| SQLite | Database management |
| HTML | Webpage structure |
| CSS | Styling and responsive layout |
| pytest | Automated testing |
| Pandas and NumPy | Data manipulation and numerical operations, where used |
| Joblib | Model artifact persistence, where used |

## 📂 Project Structure

```text
SmartCart-AI/
├── templates/
│   └── index.html
├── static/
│   └── css/
│       └── style.css
├── app.py
├── recommender.py
├── train_model.py
├── database.py
├── evaluate_recommender.py
├── test_recommender.py
├── requirements.txt
├── README.md
└── .gitignore
```

*Note: This lists the main project files. Update the structure if your repository contains additional files or folders.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

Replace the placeholder with your actual GitHub repository URL.

```powershell
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd SmartCart-AI
```

### 2. Create a Virtual Environment

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

If pytest is not included in your requirements file, install it using:

```powershell
python -m pip install pytest
```

## 🗄️ Database Initialization

The application initializes and synchronizes its SQLite database through the database code used by the application.

If `database.py` supports direct execution in your version, you can also run:

```powershell
python database.py
```

The database is intended to store product details in the `products` table and search queries in the `search_history` table.

The local database file `smartcart.db` is excluded from Git tracking and can be generated locally by the application.

## 🤖 Train the Recommendation Model

If your project uses the training script to generate model artifacts, run:

```powershell
python train_model.py
```

Check the script output to confirm that training completed successfully and to identify where the model artifact is saved.

## 🚀 Run the Application

Start the Flask application:

```powershell
python app.py
```

Open the following address in your browser:

http://127.0.0.1:5000

You can now search for products, explore categories, and view similar product recommendations.

## 🧠 How the Recommendation System Works

SmartCart AI uses **content-based filtering** to identify products with similar textual features.

### Step 1: Product Text Preparation

Product titles, categories, and descriptions are used to represent each product as text.

### Step 2: TF-IDF Vectorization

TF-IDF (Term Frequency–Inverse Document Frequency) converts product text into numerical vectors. It assigns weights to terms based on their frequency in a product description and how common they are across the catalog.

### Step 3: Cosine Similarity

Cosine similarity measures how similar two product vectors are. Products with more similar text representations can receive higher similarity scores.

### Step 4: Recommendation Ranking

The system ranks candidate products by similarity and excludes the selected product from its own recommendations.

### Step 5: Display Results

The Flask application displays recommended products through the web interface.

**Limitation:** The current approach uses product content. It does not, by itself, demonstrate learning from actual user purchases, ratings, or individual shopping behavior.

## 🧪 Testing and Evaluation

### 1. Recommendation Evaluation

Run:

```powershell
python evaluate_recommender.py
```

The evaluation script checks that:

- Recommendations are returned.
- The selected product is excluded from its recommendations.
- Duplicate product IDs are not returned.

**Reported result: 30/30 checks passed across 10 products.**

This result confirms that the implemented checks passed. It does not independently measure recommendation relevance or real-world recommendation accuracy.

### 2. Automated Tests with pytest

Run:

```powershell
python -m pytest -v
```

The `test_recommender.py` test suite checks:

- The product catalog is not empty.
- Searching for `headphones` returns results.
- Recommendations exclude the selected product.
- Recommendations contain no duplicate IDs.

**Recorded result: 4 tests passed.**

Run the command again after code changes to verify the current state of your project.

## 📸 Screenshots

Screenshots of the actual running application can be added to a `screenshots/` folder.

Suggested screenshots:

1. Homepage and product catalog
2. Product search results
3. Category filtering
4. Similar product recommendations
5. Recommendation evaluation results

After adding the image files, display them in this section using:

```markdown
![SmartCart AI Homepage](screenshots/homepage.png)

![SmartCart AI Recommendations](screenshots/recommendations.png)
```

Only add these image links once the corresponding screenshot files exist.

## 🔮 Future Enhancements

- Integrate a larger, verified product dataset.
- Evaluate recommendation relevance using ranking metrics.
- Add advanced search filters and pagination.
- Explore user profiles, ratings, and purchase history.
- Improve recommendation personalization.
- Deploy the application online.

## 🎓 Learning Outcomes

This project demonstrates practical work with:

- Python application development
- Flask backend development
- Content-based recommendation techniques
- TF-IDF vectorization and cosine similarity
- SQLite database integration
- Automated testing with pytest
- HTML and CSS web development
- Git and GitHub version control

## 👩‍💻 Author

**Akanksha Samria**

GitHub: https://github.com/akankshasamria
## 📄 License

No license is specified yet. If you intend to distribute this project publicly, choose and add an appropriate open-source license.
