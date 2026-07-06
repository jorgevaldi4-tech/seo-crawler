import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SEO Intelligence Dashboard", layout="wide")
st.title("SEO Intelligence Dashboard - Jorgesellscars.com")

conn = sqlite3.connect('/home/appjorge/seo-crawler/database/crawler_data.db')
df = pd.read_sql_query("SELECT * FROM crawl_results", conn)
conn.close()

st.metric("Total Pages Crawled", len(df))

# Status Code Distribution
fig = px.pie(df, names='status_code', title="Site Health (Status Codes)")
st.plotly_chart(fig)

# Show data table
st.subheader("Crawl Data Explorer")
st.dataframe(df)