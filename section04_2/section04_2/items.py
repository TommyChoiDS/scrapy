# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MelonItems(scrapy.Item):
    rank = scrapy.Field()
    img_url = scrapy.Field()
    song_title = scrapy.Field()
    singer = scrapy.Field()
    album = scrapy.Field()
    likes = scrapy.Field()
    lyrics = scrapy.Field()
    is_pass = scrapy.Field()
