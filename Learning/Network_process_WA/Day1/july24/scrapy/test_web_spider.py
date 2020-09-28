# -*- coding: utf-8 -*-
import scrapy


class TestWebSpiderSpider(scrapy.Spider):
    name = "test_web_spider"
    allowed_domains = ["www.chandrashekar.info"]
    start_urls = ['http://www.chandrashekar.info/']

    def parse(self, response):
        pass
