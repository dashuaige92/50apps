from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class Spider(BaseSpider):
    def __init__(self, name, url):
        self.name = name
        self.allowed_domains = []
        self.start_urls = [url]

