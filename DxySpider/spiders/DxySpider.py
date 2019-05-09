import scrapy
from DxySpider.items import DxySpiderItem

class DxySpider(scrapy.Spider):
    name = "DxySpider"
    # allowed_domains = ["www.haodf.com"]
    # start_urls = ["https://www.haodf.com/doctor/DE4r0BCkuHzduw0j4cK1qIYC2U8VE.htm"]
    allowed_domains = ['dxy.com']
    start_urls = ['https://ask.dxy.com/']
    def parse(self, response):
        # for box in response.xpath('/html/body/div/div[5]/div/div[1]/div[2]/div[1]/div[1]'):
            # 实例化item
            item = DxySpiderItem()
            # 提取第一级页面中需要的信息
            # item['doctorName'] = box.xpath('./h3/text()').extract()
            item['doctorName'] = response.xpath('//*[@id="container"]/div/div[1]/div/div[1]/ul/li[1]/a/text()').extract()
            yield item
