import scrapy
import csv
import pandas as pd

class Players(scrapy.Item):
    name        = scrapy.Field()
    matches        = scrapy.Field()
    bench        = scrapy.Field()
    minutes        = scrapy.Field()

df = pd.read_csv('links.csv')
urls = df['link'].values.tolist()

class LinksSpider(scrapy.Spider):
    name = 'players'
    allowed_domains = ['http://www.hppn.pl']
    start_urls = urls[0:]
               
    def parse(self, response):
        p = Players()

        name_xpath       = '//div[text()="Imię nazwisko »"]/following-sibling::*/text()'
        matches_xpath       = '//td[text()="Mecze »"]/following-sibling::*/text()'
        bench_xpath       = '//td[text()="Mecze rozpoczęte na ławce »"]/following-sibling::td[1]/text()'
        minutes_xpath       = '//td[text()="Minuty na boisku »"]/following-sibling::*/text()'
        
        p['name']        = response.xpath(name_xpath).getall()
        p['matches']        = response.xpath(matches_xpath).getall()
        p['bench']        = response.xpath(bench_xpath).getall()
        p['minutes']        = response.xpath(minutes_xpath).getall()
        yield p
