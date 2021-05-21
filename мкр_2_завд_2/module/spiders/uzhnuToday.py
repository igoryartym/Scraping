import scrapy
from scrapy_selenium import SeleniumRequest
from module.items import ModuleItem

class UzhnutodaySpider(scrapy.Spider):
    name = 'uzhnuToday'
    start_urls = ['https://www.instagram.com/uzhnu.today/']
    default_headers = {
        "access-control-allow-origin": "https://www.instagram.com",
        "accept-language": "uk - UA, uk;q = 0.9, ru;q = 0.8, en - US;q = 0.7, en;q = 0.6",
    }
    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url = url,
                callback = self.parse,
                wait_time = 10,
                headers = self.default_headers
            )
    def parse(self, response):
        for item in response.css('.Nnq7C'):
            img = ModuleItem()
            url = item.css('div a div div.KL4Bh img::attr(src)').getall()[1]
            img['image_urls'] = [url]
            yield img
