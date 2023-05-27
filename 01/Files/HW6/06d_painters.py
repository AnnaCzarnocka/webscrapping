# -*- coding: utf-8 -*-
import scrapy

class Painter(scrapy.Item):
    name        = scrapy.Field()
    birth       = scrapy.Field()
    death       = scrapy.Field()
    nationality = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'painters'
    allowed_domains = ['https://en.wikipedia.org/']
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        p = Painter()

        name_xpath        = '//h1/span/text()'
        birth_xpath       = '//th[text()="Born"]/following-sibling::*/text()'
        death_xpath       = '//th[text()="Died"]/following-sibling::*/text()[1]'
        nationality_xpath = '//th[text()="Nationality"]/following-sibling::*/a/text()'

        p['name']        = response.xpath(name_xpath).getall()
        p['birth']       = response.xpath(birth_xpath).getall()
        p['death']       = response.xpath(death_xpath).getall()
        p['nationality'] = response.xpath(nationality_xpath).getall()

        yield p
