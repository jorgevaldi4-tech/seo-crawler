import sqlite3

class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('/home/appjorge/seo-crawler/database/crawler_data.db')
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT INTO crawl_results (url, title, meta_description, status_code)
            VALUES (?, ?, ?, ?)
        ''', (item.get('url'), item.get('title'), item.get('meta_description'), item.get('status_code')))
        self.conn.commit()
        return item