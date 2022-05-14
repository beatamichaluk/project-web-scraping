#Libraries
import scrapy
import csv
import pandas as pd

#Creating class for characteristics of each player - name (and surname), number of played matches, number of matches started on the bench and minutes played in all matches
class Players(scrapy.Item):
    name        = scrapy.Field()
    matches        = scrapy.Field()
    bench        = scrapy.Field()
    minutes        = scrapy.Field()

#This part of the code help to read links from CSV file - Pandas library required    
df = pd.read_csv('links.csv')
urls = df['link'].values.tolist()

#This part of a code extract final data from webpages
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
