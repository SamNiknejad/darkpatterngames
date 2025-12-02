import scrapy


class RatingSpider(scrapy.Spider):
    name = "hrating"

    f = open("hlinks.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()

    def parse(self, response):
        for rating in response.css('head'):
            yield {
                'title': rating.css('title *::text').getall()
            }

        for rating in response.css('div.score_box'):
            yield {
                'reported': rating.css('div.score_heading *::text').extract()

            }
        for rating in response.css('#gt_getit'):
            yield {
                'price': rating.css('#gt_getit::text').extract()

            }
