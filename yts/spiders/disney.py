import scrapy
from yts.spiders import YTSSpider


MOVIE_TITLE_XPATH = '//table[@class="wikitable sortable plainrowheaders"][1]//i/a/text()'


class DisneyYTSSpider(YTSSpider):
    """Scrape all Disney movies from yts.mx."""

    name = "disney"
    start_urls = ["https://en.wikipedia.org/wiki/List_of_Disney_theatrical_animated_feature_films"]

    def parse(self, response):
        """Get a list of titles of Disney animated movies from wikipedia.

        For each title, use yts API to search for movies.
        """
        titles = response.xpath(MOVIE_TITLE_XPATH).getall()
        for title in titles:
            yield scrapy.FormRequest(
                url="https://yts.mx/api/v2/list_movies.json",
                method="GET",
                formdata={"quality": "720p", "genre": "Animation", "query_term": title},
                callback=self.parse_api,
            )
