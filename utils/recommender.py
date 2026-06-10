import pandas as pd

from utils.loader import (
    bits_df,
    interaction_df,
    cosine_sim,
    indices
)


# ==================================
# CONTENT BASED
# ==================================

def recommend_similar_reels(
    reel_id,
    top_n=5
):

    if reel_id not in indices.index:
        return []

    idx = indices[reel_id]

    sim_scores = list(
        enumerate(
            cosine_sim[idx]
        )
    )

    sim_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )

    sim_scores = sim_scores[1:top_n+1]

    reel_indices = [
        i[0]
        for i in sim_scores
    ]

    result = bits_df.iloc[
        reel_indices
    ][
        [
            "_id",
            "title"
        ]
    ]

    return result.to_dict(
        orient="records"
    )


# ==================================
# TRENDING REELS
# ==================================

def recommend_trending_reels(
    top_n=10
):

    result = bits_df.sort_values(

        by="reel_popularity_score",

        ascending=False

    ).head(top_n)

    return result[
        [
            "_id",
            "title",
            "reel_popularity_score"
        ]
    ].to_dict(
        orient="records"
    )


# ==================================
# NEW USER
# ==================================

def recommend_new_user():

    return recommend_trending_reels()

def get_user_history(
    user_id
):

    user_data = interaction_df[

        interaction_df["userId"] == user_id

    ]

    watched = user_data[
        "bitId"
    ].unique()

    return list(watched)

def recommend_for_user(
    user_id,
    top_n=5
):

    watched = get_user_history(
        user_id
    )

    if len(watched) == 0:

        return recommend_trending_reels(
            top_n
        )

    recommendations = []

    for reel_id in watched:

        if reel_id in indices.index:

            idx = indices[reel_id]

            sim_scores = list(
                enumerate(
                    cosine_sim[idx]
                )
            )

            sim_scores = sorted(
                sim_scores,
                key=lambda x: x[1],
                reverse=True
            )

            sim_scores = sim_scores[
                1:3
            ]

            for i in sim_scores:

                recommendations.append(
                    i[0]
                )

    recommendations = list(
        set(
            recommendations
        )
    )

    result = bits_df.iloc[
        recommendations
    ]

    result = result[
        ~result["_id"].isin(
            watched
        )
    ]

    return result[
        [
            "_id",
            "title",
            "reel_popularity_score"
        ]
    ].head(
        top_n
    ).to_dict(
        orient="records"
    )