from scrapy.exceptions import DropItem


class DuplicatesPipeline:
    def __init__(self):
        self.seen = set()

    def process_item(self, item, spider):
        if item["guid"] in self.seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.seen.add(item["guid"])
            return item
