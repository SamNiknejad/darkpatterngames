# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DarkgamesPipeline:
    def process_item(self, item, spider):
        #if not (item['reported'] == "\n" and item['rating'] == "\n" and item['link'] == "\n" and item['title'] == "\n"):
        #items.append(item)
        return item
        