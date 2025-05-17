import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load data
df = pd.read_csv('movies.csv')

# Vectorize descriptions
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# Recommendation function
def recommend(title, n=5):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Streamlit UI
st.title("🎬 Movie Recommendation System")
st.markdown("Get movie suggestions based on your favorite.")

selected_movie = st.selectbox("Choose a movie you like:", df['title'].values)

if st.button("Recommend"):
    st.subheader("You might also like:")
    recommendations = recommend(selected_movie)
    for movie in recommendations:
        st.write("✅", movie)
