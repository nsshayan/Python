# -*- coding: utf-8 -*-
import scrapy


class ChandraSpider(scrapy.Spider):
    name = "chandra"
    allowed_domains = ["chandrashekar.info"]
    start_urls = ['http://www.chandrashekar.info/']

    def parse(self, response):
        print(response.css("title"))
