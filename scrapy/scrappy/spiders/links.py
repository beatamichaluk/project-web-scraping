import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'links'
    allowed_domains = ['http://www.hppn.pl']
    start_urls = ['http://www.hppn.pl/reprezentacja/pilkarze']

    def parse(self, response):
        xpath = '/html/body/div[2]/div[1]/div[2]/div[2]/div[2]/section/div[2]/div[2]/table[1]/tbody/tr/td[2]/a/@href'
        selection = response.xpath(xpath)
        for s in selection[::2]:
            l = Link()
            l['link'] = 'http://www.hppn.pl' + s.get()
            print(l)
            yield l
