# -*- coding: utf-8 -*-
import scrapy


class TestWebsiteSpiderSpider(scrapy.Spider):
    name = 'test_website_spider'
    allowed_domains = ['www.chandrashekar.info']
    start_urls = ['http://www.chandrashekar.info/']

    def parse(self, response):
        pass
