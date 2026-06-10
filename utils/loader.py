import pickle
import pandas as pd


# =========================
# LOAD DATA
# =========================

bits_df = pd.read_csv(
    "data/processed/bits_cleaned.csv"
)

users_df = pd.read_csv(
    "data/processed/users_cleaned.csv"
)

interaction_df = pd.read_csv(
    "data/processed/interaction_dataset.csv"
)


# =========================
# LOAD MODELS
# =========================

with open(
    "models/content_similarity.pkl",
    "rb"
) as f:

    cosine_sim = pickle.load(f)


with open(
    "models/user_similarity.pkl",
    "rb"
) as f:

    user_similarity = pickle.load(f)


with open(
    "models/item_similarity.pkl",
    "rb"
) as f:

    item_similarity = pickle.load(f)


with open(
    "models/reel_indices.pkl",
    "rb"
) as f:

    indices = pickle.load(f)


print("Data & Models Loaded Successfully")