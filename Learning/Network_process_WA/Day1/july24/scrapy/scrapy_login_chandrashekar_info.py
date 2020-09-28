import scrapy

class LoginTest(scrapy.Spider):
    name = "login_test"
    start_urls = ["http://www.chandrashekar.info/user/login"]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
                        response,
                        formdata={'name': 'testuser', 'pass': 'w3lc0me'},
                        callback=self.after_login
                    )

    def after_login(self, response):
        # check login succeed before going on
        if b"unrecognized username" in response.body:
           self.logger.error("Login failed")
           return
        return scrapy.Request("http://www.chandrashekar.info/node/add/blog",
                              callback=self.create_blog_post)

    def create_blog_post(self, response):
        return scrapy.FormRequest.from_response(
                response,
                formdata={
                       "title"                 :  "Hello world October 4th blog",
                       "body[und][0][value]"   :  "this is a blog message sdlkf ksdj lksdfj",
                       "op": "Save"
              }, callback=self.blog_created)

    def blog_created(self, response):
        print("Blog created...")
        return

