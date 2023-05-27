################################################################################
# Scrapy xpath playground
################################################################################
# This program allows for playing with xpaths extraction,
# and testing them for specific sites.
from scrapy import Selector
from urllib import request

################################################################################
# Testing link_list file:
url = 'https://en.wikipedia.org/wiki/List_of_painters_by_name'
html = request.urlopen(url)
sel = Selector(text=html.read(), type="html")

xpath = '//a[re:test(@title, "List of painters.*")]//@href'
sel.xpath(xpath).getall()

################################################################################
# Testing links file:
url = 'http://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22M%22'
html = request.urlopen(url)
sel = Selector(text=html.read(), type="html")

xpath = '(//ul)[2]/li/a/@href'
sel.xpath(xpath).getall()

################################################################################
# Testing painter file:
url = 'https://en.wikipedia.org/wiki/Edvard_Munch'
html = request.urlopen(url)
sel = Selector(text=html.read(), type="html")

name_xpath        = '//h1/text()'
sel.xpath(name_xpath).getall()

birth_xpath       = '//th[text()="Born"]/following-sibling::*/text()'
sel.xpath(birth_xpath).getall()

death_xpath       = '//th[text()="Died"]/following-sibling::*/text()[1]'
sel.xpath(death_xpath).getall()

nationality_xpath = '//th[text()="Nationality"]/following-sibling::*/a/text()'
sel.xpath(nationality_xpath).getall()

