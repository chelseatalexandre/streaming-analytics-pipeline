Streaming Analytics Pipeline & Dashboard

This project demonstrates an end-to-end analytics workflow using Python, PostgreSQL, and Streamlit.
Raw MovieLens datasets are ingested, transformed into structured analytics tables, and queried to produce insights on user activity, rating trends, and genre performance.
The final output is an interactive Streamlit dashboard that visualizes:
Top movies by rating volume and average score
Daily engagement metrics over time
Genre-level performance comparisons
This project simulates a real data engineering and analytics pipeline, showcasing database design, SQL querying, and dashboard development in a production-style workflow.

# MovieLens Streaming Analytics Pipeline & Dashboard

An end to end analytics project that ingests MovieLens data, transforms it into structured tables, and serves insights through an interactive Streamlit dashboard.

## What this project does
- Loads raw MovieLens CSV files
- Cleans and transforms the data into analysis friendly tables
- Produces metrics like top movies by rating volume, average ratings, and daily activity trends
- Displays results in a Streamlit dashboard

## Tech stack
- Python
- Pandas
- Streamlit
- PostgreSQL (optional depending on your setup)

## Project structure
- `dashboard.py` Streamlit dashboard app
- `data/` raw input files and assets used by the project
- `screenshots/` dashboard screenshots for README visuals

## How to run locally
1. Clone the repo
```
git clone https://github.com/chelseatalexandre/streaming-analytics-pipeline.git
cd streaming-analytics-pipeline
```
2. Install dependencies
```
python3 -m pip install -r requirements.txt
```
3.Run the Streamlit dashboard
```
python3 -m streamlit run dashboard.py


