import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class JorgeSpider(CrawlSpider):
    name = "jorgesellscars"
    allowed_domains = ["jorgesellscars.com"]
    start_urls = ["https://jorgesellscars.com"]

    # Rule: Follow all internal links
    rules = (
        Rule(LinkExtractor(allow_domains=("jorgesellscars.com",)), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'url': response.url,
            'title': response.css('title::text').get() or 'No Title',
            'meta_description': response.xpath('//meta[@name="description"]/@content').get() or 'No Description',
            'status_code': response.status,
        }