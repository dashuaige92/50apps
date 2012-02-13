from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.loader import XPathItemLoader

from webcrawler.items import HNItem

class DeepSpider(BaseSpider):
    name = 'hackernews'
    allowed_domains = ['hackernews.com', 'ycombinator.com']
    start_urls = ['http://news.ycombinator.com']

    def parse(self, response):
        #filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)

        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//td[@class="title"]')
        items = []
        for site in sites:
           item = HNItem()
           item['name'] = site.select('a/text()').extract()
           item['link'] = site.select('a/@href').extract()
           #item['description'] = site.select('text()').extract()
           items.append(item)
        return items
