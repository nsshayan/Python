import scrapy

class Quotes(scrapy.Item):
    author = scrapy.Field()
    quote = scrapy.Field()


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            #yield {
            #    'text': quote.css('span.text::text').extract_first(),
            #    'author': quote.xpath('span/small/text()').extract_first(),
            #}
            yield Quotes(quote=quote.css('span.text::text').extract_first(),
                         #author=quote.css('span small::text').extract_first())
                         author=quote.xpath('span/small/text()').extract_first())

        # next_page = response.xpath("./li[@class='next']/a/@href").extract_first()
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
