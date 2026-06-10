# 🎬 Zatch Reel Recommendation Engine

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-API-black?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-purple?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?style=for-the-badge&logo=numpy)

</p>

---

## 📌 Project Overview

Zatch Reel Recommendation Engine is a Hybrid Recommendation System designed to deliver personalized reel recommendations using Machine Learning techniques.

The system combines:

✅ Content-Based Filtering  
✅ User-Based Collaborative Filtering  
✅ Item-Based Collaborative Filtering  
✅ Hybrid Recommendation Strategy

The project exposes recommendation services through a Flask REST API and is designed for cloud deployment using Render.

---

# 🚀 Key Features

### 🎯 Personalized Recommendations

Recommend reels based on user interaction history.

### 🎥 Similar Reel Recommendations

Find reels similar to a given reel using content similarity.

### 👥 User-Based Collaborative Filtering

Recommend content liked by users with similar behavior.

### 📊 Item-Based Collaborative Filtering

Recommend reels that are frequently consumed together.

### 🔥 Trending Reels

Show top-performing reels based on popularity score.

### 🌐 REST API

Production-ready Flask API endpoints.

---

# 🏗️ System Architecture

```text
Raw Data
   │
   ▼
Data Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
Content-Based Model
   │
   ├──────────────┐
   ▼              │
Collaborative     │
Filtering         │
(User + Item)     │
   │              │
   └──────┬───────┘
          ▼
 Hybrid Recommendation Engine
          ▼
       Flask API
          ▼
      End Users
```

---

# 📂 Project Structure

```text
zatch-reel-recommendation-engine/
│
├── app.py
│
├── requirements.txt
├── runtime.txt
├── Procfile
├── README.md
│
├── data/
│   └── processed/
│       ├── bits_cleaned.csv
│       ├── interaction_dataset.csv
│       ├── products_cleaned.csv
│       ├── reelviews_cleaned.csv
│       ├── reel_features.csv
│       ├── users_cleaned.csv
│       └── user_features.csv
│
├── models/
│   ├── content_similarity.pkl
│   ├── item_similarity.pkl
│   ├── reel_indices.pkl
│   └── user_similarity.pkl
│
├── utils/
│   ├── loader.py
│   └── recommender.py
│
└── .gitignore
```

---

# 📊 Dataset Statistics

| Metric | Value |
|----------|----------|
| Total Users | 141 |
| Total Reels | 87 |
| Total Products | 106 |
| Total Interactions | 1659 |
| User Features | 141 × 8 |
| Reel Features | 87 × 8 |
| Interaction Dataset | 1659 × 13 |

---

# 🧹 Data Preprocessing

The preprocessing pipeline performs:

- Missing Value Handling
- Feature Extraction
- Engagement Score Calculation
- Popularity Score Generation
- User Feature Creation
- Reel Feature Creation
- Interaction Dataset Generation

Generated files:

```text
bits_cleaned.csv
users_cleaned.csv
products_cleaned.csv
reelviews_cleaned.csv
user_features.csv
reel_features.csv
interaction_dataset.csv
```

---

# 🤖 Recommendation Models

## 1️⃣ Content-Based Filtering

Uses:

- Title
- Description
- Hashtags

Technique:

```python
TF-IDF Vectorization
+
Cosine Similarity
```

Model Shape:

```text
TF-IDF Matrix:
(87, 772)

Cosine Similarity Matrix:
(87, 87)
```

---

## 2️⃣ User-Based Collaborative Filtering

Uses:

- User-Reel Interaction Matrix
- Cosine Similarity

Matrix Shape:

```text
User-Reel Matrix:
(52, 78)

User Similarity Matrix:
(52, 52)
```

---

## 3️⃣ Item-Based Collaborative Filtering

Uses:

- Reel-User Interaction Matrix
- Cosine Similarity

Matrix Shape:

```text
Item-User Matrix:
(78, 52)

Item Similarity Matrix:
(78, 78)
```

---

## 4️⃣ Hybrid Recommendation System

Combines:

- Content Similarity
- User Similarity
- Item Similarity
- Reel Popularity

Result:

More accurate and robust recommendations.

---

# 📈 Model Performance

### Catalog Coverage

```text
89.66%
```

### Average Interactions Per User

```text
31.90
```

### Engagement Score Statistics

```text
Mean: 28.40
Median: 26.60
Maximum: 125.00
```

---

# 🌐 API Endpoints

## Health Check

```http
GET /health
```

Response:

```json
{
  "service": "recommendation-engine",
  "status": "healthy"
}
```

---

## Dataset Statistics

```http
GET /stats
```

---

## Trending Reels

```http
GET /recommend/trending
```

---

## Similar Reel Recommendations

```http
GET /recommend/reel/<reel_id>
```

Example:

```http
GET /recommend/reel/698e30532c63bfbc04769c5e
```

---

## User Recommendations

```http
GET /recommend/user/<user_id>
```

Example:

```http
GET /recommend/user/69f8608068f7e97ef44183e4
```

---

# 🛠️ Tech Stack

### Programming

- Python

### Data Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-Learn

### Backend

- Flask

### Deployment

- Render
- Gunicorn

### Version Control

- Git
- GitHub

---

# 📸 Sample Outputs

### Trending Recommendations

```json
[
  {
    "title": "Maheshwari silk sarees",
    "reel_popularity_score": 38.01
  }
]
```

### Similar Reels

```json
[
  {
    "title": "Mens formal shirts"
  }
]
```

### Personalized Recommendations

```json
[
  {
    "title": "6*8 Classic Photo frame"
  }
]
```

---

# 👨‍💻 Author

### Rutujaa Murkute

Data Science | Machine Learning | Recommendation Systems

---

# ⭐ If you found this project useful

Please consider giving it a Star ⭐ on GitHub.

It helps support the project and motivates future improvements.
