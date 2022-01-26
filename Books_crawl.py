import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

                                                         ## scrapy genspider -t crawl Books_crawl +website links !!!       to create crawl Spider template
                                                         ## scrapy runspider Books_crawl.py    !!!             to run/execute  the code

class BooksCrawlSpider(CrawlSpider):
    name = 'Books_crawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/page-3.html']

    le_book_detail = LinkExtractor(restrict_css='h3 > a')
    rules_books_detail = Rule(le_book_detail, callback='parse_item', follow=True)
                                                                                ## True mean all links in links  && False means only links data  !!!

    rules =(
        rules_books_detail,
    )

    def parse_item(self, response):
        Books_data = {
            "Name ": response.css('h1::text').get(),
            "Price ": response.css('.price_color::text').get()
        }
        yield Books_data