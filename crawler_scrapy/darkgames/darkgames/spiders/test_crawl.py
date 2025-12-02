import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    
    def start_requests(self):
        urls = [
            'https://www.darkpattern.games/game/365/0/lords-mobile-war-kingdom.html'       
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for rating in response.css('head'):
            yield {
                'title' : rating.css('title *::text').getall()
                }

        for rating in response.css('div.score_box'):
            yield {
                'reported': rating.css('div.score_heading *::text').extract()

           }
           
        for rating in response.css('#gt_getit'):
            yield {
                'price': rating.css('#gt_getit::text').extract()

           }