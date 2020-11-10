BOT_NAME = "yts"

SPIDER_MODULES = ["yts.spiders"]
NEWSPIDER_MODULE = "yts.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {"yts.pipelines.DuplicatesPipeline": 100}

FEED_EXPORTERS = {"rss": "yts.exporters.BitTorrentRSSExporter"}
FEEDS = {
    "disney_movies.rss": {
        "format": "rss",
        "indent": 2,
        "item_export_kwargs": {
            "feed_title": "Disney Animated Movies",
            "feed_description": "Disney Animated Movies from yts.mx",
        },
        "overwrite": True,
    },
    "oscar_winners.rss": {
        "format": "rss",
        "indent": 2,
        "item_export_kwargs": {
            "feed_title": "Academy Award-winning Movies",
            "feed_description": "Academy Award-winning Movies from yts.mx",
        },
        "overwrite": True,
    },
}
