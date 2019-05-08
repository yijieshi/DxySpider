import scrapy
from DxySpider.items import DxySpiderItem

class DxySpider(scrapy.Spider):
    name = "DxySpider"
    allowed_domains = ["ask.dxy.com"]
    start_urls = ["https://ask.dxy.com/ama/index#/find/user/13848149/comment"]

    def parse(self, response):
        for box in response.xpath('/html/body/div[1]/div[4]/div/div/div'):
            # 实例化item
            item = DxySpiderItem()
            # 提取第一级页面中需要的信息
            item['doctorName'] = box.xpath('./div/div/div[2]/text()').extract()
            yield item