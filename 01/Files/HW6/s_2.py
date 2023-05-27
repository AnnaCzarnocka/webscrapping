import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'links'
    allowed_domains = ['https://en.wikipedia.org/']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_acid_rock_artists']
    try:
        with open("link_lists.csv", "rt") as f:
            start_urls = [url.strip() for i, url in enumerate(f.readlines()) if i == 1]
    except:
        start_urls = []

    def parse(self, response):
        print(response)
        xpath = '//span[@id="Artists"]/ancestor::h2/following-sibling::div[1]/ul/li/a/@href'
        selection = response.xpath(xpath)
        for s in selection:
            l = Link()
            l['link'] ='https://en.wikipedia.org/' + s.get()
            print(l)
            yield l