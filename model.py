import pandas as pd
import ast
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Datasets


movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

print("Movies Dataset Shape:", movies.shape)
print("Credits Dataset Shape:", credits.shape)


# Merge Datasets


movies = movies.merge(credits, on="title")

print("\nMerged Dataset Shape:", movies.shape)


# Select Required Columns


movies = movies[
    [
        "movie_id",
        "title",
        "overview",
        "genres",
        "keywords",
        "cast",
        "crew"
    ]
]

print("\nSelected Columns:")
print(movies.head())


# Remove Missing Values


print("\nMissing Values:")
print(movies.isnull().sum())

movies.dropna(inplace=True)

print("\nAfter Removing Missing Values:")
print(movies.shape)


# Helper Functions


def convert(text):
    L = []

    for i in ast.literal_eval(text):
        L.append(i["name"])

    return L


def fetch_director(text):
    L = []

    for i in ast.literal_eval(text):
        if i["job"] == "Director":
            L.append(i["name"])

    return L


def fetch_cast(text):
    L = []

    counter = 0

    for i in ast.literal_eval(text):

        if counter < 3:

            L.append(i["name"])
            counter += 1

        else:

            break

    return L

def collapse(L):
    return [i.replace(" ", "") for i in L]    

# Data Preprocessing


movies["genres"] = movies["genres"].apply(convert)

movies["keywords"] = movies["keywords"].apply(convert)

movies["cast"] = movies["cast"].apply(fetch_cast)

movies["crew"] = movies["crew"].apply(fetch_director)

# Convert overview to list
movies["overview"] = movies["overview"].apply(lambda x: x.split())
movies["genres"] = movies["genres"].apply(collapse)

movies["keywords"] = movies["keywords"].apply(collapse)

movies["cast"] = movies["cast"].apply(collapse)

movies["crew"] = movies["crew"].apply(collapse)


movies["tags"] = (
    movies["overview"] +
    movies["genres"] +
    movies["keywords"] +
    movies["cast"] +
    movies["crew"]
)

new_df = movies[["movie_id", "title", "tags"]].copy()

new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x))

new_df["tags"] = new_df["tags"].apply(lambda x: x.lower())

print(new_df.head())

cv = CountVectorizer(max_features=5000, stop_words="english")

vectors = cv.fit_transform(new_df["tags"]).toarray()

print("\nVector Shape:")
print(vectors.shape)

similarity = cosine_similarity(vectors).astype(np.float32)

print("\nSimilarity Matrix Shape:")
print(similarity.shape)

def recommend(movie):

    movie_index = new_df[new_df["title"] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    print("\nRecommended Movies:\n")

    for i in movies_list:

        print(new_df.iloc[i[0]].title)

recommend("Avatar") 
# Save processed dataframe
pickle.dump(new_df, open("models/movies.pkl", "wb"))

# Save similarity matrix
pickle.dump(similarity, open("models/similarity.pkl", "wb"))

print("\nModels saved successfully!")       


# Check Output

print("\nGenres:")
print(movies["genres"].head())

print("\nKeywords:")
print(movies["keywords"].head())

print("\nCast:")
print(movies["cast"].head())

print("\nDirector:")
print(movies["crew"].head())

print("\nProcessed Dataset:")
print(new_df.head())