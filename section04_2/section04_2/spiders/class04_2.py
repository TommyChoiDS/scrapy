import scrapy
from .. items import MelonItems


class Test2Spider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['melon.com/chart/index.htm']
    start_urls = ['http://www.melon.com/chart/index.htm']

    def parse(self, response):

        for i in response.css('tbody > tr'):
            item = MelonItems()
            item['rank'] = i.css('td > div > span.rank::text').get()
            item['img_url'] = i.css('img::attr(src)').get()
            item['song_title'] = i.css('div.ellipsis.rank01 a::text').get()
            item['singer'] = i.css('div.ellipsis.rank02 > a::text').get()
            item['album'] = i.css('div.ellipsis.rank03 > a::text').get()
            
            yield item
        