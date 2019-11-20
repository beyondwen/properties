import scrapy

from properties.items import PropertiesItem


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["lianjia"]
    start_urls = ['https://cd.lianjia.com/ershoufang/']

    def parse(self, response):
        item = PropertiesItem()
        item['title'] = response.xpath('//*[@class="title"]/text()').extract()
        item['houseInfo'] = response.xpath('//*[@class="houseInfo"]/text()').extract()
        item['followInfo'] = response.xpath('//*[@class="followInfo"]/text()').extract()
        item['totalPrice'] = response.xpath('//*[@class="totalPrice"]//span/text()').extract()
        # self.log("title: %s" % response.xpath('//*[@class="title"]/text()').extract())
        # self.log("positionInfo: %s" % response.xpath('//*[@class="positionInfo"]/text()').extract())
        # self.log("houseInfo: %s" % response.xpath('//*[@class="houseInfo"]/text()').extract())
        # self.log("followInfo: %s" % response.xpath('//*[@class="followInfo"]/text()').extract())
        # self.log("totalPrice: %s" % response.xpath('//*[@class="totalPrice"]//span/text()').extract())
        return item
