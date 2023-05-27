import scrapy

class Musican(scrapy.Item):
    name = scrapy.Field()
    years_active = scrapy.Field()

class LinkSpider(scrapy.Spider):
    name = 'musicians'
    allowed_domains = ['https://en.wikipedia.org/']
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        m = Musican()

        name_xpath = '//h1/span/text()'
        years_active_xpath = '//span[text()="Years active"]/ancestor::th/following-sibling::*/text()'

        m['name'] = response.xpath(name_xpath).getall()
        m['years_active'] = response.xpath(years_active_xpath).getall()

        yield m