import pandas as pd
import streamlit as st
import psycopg2

st.title("MovieLens Streaming Analytics Dashboard")

DB_NAME = "chichi"
DB_USER = "chichi"
DB_HOST = "localhost"
DB_PORT = 5432

@st.cache_data
def run_query(query: str) -> pd.DataFrame:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        host=DB_HOST,
        port=DB_PORT,
    )
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

st.subheader("Top Movies by Rating Volume")
top_movies = run_query("""
SELECT
  d.title,
  COUNT(*) AS ratings_count,
  ROUND(AVG(f.rating), 2) AS avg_rating
FROM fact_rating f
JOIN dim_movie d ON f.movie_id = d.movie_id
GROUP BY d.title
ORDER BY ratings_count DESC
LIMIT 10;
""")
st.dataframe(top_movies)

st.subheader("Daily Metrics (last 30 days)")
daily = run_query("""
SELECT rating_date, ratings_count, active_users, ROUND(avg_rating, 2) AS avg_rating
FROM daily_metrics
ORDER BY rating_date DESC
LIMIT 30;
""")
st.dataframe(daily)

st.subheader("Genre Performance (Top 15)")
genres = run_query("""
SELECT genre, ratings_count, ROUND(avg_rating, 2) AS avg_rating
FROM genre_performance
ORDER BY ratings_count DESC
LIMIT 15;
""")
st.dataframe(genres)
