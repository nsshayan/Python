from parsel import Selector
sel = Selector(text=u"""<html>
                       <body>
                           <h1>Hello, Parsel!</h1>
                           <ul>
                               <li><a href="http://example.com">Link 1</a></li>
                               <li><a href="http://scrapy.org">Link 2</a></li>
                           </ul
                       </body>
                       </html>""")
print sel.css('h1::text').extract_first()
print sel.css('h1::text').re('\w+')
for e in sel.css('ul > li'):
    print(e.xpath('.//a/@href').extract_first())

