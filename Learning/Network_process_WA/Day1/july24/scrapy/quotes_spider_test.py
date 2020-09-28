from scrapy import Spider, Request

quotes_xpath = ".//div[@class='quote']"

class QuotesSpider(Spider):
    name = "quotes"

    start_urls = ["http://quotes.toscrape.com/"]

    #def start_requests(self):
    #    yield Request(url="http://quotes.toscrape.com", callback=parse)

    def parse(self, response):
        self.log("--- Crawling {}".format(response.url))
        for quote in response.xpath(quotes_xpath): 
            yield {"author": quote.xpath("./span/small[@class='author']/text()").extract_first(),
                   "quote": quote.xpath("./span[@class='text']/text()").extract_first()
            }
        next_page = response.xpath(".//nav/ul/li[@class='next']/a/@href").extract_first()
        next_url = response.urljoin(next_page)
        yield Request(url=next_url, callback=self.parse)
