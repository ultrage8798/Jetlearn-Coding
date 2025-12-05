# recommendation system

import pandas as pd

data = pd.read_csv("movies_metadata.csv")

print(data.head())
print(data.shape)

"""
Weighted Rating - (v/v+m)*R + (m/v+m)*C
v is the number of votes (vote_count)
m is the minimum votes required to be listed in chart
R is the average rating for the movie (vote_average)
C is the mean vote across the whole report
"""
m = data["vote_count"].quantile(0.90)
print(m)


c = data["vote_average"].mean()
print(c)

q_movies = data.copy().loc[data["vote_count"]>=m]
print(q_movies.shape)

def weighted_rating(x):
    v = x["vote_count"]
    r = x["vote_average"]
    return (v/(v+m)*r) + (m/(m+v)*c)

q_movies["score"] = q_movies.apply(weighted_rating,axis = 1)
q_movies = q_movies.sort_values("score", ascending = False)

print("Top 10 Movies:")
print(q_movies[["title","vote_count","vote_average","score"]].head(10))