import sqlite3
import pandas as pd
import json

with open('/home/appjorge/seo-crawler/config/config.json', 'r') as f:
    config = json.load(f)

KEYWORDS = config['keywords']

def generate_recommendations():
    conn = sqlite3.connect(config['database_path'])
    df = pd.read_sql_query("SELECT url, title FROM crawl_results", conn)
    conn.close()

    print(f"--- SEO Optimization Opportunities ---")
    # Identify pages without our primary local keywords
    for kw in KEYWORDS:
        mask = ~df['title'].str.contains(kw, case=False, na=False)
        missing_kw_df = df[mask].head(3)
        
        if not missing_kw_df.empty:
            print(f"\nOpportunities for '{kw}':")
            for _, row in missing_kw_df.iterrows():
                print(f"Update: {row['url']}")
                print(f"Suggested Title: {row['title']} | {kw.upper()} in Newark, NJ")

if __name__ == "__main__":
    generate_recommendations()