# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.spider import Spider
from scrapy.selector import Selector
 
class DmozSpider(Spider):
   name = "item"
   start_urls=[
          "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=adidas+shoes"
   ]	

   if start_urls[0].find('amazon') >= 0:

      def parse(self, response):
        sel = Selector(response)
        item_name = sel.xpath('//span[@id="productTitle"]//text()').extract()
        item_price = sel.xpath('//span[@id="priceblock_ourprice"]//text()').extract()
        item_image = sel.xpath('//div[@class="imgTagWrapper"]/img/@src').extract()
        print item_name , item_price

   else:

      def parse(self, response):
        sel = Selector(response)
        item_name = sel.xpath('//h1[@itemprop="name"]//text()').extract()
        item_price = sel.xpath('//span[@class="fk-font-verybig pprice fk-bold"]//text()').extract()
        item_image = sel.xpath('//div[@class="image-wrapper"]/img/@src').extract()
print item_image , item_name , item_price