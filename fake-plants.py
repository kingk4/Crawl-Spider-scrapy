import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PlantsCrawlSpider(CrawlSpider):
    name = 'Plants_crawl'
    allowed_domains = ['www.fake-plants.co.uk']
    start_urls = ['https://www.fake-plants.co.uk']

    le_plants_detail = LinkExtractor(restrict_css='.product-category > a')

    rules_plants_detail = Rule(le_plants_detail, callback='parse_item', follow=True)
    rules =(
        rules_plants_detail,
    )

    def parse_item(self, response):
        plant_list = response.css('.type-product')
        for plants in plant_list:
            dict ={
                "Category ": plants.css('.ast-woo-product-category::text').get(),
                "Plant Name" : plants.css('.woocommerce-loop-product__title::text').get()
            }
            yield dict


