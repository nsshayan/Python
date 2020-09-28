# -*- coding: utf-8 -*-
import scrapy


class TestspiderSpider(scrapy.Spider):
    name = "testspider"
    allowed_domains = ["http://www.chandrashekar.info"]
    start_urls = ['http://http://www.chandrashekar.info/']

    def parse(self, response):
        pass
