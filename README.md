# Streaming Analytics Pipeline & Dashboard

Python | SQL | PostgreSQL | Streamlit

An end-to-end analytics pipeline that ingests MovieLens datasets, transforms rating data using Python and SQL, and visualizes engagement insights through an interactive Streamlit dashboard.

## Dashboard Preview

![Dashboard Screenshot](screenshots/main.dashboard.png)

Example Streamlit dashboard displaying movie rating trends and engagement metrics.

## Project Architecture

Raw MovieLens CSV Files  
↓  
Data Cleaning & Transformation (Python, Pandas)  
↓  
Analytics Processing & Aggregations (SQL / Pandas)  
↓  
Interactive Visualization Dashboard (Streamlit)

---

## Skills Demonstrated

- Data cleaning and transformation with Pandas  
- SQL analytics queries for rating dataset insights 
- Data pipeline workflow from ingestion to visualization  
- Interactive dashboard development using Streamlit  
- Data visualization of user engagement and rating trends  

---

## Dataset

This project uses the **MovieLens dataset** provided by the GroupLens Research Lab.

https://grouplens.org/datasets/movielens/

---

## What this project does

- Loads raw MovieLens CSV files  
- Cleans and transforms the data into analysis-friendly tables  
- Produces metrics like top movies by rating volume, average ratings, and daily activity trends  
- Displays results in a Streamlit dashboard

## Example Metrics Generated

- Top movies by rating volume
- Average movie ratings across the dataset
- Daily rating activity trends
- Genre-level performance comparisons

---

## Key Insights

The dashboard enables exploration of:

- Highly rated movies with strong engagement
- User rating activity trends over time
- Genre performance comparisons
- Popular titles with high rating volume

## Tech Stack

- Python  
- Pandas  
- Streamlit  
- PostgreSQL (optional depending on your setup)  

---

## Project Structure

dashboard.py – Streamlit dashboard application  
data/ – raw MovieLens dataset files  
screenshots/ – images used for README previews  
requirements.txt – Python dependencies

## How to Run Locally

Clone the repository

```bash
git clone https://github.com/chelseatalexandre/streaming-analytics-pipeline.git
```
Navigate into the project directory

```bash
cd streaming-analytics-pipeline
```
Install dependencies

```bash
python3 -m pip install -r requirements.txt
```
Run the Streamlit dashboard

```bash
python3 -m streamlit run dashboard.py
```
