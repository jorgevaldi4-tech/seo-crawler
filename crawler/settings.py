BOT_NAME = 'seo_crawler'
SPIDER_MODULES = ['crawler']
NEWSPIDER_MODULE = 'crawler'

# Pipeline configuration
ITEM_PIPELINES = {
    'crawler.pipelines.SQLitePipeline': 300,
}

# Standard crawler behavior
ROBOTSTXT_OBEY = False
USER_AGENT = 'JorgeSellsCars-SEO-Bot/1.0'
CONCURRENT_REQUESTS = 4