# -*- coding: utf-8 -*-
import scrapy


class GeventProjectsSpider(scrapy.Spider):
    name = 'gevent_projects'
    allowed_domains = ['pypi.org']
    start_urls = ['http://pypi.org/search?q=gevent']

    def parse(self, response):
        for project in response.xpath(".//a[@class='package-snippet"):
            yield PyPiScrapperItem(
                    name=project.xpath("./h3/span/text()").extract_first()
                    description=project.xpath("./p/text()").extract_first()
                    url=project.xpath("./@href").extract_first())

        if response.xpath(".//
        next_url = response
