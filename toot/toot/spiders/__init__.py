# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.spider import Spider
from scrapy.selector import Selector
from toot.items import PlayerItem


from scrapy.item import Item, Field


  
class MySpider(Spider):
	name = 'kickass_spider'
	allowed_domains = ["wikipedia.org"]
	start_urls = ["http://en.wikipedia.org/wiki/2013_Denver_Broncos_season"] 

	def parse(self, response):

		sel = Selector(response)
		players = []
		table =  sel.xpath('//table[@class="toccolours"]')
		count = 0
		for table_row in table.xpath('tr') :
			print count
			for position in table_row.xpath('.//b/text()'):
				player_position = position.extract()
				for row in table_row.xpath('.//ul'):
					for li in row.xpath('.//li'):
						num = li.xpath('.//span/text()').extract()
						name = li.xpath('.//a/text()').extract()
						player = PlayerItem()
						player['name'] = name[0]
						print player["name"]
						player['position'] = player_position
						print player["position"]
						if len(num) > 0:
							player['number'] = num[0]
							#print player["number"]
						players.append(player)

						#print player['name']
				count += 1
		return players







	


		



			




		





		















