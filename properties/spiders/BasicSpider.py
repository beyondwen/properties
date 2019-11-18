import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["lianjia"]
    start_urls = "https://cd.lianjia.com/ershoufang/"

    def parse(self, response):
        self.log("title: %s" % response.xpath('//*[@id="content"]/div[1]/ul/li[2]/div[1]/div[1]/a/text()').extract())
        # self.log("location: %s" % response.xpath('//*[@itemprop="name"][1]/text()').extract())
        # self.log("price: %s" % response.xpath('//*[@itemprop="name"][1]/text()').extract())
        # self.log("description: %s" % response.xpath('//*[@itemprop="name"][1]/text()').extract())
