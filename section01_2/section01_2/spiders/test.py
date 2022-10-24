import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com/']

    def parse(self, response):
        pass
