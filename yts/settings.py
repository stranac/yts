BOT_NAME = "yts"

SPIDER_MODULES = ["yts.spiders"]
NEWSPIDER_MODULE = "yts.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {"yts.pipelines.DuplicatesPipeline": 100}

FEED_EXPORTERS = {"rss": "yts.exporters.BitTorrentRSSExporter"}
