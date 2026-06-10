from flask import Flask
from flask import jsonify

from utils.recommender import (
    recommend_similar_reels,
    recommend_trending_reels,
    recommend_new_user
)
from utils.loader import (
    bits_df,
    users_df,
    interaction_df
)
from utils.recommender import (
    recommend_similar_reels,
    recommend_trending_reels,
    recommend_new_user,
    recommend_for_user
)

app = Flask(__name__)


# ==================================
# HOME
# ==================================

@app.route("/")

def home():

    return {
        "project":
        "Zatch Reel Recommendation Engine",

        "status":
        "running"
    }

@app.route("/health")
def health():

    return {
        "status": "healthy",
        "service": "recommendation-engine"
    }
@app.route("/stats")
def stats():

    return {

        "users":
        int(users_df.shape[0]),

        "reels":
        int(bits_df.shape[0]),

        "interactions":
        int(interaction_df.shape[0])
    }
# ==================================
# REEL RECOMMENDATION
# ==================================

@app.route(
    "/recommend/reel/<reel_id>"
)

def recommend_reel(
    reel_id
):

    results = recommend_similar_reels(
        reel_id
    )

    return jsonify(results)


# ==================================
# TRENDING
# ==================================

@app.route(
    "/recommend/trending"
)

def trending():

    return jsonify(
        recommend_trending_reels()
    )


# ==================================
# NEW USER
# ==================================

@app.route(
    "/recommend/new-user"
)

def new_user():

    return jsonify(
        recommend_new_user()
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )



# ==================================
# User Recommendation Route
# ==================================

@app.route(
    "/recommend/user/<user_id>"
)
def user_recommendation(
    user_id
):

    return jsonify(

        recommend_for_user(
            user_id
        )
    )    