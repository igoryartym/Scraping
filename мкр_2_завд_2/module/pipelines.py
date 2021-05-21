# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline

class ModulePipeline(ImagesPipeline):
    count = 0

    def file_path(self, request, response=None, info=None, *, item=None):
        self.count += 1
        return f"image_{self.count}.jpg"
