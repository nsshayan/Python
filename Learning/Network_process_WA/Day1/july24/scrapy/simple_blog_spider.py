import scrapy
import json

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def __init__(self, *args, **kwargs):
        scrapy.Spider.__init__(self, *args, **kwargs)
        self.result_file = open("result.json", "w")

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            rec = {'title': title.css('a ::text').extract_first()}
            json.dump(rec, self.result_file)
            yield rec

        next_page = response.css('div.prev-post > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
