import scrapy
import json
import shelve

links_info = shelve.open("links.dat")

processed_links = set()

class SimpleSpider(scrapy.Spider):
    name = 'simple'
    start_urls = ['https://www.chandrashekar.info/']

    def parse(self, response):
        if response.status != 200:
            links_info[response.url] = "broken"

        links = { link.extract() for link in response.selector.xpath("//a/@href") }
        links = { link for link in links if not link.startswith("http://") and
                 len(link) > 1 and link not in processed_links }

        links_info.update([(link, "processed") for link in links ])

        for link in links:
            print(">>>>> Sending request for", link)
            next_page = response.urljoin(link)
            yield scrapy.Request(next_page, callback=self.parse)



        #yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
