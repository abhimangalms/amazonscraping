from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXpathSelector

class MySpider(BaseSpider):
	name = "adidas"
	allowed_domains = ["amazon.in"]
	start_urls = ["https://www.amazon.in/"]
	
	def parse(self, response):
		hxs = HtmlXpathSelector(response)
		titles = hxs.select("//p")
		for titles in titles:
			title = titles.select("a/text()").extract()
			link = titles.select("a/@href").extract()
			print title, link
			
	
	
	
	  