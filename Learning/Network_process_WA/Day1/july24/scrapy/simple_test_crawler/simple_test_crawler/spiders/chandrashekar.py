# -*- coding: utf-8 -*-
import scrapy


class ChandrashekarSpider(scrapy.Spider):
    name = "chandrashekar"
    allowed_domains = ["www.chandrashekar.info"]
    start_urls = [ 'http://www.chandrashekar.info/']

    def __init__(self, *args, **kwargs):
        scrapy.Spider.__init__(self, *args, **kwargs)
        self.broken_links = open("broken_links.txt", "a")
        self.visited = set()
        self.broken = set()

    def parse(self, response):
        print("||||Handling", response.url)
        if response.status != 200:
            print("****** Broken link:", response.url)
            self.broken.add(response.url)
            print(response.url, file=self.broken_links)
            return

        for link in response.xpath(".//a/@href").extract():
            next_page = response.urljoin(link)
            with open("visited.txt", "a") as v:
                print(next_page, file=v)

            if next_page not in self.visited:
                self.visited.add(next_page)
                print(">>>> Crawling", next_page)
                yield scrapy.Request(next_page, callback=self.parse)

