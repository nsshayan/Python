from scrapy import Spider, Item, Field, XPathItemLoader
 
 
class QuestionItem(Item):
    """Stack Overflow Questions"""
    title = Field()
    summary = Field()
    tags = Field()
 
    user = Field()
    posted = Field()
 
    votes = Field()
    answers = Field()
    views = Field()
 
 
class MySpider(Spider):
    """Stackoverflow Crawler"""
    name = "sospider"
    start_urls = ["http://stackoverflow.com/questions"]
 
    question_list_xpath = '//div[@id="content"]//div[contains(@class, "question-summary")]'
 
    def parse(self, response):
 
        for qxs in response.xpath(self.question_list_xpath):
            ques = QuestionItem(
                        title=qxs.xpath('.//h3/a/text()'),
                        summary=qxs.xpath('.//h3/a/@title'),
                        tags=qxs.xpath('.//a[@rel="tag"]/text()'),
                        user=qxs.xpath('.//div[@class="started"]/a[2]/text()'),
                        posted=qxs.xpath('.//div[@class="started"]/a[1]/span/@title'),
                        votes=qxs.xpath('.//div[@class="votes"]/div[1]/text()'),
                        answers=qxs.xpath('.//div[contains(@class, "answered")]/div[1]/text()'),
                        views=qxs.xpath('.//div[@class="views"]/div[1]/text()'))
           
            yield ques
