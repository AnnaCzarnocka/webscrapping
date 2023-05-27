import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinkSpider(scrapy.Spider):
    name = 'link_lists'
    allowed_domains = ['https://en.wikipedia.org/']
    start_urls = ['https://en.wikipedia.org/wiki/Lists_of_musicians']

    def parse(self, response):
        xpath = '//span[@id="A"]/ancestor::h3/following-sibling::div[1]/ul/li/a/@href'
        selection = response.xpath(xpath)

        for s in selection:
            l = Link()
            l['link'] = 'https://en.wikipedia.org' + s.get()
            yield l