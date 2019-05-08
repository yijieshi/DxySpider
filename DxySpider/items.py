# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DxySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 医生名字
    doctorName = scrapy.Field()

    # 职称
    title = scrapy.Field()

    # 科室
    department = scrapy.Field()

    # 所在医院
    hospital = scrapy.Field()

    # 擅长放向
    area = scrapy.Field()

    # 星级
    star = scrapy.Field()

    # 回答数量
    sum = scrapy.Field()

    # 平均响应时间
    time = scrapy.Field()

    # 图文回答价格
    price = scrapy.Field()

    # 语音回答价格
    priceVoice = scrapy.Field()