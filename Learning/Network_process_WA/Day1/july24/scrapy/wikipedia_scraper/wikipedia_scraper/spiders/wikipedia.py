# -*- coding: utf-8 -*-
import scrapy


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.com"]
    start_urls = ['http://en.wikipedia.com/']

    def parse(self, response):
        pass
