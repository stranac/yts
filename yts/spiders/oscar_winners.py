import scrapy
from yts.spiders import YTSSpider


class OscarWinnersYTSSpider(YTSSpider):
    """Scrape all Academy Award-winning movies from yts.mx."""

    name = "oscar_winners"
    start_urls = ["https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films"]

    custom_settings = {
        'FEEDS': {
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
    }

    def parse(self, response):
        """Get a list of titles of Academy Award-winning movies from wikipedia.

        For each title, use yts API to search for movies.
        """
        movies = response.xpath('//tr[@style="background:#EEDD82"]')
        for movie in movies:
            title = movie.xpath(".//b//a/text()").get()
            years = movie.xpath(".//td/a/text()").getall()
            for year in years:
                # sometimes year is present as e.g. 1934/35
                if len(year) == 2:
                    year = "19" + year
                yield scrapy.FormRequest(
                    url="https://yts.mx/api/v2/list_movies.json",
                    method="GET",
                    formdata={"quality": "720p", "query_term": f"{title} {year}"},
                    callback=self.parse_api,
                )
