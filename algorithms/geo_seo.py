import sqlite3
import pandas as pd
import json

# Load config for keywords
with open('/home/appjorge/seo-crawler/config/config.json', 'r') as f:
    config = json.load(f)

KEYWORDS = config['keywords']
DB_PATH = config['database_path']

def analyze_geo_presence():
    conn = sqlite3.connect(DB_PATH)
    # We will search titles for our target local keywords
    df = pd.read_sql_query("SELECT title FROM crawl_results", conn)
    conn.close()

    print(f"--- Local SEO Keyword Presence ---")
    for kw in KEYWORDS:
        count = df['title'].str.contains(kw, case=False, na=False).sum()
        print(f"Pages containing '{kw}': {count}")

if __name__ == "__main__":
    analyze_geo_presence()