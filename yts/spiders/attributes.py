import scrapy
from yts.spiders import YTSSpider


MOVIE_TITLE_XPATH = '//table[@class="wikitable sortable plainrowheaders"][1]//i/a/text()'


class DisneyYTSSpider(YTSSpider):
    """Scrape all Disney movies from yts.mx."""

    name = "attributes"

    custom_settings = {
        'FEEDS': {
            "custom_search.rss": {
                "format": "rss",
                "indent": 2,
                "item_export_kwargs": {
                    "feed_title": "Custom Search Movies",
                    "feed_description": "Movies from yts.mx",
                },
                "overwrite": True,
            }
        }
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.search_settings = kwargs

    def start_requests(self):
        yield scrapy.FormRequest(
            url="https://yts.mx/api/v2/list_movies.json",
            method="GET",
            formdata={
                "quality": "720p",
                'limit': '50',
                'sort_by': 'latest',
                **self.search_settings
            },
            callback=self.parse_api,
        )
