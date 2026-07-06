import sqlite3
import pandas as pd

DB_PATH = "/home/appjorge/seo-crawler/database/crawler_data.db"

def run_technical_audit():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM crawl_results", conn)
    conn.close()

    # Identify broken links (Anything not status code 200)
    broken_links = df[df['status_code'] != 200]
    
    print(f"--- Technical SEO Audit ---")
    print(f"Pages with Issues: {len(broken_links)}")
    
    if not broken_links.empty:
        print("\nBroken Link Report:")
        print(broken_links[['url', 'status_code']])
    else:
        print("No broken links detected! Your site structure is healthy.")

if __name__ == "__main__":
    run_technical_audit()