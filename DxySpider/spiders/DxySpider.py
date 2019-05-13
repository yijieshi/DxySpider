import scrapy
from DxySpider.items import DxySpiderItem

class DxySpider(scrapy.Spider):
    name = "DxySpider"
    # allowed_domains = ["www.haodf.com"]
    # start_urls = ["https://www.haodf.com/doctor/DE4r0BCkuHzduw0j4cK1qIYC2U8VE.htm"]
    allowed_domains = ['haodf.com']
    start_urls = ['https://www.haodf.com/doctor/DE4rO-XCoLUnz3tSkhlkqINLVW.htm']

    # def start_requests(self):
    #     headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
    #     for url in self.start_urls:
    #         yield Request(url, headers=headers)

    def parse(self, response):
        # for box in response.xpath('/html/body/div/div[5]/div/div[1]/div[2]/div[1]/div[1]'):
            # 实例化item
            item = DxySpiderItem()
            # 提取第一级页面中需要的信息
            # item['doctorName'] = box.xpath('./h3/text()').extract()
            item['doctorName'] = response.xpath('//body/div[1]').extract()
            # item['doctorName'] = response.body

            yield item
