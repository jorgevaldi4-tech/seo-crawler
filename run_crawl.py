from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.spider import JorgeSpider
import os

# Set the path to settings
os.environ['SCRAPY_SETTINGS_MODULE'] = 'crawler.settings'

process = CrawlerProcess(get_project_settings())
process.crawl(JorgeSpider)
process.start()